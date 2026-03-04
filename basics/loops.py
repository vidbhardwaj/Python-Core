#for loop
for i in range(1, 6):
    print("For loop:", i)
# while loop
count = 1
while count <= 5:
    print("While loop:", count)
    count += 1
#break and continue
for i in range(1, 6):
    if i == 3:
        continue  # skip 3
    if i == 5:
        break     # stop at 5
    print("Loop with break/continue:", i)