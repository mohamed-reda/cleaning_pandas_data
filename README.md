to clean data ask what to do if data is:
---

1 missing
2 duplicated
3 has unuseful spaces,+,_,-....etc
4 format
5 the data range
6 the data length or size
7 has the same measure


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
