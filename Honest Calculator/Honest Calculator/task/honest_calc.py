msg_ = ["Enter an equation",
        "Do you even know what numbers are? Stay focused!",
        "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
        "Yeah... division by zero. Smart move...",
        "Do you want to store the result? (y / n):",
        "Do you want to continue calculations? (y / n):",
        " ... lazy",
        " ... very lazy",
        " ... very, very lazy",
        "You are",
        "Are you sure? It is only one digit! (y / n)",
        "Don't be silly! It's just one number! Add to the memory? (y / n)",
        "Last chance! Do you really want to embarrass yourself? (y / n)"]
memory = 0


def is_yesno(msg):
    while True:
        print(msg)
        ans = input()
        if ans not in ['y', 'n']:
            continue
        else:
            return ans


def is_one_digit(v):
    return -10 < v < 10 and v.is_integer()


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_[6]
    if (v1 == 1 or v2 == 2) and v3 == "*":
        msg = msg + msg_[7]
    if (v1 == 0 or v2 == 0) and v3 in ["*", "+", "-"]:
        msg = msg + msg_[8]
    if msg != "":
        msg = msg_[9] + msg
    print(msg)


while True:
    print(msg_[0])
    x, oper, y = input().split()
    # Use memory?
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    # Is a number?
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_[1])
        continue
    # Is valid operation?
    if oper not in ['+', '-', '*', '/']:
        print(msg_[2])
        continue
    # Check laziness
    check(x, y, oper)
    # calculate
    if oper == "+":
        result = x + y
    elif oper == "-":
        result = x - y
    elif oper == "*":
        result = x * y
    elif oper == "/" and y != 0:
        result = x / y
    else:
        print(msg_[3])
        continue
    print(result)
    # Memorize?
    if is_yesno(msg_[4]) == 'y':
        # Saving memory
        if is_one_digit(result):
            msg_index = 10
            while is_yesno(msg_[msg_index]) == 'y':
                if msg_index < 12:
                    msg_index += 1
                    continue
                else:
                    memory = result
                    break
        else:
            memory = result
    # Continue?
    if is_yesno(msg_[5]) == 'y':
        continue
    else:
        break
