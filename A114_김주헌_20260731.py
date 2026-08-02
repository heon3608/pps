class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        prime_count = 0
        for i in range(1, n + 1):
            if i > 1:
                is_prime = True
                for j in range(2, i):
                    if i % j == 0:
                        is_prime = False
                        break
                if is_prime:
                    prime_count += 1
                    
        non_prime_count = n - prime_count
        MOD = 1000000007
        
        result = 1
        for i in range(1, prime_count + 1):
            result = (result * i) % MOD
            
        for i in range(1, non_prime_count + 1):
            result = (result * i) % MOD
            
        return result