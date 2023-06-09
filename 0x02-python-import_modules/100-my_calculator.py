#!/usr/bin/python3
if __name__ == "__main___":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    operator = sys.argv[3]

    answer = None
    if operator == '+':
        answer = add(a, b)
    elif operation == '-':
        answer = sub(a, b)
    elif operation == '*':
        answer = mul(a, b)
    elif operation == '/':
        answer = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print(f"{a} {operator} {b} = {answer}")
