#!/usr/bin/perl

use strict;
use warnings;

sub generation
{
  my $shoalref = $_[0];
  my $x = shift @$shoalref;
  push @$shoalref, 0;
  $shoalref->[6] += $x;
  $shoalref->[8] += $x;
  return $x;
}

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
  $total += generation \@shoal;
}
print("Part 1: ", $total, "\n");
for (81..256)
{
  $total += generation \@shoal;
}
print("Part 2: ", $total, "\n");
