def solution(babbling):
    answer = 0
    sounds = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        is_valid = True
        for sound in sounds:
            if sound * 2 in word:
                is_valid = False
                break
                
        if not is_valid:
            continue

        for sound in sounds:
            word = word.replace(sound, " ")
            
 
        if word.strip() == "":
            answer += 1
            
    return answer