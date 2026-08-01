def solution(a, b):
    months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    total_days = sum(months[:a]) + b
    answer = days[total_days % 7]
    return answer