"""
I have sorted the array and used 3 pointers to find the closest sum.
I used 2 pointers to find the best pair in each fixed element.
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = (float("inf"), 0)
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = num + nums[l] + nums[r]
                diff = abs(target - threeSum)
                if res[0] > diff:
                    res = (diff, threeSum)
                if threeSum > target:
                    r -= 1
                elif threeSum < target:
                    l += 1
                else:
                    return target
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res[1]