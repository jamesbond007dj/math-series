def fibonacci(n):
    if n < 0:
        raise ValueError('numbers smaller than zero can not be used')
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)



def lucas(n):
    if n < 0:
        raise ValueError('numbers smaller than zero can not be used')
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)

def sum_series(n, a=0, b=1):
    if n < 0:
        raise ValueError('numbers smaller than zero can not be used')
    if n == 0:
        return a
    if n == 1:
        return b
    else:
        return sum_series(n-1,a,b)+sum_series(n-2,a,b)


