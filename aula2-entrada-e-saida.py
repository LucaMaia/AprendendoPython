nome = input("Escreva seu nome:")
idade = input("Escreva sua idade:")
altura = input("Escreva sua altura:")

# Concatenação com vígula
print(nome, 'tem', idade, 'anos')
print("e" , altura, "de altura")

# Concatenação com +
print(nome + "tem" + str(idade) + "anos")
print("e" + str(altura) +  "de altura")

print(type(nome))
