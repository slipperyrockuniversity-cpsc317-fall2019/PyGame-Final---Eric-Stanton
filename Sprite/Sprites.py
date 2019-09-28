# Initial Imports for the pyGame Module
from index import window_height, window_width


def movement_Check(self):
    self.rect.x += 5
    if self.rect.left > window_width:
        self.rect.right = 0
