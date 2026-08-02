class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        unique_transformations = set()
        
        for word in words:
            transformed = ""
            for char in word:
                index = ord(char) - ord('a')
                transformed += morse[index]
            unique_transformations.add(transformed)
            
        return len(unique_transformations)