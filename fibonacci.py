def fibonacciRec(n):
    if n == 0 or n == 1:
        return n
    
    return fibonacciRec(n - 1) + fibonacciRec(n - 2)

def fibonacciIter(n):
    f = [0, 1]
    
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])
    
    return f[n]

def fibonacciIter2(n): 
    if n<=1:
        return n
    
    fibminus1=1
    fibminus2=0
    fib=0
    
    for i in range(2,n+1):
        fib=fibminus1+fibminus2
        fibminus2=fibminus1
        fibminus1=fib
    
    return fib

n=int(input("Enter n: "))
print(f"Recursive method, {n}th fibonacci number: {fibonacciRec(n)}")
print(f"Iterative method 1, {n}th fibonacci number: {fibonacciIter(n)}")
print(f"Iterative method 2, {n}th fibonacci number: {fibonacciIter2(n)}")
