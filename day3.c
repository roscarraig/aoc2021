#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int most(int *numbers, int pos, int len, int count)
{
  int ones = 0, mask = 1 << (len - pos - 1), i;

  for(i = 0; i < count; i++)
    if(mask & numbers[i] == mask)
      ones++;
  if(ones * 2 >= count)
    return(1);
  return(0);
}

int least(int *numbers, int pos, int len, int count)
{
  int ones = 0, mask = 1 << (len - pos - 1), i;

  for(i = 0; i < count; i++)
    if(mask & numbers[i] == mask)
      ones++;
  if(ones * 2 < count)
    return(1);
  return(0);
}

int main(int argc, char **argv)
{
  FILE *fp = fopen(argv[1], "r");
  char  buffer[16];
  int   count = 0, i, width = 0, gamma = 0, epsilon = 0;
  int  *numbers;

  while (fgets(buffer, 256, fp))
    count++;

  rewind(fp);
  numbers = (int *) malloc(count * sizeof(int));

  for(i = 0; i < count; i++)
  {
    int j;

    fgets(buffer, 256, fp);

    if(width == 0)
      width = strlen(buffer) - 1;
    
    for(j = 0; j < width; j++)
    {
      numbers[i] *= 2;
      if(buffer[j] == '1')
        numbers[i]++;
    }
    printf("%d ", numbers[i]);
  }
  printf("\n");
  for(i = 0; i < width; i++)
  {
    gamma *= 2;
    epsilon *= 2;
    gamma += most(numbers, i, width, count);
    epsilon += least(numbers, i, width, count);
  }
  printf("Part 1 %d %d\n", gamma, epsilon);
  printf("Part 1 %d\n", gamma * epsilon);
}
