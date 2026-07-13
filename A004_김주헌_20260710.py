def solution(arr, divisor):
    
    
    answer = [x for x in arr if x% divisor == 0]
    
    if not answer:
        return[-1]
    return sorted(answer)

