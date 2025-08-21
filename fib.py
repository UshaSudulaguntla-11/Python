n=int(input("Enter the value of n:"))
fib1=0
fib2=1
fib_next=fib1+fib2
for i in range(n):
    print(fib1)
    fib_next=fib1+fib2
    fib1=fib2
    fib2=fib_next
