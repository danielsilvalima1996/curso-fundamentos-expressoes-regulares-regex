import re

texto = '0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f'

pattern9 = re.compile('9')
match1 = re.search(pattern9, texto)
print(f'Posicoes: {match1.start()}, {match1.end()}; Valor: {match1.group(0)}.')

valores = re.findall('[a-f]', texto)
print(f'Valores: {valores}')