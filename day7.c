#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int min(int *arr, int count)
{
  int result = arr[0], i;

  for(i = 1; i < count; i++)
  {
    if(arr[i] < result)
      result = arr[i];
  }
  return(result);
}

int cost(int *crabs, int pos, int count, int *costs)
{
  int result = 0, i;

  for(i = 0; i < count; i++)
    result += costs[abs(pos - crabs[i])];
  return(result);
}

int main(int argc, char **argv)
{
  FILE *fp = fopen(argv[1], "r");
  char  buffer[8192], *p = buffer;
  int   count = 0, i = 0;
  int  *crabs, low, high, *costs, result;

  fgets(buffer, 8192, fp);

  while(p)
  {
    p = index(p, ',');
    count++;
    if(p)
      p++;
  }
  crabs = malloc(count * sizeof(int));
  memset(crabs, 0, sizeof(int) * count);
  p = buffer;

  while(p)
  {
    sscanf(p, "%d", crabs + i++);
    p = index(p, ',');

    if(p)
      p++;
  }
  low = crabs[0];
  high = crabs[0];

  for(i = 1; i < count; i++)
  {
    if(crabs[i] < low)
      low = crabs[i];
    else if (crabs[i] > high)
      high = crabs[i];
  }
  costs = malloc((1 + high - low) * sizeof(int));
  memset(costs, 0, (1 + high - low) * sizeof(int));

  for (i = 1; i <= 1 + high - low; i++)
    costs[i] = i;

  result = cost(crabs, low, count, costs);
  for (i = low + 1; i <= high; i++)
  {
    int tmp = cost(crabs, i, count, costs);

    if(tmp < result)
      result = tmp;
  }
  printf("Part 1: %d\n", result);
  for (i = 1; i <= 1 + high - low; i++)
    costs[i] += costs[i - 1];
  result = cost(crabs, low, count, costs);
  for (i = low + 1; i <= high; i++)
  {
    int tmp = cost(crabs, i, count, costs);

    if(tmp < result)
      result = tmp;
  }
  printf("Part 2: %d\n", result);
}
