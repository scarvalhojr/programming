
/* @JUDGE_ID: 8580TT 100 C++ "<marquee>Top secret algorithm</marquee>" */

/* **********************************************************
   Problema:     The 3n+1 problem
   Estratégia:   Força bruta evitando o cálculo de números
   				 cujo dobro já foi calculado e o cálculo de
   				 números n tais que o resultado de (n-1)/3 é
   				 um número que ainda será calculado
   Tempo de CPU: 0.050 segundos
   Memória:      low memory spent

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
	char achou;
	int  qtde = 0;

	for (int max = 262; ((max > 0) && (qtde <= 30)) ; max--)
	{
		achou = 0;

		for (int num = 1; num <= 1000; num++)
			if (ciclos(num) == max)
			{
				if(!achou)
				{
					achou = 1;
					qtde++;
					printf("\n%d:", max);
				}

				printf(" %d",num);
			}
	}

}
