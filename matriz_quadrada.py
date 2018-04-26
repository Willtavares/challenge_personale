matrix = [[11,2,4],[4,5,6],[10,8,-12]]

# Será utilizado a regra de Sarrus
# Mas o enunciado pede a soma das diagonais. Diferente do propósito original da regra de Sarrus

valor1 = (matrix[0][0] + matrix [1][1] + matrix [2] [2]) + (matrix [0][1] + matrix [1][2] + matrix[2][0]) + (matrix[0][2] + matrix[1][0] + matrix[2][1])

valor2 = (matrix[0][1] + matrix[1][0] + matrix[2][2]) + (matrix[0][0] + matrix[1][2] + matrix[2][1]) + (matrix[0][2] + matrix[1][1] + matrix[2][0])

determinante = valor1 - valor2

print (determinante)