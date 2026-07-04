
# Coleta de dados
print('Identificador de palavra')

#Palavra chave
key = str(input('Digite a palavra que quer achar: ')).strip().lower()

#Texto
txt = str(input('Cole o texto: ').strip().lower())

#Resultado
print(f'Seu texto tem a palavra '{key}'? {key in txt}')
