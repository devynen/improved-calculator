#program to print sum of even numbers from 1-100
total=0

for i in range(1,101):
	if i % 2 == 0:
		total += i
		 
print(total)		


#program to get unique characters in a string.
#using count method
string = "rpptooo"

for i in string:
	if string.count(i)==1:
		print(i)
 



#doing it without using method.
string = "longs"
dic = {}


for i in string:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1


for item in dic:
    if dic[item] == 1:
        print(item)

