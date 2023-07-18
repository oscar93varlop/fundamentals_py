person = {
  'name': 'oscar',
  'last': 'vargas',
  'skills': ['python', 'AWS', 'linux'],
  'age': 29,
  'single' : False
}
print(person)
person['name'] = 'Adolfo'
print(person)
person['age'] -= 5
print(person)
person['skills'].append('Terraform')
print(person)

del person['name']
print(person)
person.pop('age')
print('***items***')
print(person.items())
print('***keys***')
print(person.keys())
print('***values***')
print(person.values())

person2 = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'age': 29
}

# Escribe tu solución 👇
person2['twitter'] = '@nicobytes'
person2['name'] = 'Felipe'
person2.pop('age')
print(person2.keys())
print(person2.values())
print(person2)