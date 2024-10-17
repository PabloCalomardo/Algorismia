import pandas as pd
import matplotlib.pyplot as plt

# Carrega les dades del fitxer estadisticageneral.csv
df = pd.read_csv('estadisticageneral.csv')

# Crea el gràfic
plt.figure(figsize=(10, 6))
plt.plot(df['ID'], df['Mitjana'], linestyle='-', color='b')  # Sense marcador de punts

# Configuració del gràfic
plt.title('Visualització de la mitjana per identificador', fontsize=14)
plt.xlabel('ID', fontsize=12)
plt.ylabel('Mitjana', fontsize=12)

# Mostra tots els valors de l'eix X
plt.xticks(df['ID'], rotation=45)

# Mostra el gràfic
plt.grid(True)
plt.tight_layout()
plt.show()
