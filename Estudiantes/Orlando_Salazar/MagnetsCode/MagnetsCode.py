""" 
Titulo:            MagnetsCode.py
Descripcion:       Proyecto Ordenar codigo para procesar archivo de texto y dar como salida otro archivo con los valores agregados al I.V.A
Requirimientos:    Interprete Python
Uso:               py .\\MagnetsCode.py 
Escrito por:       Orlando Salazar<orsaac@gmail.com>
Fecha:             2024-04-22
 """

impuesto = 1.13

with open('lista_compras.txt', 'r') as f:
    lista = f.readlines()
    
quita_fin_de_linea = [elemento.rstrip() for elemento in lista]

lista_fruta_precio = [elemento.split(',') for elemento in quita_fin_de_linea]

lista_fruta_precio_impuesto = []
for fruta, precio in lista_fruta_precio:
	lista_fruta_precio_impuesto.append([fruta, str(round(int(precio) * impuesto))])
    
list_reglon = [','.join(elemento) for elemento in lista_fruta_precio_impuesto]

pone_fin_de_linea = [f'{elemento}\n' for elemento in list_reglon]

with open('lista_compras_procesada.txt', 'w') as f:
	f.writelines(pone_fin_de_linea)
    
