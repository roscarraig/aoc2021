#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv)
{
  FILE *fp = fopen(argv[1], "r");
  char buffer[256];
  int count = 0, i;
  int *numbers;
  int  part1 = 0, part2 = 0;

  while(!feof(fp))
  {
    fgets(buffer, 256, fp);
    count++;
  }
  rewind(fp);
  numbers = (int *) malloc(count * sizeof(int));
  for(i = 0; i < count; i++)
  {
    fgets(buffer, 256, fp);
    sscanf(buffer, "%d\n", &(numbers[i]));
    if(i > 0 && numbers[i] > numbers[i - 1])
      part1++;
  }
  for(i = 0; i < count - 4; i++)
    if(numbers[i] < numbers[i + 3])
      part2++;
  printf("Part 1 %d\n", part1);
  printf("Part 2 %d\n", part2);
}
