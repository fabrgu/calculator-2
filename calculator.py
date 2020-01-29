"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

import arithmetic

# Your code goes here
while True:
    input_str = input("Enter your calculations: ")
    tokens = input_str.split(" ")
    first_token = tokens[0]
    if first_token.lower() == "q":
        break
    else:
        answer = ""
        if len(tokens) > 3:
            num_list = []
            i = 1
            while i < len(tokens):
                num_list.append(float(tokens[i]))
                i += 1
            if first_token == "+":
                answer = arithmetic.add_list(num_list)
            elif first_token == "-":
                answer = arithmetic.subtract_list(num_list)
            elif first_token == "*":
                answer = arithmetic.mult_list(num_list)

        else:
            second_token = float(tokens[1])
            third_token = None
            if len(tokens) == 3:
                third_token = float(tokens[2])
            if first_token == "+":
                answer = arithmetic.add(second_token, third_token)
            elif first_token == "-":
                answer = arithmetic.subtract(second_token, third_token)
            elif first_token == "*":
                answer = arithmetic.multiply(second_token, third_token)
            elif first_token == "/":
                answer = arithmetic.divide(second_token, third_token)
            elif first_token == "square":
                answer = arithmetic.square(second_token)
            elif first_token == "cube":
                answer = arithmetic.cube(second_token)
            elif first_token == "pow":
                answer = arithmetic.power(second_token, third_token)
            elif first_token == "mod":
                answer = arithmetic.mod(second_token, third_token)

        print(answer)
