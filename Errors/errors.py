def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Division by 0 is meaninless"

print(divide(1, 0))
