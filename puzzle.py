import random
import itertools
import collections
import time

class Puzzle:
    """
    A class representing an '8-puzzle'.
    - 'board' should be a square list of lists
       e.g. [[1,2,3],[4,0,6],[7,5,8]]
    """
    def __init__(self, board,heuristic):
        self.width = len(board[0])
        self.board = board
        self.heuristic = heuristic

    @property
    def solved(self):
        """
        The puzzle is solved if the flattened board's numbers are in
        increasing order from left to right and the '0' tile is in the
        last position on the board
        """
        N = self.width * self.width
        return str(self) == '0' + ''.join(map(str, range(1,N))) 

    @property
    def actions(self):
        """
        Return a list of 'move', 'action' pairs. 'move' can be called
        to return a new puzzle that results in sliding the '0' tile in
        the direction of 'action'.
        """
        def create_move(at, to):
            return lambda: self._move(at, to)

        moves = []
        for i, j in itertools.product(range(self.width),
                                      range(self.width)):
            direcs = {'R':(i, j-1),
                      'L':(i, j+1),
                      'D':(i-1, j),
                      'U':(i+1, j)}

            for action, (r, c) in direcs.items():
                if r >= 0 and c >= 0 and r < self.width and c < self.width and \
                   self.board[r][c] == 0:
                    move = create_move((i,j), (r,c)), action
                    moves.append(move)
        return moves

    @property
    def sum_not_placed(self):
      right_positions  = []
      for i in range(3):
        for j in range(3):
          right_positions.append((i,j))
      right_positions
      distance = 0
      for i in range(3):
          for j in range(3):
              if self.board[i][j] != 0:
                  if (i!=right_positions[self.board[i][j]][0]) or (j!=right_positions[self.board[i][j]][1]):
                    distance+=1
      return distance

    @property
    def sum_distance(self):
      right_positions  = []
      for i in range(3):
        for j in range(3):
          right_positions.append((i,j))
      right_positions
      distance = 0
      for i in range(3):
          for j in range(3):
              if self.board[i][j] != 0:
                  distance += abs(right_positions[self.board[i][j]][0] - i)+abs(right_positions[self.board[i][j]][1] - j)
      return distance

    @property
    def h(self):
      if self.heuristic == 'sum_distance':
        return self.sum_distance
      elif self.heuristic == 'sum_not_placed':
        return self.sum_not_placed
      else:
        raise Exception('heuristic not knonw')

    def copy(self):
        """
        Return a new puzzle with the same board as 'self'
        """
        board = []
        for row in self.board:
            board.append([x for x in row])
        return Puzzle(board,self.heuristic)

    def _move(self, at, to):
        """
        Return a new puzzle where 'at' and 'to' tiles have been swapped.
        NOTE: all moves should be 'actions' that have been executed
        """
        copy = self.copy()
        i, j = at
        r, c = to
        copy.board[i][j], copy.board[r][c] = copy.board[r][c], copy.board[i][j]
        return copy

    def pprint(self):
        for row in self.board:
            print(row)
        print()

    def shuffle(self,n):
      "shuffles the puzzle n times randomly"
      puzzle = self
      for _ in range(n):
          puzzle = random.choice(puzzle.actions)[0]()
      return puzzle

    def __str__(self):
        return ''.join(map(str, self))

    def __iter__(self):
        for row in self.board:
            yield from row