##### MÉDIA DE NOTAS 
nome = input("digite o seu nome: ")
nota1 = float(input("digite a sua primeira nota: "))
nota2 = float(input("digite a sua segunda nota: "))
media = (nota1 + nota2) / 2
print(f"Olá {nome}, a sua média é: {media}")
print(f"Média: {media}")   
print("Aprovado" if media >= 5.75 else "Reprovado")
print("Seu rendimento melhorou" if nota1 < nota2 else "Seu rendimento piorou")





