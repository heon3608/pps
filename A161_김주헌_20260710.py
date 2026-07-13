def solution(keymap, targets):
    answer = []
    
    
    min_presses={}
    for key in keymap:
        for i, char in enumerate(key):
            press = i + 1 
            if char not in min_presses:
                min_presses[char] = press
            else:
                min_presses[char] = min(min_presses[char], press)
                
    
    for target in targets:
        total = 0
        for char in target:
            if char in min_presses:
                total += min_presses[char]
            else:
               
                total = -1
                break
        
        answer.append(total)
        
    return answer