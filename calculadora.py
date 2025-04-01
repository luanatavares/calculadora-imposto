# Função lambda: função para calcular imposto com base em porcentagens
calcular_imposto = lambda valor, taxa: valor * (taxa / 100)

# Função de alta ordem: recebe uma função para aplicar em cada valor de uma lista
def aplicar_imposto(lista, func, taxa):
    return [func(valor, taxa) for valor in lista]

# Closure: Função que retorna outra função que calcula o imposto específico para um tipo de imposto
def tipo_imposto(taxa):
    def calcular(tipo_valor):
        return tipo_valor * (taxa / 100)
    return calcular

# Usando a closure para criar duas funções com diferentes taxas de imposto
imposto_10 = tipo_imposto(10)
imposto_20 = tipo_imposto(20)

# Exemplo de valores de compras
valores_compras = [100, 200, 300, 400, 500]

# Usando a função de alta ordem para aplicar o imposto de 10% e 20% sobre os valores das compras
impostos_10 = aplicar_imposto(valores_compras, calcular_imposto, 10)
impostos_20 = aplicar_imposto(valores_compras, calcular_imposto, 20)

# Imprimir os resultados
print(f"Impostos com 10%: {impostos_10}")
print(f"Impostos com 20%: {impostos_20}")

# Usando a closure diretamente para calcular impostos
print(f"Impostos com 10% (via closure): {[imposto_10(valor) for valor in valores_compras]}")
print(f"Impostos com 20% (via closure): {[imposto_20(valor) for valor in valores_compras]}")

