
/* @JUDGE_ID: 8580TT 100 C++ "<marquee>Top secret algorithm</marquee>" */

/* **********************************************************
   Problema:     The 3n+1 problem
   Estratégia:   Força bruta evitando o cálculo de números
   				 cujo dobro já foi calculado, o cálculo de
   				 números n tais que o resultado de (n-1)/3 é
   				 um número que ainda será calculado, e
   				 evitando chamada de funções
   Tempo de CPU: 0.090 segundos
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
	char troca;
    int  inicial, final, num, n, ciclos, max;

	// Lê dois números
    while (scanf("%d %d\n", &inicial, &final)==2)
    {
		max = 0;

		// Verifica a ordenação do intervalo
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

		for (num = inicial; num <= final; num++)
		{
			// Ignora se o dobro do número será calculado
			if (num * 2 <= final) continue;

			// Ignora se (num-1)/3 é ímpar e é um número que já foi calculado
			n = (num - 1) / 3;
			if ( (n >= inicial) && ((3 * n + 1) == num) && ((n % 2) > 0) ) continue;

			// Calcula a quantidade de ciclos
			n = num;
			ciclos = 1;
		    while (n != 1)
    		{
				if (n % 2 == 0)
	    			n = n / 2;
				else
					n = 3 * n + 1;

				ciclos++;
			}

			// Verifica se a quantidade de ciclos calculada é maior que a máxima atual
			if (ciclos > max) max = ciclos;
		}

		/* Imprime a resposta */
		if (troca)
			printf("%d %d %d\n", final, inicial, max);
		else
			printf("%d %d %d\n", inicial, final, max);
    }
}
