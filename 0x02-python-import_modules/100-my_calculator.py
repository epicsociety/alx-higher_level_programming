#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as calc
    operators = ["+", "-", "*", "/"]
    x = sys.argv
    if len(x) != 4:
        (print("{}"
         .format("Usage: ./100-my_calculator.py <a> <operator> <b>")))
        exit(1)
    if not x[2] in operators:
        (print("{}"
         .format("Unknown operator. Available operators: +, -, * and /")))
        exit(1)
    a = int(x[1])
    b = int(x[3])
    op = x[2]
    result = (calc.add(a, b)
              if op is "+" else calc.sub(a, b)
              if op is "-" else calc.mul(a, b)
              if op is "*" else calc.div(a, b)
              if op is "/" else 0)
    print("{} {} {} = {}".format(a, op, b, result))
