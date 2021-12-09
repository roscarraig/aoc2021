#!/usr/bin/perl

use strict;
use warnings;

sub mark_basin
{
  my $i = shift;
  my $j = shift;
  my $size = 0;
  my $floorref = shift;

  if(substr($floorref->[$i], $j, 1) == '9')
  {
    return(0);
  }
  substr($floorref->[$i], $j, 1, '9');
  $size++;

  if($i > 0)
  {
    $size += mark_basin($i - 1, $j, $floorref);
  }
  if($j > 0)
  {
    $size += mark_basin($i, $j - 1, $floorref);
  }
  if($i < scalar(@$floorref) - 1)
  {
    $size += mark_basin($i + 1, $j, $floorref);
  }
  if($j < length($floorref->[0]) - 1)
  {
    $size += mark_basin($i, $j + 1, $floorref);
  }
  return($size);
}

sub main
{
  my @floor;
  open FIN, '<'.$ARGV[0];
  while(<FIN>)
  {
    chomp;
    push @floor, $_;
  }
  my $rl = length($floor[0]) - 1;
  my $ml = scalar(@floor) - 1;
  my $part1 = 0;
  my $part2 = 1;
  my $i;
  my $j;

  foreach $i (0..$ml)
  {
    foreach $j (0..$rl)
    {
      my $x = substr($floor[$i], $j, 1);

      if(!(($i > 0 && $x >= substr($floor[$i - 1], $j, 1))
       ||($j > 0 && $x >= substr($floor[$i], $j - 1, 1))
       ||($j < $rl && $x >= substr($floor[$i], $j + 1, 1))
       ||($i < $ml && $x >= substr($floor[$i + 1], $j, 1))))
      {
        $part1 += $x + 1;
      }
    }
  }
  print "Part 1: ", $part1, "\n";

  my @basins;
  foreach $i (0..$ml)
  {
    foreach $j (0..$rl)
    {
      push @basins, mark_basin($i, $j, \@floor);
    }
  }
  my @basinss = sort {$b <=> $a} @basins;
  foreach $i (0..2)
  {
    $part2 *= $basinss[$i];
  }
  print "Part 2: ", $part2, "\n";
}

main;
