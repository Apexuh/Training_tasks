# t = 'esdwefAsdf'
# test = 'abcdefghijklmnopqrstuvwxyz'
# if all([i in test for i in t]):
#     print('yes')
# else:
#     print('False')


# 1 1 2 3 5 8

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n-2)
#
# print(fib(6))

def plus(m1, m2):
    m3 = [m1[i][j] + m2[i][j] for j in range(len(m1[0])) for i in range(len(m1))]
    return m3
m1 = [1, 2, 3]
m2 = [4, 5, 6]
m3 = plus(m1, m2)
print(m3)