# fibonacci.py

def fib():
    fibs = [1, 2]

    for i in range(1,9):

        ''' 
        implement Fibonacci sequence to calculate the 
        first 10 Fibonacci numbers, note Fn = Fn-1 + Fn-2
        '''
        fiber = fibs[i] + fibs[i-1]
        fibs.append(fiber)
    return fibs

def main():
    print('OUTPUT', fib())


print('OUTPUT', fib())
