#clase uso de concatenacion
name = "Oscar Adolfo"
last_name = "Vargas Lopez"
print(name)
print(last_name)
full_name = name + " "+ last_name
print(full_name)
age = 29
quote = "I'm Nicolas"
print(quote)
qoute2 = 'she said "Hello MTF"'
print(qoute2)
template = "Hola mi nombre es " + name + " y mi apellido es " + last_name
print(template)
template2 = "Hola mi nombre es {} y mi apellido es {}".format(name, last_name)
print(template2)
template3 = f"hola mi nombre es {name} y mi apellido es {last_name}"
print(template3)

# tres formas diferentes de obtener el mismo resultado (concatenar strings)
template = "Hola mi nombre es " + name + " y mi apellido es " + last_name + "y mi edad es "+str(age)
print(template)
template2 = "Hola mi nombre es {} y mi apellido es {} y mi edad es {}".format(name, last_name, age)
print(template2)
template3 = f"hola mi nombre es {name} y mi apellido es {last_name} y mi edad esa {age}"
print(template3)