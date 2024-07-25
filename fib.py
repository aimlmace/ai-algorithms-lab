n=int(input("Enter No. of terms"))

f1=0
f2=1
next=f2
count = 2
print(f1,"",f2,end=" ")
while n>=count:
	next=int(f1)+int(f2)
	print(next,end=" ")
	f1,f2=f2,next
	count+=1
print()	
