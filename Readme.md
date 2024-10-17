Algorismia:
Experiment de la probabilitat de Transició d'un graf geomètric de graella triangular

Funcionament:
1.  Desde el directori principal, Genera els Grafs Triangulars amb l'script Generador_Triangular.py 
2. Dins del directori /resource/, executa el programa main.exe, Això pot trigar una estona, ja que estarà executant l'experiment
3. Dins del directori /resource/, executa l'script Compactador_estadistiques.py que compactarà fent la mitjana de tots els documents estadisticas#.csv al document estadisticageneral.csv
4. Com a pas final, dins de /resource/, executa l'script Grafic_est_general.py per a poder observar els resultats



Notes:
1. Si desitjes visualitzar cap graf, executa el visualitzador.py i indica el path del fitxer .csv que conté el graf que desitjes visualitzar, et crearà un document .png al directori del graf on estarà la visualització.
2. Si desitjes que l'experiment guardi cada graf percolat, és recomanable que només hagis creat un graf amb el generador, ja que sinò et podrà crear un conjunt molt gran d'arxius .csv
3. Fixa't des d'on s'executa cada un dels scripts i executables, ja que funcionen amb camins absoluts i alguns poden fallar si no estas al directori indicat