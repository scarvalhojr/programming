
/* @JUDGE_ID: 8580TT 297 C++ "<marquee>Top secret algorithm</marquee>" */

/* **********************************************************
   Problema:     Quadtrees
   Estratégia:   Força bruta
   Tempo de CPU: 0.000 segundos
   Memória:      low memory spent

   3 Jan 2001

   Sérgio Anibal de Carvalho Junior
   http://pagina.de/sergioanibal
   http://i.am/sergioanibal
   ********************************************************** */

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

// Limites da entrada
// const int DIM_VERT = 32;
// const int DIM_HORIZ = 32;
// const int QT_PIXELS = DIM_VERT * DIM_HORIZ;
const int ALTURA_MAX = 5; // log10(QT_PIXELS) / log10(4); // = log4(QT_PIXELS)

// Tamanho máximo da string de representação da imagem
// É igual ao somatório de 4 ^ h, 0 <= h <= ALTURA_MAX
// (com mais um caracter nulo no final)
const int TAM_MAX = 1622;

// Representação da imagem em forma de string
char imagem[2][TAM_MAX];

// Constantes para os possíveis caracteres da string
const char PARENT = 'p';
const char FULL = 'f';
const char EMPTY = 'e';
const char FIM = '\0';

/*
 *
 */
int calcularValorParcial(int num, int *pos, int nivel)
{
	int valor = 0;

	// printf("Iniciando calcularVP(%d, %d, %d)\n",num,*pos,nivel);

	// Deve sempre começar num nodo pai
	if (imagem[num][*pos] != PARENT)
	{
		puts("ERRO: Funcao calcularValorParcial chamada para um nodo nao-pai");
		exit(0);
	}

	nivel++;

	for (int i = 0; i < 4; i++)
	{
		(*pos)++;
		// printf("DEBUG: nivel %d, nodo %d, posicao %d = %c\n",nivel,i,*pos,imagem[num][*pos]);

		if (imagem[num][*pos] == PARENT)
			valor = valor + calcularValorParcial(num, pos, nivel);

		else if (imagem[num][*pos] == FULL)
			valor = valor + pow(4,ALTURA_MAX - nivel);

		else if (imagem[num][*pos] == FIM)
		{
			puts("ERRO: Fim inesperado da string.");
			exit(0);
		}
	}

	nivel--;

	// printf("retornando %d\n",valor);
	return valor;

}

/*
 *
 */
int somar (int *pos0, int *pos1, int nivel)
{
	int soma = 0, tmp;

	// printf("Iniciando somar(%d, %d, %d)\n",*pos0,*pos1,nivel);

	if ((imagem[0][*pos0] == FIM) || (imagem[1][*pos1] == FIM))
	{
		puts("ERRO: Fim inesperado de uma ou das duas strings");
		exit(0);
	}

	// Total
	if ((imagem[0][*pos0] == FULL) || (imagem[1][*pos1] == FULL))
	{
		// printf("pelo menos um full!\n");
		soma = pow(4,ALTURA_MAX - nivel);
		if (imagem[0][*pos0] == PARENT)
		{
			tmp = calcularValorParcial(0, pos0, nivel);
			// printf("desperdicado %d da imagem 0",tmp);
		}
		else if (imagem[1][*pos1] == PARENT)
		{
			tmp = calcularValorParcial(1, pos1, nivel);
			// printf("desperdicado %d da imagem 1",tmp);
		}
	}
	else if ((imagem[0][*pos0] == PARENT) && (imagem[1][*pos1] == PARENT))
	{
		// printf("dois parent\n");
		for (int i = 0; i < 4; i++)
		{
			(*pos0)++;
			(*pos1)++;
			tmp = somar(pos0, pos1, nivel + 1);
			// printf("%d > tmp = %d\n",i,tmp);
			soma = soma + tmp;
		}
	}
	else if (imagem[0][*pos0] == PARENT)
	{
		soma = calcularValorParcial(0, pos0, nivel);
		// printf("imagem 0 eh parent dominante -> soma =%d\n",soma);
	}
	else if (imagem[1][*pos1] == PARENT)
	{
		soma = calcularValorParcial(1, pos1, nivel);
		// printf("imagem 1 eh parent dominante -> soma =%d\n",soma);
	}
	else
	{
		// printf("dois empty\n");
		soma = 0;
	}

	// printf("retornando %d\n",valor);
	return soma;

}

/*
 * Programa principal
 */
void main()
{
	int qtcasos, valor0, valor1, total, pos0, pos1, nivel;

	// Verifica quantos casos serão processados
	scanf("%d\n", &qtcasos);

	// Processa cada caso
	for (int c = 0; c < qtcasos; c++)
	{
		imagem[0][0] = '\0';
		imagem[1][0] = '\0';

		// Lê as duas strings de entrada
		scanf("%s",imagem[0]);
		scanf("%s",imagem[1]);

		nivel = valor0 = valor1 = pos0 = pos1 = 0;

		// valor0 = calcularValorParcial(0, &pos0, 0);
		// valor1 = calcularValorParcial(1, &pos1, 0);

		// Imagem 0
		if (imagem[0][0] == FULL)
		{
			valor0 = pow(4,ALTURA_MAX - nivel);
		}
		else
			if (imagem[0][0] == PARENT)
			{
				valor0 = calcularValorParcial(0, &pos0, nivel);
				pos0 = 0;
			}
			else
				valor0 = 0;

		// Imagem 1
		if (imagem[1][0] == FULL)
		{
			valor1 = pow(4,ALTURA_MAX - nivel);
		}
		else
			if (imagem[1][0] == PARENT)
			{
				valor1 = calcularValorParcial(1, &pos1, nivel);
				pos1 = 0;
			}
			else
				valor1 = 0;


		// Total
		if (imagem[0][0] == FIM)
			total = valor1;
		else if (imagem[1][0] == FIM)
			total = valor0;
		else
		{

		if ((imagem[0][pos0] == FULL) || (imagem[1][pos1] == FULL))
			total = pow(4,ALTURA_MAX - nivel);

		else if ((imagem[0][pos0] == PARENT) && (imagem[1][pos1] == PARENT))
			total = somar(&pos0, &pos1, nivel);

		else if (imagem[0][pos0] == PARENT)
			total = calcularValorParcial(0, &pos0, nivel);

		else if (imagem[1][pos1] == PARENT)
			total = calcularValorParcial(1, &pos1, nivel);

		else
			total = 0;

		}

		// printf("%d:\n%s = %d\n%s = %d\n", c, imagem[0], valor0, imagem[1], valor1);
		printf("There are %d black pixels.\n", total);
	}
}
