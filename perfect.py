n=int(input("Enter the value of n:"))
sum=0
for i in range(1,n):
  if(n%i==0):
    sum+=i
if(sum==n):
  print(n,"is Perfect Number")
else:
    print(n,"is not a Perfect Number")
