to clean data ask what to do if data is:
---

1. missing (for NAN use df['column_name'].isna().sum()) but there is also
   {'NA' , 'nan' , '0'(sometimes it's not valid) , '.' ,...}
2. duplicated
3. has unuseful spaces,+,_,-....etc
4. format
5. the data range
6. the data length or size
7. has the same measure
8. the logic (for example check if the age = today - birthday) for each row, this is the Cross field validation

----

How to deal with missing data?
--
Simple approaches:

1. Drop missing data
2. Impute with statistical measures (mean, median, mode..)
   More complex approaches:
1. Imputing using an algorithmic approach
2. Impute with machine learning models

-----
to run jupyter:

jupyter notebook

(Use Control-C to stop this server)

----
pip install -r requirements.txt

python -m pip install jupyter

---
memory profile:

@memory_profiler.profile

python -m memory_profiler main.py

---

from line_profiler_pycharm import profile

@profile

python -m line_profiler main.py.lprof > results.txt
