#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare(const void *a, const void *b)
{
  int ia = *((int *) a);
  int ib = *((int *) b);

  if (ia == ib)
    return 0;
  if (ia < ib)
    return 1;
  return -1;
}

int mark_basin(int i, int j, int count, int len, char *floor)
{
  int size = 0;

  if(floor[i * len + j] == '9')
    return (0);

  floor[i * len + j] = '9';
  size++;

  if(i > 0)
    size += mark_basin(i - 1, j, count, len, floor);

  if(j > 0)
    size += mark_basin(i, j - 1, count, len, floor);

  if(i < count - 1)
    size += mark_basin(i + 1, j, count, len, floor);

  if(j < len - 1)
    size += mark_basin(i, j + 1, count, len, floor);

  return(size);
}

int main(int argc, char **argv)
{
  FILE *fp = fopen(argv[1], "r");
  char  buffer[256], x;
  int   count = 0, len, i, j, part1 = 0, part2 = 1, y;
  char *floor;
  int  *sizes = NULL, basincount = 0;

  while (fgets(buffer, 256, fp))
  {
    count++;
    len = strlen(buffer) - 1;
  }
  rewind(fp);
  floor = malloc(count * len);
  memset(floor, 0, count * len);

  for(i = 0; i < count; i++)
  {
    fgets(buffer, 256, fp);
    memcpy(floor + i * len, buffer, len);
  }

  for(i = 0; i < count; i++)
  {
    for(j = 0; j < len; j++)
    {
      x = floor[i * len + j];
      if(!(
            (i > 0 && x >= floor[(i - 1) * len + j])
            || (j > 0 && x >= floor[i * len + j - 1])
            || (j < len - 1 && x >= floor[i * len + j + 1])
            || (i < count - 1 && x >= floor[(i + 1) * len + j])))
        part1 += 1 + (int) (x - '0');
    }
  }
  printf("Part 1: %d\n", part1);

  for(i = 0; i < count; i++)
  {
    for(j = 0; j < len; j++)
    {
      y = mark_basin(i, j, count, len, floor);
      if(y > 0)
      {
        int *new = (int *) malloc(++basincount * sizeof(int));

        if (sizes)
        {
          memcpy(new, sizes, (basincount - 1) * sizeof(int));
          free(sizes);
        }
        sizes = new;
        sizes[basincount - 1] = y;
      }
    }
  }
  qsort(sizes, basincount, sizeof(int), compare);
  for(i = 0; i < 3; i++)
    part2 *= sizes[i];

  printf("Part 2: %d\n", part2);
}
