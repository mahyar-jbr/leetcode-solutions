# 380. Insert Delete GetRandom O(1)
# Time: O(1) for all operations | Space: O(n)
# HashMap + Array combo for O(1) insert/delete/getRandom

import random

class RandomizedSet(object):

    def __init__(self):
        self.nums = []           
        self.nums_dict = {}      

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.nums_dict:
            return False
        
        self.nums.append(val)
        self.nums_dict[val] = len(self.nums) - 1
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.nums_dict:
            return False
        
        removeIndex = self.nums_dict[val]
        lastElement = self.nums[-1]
        
        self.nums[removeIndex] = lastElement
        self.nums_dict[lastElement] = removeIndex
        
        self.nums.pop()
        del self.nums_dict[val]
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.nums)