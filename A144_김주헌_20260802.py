def solution(word):
    vowels = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    gaps = [781, 156, 31, 6, 1]
    answer = 0
    
    for i, char in enumerate(word):
        answer += vowels[char] * gaps[i] + 1
        
    return answer