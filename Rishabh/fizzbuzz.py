# def fizzbuzz(n):

#     if n % 3 == 0 and n % 5 == 0:
#         return 'FizzBuzz'
#     elif n % 3 == 0:
#         return 'Fizz'
#     elif n % 5 == 0:
#         return 'Buzz'
#     else:
#         return str(n)

# print("\n".join(fizzbuzz(n) for n in range(1, 21)))

# Recursive FizzBuzz
def fizzbuzz_recursive(n):
    if n == 0:
        return
    fizzbuzz_recursive(n - 1)
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)
n = [n for n in range(21)]
fizzbuzz_recursive(n)