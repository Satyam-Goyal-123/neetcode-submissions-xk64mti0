class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        d=dict()
        for i in range(n):
            d[nums[i]]=i

        for i in range(n):
            need=target-nums[i]
            if(need in d.keys() and d[need]!=i):
                return[i,d[need]]