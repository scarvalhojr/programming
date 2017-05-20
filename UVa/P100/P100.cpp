
/* @JUDGE_ID: 8581JZ 100 C++ "<marquee>Top secret algorithm</marquee>" */

/* **********************************************************
   Problema:     The 3n+1 problem
   Estratégia:   Força bruta, evitando o cálculo de número
   				 cujo dobro foi ou será calculado
   Tempo de CPU: 0.070 segundos
   Memória:      low memory spent

   16 Dez 2000

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
 * imprimindo o maior ciclo encontrado
 */
void main()
{
	char troca;
    int  inicial, final, max, n;

	// Lê dois números
    while (scanf("%d %d\n", &inicial, &final)==2)
    {
		// Verifica a ordenação do intervalo
		if (inicial <= final)
		{
			troca = 0;
		}
		else
		{
			troca = 1;

			n = inicial;
			inicial = final;
			final = n;
		}

		max = 0;

		// Percorre todos os números do intervalo
		for (int num = inicial; num <= final; num++)
		{
			// Ignora se o dobro do número será calculado
			if (num * 2 <= final) continue;

			/*
			// Ignora se (num-1)/3 é ímpar e é um número que já foi calculado
			n = (num - 1) / 3;
			if ( (n >= inicial) && ((3 * n + 1) == num) && ((n % 2) > 0) ) continue;
			*/

			// Calcula a quantidade de ciclos e verifica se é maior que a máxima atual
			int n = ciclos(num);
			if (n > max) max = n;
		}

		// Imprime a resposta
		if (troca)
			printf("%d %d %d\n", final, inicial, max);
		else+
			printf("%d %d %d\n", inicial, final, max);
    }
}
