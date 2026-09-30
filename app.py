# Projeto Exemplo: Calculadora de Média do Aluno

def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

print("\033[36;40m=\033[m" * 40)
print("       \033[36mSistema de Notas do Aluno\033[m")
print("\033[36;40m=\033[m" * 40)

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = calcular_media(n1, n2)

print(f"A média final é: {media:.2f}")


if media >= 7:
    print("Status: \033[32mAPROVADO!\033[m")
elif media == 6:
    print("Status: \033[33mRECUPERAÇÃO\033[m")
else:
    print("Status: \033[31mREPROVADO!\033[m")