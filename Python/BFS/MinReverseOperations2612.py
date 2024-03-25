# Definition for a binary tree node.
import heapq
import unittest

# Read about enumerate in python
from collections import defaultdict, deque
from typing import List

class Template(unittest.TestCase):

    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        minOp = dict()
        bfsQueue = deque()
        bannedSet = set(banned)
        bfsQueue.append(p)
        depth = 0
        levelSize = len(bfsQueue)
        while bfsQueue:
            for i in range(levelSize):
                head = bfsQueue.popleft()
                if head in bannedSet:
                    continue
                minOp[head] = depth

                minStart = head - (k - 1)
                while minStart < 0:
                    minStart += 1
                maxStart = head
                while maxStart + k - 1 > n - 1:
                    maxStart -= 1
                for start in range(minStart, maxStart + 1):
                    mirroredPos = start + start + k - 1 - head
                    if 0 <= mirroredPos < n and mirroredPos not in minOp:
                        bfsQueue.append(mirroredPos)

            levelSize = len(bfsQueue)
            depth += 1

        result = []
        for i in range(n):
            if i not in minOp:
                result.append(-1)
            else:
                result.append(minOp[i])

        return result

    def test_example1(self):
        n = 4
        p = 0
        banned = [1, 2]
        k = 4

        # [0,-1,-1,1]
        result = self.minReverseOperations(n, p, banned, k)
        print(result)

    def test_example2(self):
        n = 5
        p = 0
        banned = [2, 4]
        k = 3

        # [0,-1,-1,-1,-1]
        result = self.minReverseOperations(n, p, banned, k)
        print(result)

    def test_example3(self):
        n = 4
        p = 2
        banned = [0, 1, 3]
        k = 1

        # [-1,-1,0,-1]
        result = self.minReverseOperations(n, p, banned, k)
        print(result)

    def test_example4(self):
        n = 4
        p = 0
        banned = []
        k = 4

        # [0,-1,-1,1]
        result = self.minReverseOperations(n, p, banned, k)
        print(result)

    def test_example5(self):
        n = 5
        p = 0
        banned = []
        k = 2

        # [0,1,2,3,4]
        result = self.minReverseOperations(n, p, banned, k)
        print(result)

if __name__ == '__main__':
    unittest.main()