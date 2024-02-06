import unittest
from typing import List 
from collections import defaultdict

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        """ 
        Given two arrays of strings `list1` and `list2`, find the common strings with the least index sum.
        """
        res = defaultdict(list) 
        for i in range(len(list1)):
            if list1[i] in list2:
                res[i + list2.index(list1[i])].append(list1[i])

        return res[min(res.keys())]
    
class TestEvalMinimumIndexSumTwoLists(unittest.TestCase):
    def setUp(self):
        print(f"Running {self._testMethodName} for Minimum Index Sum Two Lists...")

    def test_case1(self):
        list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
        list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
        output = ["Shogun"]
        result = Solution().findRestaurant(list1,list2)
        self.assertCountEqual(result,output)

    def test_case2(self):
        list1 = ["happy","sad","good"]
        list2 = ["sad","happy","good"] 
        output = ["sad","happy"]
        result = Solution().findRestaurant(list1,list2)
        self.assertCountEqual(result, output)

if __name__ == "__main__":
    unittest.main()
