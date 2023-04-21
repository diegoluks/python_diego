segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs = int(segundos_str)

dias = total_segs // 86400
segs_rest = total_segs % 86400

horas = segs_rest // 3600
segs_rest = segs_rest % 3600

minutos = segs_rest // 60
segs_rest = segs_rest % 60

print("{} dias, {} horas, {} minutos e {} segundos.".format(dias, horas, minutos, segs_rest))
