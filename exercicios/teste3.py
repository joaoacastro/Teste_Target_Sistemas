# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

# Lê o arquivo JSON
with open('../db/arquivo1.json', 'r') as file:
    dados = json.load(file)

# Inicializa as variáveis
menor_faturamento = float('inf')
maior_faturamento = float('-inf')
soma_faturamento = 0
dias_com_faturamento = 0
dias_acima_media = 0

# Processa os dados
for dia in dados:
    valor = dia['valor']
    
    # Considera apenas os dias com faturamento (ignora os dias com valor 0)
    if valor > 0:
        soma_faturamento += valor
        dias_com_faturamento += 1
        
        # Atualiza o menor e maior faturamento
        if valor < menor_faturamento:
            menor_faturamento = valor
        if valor > maior_faturamento:
            maior_faturamento = valor

# Calcula a média mensal
media_faturamento = soma_faturamento / dias_com_faturamento

# Verifica o número de dias acima da média
for dia in dados:
    if dia['valor'] > media_faturamento:
        dias_acima_media += 1

# Exibe os resultados
print(f'Menor faturamento: {menor_faturamento}')
print(f'Maior faturamento: {maior_faturamento}')
print(f'Dias com faturamento acima da média: {dias_acima_media}')

# Com o JSON fornecido (db/arquivo1.json), o programa calcularia o menor e maior faturamento e quantificaria os dias com faturamento acima da média. A saída seria algo como:

# Menor faturamento: 373.7838
# Maior faturamento: 48924.2448
# Dias com faturamento acima da média: 14
