import random


def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """

    total = 0
    numbers = [0] * 5
    index = 0

    while index < 5:
        numbers[index] = random.randint(0, 100)
        total = total + numbers[index]
        index = index + 1


    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
