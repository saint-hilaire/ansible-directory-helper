import os
from .inventory_file import InventoryFile


class PrivateData:

    DEFAULT_INVENTORY_PATH = os.path.join(
        'inventory',
        'hosts'
    )

    def __init__(self, dir_path):
        self.dir_path = dir_path
        self.init_dir()
        self.set_inventory(PrivateData.DEFAULT_INVENTORY_PATH)


    def init_dir(self):
        try:
            os.makedirs(self.dir_path)
        except PermissionError:
            # TODO: Implement custom exceptions for this stuff,
            # or just don't catch them?
            pass
        except FileExistsError:
            pass


    def get_dir_path(self):
        return self.dir_path


    def set_inventory(self, inventory_file_path):
        self.inventory_file = InventoryFile(os.path.join(
            self.get_dir_path(),
            inventory_file_path
        ))
