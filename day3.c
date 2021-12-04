#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int most(int *numbers, int pos, int len, int count)
{
  int ones = 0, mask = 1 << (len - pos - 1), i;

  for(i = 0; i < count; i++)
    if((mask & numbers[i]) == mask)
      ones++;
  if(ones * 2 >= count)
    return(1);
  return(0);
}

int least(int *numbers, int pos, int len, int count)
{
  int ones = 0, mask = 1 << (len - pos - 1), i;

  for(i = 0; i < count; i++)
    if((mask & numbers[i]) == mask)
      ones++;
  if(ones * 2 < count)
    return(1);
  return(0);
}

int filter(int *numbers, int width, int bit, int count)
{
  int *c1 = malloc(count * sizeof(int));
  int *c2 = malloc(count * sizeof(int));
  int  value = 0, i, j, k, cbit, count2;

  memcpy(c1, numbers, count * sizeof(int));

  for(i = 0; i < width; i++)
  {
    count2 = 0;
    if(bit)
      cbit = most(c1, i, width, count) << (width - i - 1);
    else
      cbit = least(c1, i, width, count) << (width - i - 1);
    value += cbit;

    for(j = 0; j < count;j++)
    {
      if((c1[j] & (1 << (width - i - 1))) == cbit)
      {
        c2[count2++] = c1[j];
      }
    }
    memcpy(c1, c2, count2 * sizeof(int));
    count = count2;

    if(count == 1)
      return(c1[0]);
  }
  return(value);
}

int main(int argc, char **argv)
{
  FILE *fp = fopen(argv[1], "r");
  char  buffer[16];
  int   count = 0, i, width = 0, gamma = 0, epsilon = 0;
  int  *numbers;

  while (fgets(buffer, 16, fp))
    count++;

  rewind(fp);
  numbers = (int *) malloc(count * sizeof(int));

  for(i = 0; i < count; i++)
  {
    int j;

    fgets(buffer, 16, fp);

    if(width == 0)
      width = strlen(buffer) - 1;
    
    for(j = 0; j < width; j++)
    {
      numbers[i] *= 2;
      if(buffer[j] == '1')
        numbers[i]++;
    }
  }
  for(i = 0; i < width; i++)
  {
    gamma *= 2;
    epsilon *= 2;
    gamma += most(numbers, i, width, count);
    epsilon += least(numbers, i, width, count);
  }
  printf("Part 1 %d\n", gamma * epsilon);
  printf("Part 2 %d\n", filter(numbers, width, 1, count) * filter(numbers, width, 0, count));
}
