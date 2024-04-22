# Lectura y escritura de archivos en Python para análisis de datos

**1. Lectura de archivos:**

**1.1 Abriendo la puerta a los datos con** open()

Para leer un archivo, utilizamos la función open(), la cual nos devuelve un objeto file. Este objeto nos permite acceder al contenido del archivo. Veamos la sintaxis básica:


```python
archivo = open("archivo.txt", "r")  # "r" indica modo lectura
```


**Explicación:**

- archivo es la variable que almacena el objeto file asociado al archivo "archivo.txt".
- "r" indica que abrimos el archivo en modo lectura.

**1.2 Leyendo línea a línea con** readline()

  La función readline() lee una línea del archivo a la vez y la devuelve como una cadena de texto. Veamos un ejemplo:


```python
linea = archivo.readline()
print(linea)  # Imprime la línea leída

# Leyendo y procesando cada línea
while linea:
    # Procesar la línea aquí (por ejemplo, limpiar o analizar datos)
    linea = archivo.readline()
```

  **Explicación:**

- linea almacena la línea leída del archivo.
- print(linea) muestra la línea en la consola.
- El bucle while lee líneas hasta que no haya más en el archivo.

**1.3 Leyendo todo el contenido con** read()

  Si deseas leer todo el contenido del archivo a la vez, puedes usar read():


```python
contenido = archivo.read()
print(contenido)
```

**Explicación:**

- contenido almacena todo el texto del archivo como una cadena de texto.
- print(contenido) muestra todo el contenido en la consola.

**1.4 Cerrando la puerta con** close()

  Es fundamental cerrar el archivo una vez que termines de usarlo:



```python
archivo.close()
```

**Explicación:**

- archivo.close() libera los recursos asociados al archivo y garantiza su correcto cierre.

**2. Escritura de archivos:**

**2.1 Creando y escribiendo con** open()

  Para escribir en un archivo, utilizamos open() en modo escritura:


```python
archivo = open("archivo_nuevo.txt", "w")  # "w" indica modo escritura
archivo.write("¡Hola, mundo!\n")  # Escribe una línea en el archivo
archivo.close()
```

  **Explicación:**

- archivo es la variable que almacena el objeto file asociado al archivo "archivo\_nuevo.txt".
- "w" indica que abrimos el archivo en modo escritura (sobrescribiendo el contenido existente).
- archivo.write("¡Hola, mundo!\n") escribe la cadena "Hola, mundo!" en el archivo, incluyendo un salto de línea (\n).
- archivo.close() cierra el archivo.


**2.2 Agregando contenido con** append()

  Si deseas agregar contenido al final de un archivo existente, utiliza el modo append:


```python
archivo = open("archivo_existente.txt", "a")
archivo.write("¡Más datos para el archivo!\n")
archivo.close()
```

**Explicación:**

- "a" indica que abrimos el archivo en modo append (agregando contenido al final).
- La escritura funciona igual que en modo w.

**3. Manejo de excepciones:**

  **3.1 Protegiéndonos con** try...except

  Es importante proteger nuestro código de posibles errores al trabajar con archivos. Para ello, utilizamos el bloque try...except:


```python
try:
    archivo = open("archivo.txt", "r")
    # Operaciones con el archivo
except Exception as e:  # Captura cualquier excepción
    print(f"Error al abrir el archivo: {e}")
finally:
    if archivo:
        archivo.close()
```

  **Explicación:**

- try: contiene el código que podría generar errores.
- except Exception as e: captura cualquier excepción que ocurra en el bloque try.
- print(f"Error al abrir el archivo: {e}") muestra un mensaje de error con la información de la excepción.
- finally: se ejecuta siempre, incluso si hay un error o no.
