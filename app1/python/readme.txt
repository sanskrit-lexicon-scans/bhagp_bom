Convert the tab-delimited index file into a json object,
python make_js_index.py Bombay.BhP.index.txt index.js

1924 Page records read from Bombay.BhP.index.txt
2620 lines written to index.js

# install in app
cp index.js ../ksverse.js
---------------------------------------------------------------------
# concatenate the index files for volumes 1 and 2:
cat Bombay.BhP.index.Vol1.txt Bombay.BhP.index.Vol2.txt > Bombay.BhP.index.txt

# manual edit Bombay.BhP.index.txt
- remove header text from volume II.
- add newline after last line.
- offload lines from 'II	878	(XII)		1	7	30b'
  to end (this line has blank 'skanda' field
  -- These are verses in an 'appendix'
  Put in file
  Bombay.BhP.appendix.index.txt   31 lines
----------------------------
# adjustments to make_js_index.py
---
droman_int  add X, XI, XII
add 'ipage' for last field -- currently unused
set flagnum to skip lines with blank 'kanda'
lines after end of 12th skandha of volume II.
These are currently ignored.
THe 'kanda' field is blank
---
vol -  two volumes (Burnouf had three)
---

