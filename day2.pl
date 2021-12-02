#!/usr/bin/perl

use strict;
use warnings;

my $h = 0;
my $d = 0;
my $d2 = 0;
my $a = 0;

open FIN, '<'.$ARGV[0];
while(<FIN>)
{
  if(/(forward|down|up) (\d+)/)
  {
    if($1 eq 'forward')
    {
      $h += $2;
      $d2 += $a * $2;
    } elsif ($1 eq 'down') {
      $d += $2;
      $a += $2;
    } elsif ($1 eq 'up') {
      $d -= $2;
      $a -= $2;
    }
  }
}
print("Part 1:", $h * $d, "\n");
print("Part 2:", $h * $d2, "\n");
