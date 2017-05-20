
/* @JUDGE_ID: 8581JZ 101 C++ "<marquee>Top secret algorithm</marquee>" */

/* **********************************************************
   Problema:     The blocks problem
   Estrat�gia:   Vetor de ponteiros pr�-alocados com pequenas
   				 melhorias
   Tempo de CPU: 0.060 segundos
   Mem�ria:      low memory spent

   17 Dez 2000

   S�rgio Anibal de Carvalho Junior
   http://pagina.de/sergioanibal
   http://i.am/sergioanibal
   ********************************************************** */

#include <stdio.h>
#include <string.h>

/*
 * N�mero m�ximo de elementos no vetor
 */
const int MAX_BLOCOS = 24;

/*
 * Define a estrutura de um bloco
 */
struct blocodef
{
	int			numero;
	int			fila;
	blocodef	*anterior;
	blocodef	*proximo;
};

/*
 * Declara um vetor de blocos
 */
struct blocodef bloco[MAX_BLOCOS];

/*
 * Declara um vetor de ponteiros que apontam
 * para os primeiros blocos de cada fila
 */
struct blocodef *fila[MAX_BLOCOS];

/*
 * Dimensao do mundo
 */
int dimensao;

/*
 * Prepara as estruturas do programa alocando mem�ria
 * para os blocos e para os ponteiros
 */
void iniciar()
{
	for (int i = 0; i < dimensao; i++)
	{
		bloco[i].numero = i;
		bloco[i].fila = i;
		bloco[i].proximo = NULL;
		bloco[i].anterior = NULL;
		fila[i] = &bloco[i];
	}
}

/*
 * Mostra o estado atual das filas
 */
void mostrarFilas ()
{
	blocodef *b;

	// Percorre todas as filas
	for (int i = 0; i < dimensao; i++)
	{
		printf("%d:",i);

		// Percorre todos os blocos da fila
		b = fila[i];
		while (b)
		{
			// Imprime o n�mero do bloco
			printf(" %d", b->numero);

			// Passa para o pr�ximo
			b = b->proximo;
		}
		putchar('\n');
	}
}

/*
 * Move um bloco para uma determinada fila,
 * organizando a estrutura de ponteiros.
 */
void moverBloco (int numbloco, int numfila)
{
	blocodef *f, *b;

	b = &bloco[numbloco];

	// Verifica se o bloco � o primeiro da sua fila atual
	if (fila[b->fila] == b)
		// Sim: esvazia a fila
		fila[b->fila] = NULL;
	else
		// N�o: torna nulo o ponteiro do
		// bloco imediatamente anterior
		(b->anterior)->proximo = NULL;

	// Verifica se a fila destino est� vazia
	if (!fila[numfila])
	{
		// Sim: o bloco ser� o primeiro da fila
		fila[numfila] = b;
		b->anterior = NULL;
	}
	else
	{
		// A fila destino nao esta vazia: procura o �ltimo bloco da fila
		f = fila[numfila];
		while (f->proximo)
			f = f->proximo;

		// Insere o novo bloco no final da fila
		f->proximo = b;
		b->anterior = f;
	}

	// Atualiza o indicador de fila do bloco
	b->fila = numfila;
}

/*
 * Move uma pilha de blocos iniciada pelo bloco b
 * para uma determinada fila
 */
void moverPilha (int numbloco, int numfila)
{
	blocodef *b;

	// Move o primeiro bloco e mant�m
	// a estrutura de ponteiros
	moverBloco(numbloco, numfila);

	// Percorre os demais blocos atualizando
	// o indicador de fila
	b = &bloco[numbloco];
	while (b->proximo)
	{
		b = b->proximo;
		b->fila = numfila;
	}
}

/*
 * Retira blocos que est�o empilhados em cima de um determinado bloco,
 * movendo-os para as suas filas originais.
 */
void liberarBloco (int numbloco)
{
	blocodef *b, *temp;

	// Obt�m um ponteiro pro bloco a partir do seu n�mero
	b = &bloco[numbloco];

	// Percorre a lista de blocos empilhados,
	// movendo-os para as suas filas originais
	b = b->proximo;
	while (b)
	{
		// Move o bloco empilhado para a sua fila
		moverBloco(b->numero, b->numero);

		// Passa para o pr�ximo
		temp = b->proximo;
		b->proximo = NULL;
		b = temp;
	}
}

/*
 * Programa principal
 */
void main()
{
	char	comando[5], modo[5];
	int		origem, destino;

	// L� a dimens�o do mundo
    if(scanf("%d\n", &dimensao)!=1) return;

	// Inicia a configura��o dos blocos
	iniciar();

    // L� os comandos
    while (scanf("%s %d %s %d\n", &comando, &origem, &modo, &destino)==4)
    {
		// Valida os n�meros dos blocos
		if ((origem < 0) || (origem >= dimensao) || (destino < 0) || (destino >= dimensao))
			continue;

		// Verifica se os blocos est�o na mesma fila
		if (bloco[origem].fila == bloco[destino].fila)
			continue;

		// Verifica se deve liberar o bloco destino
		if (strcmp(modo,"onto")==0)
			// Retira os blocos empilhados sobre o bloco de
			// destino, movendo-os para as suas filas originais
			liberarBloco(destino);

		// Determina qual comando deve ser executado
		if (strcmp(comando,"move")==0)
		{
			// Retira os blocos empilhados sobre o bloco de
			// origem, movendo-os para as suas filas originais
			liberarBloco(origem);

			// Move o bloco de origem para a fila do bloco de destino
			moverBloco(origem, bloco[destino].fila);
		}
		else if (strcmp(comando,"pile")==0)
		{
			// Move a pilha iniciada pelo bloco de origem para a fila do bloco de destino
			moverPilha(origem, bloco[destino].fila);
		}
		else
			// Comando desconhecido: ignora
			continue;
	}

	// Imprime o estado das filas
	mostrarFilas();
}
