import collections
from node import Node
class Solver:
    def __init__(self, start):
        self.start = start
        self.num_seen = []
        self.depth = []
    def solve(self):
        """
        Perform breadth first search and return a path
        to the solution, if it exists
        """
        current_depth = 0
        current_seen  = 0
        queue = collections.deque([Node(self.start)])
        seen = set()
        seen.add(queue[0].state)
        while queue:
            queue = collections.deque(sorted(list(queue), key=lambda node: node.f))
            node = queue.popleft()
            current_depth += 1
            
            if node.solved:
                return node.path
            for move, action in node.actions:
                child = Node(move(), node, action)
                if child.state not in seen:
                    queue.appendleft(child)
                    seen.add(child.state)
                    current_seen+=1
                    self.num_seen.append(current_seen)
                    self.depth.append(current_depth)