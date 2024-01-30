# evaluate reverse polish notation
# You are given an array of strings 'tokens', that represents an arithmetic expression in a Reverse Polish Notation.
# Evaluate the expression. Return an integer that represents the value of the expression. 

# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
# each operand may be an integer or another expression
# Note: Division between two integers should truncate toward zero.
# There will be no division by zero.

class Solution:
    def evalRPN(tokens):
        stack = []
        for token in tokens: # iterate through the tokens
            if token in ["+", "-", "*", "/"]: # if the token is an operator
                num2 = stack.pop() # pop the last two numbers
                num1 = stack.pop() # pop the last two numbers
                if token == "+": # perform the operation
                    stack.append(num1 + num2) # append the result to the stack
                elif token == "-": # perform the operation
                    stack.append(num1 - num2) # append the result to the stack
                elif token == "*": # perform the operation
                    stack.append(num1 * num2) # append the result to the stack
                elif token == "/": # perform the operation
                    stack.append(int(num1 / num2))  # use int() for truncating towards zero
            else:
                stack.append(int(token)) # append the number to the stack
        return stack.pop() 
    
    print(evalRPN(["2", "1", "+", "3", "*"])) # 9