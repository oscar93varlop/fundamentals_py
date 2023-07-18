'''
for element in range (1, 50):
	if element % 2 == 0:
	    print("El número", {element}, "es par.")
	else:
	    print("El número", {element},"es impar.")
'''

'''
with open("resultado.txt", "w") as archivo:
  for elemento in range(1, 50):
    if elemento % 2 == 0:
      mensaje = "El número {} es par.\n".format(elemento)
    else:
      mensaje = "El número {} es impar.\n".format(elemento)
    archivo.write(mensaje)

print('*' * 20)

filename = "my_file.txt"
counter = 0
try:
  # Using 'x' (exclusive creation) mode will create the file if it doesn't exist.
  # If it exists, it will raise a FileExistsError.
  with open(filename, 'x') as file:
    while counter < 100:
      counter = counter + 1
      text = str(counter)+"\n"
      file.write(text)
#    pass
except FileExistsError:
  print(f"{filename} already exists.")
  print('*' * 20)

'''
filename = "my_file.txt"
counter = 0
try:
  # Using 'x' (exclusive creation) mode will create the file if it doesn't exist.
  # If it exists, it will raise a FileExistsError.
  with open(filename, ' x') as file:
    while counter < 100:
      counter = counter + 1
      text = str(counter)+"\n"
      file.write(text)
    file.close()
except FileExistsError:
  print(f"{filename} already exists.")
  print('*' * 20)   
''''