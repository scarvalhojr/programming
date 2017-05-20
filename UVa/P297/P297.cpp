
/* @JUDGE_ID: 8581JZ 297 C++ "<marquee>Top secret algorithm</marquee>" */

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
 * Calcula o valor parcial de uma imagem a
 * partir de um determinado nodo pai
 */
void localizarFimNodoPai(int num, int *pos)
{
	/*
	// Validação da entrada
	if (imagem[num][*pos] != PARENT)
	{
		puts("ERRO: Funcao de localizacao do fim do nodo pai chamada para um nodo nao pai.");
		exit(0);
	}
	*/

	// Percorre todos os quatro nodos filhos
	for (int i = 0; i < 4; i++)
	{
		// Incrementa o ponteiro de posição
		(*pos)++;

		// Se é um nodo pai
		if (imagem[num][*pos] == PARENT)
			// Prossegue localizando o seu fim
			localizarFimNodoPai(num, pos);

		/*
		// Validação da entrada
		else if (imagem[num][*pos] == FIM)
		{
			puts("ERRO: Fim inesperado das string de representacao da imagem.");
			exit(0);
		}
		*/
	}
}

/*
 * Calcula o valor parcial de uma imagem a
 * partir de um determinado nodo pai
 */
int calcularValorParcial(int num, int *pos, int nivel)
{
	int valor = 0;

	/*
	// Validação da entrada
	if (imagem[num][*pos] != PARENT)
	{
		puts("ERRO: Funcao de calculo parcial chamada para um nodo nao pai.");
		exit(0);
	}
	*/

	// Percorre todos os quatro nodos filhos
	for (int i = 0; i < 4; i++)
	{
		// Incrementa o ponteiro de posição
		(*pos)++;

		// Se é um nodo pai
		if (imagem[num][*pos] == PARENT)
			// Prossegue calculando o seu valor parcial
			valor = valor + calcularValorParcial(num, pos, nivel + 1);

		// Se é um nodo preenchido, acrescenta ao valor
		else if (imagem[num][*pos] == FULL)
			valor = valor + pow(4,ALTURA_MAX - nivel);

		/*
		// Validação da entrada
		else if (imagem[num][*pos] == FIM)
		{
			puts("ERRO: Fim inesperado das string de representacao da imagem.");
			exit(0);
		}
		*/
	}

	// Retorna o valor parcial
	return valor;
}

/*
 * Calcula a soma das duas árvores, partindo de um determinado nodo
 * (em um determinado nivel) e comparando os nodos descendentes
 * das duas imagens
 */
int somarImagens (int *pos0, int *pos1, int nivel)
{
	int soma = 0;

	/*
	// Validacao da entrada
	if ((imagem[0][*pos0] == FIM) || (imagem[1][*pos1] == FIM))
	{
		puts("ERRO: Fim inesperado da string de representacao da imagem.");
		exit(0);
	}
	*/

	// Se pelo menos um nodo esta preenchido
	if ((imagem[0][*pos0] == FULL) || (imagem[1][*pos1] == FULL))
	{
		soma = pow(4,ALTURA_MAX - nivel);

		// Se existe um nodo pai, atualiza o ponteiro para
		// o ultimo nodo filho
		if (imagem[0][*pos0] == PARENT)
			localizarFimNodoPai(0, pos0);

		else if (imagem[1][*pos1] == PARENT)
			localizarFimNodoPai(1, pos1);
	}

	// Se os dois nodos sao nodos pai, desce um nivel
	// e calcula a soma para os quatro nodos filhos
	else if ((imagem[0][*pos0] == PARENT) && (imagem[1][*pos1] == PARENT))
		for (int n = 0; n < 4; n++)
		{
			// Incrementa os ponteiros de posição
			(*pos0)++;
			(*pos1)++;
			soma = soma + somarImagens(pos0, pos1, nivel + 1);
		}

	// Se o nodo da imagem 0 é um nodo pai (e o da imagem 1 é vazio)
	else if (imagem[0][*pos0] == PARENT)
		// Calcula o valor parcial do nodo pai
		soma = calcularValorParcial(0, pos0, nivel + 1);

	// Se o nodo da imagem 1 é um nodo pai (e o da imagem 0 é vazio)
	else if (imagem[1][*pos1] == PARENT)
		// Calcula o valor parcial do nodo pai
		soma = calcularValorParcial(1, pos1, nivel + 1);

	// Dois nodos vazios
	else
		soma = 0;

	// Retorna a soma das imagens
	return soma;
}

/*
 * Programa principal
 */
void main()
{
	int qtcasos, total, pos0, pos1;

	// Verifica quantos casos serão processados
	scanf("%d\n", &qtcasos);

	// Processa cada caso
	for (int c = 0; c < qtcasos; c++)
	{
		// Lê as duas strings de entrada
		scanf("%s",imagem[0]);
		scanf("%s",imagem[1]);

		// Inicia os ponteiros de posição
		pos0 = pos1 = 0;

		// Calcula a soma das duas strings
		total = somarImagens(&pos0, &pos1, 0);

		// Imprime a resposta
		printf("There are %d black pixels.\n", total);
	}
}
