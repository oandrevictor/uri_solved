#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

struct Aresta
{
	int origem, destino, peso;
};

bool compara(Aresta A, Aresta B)
{
	return (A.peso < B.peso);
}

int checa_ciclo(int p[], int origem, int destino)
{
	while (p[origem] > -1)
	{
		origem = p[origem];
	}

	while (p[destino] > -1)
	{
		destino = p[destino];
	}

	if (origem != destino)
	{
		p[destino] = origem;

		return 1;
	}

	return 0;
}

int main()
{
	int qtd_vertices, qtd_arestas;

	int p[200000];
	Aresta arestas[200000];

	while (cin >> qtd_vertices >> qtd_arestas)
	{
		if (qtd_vertices == 0 and qtd_arestas == 0)
		{
			return 0;
		}

		int custo = 0, custoTotal = 0;

		for (int i = 0; i < qtd_vertices; i++)
		{
			p[i] = -1;
		}

		for (int i = 0; i < qtd_arestas; i++)
		{
			cin >> arestas[i].origem >> arestas[i].destino >> arestas[i].peso;
			custoTotal += arestas[i].peso;
		}

		sort (arestas, arestas + qtd_arestas, compara);

		int i = 0;
		int j = 1;

		while (j < qtd_vertices and i < qtd_arestas)
		{
			if (checa_ciclo(p, arestas[i].origem, arestas[i].destino))
			{
				j++;
				custo = custo + arestas[i].peso;
			}

			i++;
		}

		cout << custoTotal - custo << endl;
	}

	return 0;
}
