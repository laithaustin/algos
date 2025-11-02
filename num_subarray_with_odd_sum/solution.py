from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        csum = 0
        odds = 0
        evens = 0
        res = 0
        mod = 10 ** 9 + 7

        for num in arr:
            csum += num
            if csum % 2:
                res = (res + 1 + evens) % mod
                odds += 1
            else:
                res = (res + odds) % mod
                evens += 1

        return res

"""
Key intuition here is to recognize the property that when you have running sum that is even: you want to know the amount of subarrays with an odd sum that you can then subtract to get another
odd subarray (even - odd = odd). similarly if you have a running sum that is odd: you want to know the amount of evens you can subtract to get more odds. This is technically a DP/prefix sum problem.
"""
        
