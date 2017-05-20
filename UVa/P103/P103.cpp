
/* @JUDGE_ID: 8580TT 103 C++ "<marquee>Top secret algorithm</marquee>" */

/* **********************************************************
   Problema:     Stacking Boxes
   Estratégia:   Força bruta
   Tempo de CPU: ? segundos
   Memória:      ? kbytes

   1 Jan 2001

   Sérgio Anibal de Carvalho Junior
   http://pagina.de/sergioanibal
   http://i.am/sergioanibal
   ********************************************************** */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

// Limites da entrada
const int MAXDIM = 10;
const int MAXQTCAIXAS = 30;

// Características da entrada
int dim, qtcaixas;

// Matriz de dimensões das caixas
int caixa[MAXQTCAIXAS][MAXDIM];

// Ordem das caixas
int ordem[MAXQTCAIXAS];

// Resposta (sequência e quantidade de caixas da sequência)
int prox[MAXQTCAIXAS], cont[MAXQTCAIXAS];

/*
 * Converte um número para string
 */
void itoa(int num, char *s)
{
	int d, pos;

	if (num == 0)
	{
		s[0] = '0';
		s[1] = '\0';
		return;
	}

	pos = floor(log10(num)) + 1;
	s[pos--] = '\0';

	while(num > 0)
	{
		d = num - floor(num / 10) * 10;
		s[pos--] = '0' + d;
		num = (num - d) / 10;
	}
}

/*
 * Classifica as dimensões de uma determinada caixa
 */
void classificarDimensoes (int c)
{
	int i, temp, troca;

	for (int p = dim - 1; p >= 1; p--)
	{
		troca = 0;

		for (i = 0; i < p; i++)
			if (caixa[c][i] > caixa[c][i+1])
			{
				temp = caixa[c][i];
				caixa[c][i] = caixa[c][i+1];
				caixa[c][i+1] = temp;
				troca = 1;
			}

		if (troca == 0) return;
	}
}

/*
 * Verifica se uma caixa cabe dentro da outra
 */
int cabe (int menor, int maior)
{
	// Para cada dimensão
	for (int d = 0; d < dim; d++)
		// Se pelo menos uma dimensão é maior ou igual...
		if (caixa[menor][d] >= caixa[maior][d])
			// ...a caixa não cabe
			return 0;

	// A caixa menor cabe na maior
	return 1;
}

/*
 * Compara o tamanho de duas caixas, retornando 1 (c1>c2),
 * 0 (c1=c2) ou -1 (c1<c2)
 */
int comparaTamanho (int c1, int c2)
{
	// Para cada dimensão
	for (int d = 0; d < dim; d++)
		// Compara o valor da dimensão das duas caixas
		if (caixa[c1][d] > caixa[c2][d])
			// A caixa c1 é maior
			return 1;
		else if (caixa[c1][d] < caixa[c2][d])
			// A caixa c1 é menor
			return -1;

	// As caixas são iguais
	return 0;
}

/*
 * Classifica as caixas de forma ascendente
 */
void classificarCaixas ()
{
	int i, temp, troca;

	for (int p = 0; p < qtcaixas - 1; p++)
	{
		troca = 0;

		for (i = qtcaixas - 1; i > p; i--)
			if (comparaTamanho(ordem[i],ordem[i-1]) < 0)
			{
				temp = ordem[i];
				ordem[i] = ordem[i-1];
				ordem[i-1] = temp;
				troca = 1;
			}

		if (troca == 0) return;
	}
}

/*
 * Imprime as caixas
 */
void imprimeCaixas ()
{
	for (int c = 0; c < qtcaixas; c++)
	{
		printf("CAIXA %d:\t",ordem[c]+1);
		for (int d = 0; d < dim; d++)
			printf("%d\t",caixa[ordem[c]][d]);
		printf("\t=>%d (%d)\n",prox[ordem[c]],cont[ordem[c]]);
		// printf("\n");
	}
}

int lexi(int a, int b)
{
	char sa[10], sb[10];

	// return 0;
/*
	if (a < b)
		return 1;
	else
		return 0;
		*/

	itoa(a+1, sa);// , 10);
	itoa(b+1, sb);// , 10);

	if (strcmp(sa,sb) < 0)
		return 1;
	else
		return 0;
}

/*
 * Programa principal
 */
void main()
{
	int c , d, resp, max;

	// Lê a quantidade e a dimensão das caixas
	while (scanf("%d %d\n",&qtcaixas,&dim)==2)
	{
		// Valida a entrada
		if ((qtcaixas < 1) || (qtcaixas > MAXQTCAIXAS) || (dim < 1) || (dim > MAXDIM))
			continue;

		// Inicia as estruturas auxiliares
		for (c = 0; c < qtcaixas; c++)
		{
			ordem[c] = c;
			prox[c] = -1;
			cont[c] = 0;
		}

		// Para cada caixa...
		for (c = 0; c < qtcaixas; c++)
		{
			// ...lê as suas dimensões...
			for (d = 0; d < dim; d++)
				scanf("%d",&caixa[c][d]);

			// ...e as ordena de forma ascendente
			classificarDimensoes(c);
		}

		imprimeCaixas();

		// return;

		// Classifica as caixas de forma ascendente
		classificarCaixas();

		imprimeCaixas();

		// return;


		for (c = 0; c < qtcaixas; c++)
		{
			printf ("Na caixa %d cabem as seguintes caixas: ",ordem[c]+1);
			for (d = c - 1; d >= 0; d--)
				if (cabe(ordem[d],ordem[c]))
					printf("%d ",ordem[d]+1);
			printf("\n");
		}


		// Calcula o caminho mais longo na arvore
		max = 0;
		for (c = qtcaixas - 1; c >= 0; c--)
		{
			if (cont[ordem[c]] == 0)
			{
				// printf("caixa %d é folha\n",ordem[c]);
				// prox[ordem[c]] = -1;
				cont[ordem[c]] = 1;

				if ( (max == 0) || ((max == 1) && lexi(ordem[c],resp)) )
				{
					max = 1;
					resp = ordem[c];
				}
			}

			for (d = c - 1; d >= 0; d--)
				if (cabe(ordem[d],ordem[c]))
				{
					// printf("  caixa %d cabe\n",ordem[d]);
					if ( (cont[ordem[d]] < cont[ordem[c]] + 1) || ((cont[ordem[d]] == cont[ordem[c]] + 1) && (lexi(ordem[c],prox[ordem[d]]))) )
					{
						// printf("    caixa %d atualizada",ordem[d]);
						prox[ordem[d]] = ordem[c];
						cont[ordem[d]] = cont[ordem[c]] + 1;

						if (cont[ordem[d]] >= max)
						{
							max = cont[ordem[d]];
							resp = ordem[d];
						}
					}
					/* else
						printf("    caixa %d já possui um caminho maior",ordem[d]); */
				}
				/* else
					printf("  caixa %d NÃO cabe",ordem[d]); */
		}

		imprimeCaixas();

		// Imprime o maior caminho
		printf("%d\n%d",max,resp+1);
		resp = prox[resp];
		while (resp >= 0)
		{
			printf(" %d",resp+1);
			resp = prox[resp];
		}
		printf("\n");
	}
}
