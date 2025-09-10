n=int(input("Enter the value of n:"))
l=[]
for i in range(n):
  ele=int(input("Enter a number:"))
  l.append(ele)
freq={}
for i in l:
  if i in freq:
      freq[i]+=1
  else:
      freq[i]=1
if n==len(freq):
  print("None")
else:
  mode=max(freq,key=freq.get)
  print("Mode:",mode)
