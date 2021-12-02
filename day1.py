f=list(map(int,open("1.txt").read().splitlines()))
a=0
for i in range(len(f)-1):
 if f[i]<f[i+1]:a+=1
print(a)
b=0
for i in range(len(f)-3):
 if f[i]+f[i+1]+f[i+2]<f[i+1]+f[i+2]+f[i+3]:b+=1
print(b)

#sum()
#zip()