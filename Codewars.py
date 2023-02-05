# Complete the function that
#
#     accepts two integer arrays of equal length
#     compares the value each member in one array to the corresponding member in the other
#     squares the absolute value difference between those two values
#     and returns the average of those squared absolute value difference between each member pair.

# Examples
#
# [1, 2, 3], [4, 5, 6]              -->   9   because (9 + 9 + 9) / 3
# [10, 20, 10, 2], [10, 25, 5, -2]  -->  16.5 because (0 + 25 + 25 + 16) / 4
# [-1, 0], [0, -1]                  -->   1   because (1 + 1) / 2



# def solution(array_a, array_b):
#     result = sum(abs(array_a[i] - array_b[i]) ** 2 for i in range(len(array_a))) / len(array_a)
#     return result
#
# a1 = [1, 2, 3]
# a2 = [4, 5, 6]
#
# assert solution(a1, a2) == 9
#
# b1 = [10, 20, 10, 2]
# b2 = [10, 25, 5, -2]
#
# assert solution(b1, b2) == 16.5
#
# c1 = [0, -1]
# c2 = [-1, 0]
#
# assert solution(c1, c2) == 1
#
# d1 = [10, 10]
# d2 = [10, 10]
#
# assert solution(d1, d2) == 0

# ==================================================


# Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:
# a = Vector([1, 2, 3])
# b = Vector([3, 4, 5])
# c = Vector([5, 6, 7, 8])
# a.add(b)      # should return a new Vector([4, 6, 8])
# a.subtract(b) # should return a new Vector([-2, -2, -2])
# a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
# a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
# a.add(c)      # raises an exception
# If you try to add, subtract, or dot two vectors with different lengths, you must throw an error!
# Also provide:
#     a toString method, so that using the vectors from above, a.toString() === '(1,2,3)' (in Python, this is a __str__ method, so that str(a) == '(1,2,3)')
#     an equals method, to check that two vectors that have the same components are equal
# Note: the test cases will utilize the user-provided equals method.

class Vector:
    def __init__(self, *args):
        self._data = list(*args)

    def add(self, other):
        return Vector([self._data[i] + other._data[i] for i in range(len(self._data))])

    def substract(self, other):
        return Vector([self._data[i] - other._data[i] for i in range(len(self._data))])

    def dot(self, other):
        return sum(self._data[i] * other._data[i] for i in range(len(self._data)))

    def norm(self):
        return sum(i ** 2 for i in self._data) ** 0.5

    def equals(self, other):
        return self._data == other._data

    def __str__(self):
        return f"{str(tuple(self._data))}".replace(' ','')
a = Vector([1, 2, 3])
# print(a)
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])
a.add(b)      # should return a new Vector([4, 6, 8])
# a.subtract(b) # should return a new Vector([-2, -2, -2])
# a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
# a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
# a.add(c)
print(a)