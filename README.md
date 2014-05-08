# Cloudify Python Plugin

This plugin allows the execution of python scripts as part of a node's lifecycle interface operations.


- Build Status (master) [![Build Status](https://secure.travis-ci.org/cloudify-cosmo/cloudify-python-plugin.png?branch=develop)](http://travis-ci.org/cloudify-cosmo/cloudify-python-plugin)

## Usage

**built-in python types**

Currently, cloudify does not offer built-in types for using the python plugin. In order to use this plugin,
you will have to create a type, Like so:

* Each lifecycle operation is mapped to the plugin. (see [Lifecycle Interface](https://github.com/cloudify-cosmo/cloudify-manager/blob/develop/resources/rest-service/cloudify/types/types.yaml#L19)) <br><br>
* 'scripts' property is a <b>MUST</b>, mapping each interface operation to a specific script.

For example: <br><br>

    types:

        # A web server configured with python scripts
        cloudify.types.python.web_server:
            derived_from: cloudify.types.web_server
            interfaces:
                cloudify.interfaces.lifecycle:
                    - create: python_script_executor.tasks.run
                    - configure: python_script_executor.tasks.run
                    - start: python_script_executor.tasks.run
                    - stop: python_script_executor.tasks.run
                    - delete: python_script_executor.tasks.run
            properties:
                - scripts


Now you can use this type in your blueprint:

    -   name: http_web_server
        type: cloudify.types.python.web_server
        properties:
          scripts:
            configure: scripts/configure.py
            start: scripts/start.py
            stop: scripts/stop.py

This means that the 'configure', 'start' and 'stop' operations will be executed by the 'configure.py', 'start.py' and 'stop.py' scripts respectively. You can of course create you own interface and map any operation to any script.

**direct operation mapping**

You can also specify a script for execution on a specific operation by mapping it directly inside the interface declaration.

for example:

    types:
      my_new_type:
        derived_from: cloudify.types.base
        interfaces:
            my_new_interface:
                - my_new_operation:
                      mapping: 'python_script_executor.tasks.run'
                      properties:
                          script_path: 'scripts/my-new-script.py'

This means the operation 'my_new_operation' of interface 'my_new_interface' for the type 'my_new_type' is mapped to the python plugin, with the 'my-new-script.py' set for execution.

## API

As far as API goes, since these python script run in the same process, they have complete access to the 'ctx' parameter. For a complete API see [Cloudify Context](https://github.com/cloudify-cosmo/cloudify-plugins-common/blob/develop/cloudify/context.py)

