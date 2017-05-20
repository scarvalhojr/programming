
/* @JUDGE_ID: 8580TT 100 C++ "Top secret algorithm" */

/* **********************************************************
   Problema:     The 3n+1 problem
   Estrat�gia:   For�a bruta sem chamada de fun��o e evitando
   				 c�lculo de n�meros cujo dobro j� foi
   				 calculado.
   Tempo de CPU: 0.060 segundos
   Mem�ria:      low memory spent

   10 Dez 2000

   S�rgio Anibal de Carvalho Junior
   http://pagina.de/sergioanibal
   http://i.am/sergioanibal
   ********************************************************** */

#include <stdio.h>

/*
 * Programa principal
 * L� dois n�meros e calcula todos os ciclos entre eles
 * armazenando o maior ciclo encontrado
 */
void main()
{
	char troca;
    int  inicial, final, num, ciclos, max;

	/* L� dois n�meros */
    while (scanf("%d %d\n", &inicial, &final)==2)
    {
		max = 0;

		/* Garante a ordem do intervalo */
		if (inicial <= final)
		{
			troca = 0;
		}
		else
		{
			troca = 1;

			num = inicial;
			inicial = final;
			final = num;
		}

		/* Calcula o ciclo dos n�meros do intervalo
		   verificando se achou um ciclo maior */
		for (int i = final; i >= inicial; i--)
		{
			if (i * 2 <= final) continue;

			num = i;
			ciclos = 1;

			while (num != 1)
			{
				if (num % 2 == 0)
					num = num / 2;
				else
					num = 3 * num + 1;

				ciclos++;
			}

			if (ciclos > max) max = ciclos;
		}

		/* Imprime a resposta */
		if (troca == 1)
			printf("%d %d %d\n", final, inicial, max);
		else
			printf("%d %d %d\n", inicial, final, max);
    }
}
