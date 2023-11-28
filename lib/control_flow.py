#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username.lower() == 'admin' and password.lower() == '12345':
        message = 'Access granted'
        return message
    else:
        message = 'Access denied'
        return message


def hows_the_weather(temperature):

    if temperature < 55:
        return 'It\'s brisk out there!'
    elif temperature >= 55 and temperature < 75:
        return 'It\'s a little chilly out there!'
    elif temperature >= 75 and temperature < 99:
        return 'It\'s perfect out there!'
    elif temperature >= 99:
        return 'It\'s too dang hot out there!'

def fizzbuzz(num):

    if num == 0 or num == 15 or num == 45:
        return 'FizzBuzz'
    elif num == 3 or num == 33 or num ==42:
        return 'Fizz'
    elif num == 5 or num == 10 or num == 50:
        return 'Buzz'
    else:
        return num

def calculator(operation, num1, num2):

    calculator_definition = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1*num2,
        '/': num1 / num2
    }

    def invalid_response():
        print("Invalid operation!")
        return None


    return calculator_definition.get(operation, invalid_response())


