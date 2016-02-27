time printf '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0' | python  /Users/erofeev/projects/students/a3200-2015-algs/tmp.py | python /Users/erofeev/projects/students/a3200-2015-algs/lab4/erofeev/check_sorted.py | python



p="/Users/erofeev/projects/students/a3200-2015-algs/lab6/erofeev/radix_sort.py"
# /Users/erofeev/projects/students/a3200-2015-algs/tmp.py
cat ~/norm-random.data | python ${p}| python /Users/erofeev/projects/students/a3200-2015-algs/lab4/erofeev/check_sorted.py
cat ~/same-data.data | python ${p} | python /Users/erofeev/projects/students/a3200-2015-algs/lab4/erofeev/check_sorted.py