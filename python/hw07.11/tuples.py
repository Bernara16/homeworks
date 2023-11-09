# Exercises: Level 1
# 1
empty_tuple = tuple()

# 2
brothers_names = ("Mukhitdin", "Amanzhol", "Akhmed")
sisters_names = ("Bernara", "Gulya", "Aliya")

# 3
siblings = brothers_names + sisters_names
print(siblings)

# 4
print(len(siblings))

# 5
siblings = ('Mukhitdin', 'Amanzhol', 'Akhmed', 'Bernara', 'Gulya', 'Aliya')
family_members = list(siblings)
family_members.insert(0, "Bolat")
family_members.insert(1, "Yakhitzhan")
family_members = tuple(family_members)
print(family_members)



# Exercises: Level 2
# 1
family_members = ('Bolat', 'Yakhitzhan', 'Mukhitdin', 'Amanzhol', 'Akhmed', 'Bernara', 'Gulya', 'Aliya')
family_members = list(family_members)
first_item

# 2
fruits = ("Apple", "Orange", "Banana", "Strawberry")
vegetables = ("Potato", "Carrot", "Tomato", "Cucumber", "Onion")
animal_products = ("Meat", "Eggs", "Milk", "Fish")
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
 
# 3 
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
middle_index = int((len(food_stuff_lt) - 1) / 2)
middle_item = food_stuff_lt[middle_index]
print(middle_item)

# 4
food_stuff_lt = ['Apple', 'Orange', 'Banana', 'Strawberry', 'Potato', 'Carrot', 'Tomato', 'Cucumber', 'Onion', 'Meat', 'Eggs', 'Milk', 'Fish']
first_three_items = food_stuff_lt[0 : 3]
last_three_items = food_stuff_lt[-3 :]
print(f"First three items: {first_three_items}. Last three items: {last_three_items}")

# 5
del food_stuff_tp