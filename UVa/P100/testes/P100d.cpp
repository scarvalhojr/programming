
/* @JUDGE_ID: 8580TT 100 C++ "Top secret algorithm" */

/* **********************************************************
   Problema:     The 3n+1 problem
   Estratégia:   Força bruta sem chamada de função, evitando
   				 cálculo de números cujo dobro já foi
   				 calculado, e evitando trocar a ordem dos
   				 números.
   Tempo de CPU: 0.060 segundos
   Memória:      low memory spent

   10 Dez 2000

   Sérgio Anibal de Carvalho Junior
   http://pagina.de/sergioanibal
   http://i.am/sergioanibal
   ********************************************************** */

#include <stdio.h>

/*
 * Programa principal
 * Lê dois números e calcula todos os ciclos entre eles
 * armazenando o maior ciclo encontrado
 */
void main()
{
	int  n1, n2, num, ciclos, max;

	/* Lê dois números */
    while (scanf("%d %d\n", &n1, &n2)==2)
    {
		max = 0;

		if (n1 <= n2)
		{

			for (int i = n2; i >= n1; i--)
			{
				if (i * 2 <= n2) continue;

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

		}
		else
		{

			for (int i = n1; i >= n2; i--)
			{
				if (i * 2 <= n1) continue;

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

		}

		printf("%d %d %d\n", n1, n2, max);
    }
}
