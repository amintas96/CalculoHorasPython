from datetime import datetime, timedelta

hor1 = input("Digite a primeira hora: ")
time_1 = datetime.strptime(hor1, "%H:%M")

hor2 = input("Digite a hora que saiu para o almoço: ")
time_2 = datetime.strptime(hor2, "%H:%M")

soma_date = time_2 - time_1

hor3 = input("Digite a hora que voltou do almoço: ")
time_3 = datetime.strptime(hor3, "%H:%M")

hor4 = input("Digite a hora que terminou de trabalhar hoje: ")
time_4 = datetime.strptime(hor4, "%H:%M")

soma_date+= time_4 - time_3


print(soma_date)



