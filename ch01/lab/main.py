#PartA
weeks = 16
print("Number of weeks", type(weeks))
classes = 4
print("Number of classes", type(classes))
tuition = 6000
print("tuition",type(tuition))
cost_per_week = ((tuition/classes)/weeks)
print("Cost per week:", type(cost_per_week))
classes_per_week = 12
print("Classes per week", type(classes_per_week))
cost_per_class = cost_per_week/classes_per_week
print("Cost per class:", type(cost_per_class))
#PartB
import random
mylist=["yellow","banana","alien","cyan","panda"]
print(random.choice(mylist))