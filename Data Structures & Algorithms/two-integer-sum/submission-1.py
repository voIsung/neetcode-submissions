class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_hashmap = {}
        output = []

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference not in new_hashmap:
                new_hashmap[nums[i]] = i
            else:
                  output.extend([new_hashmap[difference], i])

        return output      