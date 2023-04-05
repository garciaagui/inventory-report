from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, inventory):
        self.inventory = inventory
        self.index = 0

    def __next__(self):
        try:
            product = self.inventory[self.index]
        except IndexError:
            raise StopIteration()
        else:
            self.index += 1
            return product
