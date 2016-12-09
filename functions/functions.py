__author__ = 'Cue'
def square_number(num):
    return(num * num)
print(square_number(5))

def is_prime(value):
    """
       function to check if a number is prime or not
       """
    :param value:
    :return:
    """

    i = 2
    while i < value:
        remainder = value % i
        if remainder == 0:
            return False
        i += 1
    return True

print(is_prime(5))

def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32.0

