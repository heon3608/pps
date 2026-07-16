class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total_sum = 0
        n = len(arr)
        
        for i in range(n):
            current_sum = 0
            

            for j in range(i, n):
                current_sum += arr[j]
                if (j - i + 1) % 2 != 0:

                    
                    total_sum += current_sum
                    
        return total_sum