
#include <stdio.h>
#include <math.h>

double log2(int num)
{
	return log10(num) / M_LN2;
}

void main()
{
	double	ed, resto;
	int 	e, p;

	for (int i = 2; i > 0; i *= 2)
	{
		resto = modf( log2(i) , &ed );

		if (resto > 0) printf("resto = %f\n", resto);

		e = (int) ed;

		p = pow(2,e);

		if (i == p)
			printf("log2(%d)\t= %d\tpois 2^%d\t= %d\n", i, e, e, p);
		else
			printf("log2(%d)\t= %d\tmas 2^%d\t= %d e nao %d !!!\n", i, e, e, p, i);
    }
}
