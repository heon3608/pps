class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            total = 0
            for n in str(num):
                
                total += int(n)
            num = total
            
        return num