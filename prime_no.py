
# a = int(input("Enter the number: "))
# b = int(input("Enter the number: "))


# sum = a + b

# # Print the result
# print("The sum of a and b is:", sum)


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_of_primes(limit):
    prime_sum = 0
    count = 0
    for num in range(2, 2 * limit):  # Just a rough upper bound to ensure we get 2 million primes
        if is_prime(num):
            prime_sum += num
            count += 1
        if count == limit:
            break
    return prime_sum

# Sum of the first 2 million prime numbers
limit = 200000
sum_primes = sum_of_primes(limit)
print(f"The sum of the first {limit} prime numbers is: {sum_primes}")

