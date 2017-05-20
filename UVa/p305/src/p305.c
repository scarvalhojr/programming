/*
 ============================================================================
 Name        : p305.c
 Author      : Sergio A. de Carvalho Jr.
 Method      : Clever with pre-computation
 Result      : Accepted
 ============================================================================
 */

#include <stdio.h>

#define MAX_K 13

void main (void)
{
	int answer[MAX_K];
	int k, m, g, alive;

	/* initialise result table */
	for (g = 0; g < MAX_K; g++) answer[g] = 0;

	while (scanf("%d\n", &k) == 1 && k != 0)
	{
		/* if we don't know the answer yet */
		if (!answer[k-1])
		{
			/* number of guys alive (good & bad) */
			alive = 2 * k;

			/* m must be > k */
			m = k;

			/* stop when only k (good) guys are left */
			while (alive > k)
			{
				m++;

				/* reset number of live guys */
				alive = 2 * k;

				/* start aiming at mth guy */
				g = 1 + (m - 1) % alive;

				/* while we're aiming at a bad guy */
				while (g > k)
				{
					/* kill bad guy */
					g--;
					alive--;

					/* cycle to next guy */
					g = 1 + (g + m - 1) % alive;
				}
			}

			/* save answer for k */
			answer[k-1] = m;
		}

		printf ("%d\n", answer[k-1]);
	}
}
