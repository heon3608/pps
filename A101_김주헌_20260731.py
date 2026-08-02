class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_alice = sum(aliceSizes)
        sum_bob = sum(bobSizes)
        
        diff = (sum_bob - sum_alice) // 2
        bob_set = set(bobSizes)
        
        for candy in aliceSizes:
            target = candy + diff
            if target in bob_set:
                return [candy, target]