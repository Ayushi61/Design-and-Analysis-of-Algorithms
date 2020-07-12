#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <pthread.h>
#include <time.h>
#define MAX_STRING_SIZE 100
#define MAX_LINES 100
int max_level;
int thread;
char *array[MAX_LINES];
int tot_size,min;
typedef struct m_t{
	int tid;
	int curr_level;
	int size_arr;
	//int max_level;
} merge_thread;

void merge(char** array, int l,int m, int r)
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
	{
		strcpy( L1[i],array[l + i]);
		//printf("array is %s\n",L1[i]);
	}
	for (i = 0; i < n2; i++)
		strcpy(R1[i],array[m+1 + i]);
	
	i = 0;
	j = 0;
	k = l;

	while (i < n1 && j < n2)
	{
		if (strcmp(L1[i], R1[j])<=0)
		{
			strcpy(array[k],L1[i]);
			i++;
		}
		else
		{
			strcpy(array[k],R1[j]);
			j++;
		}
		k++;
	}
	while (i < n1)
	{
		strcpy( array[k],L1[i]);
		i++;
		k++;
	}
	while (j < n2)
	{
		strcpy( array[k],R1[j]);
		j++;
		k++;
	}
	free(R1);
	free(L1);
	
}

int mergeSort(char **array, int l, int r)
{
	int m;
	if (l < r)
	{
		m = (int)((l + r - 1) / 2);
		//printf("line is %s\n",array[m]);
		mergeSort(array, l, m);
		mergeSort(array, m+1, r);
		merge(array, l, m, r);
	}
	return 0;
}
/* merge locally sorted sections */
void merge_sections_of_array(char **arr, int number, int aggregation) {
    for(int i = 0; i < number; i = i + 2) {
        int left = i * (min * aggregation);
        int right = ((i + 2) * min * aggregation) - 1;
        int middle = left + (min * aggregation) - 1;
        if (right >= tot_size) {
            right = tot_size - 1;
        }
        merge(array, left, middle, right);
    }
    if (number / 2 >= 1) {
        merge_sections_of_array(arr, number / 2, aggregation * 2);
    }
}
void* wrap_thread(void *arg)
{
	merge_thread *m_thread=arg;
	//int id=
	int l,r,i,m;
	int tid=m_thread->tid;
	int curr_level=m_thread->curr_level;
	int size_arr=m_thread->size_arr;
	if(curr_level==max_level)
	{
		
		l=tid*min;
		r=(tid+1)*min - 1;
		m=l+(r-l)/2;
		if(l<r)
		{
			mergeSort(array,l,r);
			mergeSort(array,l+1,r);
			merge(array,l,m,r);
		}
		
	}
	else
	{
		pthread_t *threads=(pthread_t *)malloc(sizeof(pthread_t)*thread);
		for(i=0;i<thread;i++)
		{
			m_thread->tid=i;
			m_thread->curr_level=curr_level+1;
			m_thread->size_arr=size_arr/thread;
			pthread_create(&threads[i], NULL, wrap_thread, m_thread);
			
		}
		for(i=0;i<thread;i++)
		{
			pthread_join(threads[i],NULL);
		}
		merge_sections_of_array(array, thread, 1);
    
	}
}

int main(int argc,char **argv)
{
	if (argc != 4)
	{
		printf("enter the file name min and thread only");
		exit(1);
	}
	
	int i = 0;
	char arr[256];
	//char* array[MAX_LINES];
	min=atoi(argv[2]);
	thread=atoi(argv[3]);
	//array= (char**)malloc(sizeof(char*) * MAX_LINES);
	for (i = 0; i < MAX_LINES; i++)
		array[i] = (char*)malloc(sizeof(char) * MAX_STRING_SIZE);
	FILE* fp= fopen(argv[1], "r");
	i = 0;
	while (fgets(array[i], sizeof(array[i]), fp) != NULL) {
//		fprintf(stdout, "got line: %s\n", array[i]);
		i++;
	}
	tot_size=i-1;
	int size=i-1;
	int l=0;
	int r=size;
//	printf("size of is %s\n",array[r]);
	pthread_t *threads=(pthread_t *)malloc(sizeof(pthread_t));
	merge_thread *m_thread=(merge_thread *)malloc(sizeof(merge_thread));
	m_thread->tid=0;
	m_thread->curr_level=0;
	m_thread->size_arr=size+1;
	//m_thread->max_level=;
	max_level=(size+1)/(min*thread);
	if(tot_size/thread>min)
	{
	pthread_create(&threads[0], NULL, wrap_thread, m_thread);
	pthread_join(threads[0],NULL);
	}
	else
	{
		mergeSort(array,l,r);
	}
	//for(i=0;i<thread;i++)
	//{
	//	pthread_create(&threads[i], NULL, sort_thread, tsk);
	//}
	//merge_thread *m_thread=(merge_thread *)malloc(sizeof(merge_thread)*thread);
	/*int arrsize=(size+1)/thread;
	if(arrsize>min)
	{
		for(i=0;i<thread;i++)
		{
			m_thread.thread_no=i;
			m_thread.arr_p=array+i*arrsize;
			m_thread.l=i*arrsize;
			m_thread.r=(i+1)*arrsize-1;
			pthread_create(&threads[i], NULL, wrap_thread, m_thread);
		}
	}
	else{
		mergeSort(array,l,r);
	}*/
	//mergeSort(array,l,r);
	FILE *wfp=fopen("output.txt","w");
	
	for(i=0;i<=size;i++)
	{
		fprintf(wfp, "%s", array[i]);
	}
	 
	fclose(fp);
	fclose(wfp);
//	printf("hello");
	return 0;
}


