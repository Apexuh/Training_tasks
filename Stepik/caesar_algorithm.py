

def caesar(s, step):
    st = ''
    not_good = '!#$%&*+-=?@^_",.:;'
    count_not_good = 0
    for k in not_good:
        count_not_good += s.count(k)
    for i in s:
        char = ord(i)
        if char in range(1040, 1072):
            char += step - count_not_good
            if char > 1071:
                char -= 32
            elif char < 1040:
                char += 32
        elif char in range(1072, 1104):
            char += step - count_not_good
            if char > 1103:
                char -= 32
            elif char < 1072:
                char += 32
        elif char in range(97, 123):
            char += step - count_not_good
            if char > 122:
                char -= 26
            elif char < 97:
                char += 26
        elif char in range(65, 91):
            char += step - count_not_good
            if char > 90:
                char -= 26
            elif char < 65:
                char += 26
        st += chr(char)
    return st


# ------
# s = input()
# s = 'Day, mice. "Year" is a mistake!'         # Gdb, qmgi. "Ciev" ku b tpzahrl!
# print(*[caesar(k, len(k)) for k in s.split()])

# ------
# print(caesar('Блажен, кто верует, тепло ему на свете!', 10))
# print(caesar('To be, or not to be, that is the question!', 17))

# print(caesar('Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг.',step = -7))
# print(caesar('Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.', -25))
#
# for i in range(25):
#     print(caesar('Hawnj pk swhg xabkna ukq nqj.',step=i))