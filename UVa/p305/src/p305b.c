/*
 ============================================================================
 Name        : p305.c
 Author      : Sergio A. de Carvalho Jr.
 Method      : Stupid brute force
 Result      : Time exceed
 ============================================================================
 */

#include <stdio.h>

#define MAX_K 13

/* Guy g => position g - k - 1 in the array */
#define pos(g) (g - k - 1)

void mainb (void)
{
	int alive[MAX_K];
	int k, m, g, s, left, found;

	while (scanf("%d\n", &k) == 1 && k != 0)
	{
		/* Search for an m that satisfies the condition */
		for (m = k, found = 0; !found;)
		{
			m++;

			/* Mark all bad guys as alive
			   bad guys are numbered k+1 to 2*k */
			for (g = k + 1; g <= 2 * k; g++) alive[pos(g)] = 1;

            left = k;
			g = 0;

			while (1)
			{
                /* Count m alive guys to next target */
                s = 0;
                while (s < m)
                {
                        /* Move one position */
                        g = g < 2 * k ? g + 1 : 1;

                        /* Count if it's a good guy (always alive)
                           or bad guy alive */
                        if (g <= k || alive[pos(g)]) s++;
                }

                if (g <= k)
                {
                	/* Stop if pointing at good guy */
                	break;
                }

                /* Kill guy g */
				alive[pos(g)] = 0;
				left--;

				/* Are we done? */
				if (!left)
				{
					found = 1;
					break;
				}
			}
		}

		printf ("%d\n", m);
	}
}
