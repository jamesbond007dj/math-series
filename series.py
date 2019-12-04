def fibonacci(num):
    if num < 0:
        raise ValueError('numbers smaller than zero can not be used')
    if num == 1:
        return 0
    if num == 2:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)



def lucas(n):
    if n < 0:
        raise ValueError('numbers smaller than zero can not be used')
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)
