a=[1,2,3,5,6]
for i in range(len(a)):
   sum=0
   for j in range(i,len(a)):
       sum+=a[j]
       sub_array=a[i:j+1]
       print(sub_array,":",sum)
