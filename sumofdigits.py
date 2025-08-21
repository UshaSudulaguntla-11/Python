n=int(input("Enter the value of n:"))
sum=0
rem=0
while(n!=0):
  rem=n%10
  sum+=rem
  n=n//10
print("Sum of digits:",sum)
