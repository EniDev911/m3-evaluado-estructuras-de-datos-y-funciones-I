import sys

if len(sys.argv) >= 5:

    conversiones = {
        "Soles": sys.argv[1],
        "Pesos Argentinos": sys.argv[2],
        "Dólares": sys.argv[3]
    }

    pesos_chileno = int(sys.argv[4])

    print("Los", pesos_chileno, "equivalen a:")
    for k,v in conversiones.items():
        print(pesos_chileno * float(v), k)

else:
	print("Debes pasarme como mínimo 4 argumentos desde la línea de comando. En este orden:")
	print(*["Sol Peruano", "Peso Argentino", "Dólar americano", "Peso Chileno"], sep="\n")
	print("$python conversiones.py 0.0046 0.093 0.0013 10000")