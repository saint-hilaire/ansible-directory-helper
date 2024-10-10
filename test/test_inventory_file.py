import os
import unittest
from shutil import rmtree
import yaml
from ansible_directory_helper.inventory_file import InventoryFile


class TestInventoryFile(unittest.TestCase):

    def setUp(self):

        self.TEST_INVENTORY_PATH = os.path.join(
            'tmp',
            'inventory',
            'hosts'
        )
        self.inventory_file = InventoryFile(self.TEST_INVENTORY_PATH)
        self.inventory_file.add_groups([
            'group1',
            'group2',
        ])
        self.inventory_file.add_host('host1.example.com', 'group1')
        self.inventory_file.add_host('host2.example.com', 'group2')
        self.inventory_file.set_ansible_user('host1.example.com', 'user1')
        self.inventory_file.set_ansible_user('host2.example.com', 'user2')
        self.EXPECTED_INVENTORY_DICT = {
            'all': {'hosts': {}},
            'ungrouped': {'hosts': {}},
            'group1': {
                'hosts': {
                    'host1.example.com': {
                        'ansible_user': 'user1',
                        'inventory_dir': None,
                        'inventory_file': None,
                    },
                },
            },
            'group2': {
                'hosts': {
                    'host2.example.com': {
                        'ansible_user': 'user2',
                        'inventory_dir': None,
                        'inventory_file': None,
                    },
                },
            },
        }


    def tearDown(self):
        self.inventory_file._close_file_handle()
        rmtree('tmp')


    def test_inventory_dict(self):
        self.assertEqual(
            self.inventory_file.get_inventory_dict(),
            self.EXPECTED_INVENTORY_DICT
        )


    def test_inventory_file(self):
        self.inventory_file.write()
        with open(self.TEST_INVENTORY_PATH, 'r') as stream:
            self.assertEqual(
                yaml.safe_load(stream),
                self.EXPECTED_INVENTORY_DICT
            )


if __name__ == '__main__':
    unittest.main()
