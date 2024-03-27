# Definition for a binary tree node.
import heapq
import unittest

# Read about enumerate in python
from collections import defaultdict, deque
from typing import List

class MaxEmployeesInvitedInMeeting(unittest.TestCase):

    def findArmLen(self, node: int, forbidNode: int, inEdges: dict) -> int:
        depth = 0
        bfsQueue = deque()
        bfsQueue.append(node)
        visited = set()
        visited.add(forbidNode)
        visited.add(node)
        levelSize = len(bfsQueue)
        while bfsQueue:
            for i in range(levelSize):
                head = bfsQueue.popleft()
                for neighbor in inEdges[head]:
                    if neighbor not in visited:
                        bfsQueue.append(neighbor)
                        visited.add(neighbor)

            levelSize = len(bfsQueue)
            depth += 1
        return depth - 1

    def maximumInvitations(self, favorite: List[int]) -> int:

        # Build graphs
        outEdges = dict()
        indegrees = defaultdict(lambda: 0)
        inEdges = defaultdict(set)
        for index, value in enumerate(favorite):
            indegrees[value] += 1
            outEdges[index] = value
            inEdges[value].add(index)

        # Enqueue the bfs start
        bfsQueue = deque()
        visited = set()
        for i in range(len(favorite)):
            if i not in indegrees:
                bfsQueue.append(i)
                visited.add(i)

        while bfsQueue:
            head = bfsQueue.popleft()
            neighbor = outEdges[head]
            if neighbor not in visited:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    bfsQueue.append(neighbor)
                    visited.add(neighbor)

        # Cycle heads
        headToCycle = defaultdict(list)
        for i in range(len(favorite)):
            if indegrees[i] == 1:
                curr = i
                result = []
                while curr not in visited:
                    result.append(curr)
                    visited.add(curr)
                    neighbor = outEdges[curr]
                    if neighbor not in visited:
                        indegrees[neighbor] -= 1
                        curr = neighbor

                headToCycle[i] = result

        # for all size bigger than 2
        maxThree = 0
        twoLists = []
        for key, value in headToCycle.items():
            if len(value) > 2:
                maxThree = max(maxThree, len(value))
            else:
                # len(value) == 2:
                twoLists.append(value)

        # for all size equal to 2, calculate the arm length
        maxTwo = 2
        for nodeA, nodeB in twoLists:
            aArm = self.findArmLen(nodeA, nodeB, inEdges)
            bArm = self.findArmLen(nodeB, nodeA, inEdges)
            maxTwo = max(maxTwo, aArm + bArm + 2)

        maxTwo = maxTwo + (len(twoLists) - 1) * 2
        return max(maxTwo, maxThree)

    def test_example7(self):
        favorite = [1, 0, 3, 2, 5, 6, 7, 4, 9, 8, 11, 10, 11, 12, 10]
        self.assertEqual(11, self.maximumInvitations(favorite))

    def test_example6(self):
        favorite = [1, 3, 1, 1, 3, 3, 5, 5, 7]
        self.assertEqual(6, self.maximumInvitations(favorite))

    def test_example1(self):
        favorite = [2, 2, 1, 2]
        self.assertEqual(3, self.maximumInvitations(favorite))

    def test_example2(self):
        favorite = [1, 2, 0]
        self.assertEqual(3, self.maximumInvitations(favorite))

    def test_example3(self):
        favorite = [3, 0, 1, 4, 1]
        self.assertEqual(4, self.maximumInvitations(favorite))

    @unittest.skip
    def test_example4(self):
        favorite = [1,0,0,2,1,4,7,8,9,6,7,10,8]
        self.assertEqual(4, self.maximumInvitations(favorite))

    def test_example5(self):
        favorite = [1,2,3,4,5,6,2]
        self.assertEqual(5, self.maximumInvitations(favorite))

if __name__ == '__main__':
    unittest.main()