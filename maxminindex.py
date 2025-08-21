n=int(input("Enter the value of n:"))
l=[]
for i in range(n):
  ele=int(input("Enter a number:"))
  l.append(ele)
max_value=max(l)
min_value=min(l)
print("Position of maximum element",l.index(max_value)+1)
print("Position of minimum element",l.index(min_value)+1)
