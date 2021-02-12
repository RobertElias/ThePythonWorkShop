def solution(S, K):

    # Create a list of all days
    days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    if S in days_of_week:
        return days_of_week[(days_of_week.index(S) + K) % len(days_of_week)]
    return S






print(solution("Wed", 2))
print(solution("Sat", 23))
print(solution("Mon", 15))
