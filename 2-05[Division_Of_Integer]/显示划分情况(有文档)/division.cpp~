#include <stdio.h>
#include <iostream>

#define MAX 100

using namespace std;

int array[MAX] = {0};

static int amount = 0;

void output(int);

void division(int, int);

int
main() {
	int input;

	cout<<"Please enter a nonnegative integer: ";
	cin>>input;

	division(input, 0);

	cout<<endl<<"\t"<<amount<<" ways of division"<<endl<<endl;

	return 0;
}

void
output(int num) {
	int i;
	for (i = 0; i < num; i++) 
		cout<<array[i]<<" ";
	cout<<endl;

	amount++;
}

void
division(int max, int index) {
	int i;
	if (max == 0) 
		output(index);
	else
		for(i = max; i > 0; i--) {
			if (index == 0 || i <= array[index - 1]) {
				array[index] = i;
				division(max - i, index + 1);
			}
		}
}
