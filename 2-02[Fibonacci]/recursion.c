#include <stdio.h>
#include <stdlib.h>

int recurse(int *fibo, int index);

int
main() {
	int *fibo;
	int bound;
	int i;

	printf("This program is used to compute the Fibonacci array\n");
	printf("\tPlease enter the highest bound of the Fibonacci-index: ");
	scanf("%d", &bound);
	
	fibo = malloc(bound * sizeof(int));	/* malloc @ <stdlib.h> or <malloc.h>*/

	recurse(fibo, bound - 1);

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

int 
recurse(int *fibo, int index) {
	int value;

	if (index == 0) {
		value = *(fibo + index) = 1;
	}else if (index == 1) {
		value = *(fibo + index) = recurse(fibo, index - 1);
	}else if (index > 1) {
		value = *(fibo + index) = recurse(fibo, index - 1) + recurse(fibo, index - 2);
	}
	
	return value;
}
