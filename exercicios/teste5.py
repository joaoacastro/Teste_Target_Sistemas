# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

# Entrada da string (pode ser substituída por input, se preferir)
string = "Exemplo de string a ser invertida"

# Inverte a string manualmente
string_invertida = ""
for i in range(len(string) - 1, -1, -1):
    string_invertida += string[i]

# Exibe o resultado
print(f"String original: {string}")
print(f"String invertida: {string_invertida}")

# Saída:
# String original: Exemplo de string a ser invertida
# String invertida: aditrevni res a gnirts ed olpmxE
