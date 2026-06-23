class Solution:
        def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            occurrence_map = {}
            output = []
            
            for num in nums:
                if num not in occurrence_map:
                    occurrence_map[num] = 1
                else:
                    occurrence_map[num] += 1

            occurrence_list = []

            for key, value in occurrence_map.items():
                occurrence_list.append([value, key])

            occurrence_list.sort()

            while len(output) < k:
                output.append(occurrence_list.pop()[1])

            return output

