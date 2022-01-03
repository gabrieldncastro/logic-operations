"""Calculadora de IMC"""

height = float(input("Qual a sua altura? "))
weight = float(input("Qual é o seu peso? "))
media = (weight / (height * 2))

if media < 18.5:
    print('Você está abaixo do peso ideal')
elif media >= 18.6 and media <= 24.9:
    print('Você está no peso ideal')
elif media >= 25.0 and media <= 29.9:
    print('Você está acima do peso ideal')
elif media >= 30.0 and media <= 34.9:
    print('Você está com obesidade grau I')
elif media >= 35.0 and media <= 39.9:
    print('Você está com obesidade grau II (severa)')
else:
    print('Você está com obesidade grau III (mórbida)')
