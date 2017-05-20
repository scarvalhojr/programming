
/* @JUDGE_ID: 8580TT 100 C++ "<marquee>Top secret algorithm</marquee>" */

/* **********************************************************
   Problema:     The 3n+1 problem
   Estrat�gia:   Descobrir a caracter�stica da entrada
   Tempo de CPU: 0.000 segundos
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
 * armazenando o maior ciclo encontrado
 */
void main()
{
	char troca;
    int  inicial, final, num, c, max;

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

			num = inicial;
			inicial = final;
			final = num;
		}

		max = 0;

		if (final <= 100)
		{
			if ((inicial <= 97) && (final >= 97)) max = 119;
		}
		else if (final <= 500)
		{
			if ((inicial <= 327) && (final >= 327)) max = 144;
		}
		else if (final <= 1000)
		{
			if ((inicial <= 871) && (final >= 871)) max = 179;
		}
		else if (final <= 2000)
		{
			if ((inicial <= 1161) && (final >= 1161)) max = 182;
		}
		else if (final <= 3000)
		{
			if ((inicial <= 2919) && (final >= 2919)) max = 217;
		}
		else if (final <= 5000)
		{
			if ((inicial <= 3711) && (final >= 3711)) max = 238;
		}
		else
		{
			if ((inicial <= 6171) && (final >= 6171)) max = 262;
		}

		if (max == 0)
		{
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
		}

		/* Imprime a resposta */
		if (troca)
			printf("%d %d %d\n", final, inicial, max);
		else+
			printf("%d %d %d\n", inicial, final, max);
    }
}
