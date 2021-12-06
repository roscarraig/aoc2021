#include <stdio.h>
#include <stdlib.h>
#include <string.h>

unsigned long long int pop(unsigned long long int *arr, int size)
{
  unsigned long long int x = arr[0];

  memcpy(arr, arr + 1, (size - 1) * sizeof(unsigned long long int));
  return(x);
}

void generation(unsigned long long int *arr, int size)
{
  unsigned long long int x = pop(arr, size);

  arr[6] += x;
  arr[8] += x;
}

unsigned long long int count(unsigned long long int *arr, int size)
{
  int i;
  unsigned long long int total = 0;

  for(i = 0; i < size; i++)
    total += arr[i];

  return(total);
}

int main(int argc, char **argv)
{
  FILE *fp = fopen(argv[1], "r");
  char  buffer[1024], *p = buffer;
  unsigned long long int   shoal[11], x;
  int i;

  fgets(buffer, 1024, fp);
  memset(shoal, 0, 11 * sizeof(unsigned long long int));

  while(p)
  {
    sscanf(p, "%d", &i);
    shoal[i]++;
    p = index(p, ',');
    if(p)
      p++;
  }
  for(i = 0; i < 80; i++)
    generation(shoal, 10);

  printf("Part 1: %llu\n", count(shoal, 10));

  for(i = 80; i < 256; i++)
    generation(shoal, 10);

  printf("Part 2: %llu\n", count(shoal, 10));
}
