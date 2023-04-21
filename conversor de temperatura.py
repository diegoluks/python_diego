temperaturaFahrenheit = input("Digite uma temperatura em Fahrenheit: ")
temperaturaCelsius = (float(temperaturaFahrenheit) -32) *5 /9
c = float(input("Digite uma temperatura em Celsius: "))
f = ((9 * c) / 5) + 32
print("A temperatura em Celsius é {:.2f}C°".format(temperaturaCelsius))
print("A temperatura em Fahrenheit é {:.2f}°F".format(f))


