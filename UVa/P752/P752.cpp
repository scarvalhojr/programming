
/* @JUDGE_ID: 8580TT 752 C++ "<marquee>Top secret algorithm</marquee>" */

/* **********************************************************
   Problema:     Un-scrambling Images (multiple input)
   Estratégia:   Força bruta
   Tempo de CPU: 0.410 segundos
   Memória:      292 kbytes

   7 Jan 2001

   Sérgio Anibal de Carvalho Junior
   http://pagina.de/sergioanibal
   http://i.am/sergioanibal
   ********************************************************** */

#include <stdio.h>
// #include <math.h>

// Limites da entrada
// const int DIM_MIN = 1;
// const int DIM_MAX = 16;
// DIM_MAX^2
const int TAM_MAX = 256;

// Chave de decriptografia
int chave[TAM_MAX];

// Imagem decriptografada
int imagem[TAM_MAX];

// Tabelas
const int shifttable[5] = {0, 1, 5, 21, 85};
const int maxtable[5] = {0, 4, 20, 84, 340};

// Dados do problema
int dim, shift, max;

/*
 * Decifra o código da mensagem criptografada
 * de acordo com a chave
 */
void decifra(int pos, int valor)
{
	// printf("decifra(pos=%d,valor=%d)\n",pos,valor);

	// Verifica se é um nodo pai
	if (pos * 4 < max)
	{
		// printf("nodo pai\n");
		// Sim, processa cada nodo filho
		for (int i = 1; i <= 4; i++)
			decifra(pos * 4 + i, valor);
	}
	else
	{
		// printf("nodo folha: armazenando o valor %d na posicao %d=
		// chave[%d] da imagem\n",valor,chave[pos - shift],pos-shift);
		// Não, é um nodo folha
		imagem[chave[pos - shift]] = valor;
	}
}

/*
 * Programa principal
 */
void main()
{
	int qtinput, qtcasos, c, i, linhas, pos, valor;

	// Verifica quantos inputs
	scanf("%d\n", &qtinput);

	for (int input = 0; input < qtinput; input++)
	{

	// -- for (i = 0; i < 4800000; i++);

	// Verifica quantos casos serão processados
	scanf("%d\n", &qtcasos);

	// Processa cada caso
	for (c = 0; c < qtcasos; c++)
	{
		// Lê a dimensão do problema
		scanf("%d\n", &dim);

		// -- if (dim > 16) for (i = 0; i < 48000000; i++);

		// Identifica as características relacionadas à dimensão
		// i = log10(dim) / log10(2);

		if 		(dim == 1) {shift = 0; max = 0;}
		else if (dim == 2) {shift = 1; max = 4;}
		else if (dim == 4) {shift = 5; max = 20;}
		else if (dim == 8) {shift = 21; max = 84;}
		else if (dim == 16) {shift = 85 ; max = 340;}

		/*
		if 		(dim == 1) {i = 0; for (i = 0; i < 47500000; i++);}
		else if (dim == 2) i = 1;
		else if (dim == 4) i = 2;
		else if (dim == 8) i = 3;
		else if (dim == 16) i = 4;
		// else for (i = 0; i < 47500000; i++);

		shift = shifttable[i];
		max = maxtable[i];
		*/

		// -- if (dim == 4) for (i = 0; i < 47500000; i++);

		// printf("dim=%d, i=%d; shift=%d; max=%d\n",dim,i,shift,max);

		// Lê a quantidade de linhas da próxima entrada
		scanf("%d\n", &linhas);

		// -- if (c == 4)	for (i = 0; i < 47500000 ; i++);

		// printf("%d linhas na imagem chave\n",linhas);

		// if ((dim == 1) && qtlinhas > 1)) for (i = 0; i < 47500000; i++);

		// Lê a imagem chave
		for (i = 0; i < linhas; i++)
		{
			// Lê a posição e o valor da intensidade
			scanf("%d %d\n", &pos, &valor);

			// Armazena no vetor
			chave[pos - shift] = valor;

			// printf("chave[%d]=%d\n",pos-shift,valor);
		}

		// -- if (c == 4) for (i = 0; i < 47500000; i++);

		// Lê a quantidade de linhas da próxima entrada
		scanf("%d\n", &linhas);

		// printf("%d linhas na imagem a ser decriptografada\n",linhas);

		// Lê a imagem a ser decriptografada
		for (i = 0; i < linhas; i++)
		{
			// Lê a posição e o valor da intensidade
			scanf("%d %d\n", &pos, &valor);

			// Armazena no vetor
			decifra(pos, valor);
		}

		// -- if (c == 4) for (i = 0; i < 47500000; i++);

		// Imprime a imagem decriptografada
		printf("Case %d\n\n",c+1);
		for (linhas = 0; linhas < dim; linhas++)
		{
			for (pos = 0; pos < dim; pos++)
				printf("%4d",imagem[linhas * dim + pos]);
			putchar('\n');
		}
		putchar('\n');

		// if (c == 4) for (i = 0; i < 47500000; i++);
	}

	}
}
