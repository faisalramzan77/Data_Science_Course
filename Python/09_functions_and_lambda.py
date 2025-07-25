# For Adding
def add(a, b):
    return(a + b)
# For Sum of all elements in a list
def sum_list(lst):
    return sum(lst)

# For finding the maximum element in a list
def find_max(lst):
    return max(lst)
# For finding the factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
print("Factorial of 5:", factorial(5))
# For using lambda functions
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(add(2,4))
print("Sum:", sum_list(lst))
print("Squares:", list(map(lambda x: x ** 2, lst)))
print("Maximum:", find_max(lst))
print("The result of the addition is:", lst)
print(list(filter(lambda x: x % 2 == 0, lst)))

