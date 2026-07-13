def solution(number, limit, power):
    total_iron = 0
    
    for i in range(1, number + 1):
        div_count = 0
      
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                div_count += 1  
                if j != i // j:
                    div_count += 1
        
        if div_count > limit:
            total_iron += power
        else:
            total_iron += div_count
            
    return total_iron