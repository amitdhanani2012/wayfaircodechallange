
from itertools import combinations
a=[-1,-1,2,4,5,0,-4,3,1,1,-2]
positive1=[]
negative1=[]
zero=[]
zero1=[]
zero2=[]

# I used two loops only. It will print combinations of sum zero. Only two pair combination with one loop used. Last loop is checking negative and positive with pair summation
#  Two combinations will reduce time.

for i in set(a):
    if i>=0:
        positive1.append(int(i))
      
    elif i<=0:
        negative1.append(int(i))


#non repeat combination not permutations
h1=list(combinations(positive1,2))
g1=list(combinations(negative1,2))


for h,g in zip(h1,g1):
    x=sum([h[0],h[1]])
    if -abs(x) in negative1:
        zero.append([h[0],h[1],-x])
    y=sum([g[0],g[1]])
    if abs(y) in positive1:
        zero.append([g[0],g[1],-y])
    
print(zero)

