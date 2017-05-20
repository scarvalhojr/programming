
/* @JUDGE_ID: 8580TT 102 C++ "<marquee>Top secret algorithm</marquee>" */

/* **********************************************************
   Problema:     Ecological bin packing
   Estratégia:   Força bruta
   Tempo de CPU: ? segundos
   Memória:      ? bytes low memory spent

   19 Dez 2000

   Sérgio Anibal de Carvalho Junior
   http://pagina.de/sergioanibal
   http://i.am/sergioanibal
   ********************************************************** */

#include <stdio.h>
#include <string.h>

/*
 * Quantidade de tipos de vidros e latas diferentes
 */
const int DIM = 3;

/*
 * Declara um vetor bi-dimensional para armazenar
 * a quantidade de garrafas em cada lata ([lata][tipo])
 */
int 	lata[DIM][DIM];

char	letra[DIM];

/*
 * Calcula o custo de uma determinada configuração
 */
int custo(int p, int s, int t)
{
	int custo = 0;

	// printf("Calculando o custo de %d,%d,%d\n",p,s,t);

	for (int cor = 0; cor < DIM; cor++)
		if (cor != p)
			custo = custo + lata[0][cor];

	for (int cor = 0; cor < DIM; cor++)
			if (cor != s)
			custo = custo + lata[1][cor];

	for (int cor = 0; cor < DIM; cor++)
		if (cor != t)
			custo = custo + lata[2][cor];

	// printf("Config %c%c%c = %d\n",letra[p],letra[s],letra[t],custo);

	return custo;
}

/*
 * Programa principal
 */
void main()
{
	char		resposta[DIM + 1];
	int			c, min;

	const int	BROWN = 0;
	const int	CLEAR = 1;
	const int	GREEN = 2;

	letra[BROWN] = 'B';
	letra[CLEAR] = 'C';
	letra[GREEN] = 'G';

	// Lê a configuração das latas
	while (scanf("%d %d %d %d %d %d %d %d %d\n",
		   &lata[0][BROWN], &lata[0][GREEN], &lata[0][CLEAR],
		   &lata[1][BROWN], &lata[1][GREEN], &lata[1][CLEAR],
		   &lata[2][BROWN], &lata[2][GREEN], &lata[2][CLEAR])==9)
	{
		// Inicia o indicador do menor custo com um valor muito grande
		min = 32000;

		// Gera todas as possíveis configurações,
		// identificando a de menor custo
		for (int p = 0; p < DIM; p++)
			for (int s = 0; s < DIM; s++)
				if (s != p)
				{
					int t = DIM - p - s;

					// Calcula o custo desta configuração
					c = custo(p, s, t);

					// Verifica se o custo é menor que o mínimo atual
					if (c < min)
					{
						min = c;

						// Prepara a resposta
						resposta[0] = letra[p];
						resposta[1] = letra[s];
						resposta[2] = letra[t];
						resposta[3] = '\0';
					}
				}

		// Imprime a resposta
		printf("%c%c%c %d\n", resposta[0], resposta[1], resposta[2], min);
	}
}
