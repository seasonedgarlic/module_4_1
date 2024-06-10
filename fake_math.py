def divide(first, second):
    if second > 0 or second < 0:
        result = first / second
        return result
    elif second == 0:
        result = 'Error'
        return result
