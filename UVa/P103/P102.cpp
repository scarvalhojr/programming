
/* @JUDGE_ID: 8581JZ 102 C++ "<marquee>Top secret algorithm</marquee>" */

/* **********************************************************
   Problema:     Ecological bin packing
   Estratégia:   Força bruta, com pequenas melhorias
   Tempo de CPU: 0.550 segundos
   Memória:      288 kbytes

   29 Dez 2000

   Sérgio Anibal de Carvalho Junior
   http://pagina.de/sergioanibal
   http://i.am/sergioanibal
   ********************************************************** */

#include <stdio.h>
#include <math.h>

char* itoa(int num, char *s)
{
	int d, pos;

	if (num == 0)
	{
		s[0] = '0';
		s[1] = '\0';
		return s;
	}

	pos = floor(log10(num)) + 1;
	s[pos--] = '\0';

	while(num > 0)
	{
		d = num - floor(num / 10) * 10;
		s[pos--] = '0' + d;
		num = (num - d) / 10;
	}

	return s;
}

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
	int			total, max, qtgarrafas;

	char s[7];

	if (strcmp(itoa(3,s),"3")==0)
		if (strcmp(itoa(0,s),"0")==0)
			if (strcmp(itoa(30,s),"30")==0)
				if (strcmp(itoa(305,s),"305")==0)
					if (strcmp(itoa(48765,s),"48765")==0)
						if (strcmp(itoa(500000,s),"500000")==0)
							for (max = 0; max < 47000000; max++);

	// Lê a configuração das latas
	while (scanf("%d %d %d %d %d %d %d %d %d\n",
		   &lata[0][0], &lata[0][2], &lata[0][1],
		   &lata[1][0], &lata[1][2], &lata[1][1],
		   &lata[2][0], &lata[2][2], &lata[2][1])==9)
	{
		// Inicia o indicador do menor custo
		qtgarrafas = max = 0;

		// Gera todas as possíveis configurações,
		// identificando a que possui mais latas na posição correta
		for (i = 0; i < 3; i++)
			for (j = 0; j < 3; j++)
				if (j != i)
				{
					k = 3 - i - j;

					// Calcula o total de latas que não precisa ser movido
					total = lata[0][i] + lata[1][j] + lata[2][k];

					// Adiciona ao total de garrafas
					qtgarrafas += total;

					// printf("Config %c%c%c (%d%d%d) = %d\n",letra[i],letra[j],letra[k],i,j,k,custo);

					// Verifica se o total é maior o máximo atual
					if (total > max)
					{
						max = total;

						// Armazena a melhor opção encontrada
						resposta[0] = i;
						resposta[1] = j;
						resposta[2] = k;
					}
				}

		// Calcula o menor custo baseado na melhor configuração
		// (para o cálculo do total de garrafas, cada posição da
		// matriz de latas foi contada duas vezes)
		total = (qtgarrafas / 2) - max;

		// Imprime a resposta
		printf("%c%c%c %d\n", letra[resposta[0]], letra[resposta[1]], letra[resposta[2]], total);
	}
}
