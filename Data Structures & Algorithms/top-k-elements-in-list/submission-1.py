class Solution:
        def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            occurrence_map = {}
            k_elements = []
            
            for num in nums:
                if num not in occurrence_map:
                    occurrence_map[num] = 1
                else:
                    occurrence_map[num] += 1
            
            biggest = 0
            biggest_key = 0
            
            while(k > 0):
                for key, value in occurrence_map.items():
                    if occurrence_map[key] >= biggest:
                         biggest = occurrence_map[key]
                         biggest_key = key

                k_elements.append(biggest_key)
                del occurrence_map[biggest_key]
                biggest_key = 0
                biggest = 0
                k -= 1

            output = tuple(k_elements)

            return list(output)

