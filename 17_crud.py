# create, read, update, delete
numbers = [1, 2, 3, 4, 5, 6]
print(numbers[1])
numbers[-1] = 10
print(numbers)
numbers.append(700)
print(numbers)
numbers.insert(0, 'hola')
numbers.insert(3, 'adios')
print(numbers)
tasks = ['todo1', 'todo2', 'todo3']
new_list = numbers + tasks
print(new_list)
index = new_list.index(10)
new_list[index]= 'diez'
print(new_list)

new_list.remove('todo1')
print(new_list)

new_list.pop()
print(new_list)

new_list.pop(3)
print(new_list)

new_list.reverse()
print(new_list)

numbers_a = [1, 99, 50, 68, -1 ]
numbers_a.sort()
print(numbers_a)

strings = ['ab', 're', 'gb', 'ki', 'ml' ]
strings.sort()
print(strings)

#new_list.sort()
#print(new_list)

letters = ['A', 'B', 'C', 'D', 'E', 'F']

# Escribe tu solución 👇
letters.append('G')
letters[0] = 'Z'
ind = letters.index('C')
letters.remove('C')
letters.reverse()
print(letters)