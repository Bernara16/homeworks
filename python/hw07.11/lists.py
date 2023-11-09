# Exercises: Level 1
# 1 
empty_list = list()
print(empty_list)

# 2
names = ['Bernara', 'Mukhit', "Aliya", 'Nazerke', 'Alfiya', 'Nurbek', 'Amanzhol', 'Miras', 'Aray']
print(names)

#3
print('Number of names:',len(names))

#4
first_item = names[0]
middle_index = int((len(names) - 1) / 2)
middle_item = names[middle_index]
last_item = names[-1]
print(first_item, middle_item, last_item)

#5
mixed_data_types = ['Bernara', 25, 171, 'not married', 'Akhrimenko']
print(mixed_data_types)

#6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#7
print(it_companies)

#8
print('Number of companies:', len( it_companies))

#9
first_company = it_companies[0]
middle_index = int((len(it_companies) - 1) / 2)
middle_company = it_companies[middle_index]
last_company = it_companies[-1]
print(first_company, middle_company, last_company)

# #10
# it_companies.insert(2, 'Intel')
# print(it_companies)

#11
it_companies.append('Dell Technoligies')
print(it_companies)
