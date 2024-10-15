import pandas as pd
import matplotlib.pyplot as plt

# Llegeix el fitxer CSV
# Assegura't que el fitxer 'valors.csv' estigui en el mateix directori que aquest script
data = pd.read_csv('./resource/estadisticas.csv', header=None)

# Assigna les columnes a variables
x = data[0]
y = data[1]

# Crea el gràfic
plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.title('Gràfic de valors')
plt.xlabel('Eix X (Primera columna)')
plt.ylabel('Eix Y (Segona columna)')
plt.grid(True)
plt.xlim(min(x) - 0.01, max(x) + 0.01)  # Ajusta els límits de l'eix X
plt.ylim(min(y) - 5, max(y) + 5)  # Ajusta els límits de l'eix Y
plt.xticks(x)  # Marca les posicions dels valors de l'eix X
plt.yticks(range(int(min(y)), int(max(y)) + 10, 5))  # Marca les posicions dels valors de l'eix Y

# Mostra el gràfic
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# Llegeix el fitxer CSV
data = pd.read_csv('./resource/estadisticas.csv', header=None)

# Assigna les columnes a variables
x = data[0]
y = data[1]

# Crea el gràfic
plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.title('Gràfic de valors')
plt.xlabel('Eix X (Primera columna)')
plt.ylabel('Eix Y (Segona columna)')
plt.grid(True)
plt.xlim(min(x) - 0.01, max(x) + 0.01)  # Ajusta els límits de l'eix X
plt.ylim(min(y) - 5, max(y) + 5)  # Ajusta els límits de l'eix Y

# Marca les posicions dels valors de l'eix X
plt.xticks(x, rotation=45, ha='right')  # Rotació de les etiquetes de l'eix X

# Marca les posicions dels valors de l'eix Y
plt.yticks(range(int(min(y)), int(max(y)) + 10, 5))  # Marca les posicions dels valors de l'eix Y

# Mostra el gràfic
plt.tight_layout()  # Ajusta l'espai per evitar superposicions
plt.show()
