/*
 ============================================================================
 Name        : p616.c
 Author      : Sergio A. de Carvalho Jr.
 Method      : Recursive brute force
 Result      :
 ============================================================================
 */

#include <stdio.h>

#define TRUE  1
#define FALSE 0

/* Check if we can divide n coconuts
 * between p people and 1 monkey
 * after t people wake up */
int can_divide (int n, int p, int t)
{
	if (t == 0)
	{
		/* Monkeys get nothing in the morning
		 * so if we can divide n coconuts evenly
		 * between p people, we're good; otherwise
		 * the division failed */
		if (n % p == 0)
			return TRUE;
		else
			return FALSE;
	}

	/* Give 1 coconut to the monkey */
	n = n - 1;

	/* If we can't divide the remaining coconuts
	 * evenly between the people, we failed */
	if (n % p != 0) return FALSE;

	/* If we can, wake-up one person and
	 * get rid of his/her share */
	n = n - (n / p);

	/* Continue recursion with 1 less person to wake-up */
	return can_divide (n, p, t - 1);
}

void main(void)
{
	int n, p;

	while (scanf("%d\n", &n) == 1 && n != -1)
	{
		for (p = n / 2; p > 1; p--)
			if (can_divide(n, p, p))
				break;

		if (p > 1)
			printf ("%d coconuts, %d people and 1 monkey\n", n, p);
		else
			printf ("%d coconuts, no solution\n", n);
	}
}
