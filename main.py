import random
options = ('piedra', 'papel', 'tijera')
turnos = int(input('Elige la cantidad de turnos'))

if turnos % 2 != 0 and turnos < 10:
  turno = 0
  for turno in range(turnos):
    wins_user =0
    wins_machine =0
    user_option = input('Elige entre piedra, papel o tijera')
    user_option = user_option.lower()
    if not user_option in options:
      print('esa opción no es valida')
    machine_option = random.choice(options)
    print('la opion del usuaro es', user_option)
    print('la opcion de la maquina es', machine_option)
    if user_option == machine_option:
      print("esto es un empate")
    
    elif user_option == 'tijera':
      if machine_option == 'papel':
        print('tijera gana a papel')
        print('gano el usuario')
      elif machine_option == 'tijera':
        print('esto es un empate')
        print('nadie gana')
      else:
        print('Piedra gana a tijera')
        print('la maquina gana ')
    elif user_option == 'papel':
      if machine_option == 'piedra':
        print('papel  gana a piedra')
        print('gano el usuario')
      elif machine_option == 'papel':
        print('esto es un empate')
        print('nadie gana')
      else:
        print('tijera gana a papel')
        print('la maquina gana ')
    elif user_option == 'piedra':
      if machine_option == 'tijera':
        print('piedra  gana a tijera')
        print('gano el usuario')
      elif machine_option == 'piedra':
        print('esto es un empate')
        print('nadie gana')
      else:
        print('Papel gana a piedra')
        print('la maquina gana ')
    
else:
  print("la cantidad de turnos debe ser impar para que halla un ganador ")
