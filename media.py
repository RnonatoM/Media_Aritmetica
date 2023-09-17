# Programa para ler as duas notas de um aluno, calcular a sua média e mostrar se ele foi aprovado ou reprovado

# Declaração das variáveis
nota1 = float()
nota2 = float()
media = float()

# Leitura das notas do usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Cálculo da média
media = (nota1 + nota2) / 2

# Verificação da aprovação
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
