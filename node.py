import random
import itertools
import collections
import time

class Node:
    """
    A class representing node
    """
    def __init__(self, puzzle, parent=None, action=None):
        self.puzzle = puzzle
        self.parent = parent
        self.action = action
        if (self.parent != None):
            self.g = parent.g + 1
        else:
            self.g = 0
    @property
    def score(self):
        return (self.g + self.h)
    
    @property
    def state(self):
        return str(self)
 
    @property
    def path(self):
        """
        Reconstruct a path from to the root 'parent'
        """
        node, p = self, []
        while node:
            p.append(node)
            node = node.parent
        yield from reversed(p)

    @property
    def solved(self):
        return self.puzzle.solved

    @property
    def actions(self):
        return self.puzzle.actions

    @property
    def h(self):
        return self.puzzle.h

    @property
    def f(self):
        return self.h + self.g
    def __str__(self):
        return str(self.puzzle)