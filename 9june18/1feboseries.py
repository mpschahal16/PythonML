a=0
b=1
sum=a+b
num=int(input("Enter the Last tesrm range :"))
print(a,"\t",b,end="\t")
while(sum<=num):
    print(sum,end="\t")
    a=b
    b=sum
    sum=a+b