
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
	char troca;
    int  inicial, final, num, c, max;

	// L� dois n�meros
    while (scanf("%d %d\n", &inicial, &final)==2)
    {
		max = 0;

		// Verifica a ordena��o do intervalo
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
			// Ignora se o dobro do n�mero ser� calculado
			if (num * 2 <= final) continue;

			// Ignora se (num-1)/3 � �mpar e � um n�mero que j� foi calculado
			c = (num - 1) / 3;
			if ( (c >= inicial) && ((3 * c + 1) == num) && ((c % 2) > 0) ) continue;

			// Calcula a quantidade de ciclos e verifica se � maior que a m�xima atual
			c = ciclos(num);
			if (c > max) max = c;
		}

		/* Imprime a resposta */
		if (troca)
			printf("%d %d %d\n", final, inicial, max);
		else+
			printf("%d %d %d\n", inicial, final, max);
    }
}
