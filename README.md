### Deprecated

Please do not use this tool, it is deprecated and no longer maintained.
What this package sets out to do can easily be accomplished with
Ansible Runner's `interface.run()` method instead. For example:

```python
# my_automation_tool.py

from ansible_runner import interface as runner_interface

my_user = 'remote_user'
my_host = 'my-server.com'

some_string = 'Hello, World!'
some_list   = ['Hello', 'World!']

runner = runner_interface.run(
    private_data_dir='path/to/tmp-private-data',
    playbook='setup-my-server.yml',
    inventory={
        'all': {
            'hosts': {
                my_host: {'ansible_user': my_user},
            },
        },
        'ungrouped': {'hosts': {}},
    },
    extravars={
        'some_string': some_string,
        'some_list'  : some_list,
    },
    project_dir='/path/to/my_automation_tool/src/project',
    # etc...
)
if runner.rc == 0:
    print('Finished successfully')
else:
    print('Error')
```
