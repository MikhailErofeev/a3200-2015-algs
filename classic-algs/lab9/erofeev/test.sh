#!/usr/bin/env bash




printf '3\n1 2 3 4 5 6 7 8 9 10' | python /Users/erofeev/projects/students/students-prs/Sadovnikov/lab9/Sadovnikov/lab9part1.py

p="/Users/erofeev/projects/students/students-prs/Sadovnikov/lab9/Sadovnikov/lab9part1.py"
cat ~/k-norm-random.data | python ${p}| python /Users/erofeev/projects/students/a3200-2015-algs/lab4/erofeev/check_sorted.py