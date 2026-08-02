def solution(n, m, section):
    answer = 0
    painted_until = 0
    
    for sec in section:
        if sec > painted_until:
            answer += 1
            painted_until = sec + m - 1
            
    return answer