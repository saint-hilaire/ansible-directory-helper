### About

This is a small helper library to make it easier to supply different variables - currently primarily Ansible inventories - to the Ansible Runner library,
specifically its _Input Directory Hierarchy_.

I am building this primarily to help me with [Lampsible](https://github.com/saint-hilaire/lampsible)
and [Docksible](https://github.com/saint-hilaire/docksible), but anyone who is working with
Ansible Runner might find this useful.

### Installing

Do something like this:

```
# pyproject.toml
...
dependencies = [
    ...
    "ansible-directory-helper@git+https://github.com/saint-hilaire/ansible-directory-helper",
    ...
]
```

### Usage

If you are using Ansible Runner to develop tools to automate server installations, you likely
have many dynamic variables, including but not limited to the system users and host addresses
of your remote servers. Ansible Runner expects these variables to be present in the so called
_Input Directory Hierarchy_, a predefined directory structure on your local file system.
To avoid the hassle of managing these files and directories yourself, you can use this
library, which essentially manages this directory structure for you.

Example:

```python
# my_automation_tool.py

from ansible_runner import Runner, RunnerConfig
from ansible_directory_helper.inventory_file import InventoryFile

private_data_dir = './.my-tool/tmp'
project_data_dir = './my-tool/src/project'

inventory_file = InventoryFile(
    os.path.join(
        private_data_dir,
        'inventory',
        'hosts'
    )
)

inventory_file.add_groups([
    'group1',
    'group2',
])
inventory_file.add_host('host1.example.com', 'group1')
inventory_file.add_host('host2.example.com', 'group2')
inventory_file.set_ansible_user('host1.example.com', 'user1')
inventory_file.set_ansible_user('host2.example.com', 'user2')

inventory_file.write()

# Now the inventory file is in the exact location and format in which
# Ansible Runner expects it to be (private_data_dir/inventory/), so you can easily
# configure Runner by simply passing the private_data_dir.

rc = RunnerConfig(
    private_data_dir=private_data_dir,
    project_dir=project_dir,
    playbook='my-playbook.yml'
)

rc.prepare()
r = Runner(config=rc)
r.run()

```


### Running unit tests

```
python -m unittest test/test_inventory_file.py
```
