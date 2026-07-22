
# Coleta de dados
print('Identificador de palavra')

#Palavra chave
key = str(input('Digite a palavra que quer achar: ')).strip().lower()

#Texto
txt = str(input('Cole o texto: ').strip().lower())

#Resultado
print(f'Seu texto tem a palavra '{key}'? {key in txt}')

#Código bem simples, consiste em achar uma palavra específica dentro de um texto. 
#Como funciona? basta digitar a palavra que queira achar, logo depois o texto escolhido. 
