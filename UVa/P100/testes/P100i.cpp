
/* @JUDGE_ID: 8580TT 100 C++ "<marquee>Top secret algorithm</marquee>" */

/* **********************************************************
   Problema:     The 3n+1 problem
   Estrat�gia:   For�a bruta evitando calcular n�meros cujo
   				 dobro j� foi calculado e calculando
   				 pot�ncias de dois diretamente.
   Tempo de CPU: 0.650 segundos
   Mem�ria:      296 kbytes

   10 Dez 2000

   S�rgio Anibal de Carvalho Junior
   http://pagina.de/sergioanibal
   http://i.am/sergioanibal
   ********************************************************** */

#include <stdio.h>
#include <math.h>

const double LOG_2 = log(2);

/*
 * Calcula o log de um n�mero na base 2
 */
double log2(int num)
{
	return log(num) / LOG_2;
}

/*
 * Calcula a quantidade de ciclos de um determinado n�mero
 */
int ciclos(int n)
{
	int 	ciclos = 1;
	double  k, resto;

    while (n != 1)
    {

		if (n % 2 == 0)
		{
			resto = modf( log2(n) , &k );

			if (resto == 0)
			{
				ciclos = ciclos + (int) k;
				break;
			}

	    	n = n / 2;
		}
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

	/* L� dois n�meros */
    while (scanf("%d %d\n", &inicial, &final)==2)
    {
		max = 0;

		/* Verifica a ordena��o do intervalo */
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
