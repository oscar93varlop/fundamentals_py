recepts = input("Ingresa la cantidad de recepciones")
sets = input("Ingresa la cantidad de set realizados por el jugador")
attacks = input("ingresa la cantidad de ataques realizados por el jugador")

recepts = int(recepts)
sets = int(sets)
attacks = int(attacks)

total_interaction = recepts + sets +  attacks
print(" el total de las interacciones con el balon fueron ", total_interaction)

average_interaction = total_interaction / 3
print(" promedio de interaccion con el balon ", average_interaction)