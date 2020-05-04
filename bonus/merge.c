#include <stdio.h>
#include <pthread.h>
#include <time.h>
#define MAX_STRING_SIZE 100
#define MAX_LINES 100
void merge(char** array, int l, int r)
{
	int n1, n2;
	char **L1, **L2,**R1,**R2;
	int i,j,k;
	n1 = m - l + 1;
	n2 = r - m;
	L1 = (char **)malloc(sizeof(char *) * n1);
	for (i = 0; i < n1; i++)
		L1[i] = (char*)malloc(sizeof(char) * MAX_STRING_SIZE);
	//L2 = (char**)malloc(sizeof(char*) * n1);
	//for (i = 0; i < n1; i++)
	//	L2[i] = (char*)malloc(sizeof(char) * MAX_STRING_SIZE);
	R1 = (char**)malloc(sizeof(char*) * n2);
	for (i = 0; i < n2; i++)
		R1[i] = (char*)malloc(sizeof(char) * MAX_STRING_SIZE);
	//R2 = (char**)malloc(sizeof(char*) * n2);
	//for (i = 0; i < n2; i++)
	//	R2[i] = (char*)malloc(sizeof(char) * MAX_STRING_SIZE);

	for (i = 0; i < n1; i++)
		strcpy( array[l + i], L1[i]);
	for (i = 0; i < n2; i++)
		strcpy(array[m+l + i], R1[i]);
	
	i = 0;
	j = 0;
	k = 0;

	while (i < n1 && j < n2)
	{
		if (L1[i] <= R1[j])
		{
			strcpy(L1[i], array[k]);
			i++;
		}
		else
		{
			strcpy(R1[j], array[k]);
			j++;
		}
		k++;
	}
	while (i < n1)
	{
		strcpy(L1[i], array[k]);
		i++;
		k++;
	}
	while (i < n2)
	{
		strcpy(R1[j], array[k]);
		j++;
		k++;
	}
	free(R1);
	free(L1);
	
}

void mergeSort(char **array, int l, int r)
{
	int m;
	if (l < r)
	{
		m = (int)(l + r - 1) / 2;
		mergeSort(array, l, m);
		mergeSort(array, m, r);
		merge(array, l, m, r);
	}
}

int main(int argc,char **argv)
{
	/*if (argc != 1)
	{
		printf("enter the file name only");
		exit(1);
	}

	int i = 0;
	char** array;
	array= (char**)malloc(sizeof(char*) * MAX_LINES);
	for (i = 0; i < MAX_LINES; i++)
		array[i] = (char*)malloc(sizeof(char) * MAX_STRING_SIZE);
	FILE* fp= fopen(argv[0], 'r');
	i = 0;
	while (fgets(array[i], sizeof(array[i]), fp) != NULL) {
		fprintf(stderr, "got line: %s\n", array[i]);
		i++;
	}
	fclose(fp);*/
	printf("hello");
	return 0;
}
