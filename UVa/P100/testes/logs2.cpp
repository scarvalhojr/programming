
#include <stdio.h>
#include <math.h>

const double LOG10_2 = log10(2);

int log2(int num)
{
	double r = log10(num) / LOG10_2;

	return (int) r;
}

void main()
{
	int e, p;

	for (int i = 2; i > 0; i *= 2)
	{
		e = log2(i);

		p = pow(2,e);

		if (i == p)
			printf("log2(%d)\t= %d\tpois 2^%d\t= %d\n", i, e, e, p);
		else
			printf("log2(%d)\t= %d\tmas 2^%d\t= %d e nao %d !!!\n", i, e, e, p, i);
    }
}
