#!/usr/bin/env python3
"""Usage: nqueens N"""

import sys


class NQueens:
    """
    Usage: nqueens N
    If the user called the program with the wrong number of arguments,
    print Usage: nqueens N, followed by a new line, and exit with the status 1
    where N must be an integer greater or equal to 4
    If N is not an integer, print N must be a number,
    followed by a new line, and exit with the status 1
    If N is smaller than 4, print N must be at least 4,
    followed by a new line, and exit with the status 1
    The program should print every possible solution to the problem
    One solution per line
    Format: see example
    You don’t have to print the solutions in a specific order
    """
    def __init__(self, n):
        """Initialization"""
        self.n = n
        self.x = [0 for i in range(n + 1)]
        self.result = []

    def place(self, k, i):
        """check if k Quueen can be placed in i column (true)
            or if dey are attacking queens in row or diagonal (False)
        """
        for j in range(1, k):
            if self.x[j] == i or \
               abs(self.x[j] - i) == abs(j - k):
                return 0
        return 1

    def nQueen(self, k):
        """Tries to place every queen in the board

        Args:
         k: starting queen from which to evaluate (should be 1)
        """
        for i in range(1, self.n + 1):
            if self.place(k, i):
                # Queen can be placed in i column
                self.x[k] = i
                if k == self.n:
                    solution = []
                    for i in range(1, self.n + 1):
                        solution.append([i - 1, self.x[i] - 1])
                    self.result.append(solution)
                else:
                    # place morequeens
                    self.nQueen(k + 1)

        return self.result


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = sys.argv[1]

try:
    N = int(N)
except ValueError:
    print("N must be a Number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

queen = NQueens(N)
result = queen.nQueen(1)

for i in result:
    print(i)
