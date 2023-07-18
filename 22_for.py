'''
for element in range   (1, 21):
  print(element)

for element in range (20):
  print(element)
'''
mylist = [23, 45, 67, 89, 100, 5, 15]
for item in mylist:
  print(item)

mytuple = ('oscar', 'sergio', 'diego')
for item in mytuple:
  print(item)

product = {
  'name': 'imp laser',
  'valor': 500,
  'stock': 45
}

for element in product:
  print(element)

for element in product:
  print(product[element])

for key in product:
  print(key, '=>', product[key])

for key, value in product.items():
  print(key, '=>', value)

people = [
  {
    'name': 'oscar',
    'age': 29
    
  },
  {
    'name': 'sergio',
    'age': 33
  },
  {
    'name': 'diego',
    'age': 35
  }
]

for person  in people:
  print(person)

for person  in people:
  print('name =>', person['name'])

my_list = [1, -1, 2, -2, 3, -3, 4, -4]
new_list = []

# Escribe tu solución 👇
for number in my_list:
  if number > 0:
    new_list.append(number)

print(new_list)