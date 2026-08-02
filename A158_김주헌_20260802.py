def solution(players, callings):
    player_indices = {player: i for i, player in enumerate(players)}
    
    for name in callings:
        idx = player_indices[name]
        
        front_name = players[idx - 1]
        
        players[idx - 1], players[idx] = players[idx], players[idx - 1]
        
        player_indices[name] = idx - 1
        player_indices[front_name] = idx
        
    return players