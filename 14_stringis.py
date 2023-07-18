text = 'Ella sabe programar en Go'
'''
print('JavaScript' in text)
print('Python' in text)

if 'Python' in text:
  print('Elegiste Bien')
else:
  print('Que porqueria de lenguaje elegiste?')
  '''
size  = (len(text))
print(size)

print(text)
print(text.upper())
print(text.lower())
print(text.count('e'))
print(text.swapcase())
print(text.startswith('Ella'))
print(text.endswith('Go'))
print(text.replace('Go', 'PHP'))
text_2 = 'este es un titulo'
print(text_2)
print(text_2.capitalize())
print(text_2.title())
print(text_2.isdigit())
print("398".isdigit())