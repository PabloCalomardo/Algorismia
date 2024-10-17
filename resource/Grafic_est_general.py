#SCRIPT PER A CONSULTAR LES ESTADÍSTIQUES GENERALS I CREAR ELS GRÀFICS


import pandas as pd
import matplotlib.pyplot as plt

i = int(input("Introdueïx 1 al terminal si vols obtenir el grafic filtrat fins a p = 0.2, o 2 si vols obtenir el grafic amb totes les dades\n"))

if(i == 1):
    # Carrega les dades del fitxer estadisticageneral.csv
    df = pd.read_csv('estadisticageneral.csv')

    # Defineix el valor màxim de X (ID) que vols mostrar
    max_id = 0.2  # Canvia aquest valor segons el que necessitis

    # Filtra el DataFrame per mostrar només els valors fins al max_id
    df_filtered = df[df['ID'] <= max_id]

    # Crea el gràfic
    plt.figure(figsize=(10, 6))
    plt.plot(df_filtered['ID'], df_filtered['Mitjana'], linestyle='-', color='b')  # Sense marcador de punts

    # Configuració del gràfic
    plt.title('Visualització de la mitjana per identificador', fontsize=14)
    plt.xlabel('ID', fontsize=12)
    plt.ylabel('Mitjana', fontsize=12)

    # Mostra tots els valors de l'eix X
    plt.xticks(df_filtered['ID'], rotation=45)

    # Mostra el gràfic
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("outgeneral_filtered.png")
    plt.show()
else:
    # Carrega les dades del fitxer estadisticageneral.csv
    df = pd.read_csv('estadisticageneral.csv')

    # Crea el gràfic
    plt.figure(figsize=(10, 6))
    plt.plot(df['ID'], df['Mitjana'], linestyle='-', color='b')  # Sense marcador de punts

    # Configuració del gràfic
    plt.title('Visualització de la mitjana per identificador', fontsize=14)
    plt.xlabel('ID', fontsize=12)
    plt.ylabel('Mitjana', fontsize=12)

    # Configura l'eix X per mostrar només les dècimes (de 0 a 1)
    plt.xlim(0, 1)  # Estableix els límits de l'eix X
    plt.xticks([i/20 for i in range(21)])  # Crea ticks de 0.0 a 1.0

    # Mostra el gràfic
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("outgeneral_decimals.png")
    plt.show()
