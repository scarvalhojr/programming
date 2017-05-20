
/* @JUDGE_ID: 8580TT 100 C++ "<marquee>Top secret algorithm</marquee>" */

/* **********************************************************
   Problema:     The 3n+1 problem
   Estrat�gia:   For�a bruta
   Tempo de CPU: 0.120 segundos
   Mem�ria:      288 kbytes

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
    int n1, n2, num, inicial, final, c, max;

	/* L� dois n�meros */
    while (scanf("%d %d\n", &n1, &n2)==2)
    {

		/* Determina o in�cio e o fim do la�o */
		if (n1 < n2)
		{
			inicial = n1;
			final = n2;
		}
		else
		{
			inicial = n2;
			final = n1;
		}

		/* Calcula o ciclo do primeiro n�mero */
		max = ciclos(inicial);

		/* Calcula o ciclo dos demais n�meros verificando
		   se achou um ciclo maior */
		for (num = inicial + 1; num <= final; num++)
		{
			c = ciclos(num);
			if (c > max) max = c;
		}

		/* Imprime a resposta */
		printf("%d %d %d\n", n1, n2, max);
    }
}
