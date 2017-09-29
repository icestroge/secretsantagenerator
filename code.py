import random

list1 = []

file = open("people.txt", "r")

for i in file:
	list1.append(str(i)[:-1])


print(list1)
random.shuffle(list1)
print(list1)
offset = random.randint(1, len(list1) - 1)
print(offset)

list2 = []

for i in range(len(list1)):
	index = i + offset
	if index > len(list1) - 1:
		index = index - len(list1)

	list2.append(list1[index])

print(list2)

index = 0
for i in list1:	
	message = open(str(i)+ ".txt", "w")
	message.write(str(i) + " you are buying for: " + str(list2[index]))
	message.close()
	index = index + 1