# item class definition
class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
    def on_take(self):
        print(f'You have picked up a {self.name}')
    def on_drop(self):
        print(f'You have dropped a {self.name}')