12-30-2024
Bombay  editions of Bhagavata purana.

See readme_sources.txt for discussion of the pdfs.

The files further used are in orig directory:
bombay_v1.pdf and bombay_v2.pdf

---------------------------------------------------
Extract as separate pdfs
mkdir extracts
# v1
open orig/bombay_v1.pdf with Acrobat
choose menu : Document/extract pages
 From 1 to 827, Extract Pages As Separate Files, in extracts folder
Filenames: 'bombay_v1 N.pdf'  (N = 1,...,827)

# v2
open orig/bombay_v2.pdf with Acrobat
choose menu : Document/extract pages
 From 1 to 917, Extract Pages As Separate Files, in extracts folder
Filenames: 'bombay_v2 N.pdf'  (N = 1,...,917)

(+ 827 917) = 1744 files

-----------------------------------------------------------

# copy files in 'extracts' to 'pdfpages', renaming as
# 'vX_burnouf Y.pdf' to Z.pdf where
#  Z = XW  where W is 3-digit 0-filled
 Example bombay_v2 5.pdf -> 2005.pdf
# Construct script renum_bombay.sh to copy and rename
python make_renum_pages.py extracts pdfpages renum_bombay.sh

2304 files in extracts
2304 lines written to renum_bombay.sh

# init pdfpages
rm -r pdfpages
mkdir pdfpages
# copy the files:
sh renum_bombay.sh
1001.pdf - 1827.pdf
2001.pdf - 2917.pdf

-----------------------------------------------
Now, make a new public repo at github
 in organization sanskrit-lexicon-scans  
 name: bhagp_bom


cd /c/xampp/htdocs/sanskrit-lexicon-scans/
 git clone git@github.com:sanskrit-lexicon-scans/bhagp_bom.git


copy pdfpages to /c/xampp/htdocs/sanskrit-lexicon-scans/bhagp_bom
cp -r  pdfpages /c/xampp/htdocs/sanskrit-lexicon-scans/bhagp_bom

Further work done in /c/xampp/htdocs/sanskrit-lexicon-scans/bhagp_bom

THE END
