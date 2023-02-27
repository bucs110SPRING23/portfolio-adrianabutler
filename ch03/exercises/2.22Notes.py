# iteration
# iterable -- you can loop over it
mystr = "hello" # special iterable list of characters
mynums = [1, 2, 3, 4, 5]

for ch in mystr:
    print(ch)

for nums in mynums:
    print(nums)

# anything iterable can be 'indexed' into 

print(mystr[0], mystr[1], mystr[2], mystr[3], mystr[4])

# mynums[0] = "J" - cant do this

# mutable - changable
# immutable - can't be changed once created

nums = 5
mystr = "hello" # immutable
myotherstring = "hello"

mynums = [1, 2, 3, 4, 5] #mutable
myothernums= [1, 2, 3, 4, 5]

if mystr == myotherstring:
    print("They are the same")
if mynums == myothernums:
    print("They are the same")
if mystr is myotherstring:
    print("They are the same")
if mynums is myothernums:
    print("They are the same")

# substring

mystr = "hello"
print(mystr[0])
print(mystr[1:4])

mystr2 = mystr[0:5]
print(mystr,mystr2)

#index = 0
for i,v in enumerate(mynums):
#    mynums[index]= i * 2
    print(i)
print(mynums)

mynums = (5,8,1002,5) # now mutable when used parenthesis
# tuple - immutable list

x = 4
y = 3

temp = x
x=y
y = temp

x,y = y,x

num = [5] * 3
print (num)

num2 = (5) * 3
print(num2)

contacts = {"Bill": "768-3425","Suzie": "345-1294"}
name = input("Enter a name:")
for contact in contacts:
    if contact[0] == name:
        print(contacts(1))
        break
print(contacts["Suzie"])

