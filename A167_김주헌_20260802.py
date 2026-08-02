def solution(food):
    left_side = ""
    
    for i in range(1, len(food)):
        count = food[i] // 2
        left_side += str(i) * count
        
    return left_side + "0" + left_side[::-1]