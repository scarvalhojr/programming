
/* @JUDGE_ID: 8580TT 102 C++ "<marquee>Top secret algorithm</marquee>" */

/* **********************************************************
   Problema:     Ecological bin packing
   Estratégia:   Força bruta, calculando custo relativo à
   				 quantidade total de garrafas
   Tempo de CPU: 0.560 segundos
   Memória:      288 kbytes

   25 Dez 2000

   Sérgio Anibal de Carvalho Junior
   http://pagina.de/sergioanibal
   http://i.am/sergioanibal
   ********************************************************** */

#include <stdio.h>
#include <string.h>

/*
 * Programa principal
 */
void main()
{
	// Quantidade de tipos de vidros e latas diferentes
	// const int	DIM = 3;

	// Tipos de garrafas
	// const int	BROWN = 0;
	// const int	CLEAR = 1;
	// const int	GREEN = 2;

	// Declara um vetor bi-dimensional para armazenar
	// a quantidade de garrafas em cada lata ([lata][tipo])
	int 		lata[3][3];

	// Letras que representam os tipos de garrafas
	const char	letra[3] = {'B','C','G'};

	char		resposta[3], i, j, k;
	int			qtgarrafas, custo, max;

	// Lê a configuração das latas
	while (scanf("%d %d %d %d %d %d %d %d %d\n",
		   &lata[0][0], &lata[0][2], &lata[0][1],
		   &lata[1][0], &lata[1][2], &lata[1][1],
		   &lata[2][0], &lata[2][2], &lata[2][1])==9)
	{
		// Calcula a quantidade total de garrafas
		qtgarrafas = 0;
		for (i = 0; i < 3; i++)
			for (j = 0; j < 3; j++)
				qtgarrafas += lata[i][j];

		// Inicia o indicador do menor custo
		max = 0;

		// printf("Qtde de garrafas: %d\n", qtgarrafas);

		// Gera todas as possíveis configurações,
		// identificando a que possui mais latas na posição correta
		for (i = 0; i < 3; i++)
			for (int j = 0; j < 3; j++)
				if (j != i)
				{
					k = 3 - i - j;

					// Calcula o total de latas que não precisa ser movido
					custo = lata[0][i] + lata[1][j] + lata[2][k];

					// printf("Config %c%c%c (%d%d%d) = %d\n",letra[i],letra[j],letra[k],i,j,k,custo);

					// Verifica se o custo é menor que o mínimo atual
					if (custo > max)
					{
						max = custo;

						// Prepara a resposta
						resposta[0] = letra[i];
						resposta[1] = letra[j];
						resposta[2] = letra[k];
					}
				}

		// Calcula o menor custo
		custo = qtgarrafas - max;

		// Imprime a resposta
		printf("%c%c%c %d\n", resposta[0], resposta[1], resposta[2], custo);
	}
}
