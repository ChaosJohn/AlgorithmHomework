#include <stdio.h>

int recursion(int, int);

int
main() {
	printf("This Program is used to compute the number of divisions of a nonnegative-integer\n\nPlease enter a nonnegative-integer: ");
	int input;
	scanf("%d", &input);
	printf("%d\n", recursion(input, input));

	return 0;
}

int 
recursion(int total, int max) {
	if (total == 1 || max == 1)
		return 1;
	else if (total < max)
		return recursion(total, total);
	else if (total == max)
		return (1 + recursion(total, total - 1));
	else if (total > max && max > 1)
		return ((recursion(total, max - 1) +
					recursion(total - max, max)));
}
