#!/usr/bin/perl

use strict;
use warnings;

open FIN, '<'.$ARGV[0];
my $line = <FIN>;
chomp $line;
my @shoal = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
my $total = 0;
foreach (split /,/, $line) {
  $shoal[$_]++;
  $total++;
}
for (1..80)
{
  my $x = shift @shoal;
  push @shoal, 0;
  $shoal[6] += $x;
  $shoal[8] += $x;
  $total += $x;
}
print("Part 1: ", $total, "\n");
for (81..256)
{
  my $x = shift @shoal;
  push @shoal, 0;
  $shoal[6] += $x;
  $shoal[8] += $x;
  $total += $x;
}
print("Part 1: ", $total, "\n");
