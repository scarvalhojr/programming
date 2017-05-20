
/* @JUDGE_ID: 8580TT 100 C++ "<marquee>Top secret algorithm</marquee>" */

/* **********************************************************
   Problema:     The 3n+1 problem
   Estrat�gia:   For�a bruta evitando calcular n�meros cujo
   				 dobro j� foi calculado e evitando a
   				 ordena��o do intervalo.
   Tempo de CPU: 0.070 segundos
   Mem�ria:      low memory spent

   10 Dez 2000

   S�rgio Anibal de Carvalho Junior
   http://pagina.de/sergioanibal
   http://i.am/sergioanibal
   ********************************************************** */

#include <stdio.h>

/*
 * Calcula a quantidade de ciclos de um determinado n�mero
 */
int ciclos(int n)
{
	int ciclos = 1;

    while (n != 1)
    {

		if (n % 2 == 0)
	    	n = n / 2;
		else
			n = 3 * n + 1;

		ciclos++;
	}

    return ciclos;
}

/*
 * Programa principal
 * L� dois n�meros e calcula todos os ciclos entre eles
 * armazenando o maior ciclo encontrado
 */
void main()
{
	int  inicial, final, num, c, max;

	/* L� dois n�meros */
    while (scanf("%d %d\n", &inicial, &final)==2)
    {
		max = 0;

		/* Verifica a ordena��o do intervalo */
		if (inicial <= final)
		{
			for (num = final; num >= inicial; num--)
			{
				if (num * 2 <= final) continue;

				c = ciclos(num);

				if (c > max) max = c;
			}
		}
		else
		{
			for (num = inicial; num >= final; num--)
			{
				if (num * 2 <= final) continue;

				c = ciclos(num);

				if (c > max) max = c;
			}
		}

		printf("%d %d %d\n", inicial, final, max);
    }
}
