__author__ = 'yaronparasol'

from setuptools import setup

PLUGINS_COMMON_VERSION = '3.0'
PLUGINS_COMMON_BRANCH = "develop"
PLUGINS_COMMON = 'https://github.com/cloudify-cosmo/cloudify-plugins-common' \
    '/tarball/{0}'.format(PLUGINS_COMMON_BRANCH)

setup(
    name='python-script-executor-plugin',
    version='1.0',
    author='Yaron Parasol',
    author_email='yaronpa@gigaspaces.com',
    packages=["python_script_executor"],
    license='LICENSE',
    description='Cloudify plugin for executing python script in process',
    zip_safe=False,
    install_requires=[
        "cloudify-plugins-common"
    ],
    test_requires=[
        "nose"
    ],
    dependency_links=["{0}#egg=cloudify-plugins-common-{1}"
                      .format(PLUGINS_COMMON, PLUGINS_COMMON_VERSION)]
)
