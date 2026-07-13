def solution(today, terms, privacies):

    def date_to_days(date_str):
        y, m, d = map(int, date_str.split('.'))

        return y * 12 * 28 + m * 28 + d

    today_days = date_to_days(today)
    
    term_dict = {}
    for term in terms:
        t_type, t_months = term.split()
        term_dict[t_type] = int(t_months) * 28
        
    answer = []
    
    
    for i, privacy in enumerate(privacies, 1):
        collected_date, t_type = privacy.split()
        expire_days = date_to_days(collected_date) + term_dict[t_type]
       
        if today_days >= expire_days:
            answer.append(i)
            
    return answer