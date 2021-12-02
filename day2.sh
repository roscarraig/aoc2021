#!/bin/bash

h=0
d=0
d2=0
a=0

while IFS= read -r line
do
  move=$(echo $line | cut -f1 -d' ')
  dist=$(echo $line | cut -f2 -d' ')
  if [ $move == "forward" ]; then
    ((h += dist))
    ((d2 += dist * a))
  elif [ $move == "down" ]; then
    ((d += dist))
    ((a += dist))
  elif [ $move == "up" ]; then
    ((d -= dist))
    ((a -= dist))
  fi
done < $*
echo Part 1 $((h * d))
echo Part 2 $((h * d2))
