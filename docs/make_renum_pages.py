# coding=utf-8
""" make_renum_pages.py  for bombay edition
"""
# 
import sys,re,codecs
import os

def makesh(dirin,dirout):
 dirin1 = dirin
 print('dirin1=',dirin1)
 filesin = os.listdir(dirin1)
 print(len(filesin),"files in",dirin1)
 # os.chdir('../')
 ans = []
 for i,filein in enumerate(filesin):
  m = re.search('^bombay_v([12]) ([0-9]+).pdf$',filein)
  #print(filein)
  #exit(1)
  if m == None:
   print('skipping file',filein)
   continue
  vol = m.group(1)
  page = int(m.group(2))
  vol = m.group(1) # the volume
  fileout = '%s%03d.pdf' % (vol,page)
  pathin = '%s/%s' % (dirin,filein)
  pathout = '%s/%s' %(dirout,fileout)
  # quote  pathin since there is a space
  pathin1 = "'%s'" %pathin
  sh = "cp %s %s" %(pathin1,pathout)
  ans.append(sh)
 return ans 

def write_script(fileout,shfile):
 with codecs.open(fileout,"w","utf-8") as f:
   n = len(shfile)
   # f.write('echo "copying %s files from vol%s"\n' %(n,vol))
   #f.write('cd ../\n')
   for sh in shfile:
    f.write(sh+'\n')
 print(len(shfile),"lines written to",fileout)


if __name__ == "__main__":
 dirin = sys.argv[1]
 assert dirin in ['extracts']
 dirout = sys.argv[2]
 fileout = sys.argv[3]
 #voldata = voldatad[dirin]
 shfile = makesh(dirin,dirout)
 write_script(fileout,shfile)
  

