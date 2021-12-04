#!/usr/bin/perl

use strict;
use warnings;

sub tonum
{
  my $val = shift;
  my $result = 0;
  my $i = 0;
  while( $i < length($val))
  {
    $result *= 2;
    if(substr($val, $i++, 1) == '1')
    {
      $result++;
    }
  }
  return $result;
}

sub most
{
  my $ind = shift;
  my @input = @_;
  my $i = 0;
  my $ones = 0;

  while($i < scalar(@input))
  {
    if(substr($input[$i++], $ind, 1) == '1')
    {
      $ones++;
    }
  }
  if(($ones * 2) >= scalar(@input))
  {
    return 1;
  }
  return 0;
}

sub least
{
  my $ind = shift;
  my @input = @_;
  my $i = 0;
  my $ones = 0;
  
  while($i < scalar(@input))
  {
    if(substr($input[$i++], $ind, 1) == '1')
    {
      $ones++;
    }
  }
  if(($ones * 2) < scalar(@input))
  {
    return 1;
  }
  return 0;
}

sub filter
{
  my $bit = shift;
  my @input = @_;
  my $value = '';
  my $i = 0;

  while($i < length($input[0]))
  {
    my $count = scalar(@input);
    my $cbit;
    my $j = 0;
    my $count2 = 0;
    my @input2 = ();

    if($bit == 1)
    {
      $cbit = most($i, @input);
    } else {
      $cbit = least($i, @input);
    }
    $value .= ($cbit ? '1': '0');
    $i++;

    while($j < $count)
    {
      if(substr($input[$j], 0, $i) == $value)
      {
        $input2[$count2++] = $input[$j];
      }
      $j++;
    }
    @input = @input2;
    $count = $count2;
    if(scalar(@input) == 1)
    {
      return $input[0];
    }
  }
  return $value;
}

my @numbers = ();
my $count = 0;
my $gamma = 0;
my $epsilon = 0;
my $i = 0;
open FIN, '<'.$ARGV[0];
while(<FIN>)
{
  chomp;
  $numbers[$count++] = $_;
}
while($i < length($numbers[0]))
{
  $gamma *= 2;
  $epsilon *= 2;
  $gamma += most($i, @numbers);
  $epsilon += least($i, @numbers);
  $i++;
}
print "Part 1:", $gamma * $epsilon, "\n";
my $a = tonum(filter(1, @numbers));
my $b = tonum(filter(0, @numbers));
print "Part 2:", $a * $b, "\n";
