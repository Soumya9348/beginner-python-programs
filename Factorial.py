#Here is the code for calculating factorials of any number in 4 different methods. You can chose anyone of them as per your convenience :)


import math


class Factorial:


    def __init__(self, number=5):
        self.number = number

    def type_one(self):
        '''Using while loop'''

        get_factorial = 1
        nums = self.number

        while nums != 1:
            get_factorial *= nums
            nums -= 1

        return f'{self.number}! = {get_factorial}'

    def type_two(self):
        '''Using for loop'''

        get_factorial = 1

        for num in range(1, self.number + 1):
            get_factorial *= num

        return f'{self.number}! = {get_factorial}'

    def type_three(self):
        '''Using built-in <math> module'''

        get_factorial = math.factorial(self.number)
        return f'{self.number}! = {get_factorial}'

    def type_four(self, number):
        '''Using recursive method'''

        if number == 1:
            return number

        return number * self.type_four(number - 1)


if __name__ == '__main__':
    factorial = Factorial()

    print('\nType One')
    print(factorial.type_one())

    print('\nType Two')
    print(factorial.type_two())

    print('\nType Three')
    print(factorial.type_three())

    print('\nType Four')
    print(factorial.type_four(factorial.number))
