#!/bin/bash

depths=`cat $*`
depthlist=()
i=0
part1=0
part2=0

for x in $depths;
do
  depthlist[$i]=$x
  if (( i > 0 )); then
    if [[ ${depthlist[$i]} -gt ${depthlist[((i - 1))]} ]]; then
      ((part1++))
    fi
    if (( i > 2 )); then
      if [[ ${depthlist[$i]} -gt ${depthlist[((i - 3))]} ]]; then
        ((part2++))
      fi
    fi
  fi
  ((i++))
done
echo "Part 1:" $part1
echo "Part 2:" $part2
