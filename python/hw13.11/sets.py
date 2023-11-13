# Exercises: Level 1
# 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

# 2
it_companies.add('Twitter')
print(it_companies)

# 3
it_companies.update(['Oracle', 'SAP', 'Intel'])
print(it_companies)

# 4
it_companies.remove('Amazon')
print(it_companies)


# Exercises: Level 2
# 1
vegetables = {'Potato', 'Carrot', 'Tomato', 'Cucumber', 'Onion'}
animal_products = {'Meat', 'Eggs', 'Milk', 'Fish'}
print(vegetables.union(animal_products))

# 2
A = {'Facebook', 'Google', 'Microsoft', 'Apple'}
B = {'Apple', 'IBM', 'Oracle', 'Amazon'}
print(A.intersection(B))


# 3
print(A.issubset(B))

# 4
print(A.isdisjoint(B))

# 5
A = {'Facebook', 'Google', 'Microsoft', 'Amazon', 'Oracle', 'Apple'}
B = {'Apple', 'IBM', 'Oracle', 'Amazon', 'SAP', 'Facebook'}
print(A.union(B))
print(B.union(A))

# 6
print(A.symmetric_difference(B))

# 7
del A






     

