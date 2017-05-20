
/* @JUDGE_ID: 8580TT 101 C++ "<marquee>Top secret algorithm</marquee>" */

/* **********************************************************
   Problema:     The blocks problem
   Estratégia:   Vetor de ponteiros pré-alocados
   Tempo de CPU: 0.060 segundos
   Memória:      low memory spent

   17 Dez 2000

   Sérgio Anibal de Carvalho Junior
   http://pagina.de/sergioanibal
   http://i.am/sergioanibal
   ********************************************************** */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
 * Número máximo de elementos no vetor
 */
const int MAX_BLOCOS = 25;

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
 * Prepara as estruturas do programa alocando memória
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
			// Imprime o número do bloco
			printf(" %d", b->numero);

			// Passa para o próximo
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

	// Verifica se o bloco é o primeiro da sua fila atual
	if (!b->anterior)
		// Sim: esvazia a fila
		fila[b->fila] = NULL;
	else
		// Não: torna nulo o ponteiro do
		// bloco imediatamente anterior
		(b->anterior)->proximo = NULL;

	// Verifica se a fila destino está vazia
	if (!fila[numfila])
	{
		// Sim: o bloco será o primeiro da fila
		fila[numfila] = b;
		b->anterior = NULL;
	}
	else
	{
		// A fila destino nao esta vazia: procura o último bloco da fila
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

	// Move o primeiro bloco e mantém
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
 * Retira blocos que estão empilhados em cima de um determinado bloco,
 * movendo-os para as suas filas originais.
 */
void liberarBloco (int numbloco)
{
	blocodef *b, *temp;

	// Obtém um ponteiro pro bloco a partir do seu número
	b = &bloco[numbloco];

	// Se não existem blocos empilhados: nada a fazer
	if (!b->proximo) return;

	// Percorre a lista de blocos empilhados,
	// movendo-os para as suas filas originais
	b = b->proximo;
	while (b)
	{
		// Move o bloco empilhado para a sua fila
		moverBloco(b->numero, b->numero);

		// Passa para o próximo
		temp = b->proximo;
		b->proximo = NULL;
		b = temp;
	}
}

/*
 * moveOnto
 */
void moveOnto (int bloco_origem, int bloco_destino)
{
	// Retira os blocos empilhados sobre o bloco de
	// origem, movendo-os para as suas filas originais
	liberarBloco(bloco_origem);

	// Retira os blocos empilhados sobre o bloco de
	// destino, movendo-os para as suas filas originais
	liberarBloco(bloco_destino);

	// Move o bloco de origem para a fila do bloco de destino
	moverBloco(bloco_origem, bloco[bloco_destino].fila);
}

/*
 * moveOver
 */
void moveOver (int bloco_origem, int bloco_destino)
{
	// Retira os blocos empilhados sobre o bloco de
	// origem, movendo-os para as suas filas originais
	liberarBloco(bloco_origem);

	// Move o bloco de origem para a fila do bloco de destino
	moverBloco(bloco_origem, bloco[bloco_destino].fila);
}

/*
 * pileOnto
 */
void pileOnto (int bloco_origem, int bloco_destino)
{
	// Retira os blocos empilhados sobre o bloco de
	// destino, movendo-os para as suas filas originais
	liberarBloco(bloco_destino);

	// Move a pilha iniciada pelo bloco de origem para a fila do bloco de destino
	moverPilha(bloco_origem, bloco[bloco_destino].fila);
}

/*
 * pileOver
 */
void pileOver (int bloco_origem, int bloco_destino)
{
	// Move a pilha iniciada pelo bloco de origem para a fila do bloco de destino
	moverPilha(bloco_origem, bloco[bloco_destino].fila);
}

/*
 * Programa principal
 */
void main()
{
	char	comando[5], modo[5];
	int		origem, destino;

    // Lê a dimensão do mundo
    if(scanf("%d\n", &dimensao)!=1) return;

	// Inicia a configuração dos blocos
	iniciar();

    // Lê os comandos
    while (scanf("%s %d %s %d\n", &comando, &origem, &modo, &destino)==4)
    {
		// Valida os números dos blocos
		if ((origem < 0) || (origem >= dimensao) || (destino < 0) || (destino >= dimensao))
			continue;

		// Verifica se os blocos estão na mesma fila
		if (bloco[origem].fila == bloco[destino].fila)
			continue;

		// Determina qual comando deve ser executado
		if (strcmp(comando,"move")==0)
		{
			if (strcmp(modo,"onto")==0)
				moveOnto(origem, destino);
			else if (strcmp(modo,"over")==0)
				moveOver(origem, destino);
			else
				// Modo desconhecido
				continue;
		}
		else if (strcmp(comando,"pile")==0)
		{
			if (strcmp(modo,"onto")==0)
				pileOnto(origem, destino);
			else if (strcmp(modo,"over")==0)
				pileOver(origem, destino);
			else
				// Modo desconhecido
				continue;
		}
		else
			// Comando desconhecido: ignora
			continue;
	}

	// Imprime o estado das filas
	mostrarFilas();
}
