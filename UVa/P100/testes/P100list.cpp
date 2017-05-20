
#include <stdio.h>

void main()
{
	int  num, ciclos;

	for (int i = 1; i <= 30; i++)
	{
		num = i;
		ciclos = 1;

		while (num != 1)
		{
			if (num % 2 == 0)
				num = num / 2;
			else
				num = 3 * num + 1;

			ciclos++;
		}

		printf("%d %d\n", i, ciclos);
    }
}
