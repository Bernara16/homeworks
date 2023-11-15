# 1
dog = {}

# 2
dog.update({'name':'Bella'})
dog.update({'color':'gold'})
dog.update({'breed':'Golden Retriver'})
dog.update({'legs':4})
dog.update({'age':1})
print(dog)

# 3
student = {
    'first_name':'Bernara',
    'last_name':'Bolat',
    'gender':'Female',
    'age':25,
    'marital status':'single',
    'skills':['Python', 'C#', 'C++', 'Java', 'JavaScript'],
    'country':'Kazakhstan',
    'city':'Almaty',
    'address':{
        'street':'Sukhe-Bator',
        'zipcode': 56066
    }
}
print(student)

# 4
print(len(student))

# 5
values = len(student['skills'])
print(values)
