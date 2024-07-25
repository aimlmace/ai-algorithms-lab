lookup_table = {
    ('A',0):"A is clean,no action needed",
    ('B',0):"B is clean,no action needed",
    ('A',1):"A is dirty,move to location a(left),clean A",
    ('B',1):"B is dirty,move to location b(right),clean B"
}

a = input("is a dirty?(y/n): ")
b = input("is b dirty?(y/n): ")
l = input("enter starting location(A/B): ")

performace_measure = 0

if l == 'a':
    if a == 'y':
        print(lookup_table[('A',1)])
        performace_measure+=1
    else:
        print(lookup_table[('A',0)])
    if b == 'y':
        print(lookup_table[('B',1)])
        performace_measure+=1
    else:
        print(lookup_table[('B',0)])
else:
    if b == 'y':
        print(lookup_table[('B',1)])
        performace_measure+=1
    else:
        print(lookup_table[('B',0)])
    if a == 'y':
        print(lookup_table[('A',1)])
        performace_measure+=1
    else:
        print(lookup_table[('A',0)])

print(f"performance measere : {performace_measure}")
print("succesful!")
