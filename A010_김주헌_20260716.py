def solution(s):
    if len(s) == 1:
        return 1
        
  
    min_length = len(s)
    

    
    
    
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[:step]
        count = 1
        for j in range(step, len(s), step):
            curr = s[j:j+step]
            
            if prev == curr:
                count += 1
            else:
                if count > 1:
                    compressed += str(count) + prev
                else:
                    compressed += prev
                prev = curr
                count = 1
                
                
                
        if count > 1:
            compressed += str(count) + prev
        else:
            compressed += prev
        min_length = min(min_length, len(compressed))
        
    return min_length