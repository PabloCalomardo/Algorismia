#include <iostream>
#include <vector>
#include <string>
#include <random>
#include <iomanip>
#include <filesystem>
#include "Graf_impl.h"
using namespace std;

//Genera un graf amb n vèrtex i amb la probabilitat p de generar arestes entre vèrtexs
grafo genera_random(int n, float p) {
    grafo G;
    int pr = p*100;
    for (int i = 0; i < n; ++i) G.insert_vertice(i);  //Afegeix el node i al graf
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            int r = rand()%100;
            if (r < pr) G.insert_aresta(i,j); //Afegeix al node i una aresta al node j
        }
    }
    return G;
}


//Percolacion de vertice
void site_perlocation(grafo& grafo, double p) {

    //Generar distribucio aleatoria
    random_device gen_rand;
    default_random_engine generator(gen_rand());
    uniform_real_distribution<double> distribution(0,1);  

    double a; 
    list<pair<int, list<int>>> aux1 = grafo.get_vertices();
    for (auto itr = aux1.begin(); itr != aux1.end(); ++itr) {
        a = distribution(generator);
        if (a > (1-p)) {
            grafo.remove_vertice((*itr).first);
        }  
    }  
}

//percolacion de arestas
void bond_perlocation(grafo& grafo, double p) {

    random_device gen_rand;
    default_random_engine generator(gen_rand());
    uniform_real_distribution<double> distribution(0,1);


    double a;
    list<pair<int, list<int>>> aux1 = grafo.get_vertices();

    for (auto itr = aux1.begin(); itr != aux1.end(); ++itr) {
        for (auto itr2 = (*itr).second.begin(); itr2 != (*itr).second.end(); ++itr2) {
            a = distribution(generator);
            if (a > (1-p)) {
                grafo.remove_aresta((*itr).first, (*itr2));
            }  
        }
    }
}

int main() {
    ofstream file("estadisticas.csv");

    double p = 0.3;
    string directorio = "D:\\UNI 4rt\\A\\Algorismia\\docs";

    double percolados = 0;
    double descartados = 0; //si generamos un grafo y este desde el principio no es connexo no podemos ver el cambio de fase
    while(p <= 1){
        percolados = 0;
        descartados = 0;
        for(const auto& entry : filesystem::directory_iterator(directorio)){
            if(entry.is_regular_file() && entry.path().extension() == ".csv"){
                string filePath = entry.path().string();
                ifstream fgraf(filePath);

                grafo generat;
                generat.read(fgraf); //Inicialitzem el graf

                if (generat.size() > 0) { //descartamos un grafo en dos casos, si inicialmente no es connexo o si es un grafo vacio.
                int v = generat.get_element();
                int componentes = generat.CC(v);

                if (componentes > 1) ++descartados;
                else {
                    bond_perlocation(generat, p);
                    componentes = generat.CC(v);
                    if (componentes > 1) ++percolados;
                }
                } else ++descartados;
            }
        }
        double p_trans = double(percolados/(10.0-descartados));
        file << std::fixed << std::setprecision(3);
        file << p << "," << p_trans << endl;
        p += 0.01;
    }
}