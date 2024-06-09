<a href="https://colab.research.google.com/gist/EniDev911/669439a13875ab1601ef16887ca2cf3d/estructura-de-datos-y-funciones.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## Actividad 1 - Conversiones

### Enunciado

Crear un archivo programa usando una estructura de datos apropiadas que permita ingresar tasas de conversión. Las distintas tasas de conversión se deben ingresar mediante en el siguiente orden:

- Sol
- Peso Argentino
- Dolár Americano

Para ello considere las siguientes tasas de conversión de Peso Chileno:

- a Sol peruano: **0.0046**
- a Peso Argentino: **0.093**
- Dólar Americano: **0.00013**

Además, ingrese un 4to valor que será el valor chileno a convertir. El programa debe devolver el valor en peso chileno de las 3 divisas ingresadas.


```python
conversiones = {
    "Soles": input("Introduce el valor de la divisa en Soles Peruanos (0.0046): "),
    "Pesos Argentinos": input("Introduce el valor de la divisa en Peso Argentino (0.093): "),
    "Dólares": input("Introduce el valor de la divisa en Dólar Americano (0.0013): ")
}

pesos_chileno = input("Introduce el valor en Peso Chileno a convertir: ")

print("Los", pesos_chileno, "equivalen a:")
for k,v in conversiones.items():
    print(int(pesos_chileno) * float(v), k)
```

    Introduce el valor de la divisa en Soles Peruanos (0.0046): 0.0046
    Introduce el valor de la divisa en Peso Argentino (0.093): 0.093
    Introduce el valor de la divisa en Dólar Americano (0.0013): 0.0013
    Introduce el valor en Peso Chileno a convertir: 10000
    Los 10000 equivalen a:
    46.0 Soles
    930.0 Pesos Argentinos
    13.0 Dólares


## Actividad 2 - Word Count

### Enunciado

El texto **lorem ipsum** es un texto que se utiliza para demostrar tipografías además de usarse para rellenar espacios que requieran largos textos.

Genere un archivo llamado `word_count.py` que importe un texto a Python y realice las siguientes tareas:

- Utilizando una estructura de datos apropiada, cuente la cantidad de caracteres distintos que componen un texto.

- Cuente el número de palabras distintas que componen el texto ingresado. Para separar un texto puede utilizar el método `.split()`


> **TIP:** Para importar texto en python puede adaptar el siguiente código

```python
with open("texto.txt", "r") as file:
	texto = file.read()
```

Donde `texto.txt` corresponderá a la ruta del archivo a importar.

Para comprobar el correcto funcionamiento del código se provee el archivo **lorem_ipsum.txt**. Al ejecutar el programa se espera el siguiente output:

```bash
python word_count.py lorem_ipsum.txt
```

Respuesta esperada:

```plaintext
El número de caracteres distintos es: 40
El número de palabras distintas es: 243
```


```python
filename = "lorem_ipsum.txt"

with open(filename) as file:
  contenido = file.read()
  palabras_separadas = str(contenido).split(" ")

palabras_unicas = set(palabras_separadas)
caracteres_unicos = set(" ".join(palabras_separadas))

print("El número de caracteres distintos es:", len(caracteres_unicos))
print("El número de palabras distintas es:", len(palabras_unicas))
```

    El número de caracteres distintos es: 40
    El número de palabras distintas es: 243


## Actividad 3 - Recordatorios

### Enunciado

Se provee el archivo `recordatorio.py` que incluye una serie de eventos que quieren ser recordados por usted. El formato de estos recordatorios son una fecha (año-mes-día), una hora y una descripción del evento.

Aplicando métodos apropiados para la estructura de datos entregada edite la lista recordatorios de la siguiente manera:


1. Agregue un evento el `2 de Enero de 2021` a las `6 de la mañana` para `"Empezar el Año"`.
2. Al revisar los eventos, nota un error, ya que el `15 de Julio` no es feriado. Editar de tal manera que sea el `16 de Julio`.
3. Lamentablemente le tocará trabajar el día del trabajo (`1 de Mayo`). Elimine el evento del día de trabajo.
4. Agregue una cena de Navidad (`24 de diciembre`) y de Año Nuevo (`31 de diciembre`) cuando corresponda. Ambas a las `22 hrs.


```python
recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

# Formato: (YEAR-MONTH-DAY)

# 1. Agregue un evento el 2 de febrero del 2021 a las 6 de la mañana
# para 'Empezar el Año'
recordatorios.insert(1, ["2021-01-02", "06:00", "Empezar el Año"])

# 2. Al revisar los eventos, nota un error, ya que el 15 de Julio no es feriado.
# Editar de tal manera que sea el 16 de Julio.
pos = recordatorios.index(['2021-07-15', "13:00", "No hacer nada es feriado"])
recordatorios[pos][0] = '2021-07-16'

# 3. Lamentablemente le tocará trabajar el día del trabajo (2021-05-01).
# Elimine el evento del día del trabajo.
recordatorios.remove(['2021-05-01', "15:00", "No trabajar"])

# 4. Agregue una cena de Navidad y de Año Nuevo cuando corresponda
# Ambas a las 22:00 hrs
pos = recordatorios.index(['2021-12-25', "00:00", "Navidad"])
recordatorios.insert(pos, ['2021-12-24', "22:00", "Cena de Navidad"])
recordatorios.append(['2021-12-31', "22:00", "Cena de Año Nuevo"])

# Output
print(*recordatorios, sep="\n")
```

    ['2021-01-01', '11:00', 'Levantarse y ejercitar']
    ['2021-01-02', '06:00', 'Empezar el Año']
    ['2021-07-16', '13:00', 'No hacer nada es feriado']
    ['2021-09-18', '16:00', 'Ramadas']
    ['2021-12-24', '22:00', 'Cena de Navidad']
    ['2021-12-25', '00:00', 'Navidad']
    ['2021-12-31', '22:00', 'Cena de Año Nuevo']

