# Using Argparse, create a program that can calculate the mean (--mean), max (--max), min (--
# min) and sum (--sum) of one or more supplied integers (–vals). Values are required, so if no
# values are passed, show an error message. The program always has to calculate the max. You
# have to be able to supply multiple operations as well.
#
# Example: python myprog.py –vals 10 20 30 –sum –mean --min
#   Mean: 20.0
#   Min: 10
#   Max: 30
#   Sum: 60
# Example: python myprog.py –vals 10 20 30 40
#   Sum: 100
# Example: python myprog.py
#   error: the following arguments are required: --vals
# Example: python myprog.py –vals
#   error: argument --vals: expected at least one argument
# Example: python myprog.py –vals 10
#   Max: 10

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--vals', '-vals', nargs='+', type=int, required=True)
parser.add_argument('--mean', '-mean', action='store_true')
parser.add_argument('--sum', '-sum', action='store_true')
parser.add_argument('--min', '-min', action='store_true')
parser.add_argument('--max', '-max', action='store_true')

args = parser.parse_args()

val_sum = 0
val_max = args.vals[0]
val_min = args.vals[0]

for x in args.vals:
    if args.min and x < val_min:
        val_min = x
    if args.max and x > val_max:
        val_max = x
    val_sum += x

if args.mean:
    print(f"Mean: {val_sum / len(args.vals)}")
if args.min:
    print(f"Min: {val_min}")
if args.max:
    print(f"Max: {val_max}")
if args.sum:
    print(f"Sum: {val_sum}")
