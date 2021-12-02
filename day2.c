#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv)
{
  FILE *fp = fopen(argv[1], "r");
  char motion[16];
  int  delta;
  int *numbers;
  int  part1 = 0, part2 = 0;
  int  h = 0, d = 0, d2 = 0, a = 0;

  while(!feof(fp))
  {
    fscanf(fp, "%s %d\n", motion, &delta);
    if(motion[0] == 'f')
    {
      h += delta;
      d2 += a * delta;
    } else if (motion[0] == 'd') {
      d += delta;
      a += delta;
    } else if (motion[0] == 'u') {
      d -= delta;
      a -= delta;
    }
  }
  printf("Part 1: %d\n", h * d);
  printf("Part 2: %d\n", h * d2);
}
