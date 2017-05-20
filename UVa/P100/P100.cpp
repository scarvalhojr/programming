
/* @JUDGE_ID: 8581JZ 100 C++ "<marquee>Top secret algorithm</marquee>" */

/* **********************************************************
   Problema:     The 3n+1 problem
   Estrat�gia:   For�a bruta, evitando o c�lculo de n�mero
   				 cujo dobro foi ou ser� calculado
   Tempo de CPU: 0.070 segundos
   Mem�ria:      low memory spent

   16 Dez 2000

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
 * imprimindo o maior ciclo encontrado
 */
void main()
{
	char troca;
    int  inicial, final, max, n;

	// L� dois n�meros
    while (scanf("%d %d\n", &inicial, &final)==2)
    {
		// Verifica a ordena��o do intervalo
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

		// Percorre todos os n�meros do intervalo
		for (int num = inicial; num <= final; num++)
		{
			// Ignora se o dobro do n�mero ser� calculado
			if (num * 2 <= final) continue;

			/*
			// Ignora se (num-1)/3 � �mpar e � um n�mero que j� foi calculado
			n = (num - 1) / 3;
			if ( (n >= inicial) && ((3 * n + 1) == num) && ((n % 2) > 0) ) continue;
			*/

			// Calcula a quantidade de ciclos e verifica se � maior que a m�xima atual
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
