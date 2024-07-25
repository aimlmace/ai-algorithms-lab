a = int(input("Enter '1/0' if a is dirty "))
b = int(input("Enter '1/0' if b is dirty "))

loc = input("Enter the starting location ")

lookup_table = {
    ('a',0):"A is clean.Moving to location B",
    ('a',1):"A is not clean.Cleaning.Moving to left",
    ('b',0):"B is clean.Moving to location A",
    ('b',1):"B is not clean.Cleaning.Moving to right",
}
count= int(0)  
p = int(0) 

def clean(x):
    global count
    global p
    if count<2:
        if x == 'a':
            if a:
                print(lookup_table[('a',1)])
                p+=1
                count+=1
            else:
                print(lookup_table[('a',0)])
                count+=1
            clean('b')
        elif x == 'b':
            if b:
                print(lookup_table[('b',1)])
                p+=1
                count+=1
            else:
                print(lookup_table[('b',0)])
                count+=1
            clean('a')
clean(loc)

print(f"Performance measure:{p}")
