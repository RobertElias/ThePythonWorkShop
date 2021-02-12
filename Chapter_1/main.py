

# returns True if string is balanced


def balanced(s):
    for i in range(len(s)):
        if s[i].islower() and s[i].upper() not in s:
            return False
        if s[i].isupper() and s[i].lower() not in s:
            return False
    return True


# returns minimum
def solution(s):
    least = len(s)
    findMin = False
    for i in range(len(s)+1):
        for j in range(i+1, len(s)+1):
            if balanced(s[i:j]) and least >= j-i:
                least = j-i
                findMin = True
    if findMin:
        return least
    return -1


print(solution('azABaabza'))
print(solution('TocoCat'))
print(solution('AcZCbaBz'))
print(solution('abcdefghijklmnopqrstuvwxyz'))
