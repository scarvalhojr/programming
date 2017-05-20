
/* @JUDGE_ID: 8580TT 100 C++ "<marquee>Top secret algorithm</marquee>" */

/* **********************************************************
   Problema:     The 3n+1 problem
   Estratégia:   Força bruta evitando calcular números cujo
   				 dobro já foi calculado.
   Tempo de CPU: ? segundos
   Memória:      ? kbytes

   10 Dez 2000

   Sérgio Anibal de Carvalho Junior
   http://pagina.de/sergioanibal
   http://i.am/sergioanibal
   ********************************************************** */

#include <stdio.h>

/*
 * Calcula a quantidade de ciclos de um determinado número
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
 * Lê dois números e calcula todos os ciclos entre eles
 * armazenando o maior ciclo encontrado
 */
void main()
{
	char troca;
    int  inicial, final, num, c, max;

	/* Lê dois números */
    while (scanf("%d %d\n", &inicial, &final)==2)
    {
		max = 0;

		/* Verifica a ordenação do intervalo */
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

		for (num = final; num >= inicial; num--)
		{
			if (num * 2 <= final) continue;

			c = ciclos(num);

			if (c > max) max = c;
		}

		/* Imprime a resposta */
		if (troca)
			printf("%d %d %d\n", final, inicial, max);
		else
			printf("%d %d %d\n", inicial, final, max);
    }
}
