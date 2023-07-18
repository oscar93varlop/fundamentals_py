my_dict = {}
print(type(my_dict))
my_dict = {
  'name': 'oscar',
  'last': 'vargas',
  'age': 29,
  'single' : False
}
print(my_dict)
print(len(my_dict))
print(my_dict['age'])
my_dict['age'] = 30
print(my_dict)
print(my_dict['last'])
print(my_dict.get('name'))
print(my_dict.get('sinvalor'))
#print(my_dict['degree'])

print('single' in my_dict)
print('address' in my_dict)