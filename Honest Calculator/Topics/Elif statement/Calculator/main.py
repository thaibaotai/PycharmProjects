# put your python code here
a = float(input())
b = float(input())
operation = input()
operation_dict = {
    "+": a + b,
    "-": a - b,
    "*": a * b,
    "pow": a ** b,
}

if operation in ['/', "mod", "div"]:
    if b == 0:
        print('Division by 0!')
    else:
        operation_dict = {
            "/": a / b,
            "mod": a % b,
            "div": a // b,
        }
        print(operation_dict[operation])
else:
    print(operation_dict[operation])