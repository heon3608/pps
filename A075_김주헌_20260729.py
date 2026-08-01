def solution(numbers):
    numbers_str = list(map(str, numbers))
    numbers_str.sort(key=lambda x: x * 3, reverse=True)
    
    answer = ''.join(numbers_str)
    
    if answer[0] == '0':
        return '0'
        
    return answer