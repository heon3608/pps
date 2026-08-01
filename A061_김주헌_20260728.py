class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            columnNumber -= 1 
            
            
            remainder = columnNumber % 26
            
            char = chr(remainder + 65)
            result.append(char)
            
            columnNumber = columnNumber // 26
            
        return "".join(reversed(result))