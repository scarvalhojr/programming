
#include <stdio.h>
#include <string.h>

/*
 * Dimensao do mundo
 */
int dimensao;

/*
 * Programa principal
 */
void main()
{
	char	comando[5], modo[5];
	int		origem, destino;

    // Lê a dimensão do mundo
    scanf("%d\n", &dimensao);

    // Lê os comandos
    while (scanf("%s %d %s %d\n", &comando, &origem, &modo, &destino)==4)
    {
		// Valida os números dos blocos
		if ((origem < 0) || (origem >= dimensao) || (destino < 0) || (destino >= dimensao))
			continue;

		/*
		// Verifica se os blocos estão na mesma fila
		if (bloco[origem].fila == bloco[destino].fila)
			continue;
		*/

		// Determina qual comando deve ser executado
		if (strcmp(comando,"move")==0)
		{
			if (strcmp(modo,"onto")==0)
				printf("\nmoveOnto(%d,%d)", origem, destino);
			else if (strcmp(modo,"over")==0)
				printf("\nmoveOver(%d,%d)", origem, destino);
			else
				// Modo desconhecido
				continue;
		}
		else if (strcmp(comando,"pile")==0)
		{
			if (strcmp(modo,"onto")==0)
				printf("\npileOnto(%d,%d)", origem, destino);
			else if (strcmp(modo,"over")==0)
				printf("\npileOver(%d,%d)", origem, destino);
			else
				// Modo desconhecido
				continue;
		}
		else
			// Comando desconhecido: ignora
			continue;
	}
}
