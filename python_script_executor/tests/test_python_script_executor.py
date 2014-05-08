########
# Copyright (c) 2014 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.
import os
from os.path import dirname
import unittest

from cloudify.mocks import MockCloudifyContext

import python_script_executor.tests as test_path


__author__ = 'elip'


class TestPythonRunner(unittest.TestCase):

    def create_context(self, properties=None):
        return PythonRunnerMockCloudifyContext(
            node_id='test',
            blueprint_id='',
            deployment_id='test',
            execution_id='test',
            operation='cloudify.interfaces.lifecycle.start',
            properties=properties)

    def test_good_script(self):

        """
        Should finish gracefully.
        """

        from python_script_executor.tasks import run
        run(self.create_context(), script_path='good.py')

    def test_bad_script(self):

        """
        Task should throw the exception raised in the script.
        """

        try:
            from python_script_executor.tasks import run
            run(self.create_context(), script_path='bad.py')
            self.fail('Expected exception')
        except Exception as e:
            self.assertEqual(e.message, 'Bad Script!')

    def test_context_propagation(self):

        """
        Use the ctx in the script. see changes have taken affect.
        """

        from python_script_executor.tasks import run

        context = self.create_context()
        run(context, script_path='with_context.py')
        self.assertTrue(context['test'])


class PythonRunnerMockCloudifyContext(MockCloudifyContext):

    def download_resource(self, resource_path, target_path=None):
        return os.path.join(dirname(test_path.__file__),
                            "resources", resource_path)
