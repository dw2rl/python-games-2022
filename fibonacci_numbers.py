# imports
import datetime
import math


# start time of running
start_time = datetime.datetime.now()

# function to find nthterm of given n


def fibonacci_nthterm(n):
    GOLDEN_RATIO = 1.61803398875
    nthterm = (math.pow(GOLDEN_RATIO, n) -
               math.pow((1 - GOLDEN_RATIO), n)) / math.sqrt(5)
    return round(nthterm)

# function to find all Fibonacci nums till thterm


def fibonacci_nums(nthterm):
    fibonacci_numbers = []
    first_term = 0
    second_term = 1
    if nthterm > 0:
        fibonacci_numbers.append(first_term)
        fibonacci_numbers.append(second_term)
    for i in range(2, nthterm+1):
        seq = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(seq)
    return fibonacci_numbers


if __name__ == '__main__':
    # n = int(input('Enter n: '))
    # if n > 0:
    #     print(f'nth-term of {n} is {fibonacci_nthterm(n)}')
    # else:
    #     print(n)
    nthterm = 20
    print(fibonacci_nums(nthterm))

# end time of running
end_time = datetime.datetime.now()
final_time = (end_time - start_time)
print(f'Compiling time: {final_time}s')
