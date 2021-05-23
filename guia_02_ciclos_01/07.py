primer_numero = int(input('Ingrese un número: '))
segundo_numero = int(input('Ingrese un segundo número: '))

if primer_numero > segundo_numero:
    num_superior = primer_numero
    num_inferior = segundo_numero
else:
    num_superior = segundo_numero
    num_inferior = primer_numero

diferencia = num_superior - num_inferior

for i in range(num_inferior, num_superior+1):
    if i % 2 == 0:
        print(i, end = ' ')
