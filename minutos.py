print ("Exercício 1")

print ("-----------------------------------------------------------------------------")

print()

segundos = float(input("Digite os segundos:"))

dia = segundos // 86400

rest_segundos_dia = dia % 86400

horas = segundos // 3600

segundos_restantes = horas % 3600

minutos = segundos_restantes //60

segundos_restantes_final = segundos_restantes % 60

print()

print(dia, "dia, ", horas, "horas, ", minutos, "minutos e", segundos_restantes_final, "segundos,")
