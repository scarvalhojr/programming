
/* @JUDGE_ID: 8580TT 100 C++ "<marquee>Top secret algorithm</marquee>" */

/* **********************************************************
   Problema:     The 3n+1 problem
   Estrat�gia:   For�a bruta evitando o c�lculo de n�meros
   				 cujo dobro j� foi calculado e o c�lculo de
   				 n�meros n tais que o resultado de (n-1)/3 �
   				 um n�mero que ainda ser� calculado
   Tempo de CPU: 0.050 segundos
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
