#include <stdio.h>

int
main() {
	int fibo[100];
	int bound;
	int i;
	
	printf("This program is used to compute the Fibonacci array\n");
	printf("\tPlease enter the highest bound of the Fibonacci-index: ");
	scanf("%d", &bound);

	fibo[0] = fibo[1] = 1;
	for (i = 2; i < bound; i++) 
		fibo[i] = fibo[i - 1] + fibo[i - 2];

	printf("Fibonacci: \n\t");
	for (i = 0; i < bound; i++) {
		printf("%d", fibo[i]);
		if (i % 5 == 4)
			printf("\n\t");
		else
			printf("\t");
	}
	printf("\n");

	return 0;
}
