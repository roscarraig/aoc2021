#!/usr/bin/perl

use strict;
use warnings;

my @depth = ();
my $part1 = 0;
my $part2 = 0;
my $i = 0;

open FIN, '<'.$ARGV[0];
while(<FIN>)
{
  chomp;
  push @depth, int($_);
  if($i > 0)
  {
    if($depth[$i] > $depth[$i - 1])
    {
      $part1++;
    }
    if($i > 2 && $depth[$i] > $depth[$i - 3])
    {
      $part2++;
    }
  }
  $i++;
}
print "Part 1 $part1\nPart 2 $part2\n";
