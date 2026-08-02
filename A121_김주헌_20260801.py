class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counts = {}
        first_seen = {}
        last_seen = {}
        
        for i in range(len(nums)):
            num = nums[i]
            
            if num not in first_seen:
                first_seen[num] = i
                
            last_seen[num] = i
            
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
                
        degree = 0
        for num in counts:
            if counts[num] > degree:
                degree = counts[num]
                
        shortest_len = len(nums)
        
        for num in counts:
            if counts[num] == degree:
                current_len = last_seen[num] - first_seen[num] + 1
                if current_len < shortest_len:
                    shortest_len = current_len
                    
        return shortest_len