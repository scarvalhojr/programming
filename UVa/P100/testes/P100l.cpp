
/* @JUDGE_ID: 8580TT 100 C++ "<marquee>Top secret algorithm</marquee>" */

/* **********************************************************
   Problema:     The 3n+1 problem
   Estratégia:   Força bruta evitando o cálculo de números
   				 cujo dobro já foi calculado e o cálculo de
   				 números n tais que o resultado de (n-1)/3 é
   				 um número que ainda será calculado
   Tempo de CPU: time limit exceeded
   Memória:

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
	int  inicial, final, num, incremento = 1, c, max;

	// Lê dois números
    while (scanf("%d %d\n", &inicial, &final)==2)
    {
		max = 0;

		// Verifica a ordenação do intervalo
		if (inicial > final) incremento = -1;

		for (num = inicial; num <= final; num += incremento)
		{
			// Ignora se o dobro do número está no intervalo
			if (num * 2 <= final) continue;

			// Ignora se (num-1)/3 é ímpar e é um número que está no intervalo
			c = (num - 1) / 3;
			if ( (c >= inicial) && ((3 * c + 1) == num) && ((c % 2) > 0) ) continue;

			// Calcula a quantidade de ciclos e verifica se é maior que a máxima atual
			c = ciclos(num);
			if (c > max) max = c;
		}

		/* Imprime a resposta */
		printf("%d %d %d\n", final, inicial, max);
    }
}
