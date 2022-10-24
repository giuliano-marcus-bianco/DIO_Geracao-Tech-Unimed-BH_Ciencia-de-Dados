# IS = Comparando se duas variáveis ocupam o mesmo lugar de memória

curso = 'Curso de Python'
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso

curso is not nome_curso

saldo is limite

saldo = 1000
limite = 500

saldo is limite
saldo is not limite