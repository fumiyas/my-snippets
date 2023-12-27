#!/usr/bin/env perl

use strict;
use warnings;

if (@ARGV != 2) {
  printf("Usage: %s FILENAME SIZE\n", $0);
  exit(1)
}

my $fname = $ARGV[0];
my $end = ($ARGV[1] / 4) - 1;

open(my $fh, ">$fname") || die "Failed to open: $fname: $!";
for my $i (0..$end) {
  $fh->print(pack("I", $i));
}
