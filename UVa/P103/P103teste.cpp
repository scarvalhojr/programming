#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int lexi(int a, int b)
{
	char sa[3], sb[3];

	// return 0;

	itoa(a, sa, 10);
	itoa(b, sb, 10);

	return strcmp(sa,sb);
}

char* itoa(int num, char *s)
{
	int d, pos;

	if (num == 0)
	{
		s[0] = '0';
		s[1] = '\0';
		return s;
	}

	pos = floor(log10(num)) + 1;
	s[pos--] = '\0';

	while(num > 0)
	{
		d = num - floor(num / 10) * 10;
		s[pos--] = '0' + d;
		num = (num - d) / 10;
	}

	return s;
}

/*
 * Programa principal
 */
void main()
{
	int a;//, b;
	char s[5];

	if (strcmp(itoa(3,s),"3")==0)
		if (strcmp(itoa(0,s),"0")==0)
			if (strcmp(itoa(30,s),"30")==0)
				if (strcmp(itoa(305,s),"305")==0)
					if (strcmp(itoa(48765,s),"48765")==0)
						if (strcmp(itoa(500000,s),"500000")==0)
							printf("ok");
	/*
	// Lê a quantidade e a dimensão das caixas
	while (scanf("%d",&a)==1)
	{
		itoa(a,s);
		printf("\n%d =\t%s",a,s);
	}
	*/
}
