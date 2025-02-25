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
***********************************************************
01-18-2025
Ref: https://github.com/sanskrit-lexicon/PWG/issues/83#issuecomment-2592597118

Revise Bombay.BhP.index.Vol1.txt using diff_Bombay.BhP.index.Vol1.txt
Revise Bombay.BhP.index.Vol2.txt using diff_Bombay.BhP.index.Vol2.txt

cat Bombay.BhP.index.Vol1.txt Bombay.BhP.index.Vol2.txt > Bombay.BhP.index.txt

-----
# manual edit Bombay.BhP.index.txt
x- remove header text from volume II.
x- add newline after last line
  - not needed, as was done in Bombay.BhP.index.Vol2.txt
x- offload appendix  lines:
   from 'II	878	(XII)		1	7	30b'
  to end
  Put these lines in Bombay.BhP.appendix.index.txt
-----
remake index.js:
python make_js_index.py Bombay.BhP.index.txt index.js

python make_js_index.py Bombay.BhP.index.txt index.js
1924 Page records read from Bombay.BhP.index.txt
2620 lines written to index.js

# install in app
cp index.js ../ksverse.js
-------------------------------------------------------
Look for problems in index
---
# first run
python two_adhyaya_page.py Bombay.BhP.index.txt tempout.txt
4 problems identified
---
problem at irec=438 -- adhyaya wrong. corrected
---
problem at irec=440 -- adhyaya wrong

---  
problem at irec=477
I	428	(IV)	17	21	30	40b Agrees with pdf 1428.pdf
I	429	(IV)	18	13	25	42a Agrees with pdf 1429.pdf
  verses 4,18,1-12  missing!  no pdf page found here  !

---
problem at irec=602
I	540	(V)	7	7	10	16b
I	541	(V)	8	6	12	18a
 verses 5,8,1-5  missing!  No pdf page found here !


 page 1429.pdf
 https://sanskrit-lexicon-scans.github.io/bhagp_bom/pdfpages/1429.pdf

---
# end just two corrections to Bombay.BhP.index.txt

 I      397     (IV)    9       17      25      25a
-I      398     (IV)    8       26      34      25b
-I      399     (IV)    8       35      45      26a
+I      398     (IV)    9       26      34      25b
+I      399     (IV)    9       35      45      26a
 I      400     (IV)    9       46      57      26b

---
python make_js_index.py Bombay.BhP.index.txt index.js

1924 Page records read from Bombay.BhP.index.txt
2620 lines written to index.js

# install in app
cp index.js ../ksverse.js

---------------------------------------------------
01-20-2025
Edit to Bombay.BhP.index.txt
I	639	(VI)	2	1	8ab	5a
I	640	(VI)	2	8cd	12	5b

I	647	(VI)	3	17	24ab	9a
I	648	(VI)	3	24cd	27	9b

Here, Jim said he did this, but he did not actually do it before.
Now done.
---
# recompute index.js and install in app

python make_js_index.py Bombay.BhP.index.txt index.js
cp index.js ../ksverse.js

---
# commit this change.
git add .
git commit -m "Correct oversight in Bombay.BhP.index.txt
Ref: https://github.com/sanskrit-lexicon/PWG/issues/83"
git push
------------------------------------------------------
Missing pages from comments.docs.md
These are from volume 1
AB upload:
---
IV.41a.b.pdf
extract 2 pages renamed 1428x.pdf and 1428y.pdf
---
V.17.a.b.alt.pdf
extract 2 pages renamed 1540x.pdf and 1540y.pdf
---
VII.10.a.b.alt.pdf
extract 2 pages renamed 1748x.pdf and 1748y.pdf

Copy the 6 pages to bhagp_bom/pdfpages
-------------------------------------

# manual edit Bombay.BhP.index.txt
Change the index for the new pages
1428x.pdf  I	428x	(IV)	17	31	36	41a
1428y.pdf  I	428y	(IV)	18	1	12	41b
1540x.pdf  I	540x	(V)	7	11	14	17a
1540y.pdf  I	540y	(V)	8	1	5	17b
1748x.pdf  I	748x	(VII)	4	1	16	10a
   Note 1748x  -- Don't see number at end of verse 1
1748y.pdf  I	748y	(VII)	4	17	31	10b
   Note: 1749.pdf  I	749	(VII)	4	34	44	11a
      verses 32 and 33 are missing.

--------------------------
python make_js_index.py Bombay.BhP.index.txt index.js
1930 Page records read from Bombay.BhP.index.txt
2626 lines written to index.js

cp index.js ../ksverse.js

Sync to github

--------------------------
Correction to Bombay.Bhp.index.txt
OLD:
I	748	(VII)	4	1	9	9b
I	748x	(VII)	4	1	16	10a
NEW:
I	748	(VII)	4	1	9	9b
I	748x	(VII)	4	10	16	10a

python make_js_index.py Bombay.BhP.index.txt index.js
cp index.js ../ksverse.js

Sync to github

THE END
