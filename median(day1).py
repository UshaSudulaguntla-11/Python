n=int(input("Enter the value of n:"))
l=[]
for i in range(n):
  ele=int(input("Enter a number:"))
  l.append(ele)
l.sort()
print("sorted:",l)
if(n%2==0):
    median=l[n//2]+l[(n//2)-1]
else:
    median=l[(n-1)//2]
print("Median is",median)
