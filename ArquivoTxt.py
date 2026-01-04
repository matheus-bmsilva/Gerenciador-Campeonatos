L1=[]
D1={}
with open("dados.txt","r") as RP:
    for i in RP:
        L1.append(i.rstrip().split(","))
#print (L1)
for i in L1:
    D1[i[0]]=[i[1],float(i[2])]
print (D1)
