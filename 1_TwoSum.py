class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i in range(len(nums)):
            cur_val = nums[i]
            try:
                check_dict = target-cur_val
                return [temp[check_dict],i]
            except:
                temp[cur_val]=i
        
