#!/usr/bin/env python3

import operator
from fractions import Fraction


def decimal2fraction(result,test=0):
    return Fraction.from_float(result).limit_denominator()


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    'frac': decimal2fraction,
}


def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            try: 
                arg1 = stack.pop()
            except Exception as e:
                arg1 = arg2
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    result = stack.pop()
    stack.append(result)
    return result;


def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()
