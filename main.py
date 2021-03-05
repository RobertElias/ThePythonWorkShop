# def first2(s):
#     return s[:2] + ".." + " " + s[:2] + ".." + " " + s + "?"
# print(first2("incredible"))


# def first_last(name):
# 	return name[0] + name[-1]
# print(first_last("robert"))


# def make_pair(num1, num2):

#     # to convert number to list of integers
#     return [num1,num2]
# print(make_pair(51,21))


# def area(h,w):
#     if h<= 0 or w <=0:
#         return -1
#     else:
#         return h * w
# print(area(12,22))
# print(area(12, -22))

# def max_num(n1, n2):
#     if n1 > n2:
#         return n1
#     else:
#         return n2
# print(max_num(2311, 5680))

#Or a more simpler approach
def max_num(n1, n2):
    return max(n1, n2)
       


print(max_num(2311, 5680))
