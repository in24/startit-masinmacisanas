with open('dati/auto_imports.csv',mode="r") as datne:
    dati = datne.read()

dati = dati.replace("gas","1")
dati = dati.replace("diesel","2")

with open('dati/auto_imports_degviela.csv',mode="w") as datne:
    datne.write(dati)
