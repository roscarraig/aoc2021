#!/usr/bin/perl

use strict;
use warnings;

sub part1
{
  my $result = 0;

  if (/.* \| (.*)/)
  {
    foreach my $item (split ' ', $1)
    {
      my $l = length($item);
      if($l == 2 or $l == 3 or $l == 4 or $l == 7)
      {
        $result++;
      }
    }
  }
  return($result);
}

sub matches
{
  my $src = shift;
  my $dst = shift;
  my $x;

  foreach my $x (split //, $src)
  {
    if(index($dst, $x) < 0)
    {
      return(0);
    }
  }
  return(1);
}

sub part2
{
  my @found = ('', '', '', '', '', '', '', '', '', '');
  my @parts = split(' \| ', $_[0]);
  my @feed = split(' ', $parts[0]);
  my @digits = split(' ', $parts[1]);
  my %lookup;
  my $i;
  my $result = 0;

  foreach $i (0..(scalar(@feed) - 1))
  {
    my $tmp = join("", sort(split(//, $feed[$i])));
    $feed[$i] = $tmp;
  }
  foreach $i (0..(scalar(@digits) - 1))
  {
    my $tmp = join("", sort(split(//, $digits[$i])));
    $digits[$i] = $tmp;
  }
  foreach $i (@feed)
  {
    if(length($i) == 2)
    { $found[1] = $i; $lookup{$i} = 1; }
    elsif(length($i) == 3)
    { $found[7] = $i; $lookup{$i} = 7; }
    elsif(length($i) == 4)
    { $found[4] = $i; $lookup{$i} = 4; }
    elsif(length($i) == 7)
    { $found[8] = $i; $lookup{$i} = 8; }
  }

  foreach $i (@feed)
  {
    if(!exists($lookup{$i}))
    {
      if(matches($found[1], $i) and length($i) == 5)
      { $found[3] = $i; $lookup{$i} = 3; }
      elsif(matches($found[4], $i))
      { $found[9] = $i; $lookup{$i} = 9; }
    }
  }

  foreach $i (@feed)
  {
    if(!exists($lookup{$i}))
    {
      if(matches($found[1], $i))
      { $found[0] = $i; $lookup{$i} = 0; }
      elsif(length($i) == 6 and !matches($found[1], $i))
      { $found[6] = $i; $lookup{$i} = 6; }
    }
  }

  foreach $i (@feed)
  {
    if(!exists($lookup{$i}))
    {
      if(matches($i, $found[6]))
      { $found[5] = $i; $lookup{$i} = 5; }
      elsif(!matches($i, $found[6]))
      { $found[2] = $i; $lookup{$i} = 2;}
    }
  }

  foreach $i (@digits)
  {
    $result *= 10;
    $result += $lookup{$i};
  }
  return $result;
}

my $part1 = 0;
my $part2 = 0;

open FIN, '<'.$ARGV[0];
while(<FIN>)
{
  chomp;
  $part1 += part1 $_;
  $part2 += part2 $_;
}
print("Part 1:", $part1, "\n");
print("Part 2:", $part2, "\n");
