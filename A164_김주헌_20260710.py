def solution(s):
    answer = []
    last_seen = {}
    
    for i, char in enumerate(s):
        if char not in last_seen:
            answer.append(-1)
        else:
          
            distance = i - last_seen[char]
            answer.append(distance)
            

        last_seen[char] = i
        
    return answer