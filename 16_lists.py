numbers = [1,2,3,4,5,6,7,8,9,10]
print(type(numbers))
print(numbers)
tasks = ['lavar los platos','jugar videojuegos','barrer la casa']
print(tasks)

types = [1, True, 'hola']
print(types)

print(numbers[0])
print(tasks[0])

tasks[0] = 'jugar volleyball'
print(tasks)
tasks[0] = 'bañarme'
print(tasks)
print(numbers[:3])
print(numbers[::2])

print(True in types)
print('hola' in types)