
# Home work 1


def power_numbers(*numbers):
    return [i ** 2 for i in numbers]


print(power_numbers(1, 2, 3, 4, 5))


def is_prime(figure):
    if 0 in [figure%value for value in range(3,figure)]:
        return False
    else:
        return True

# ранее было посложнее для восприятия  result = 0 in list(map(lambda x: figure % x, range(3, figure)))
#     return not result


def filter_numbers(numbers, filter_type):
    if filter_type == ODD:
        return [i for i in numbers if i % 2 != 0]
    if filter_type == EVEN:
        return [i for i in numbers if i % 2 == 0]
    if filter_type == PRIME:
        return list(filter(is_prime, numbers))


ODD = "odd"
EVEN = "even"
PRIME = "prime"

print(filter_numbers([1, 2, 3], ODD))

print(filter_numbers([2, 3, 4, 5], EVEN))

print(filter_numbers([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], PRIME))
