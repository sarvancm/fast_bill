# def add(a: int, b: int) -> str:
#     return a + b


# x = add(1, 2)
# print(x + 4)


# "hfghgfh"

# def fibonacci_recursive(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# # Test the function
# n = 10
# for i in range(n):
#     print(f"Fibonacci({i}) = {fibonacci_recursive(i)}")

# def fibonacci_recursive_sequence(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         print(0)
#         return [0]
#     elif n == 2:
#         print(0)
#         print(1)
#         return [0, 1]
#     else:
#         fib_sequence = fibonacci_recursive_sequence(n - 1)
#         next_fib = fib_sequence[-1] + fib_sequence[-2]
#         print(next_fib)
#         fib_sequence.append(next_fib)
#         return fib_sequence

# # Test the function
# n = 10
# fib_sequence = fibonacci_recursive_sequence(n)
# print(f"Fibonacci sequence of length {n}: {fib_sequence}")

# import inflect

# def number_to_words(number):
#     p = inflect.engine()
#     words = p.number_to_words(number)
#     return words

# number = 12345.89
# words = number_to_words(number)
# print(f"{number} in words: {words}")



