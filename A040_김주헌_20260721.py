class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s) // 2
        a = s[:mid]
        b = s[mid:]
        
        vowels = "aeiouAEIOU"
        count_a = 0
        count_b = 0
        
        for char in a:
            if char in vowels:
                count_a += 1
                
        for char in b:
            if char in vowels:
                count_b += 1

        if count_a == count_b:
            return True
        else:
            return False