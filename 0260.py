class Solution:
    def singleNumber(self, nums: "List[int]") ->" List[int]":
            already_exist=set()
            for i in range(len(nums)-1,-1,-1):
                if(nums[i] not in already_exist):
                    already_exist.add(nums[i])
                else:
                    already_exist.remove(nums[i])
            return list(already_exist)