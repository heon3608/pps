def solution(N, stages):
    
    counts = [0] * (N + 2)
    for stage in stages:
        counts[stage] += 1
        
    total_players = len(stages)
    failure_rates = []
    
    for i in range(1, N + 1):
        stuck_players = counts[i]
        
        
        if total_players > 0:
            rate = stuck_players / total_players
        
        else:
            rate = 0
            
        failure_rates.append((i, rate))
        
        total_players -= stuck_players
        
    
    failure_rates.sort(key=lambda x: (-x[1], x[0]))
    
   
    answer = [stage for stage, rate in failure_rates]
    
    return answer
        