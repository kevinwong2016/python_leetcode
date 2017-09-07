# -*- coding: utf-8 -*-
"""
Created on Wed Sep 06 21:02:58 2017

@author: wangyao
"""
##穷举法
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = [] 
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                sum = 0
                for z in range(i,j+1):
                    sum += nums[z]
                ans.append(sum)
        return max(ans)
    
    
##优化枚举
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = []
        for i in range(0,len(nums)):
            sum = 0
            for j in range(i,len(nums)):
                sum += nums[j]
                ans.append(sum)
        return max(ans)

##贪心算法
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        sum_set = []
        ans = 0
        for i in range(0,len(nums)):
            sum += nums[i]
            sum_set.append(sum)
            ans = max(sum_set)
            if sum < 0:
                sum = 0
        return ans
        






