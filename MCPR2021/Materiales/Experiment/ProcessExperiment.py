#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands

units_folder = "/home/vladimir/VLADIMIR/VSI/Upload/Data/BM2000x30_out"
table_fname  = "BM2000x30.csv"

ofiles = commands.getoutput('ls '+units_folder).split('\n')

odir = {}

def processFile(fname):
   f = file(units_folder+"/"+fname,'r')
   lineas = f.readlines()
   f.close()
   sptname        = fname.split('_')
   bm             = '_'.join(sptname[0:-2])
   #bm             = bm.split('BM')[1]
   alg            = sptname[-2]

   time_ms        = int(lineas[1].split(':')[1].split('ms')[0])
   print bm, alg
   if odir.has_key(bm):
      if odir[bm].has_key(alg):
	 odir[bm][alg]['runtimes'].append(time_ms)
      else:
	 odir[bm].setdefault(alg,{'runtimes':[time_ms]})
   else:
      odir.setdefault(bm,{'reducts':1})
      odir[bm].setdefault(alg,{'runtimes':[time_ms]})

# Process the list
for of in ofiles:
   processFile(of)

# Load Table
f = file(table_fname,'r')
lineas = f.readlines()
f.close()

#print odir

algs = ["info","noInfo"]
# Save data
f = file(table_fname.split('.')[0]+'_out_info_vs_noInfo.csv','w')
f.write('Name,Density,MinCol,MaxCol,StdCol,MinRow,MaxRow,StdRow,info,noInfo\n')
for linea in lineas[1:]:
   bm = linea.split(',')[0].split('.')[0]
   record = odir[bm]
   str_add = ''
   f.write(linea[:-1]+',')
   # Add new data
   for alg in algs:
      if record.has_key(alg):
	 data = record[alg]
	 data['runtimes'].sort()
	 ltime = data['runtimes'][0]
	 # ~ if ltime < min_time:
	    # ~ faster = alg
	    # ~ min_time = ltime
	 str_add += str(ltime)+',' # Select the lowest runtime
   # End line
   #str_add += faster
   f.write(str_add+'\n')
f.close()
