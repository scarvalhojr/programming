
/* @JUDGE_ID: 8580TT 100 C++ "Top secret algorithm" */

/* **********************************************************
   Problema:     The 3n+1 problem
   Estratégia:   Força bruta sem chamada de função, evitando
   				 cálculo de números cujo dobro já foi
   				 calculado, evitando trocar a ordem dos
   				 números e calculando potências de 2
   				 diretamente.
   Tempo de CPU: ? segundos
   Memória:      ? bytes

   10 Dez 2000

   Sérgio Anibal de Carvalho Junior
   http://pagina.de/sergioanibal
   http://i.am/sergioanibal
   ********************************************************** */

#include <stdio.h>
#include <math.h>

/*
 * Programa principal
 * Lê dois números e calcula todos os ciclos entre eles
 * armazenando o maior ciclo encontrado
 */
void main()
{
	int  n1, n2, num, ciclos, max, k;

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
					k = log10(i) / log10(2);

					if ( pow(2,k) == num )
					{
						ciclos = ciclos + k;
						break;
					}

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

					k = log10(i) / log10(2);

					if ( pow(2,k) == num )
					{
						ciclos = ciclos + k;
						break;
					}

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
