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


from cloudify.decorators import operation


@operation
def run(ctx, script_path=None, **kwargs):

    """
    Execute python scripts.

        Parameters:

            ctx['scripts'] - A dictionary mapping lifecycle
            events to script paths.

            script_path - The path to the script relative
                          to the blueprints root directory.
                          Will only be used if the 'scripts' argument is None.
        Exceptions:

            If both 'scripts' and 'script_path' is None.
            A runtime exception will be raised since there is no
            script to run.
    """
    script_to_run = get_script_to_run(ctx, script_path)

    if script_to_run:
        execfile(script_to_run)


def get_script_to_run(ctx, script_path=None):
    if script_path:
        return ctx.download_resource(script_path)
    if 'scripts' in ctx.properties:
        operation_simple_name = ctx.operation.split('.')[-1:].pop()
        scripts = ctx.properties['scripts']
        if operation_simple_name not in scripts:
            ctx.logger.info("No script mapping found for operation {0}. "
                            "Nothing to do.".format(operation_simple_name))
            return None
        return ctx.download_resource(scripts[operation_simple_name])

    raise RuntimeError('No script to run')
