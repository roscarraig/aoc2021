#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv)
{
  FILE *fp = fopen(argv[1], "r");
  char  buffer[256], x;
  int   count = 0, len, i, j, part1 = 0;
  char *floor;

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
      if(!((i > 0 && x >= floor[(i - 1)* len + j]) || (j > 0 && x >= floor[i * len + j - 1]) || (j < len - 1 && x >= floor[i * len + j + 1]) || (i < count - 1 && x >= floor[(i + 1) * len + j])))
        part1 += 1 + (int) (x - '0');
    }
  }
  printf("Part 1: %d\n", part1);
}
