#Prime Number
n=int(input())
count=0
temp=n
for i in range(1,n+1):
    if(n%i==0):
        count+=1
if(count==2):
    print("prime")
else:
    print("not prime")



#Factorial of a number
n=int(input())
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)


#Reverse the digits of a given number
n=int(input())
s=0
while(n!=0):
    d=n%10
    s=(s*10)+d
    n=n//10
print(s)


#sum of digits of a given number
n=int(input())
s=0
while n>0:
    d=n%10
    s=s+d
    n=n//10
print(s)

#fibonacci series upto n terms
n=int(input())
n1=0
n2=1
print("Fibonacci series:",n1,n2,end=" ")
for i in range(2,n):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")
