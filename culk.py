def opers(x1, y1, op1):
    if not isinstance(x1, (int, float)) or not isinstance(y1, (int, float)):
        raise TypeError("Неправильний тип даних")
    elif y1 == 0:
        raise ZeroDivisionError("Ділити на нуль неможна")
    if op1 == "+":
        res = x1 + y1
        return float(res)
    elif op1 == "-":
        res = x1 - y1
        return float(res)
    elif op1 == "*":
        res = x1 * y1
        return float(res)
    elif op1 == "/":
        res = x1 / y1
        return float(res)
    else:
        return "ERROR"

