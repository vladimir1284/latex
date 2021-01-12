#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands

units_folder = "/home/vladimir/VLADIMIR/VSI/Upload/Data/BM2000x30_out"
table_fname  = "/home/vladimir/VLADIMIR/VSI/Review3/Experiment/Sinteticas/BM2000x30.csv"

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
   if not(odir.has_key(bm)):
	   odir.setdefault(bm,{})
   if (alg == "MinReduct"):
      size           = int(lineas[6].split(':')[1])
      nsol           = int(lineas[7].split(':')[1])
      candidates     = int(lineas[4].split(':')[1])

      odir[bm].setdefault(alg,{'candidates':candidates,'size':size,'nsol':nsol,'runtime':time_ms})
   else:
      odir[bm].setdefault(alg,{'runtime':time_ms})

# Process the list
for of in ofiles:
   processFile(of)

# Load Table
f = file(table_fname,'r')
lineas = f.readlines()
f.close()

#print odir

algs = ["sRGA","MILT"]
# Save data
f = file(table_fname.split('.')[0]+'_out_2.csv','w')
f.write('Name,Density,MinCol,MaxCol,StdCol,MinRow,MaxRow,StdRow,sRGA,MILT_PFRC\n')
for linea in lineas[1:]:
   bm = linea.split(',')[0].split('.')[0]
   record = odir[bm]
   str_add = ''
   f.write(linea[:-1]+',')
   # Add new data
   for alg in algs:
	  if record.has_key(alg):
		  data = record[alg]
		  # ~ data['runtimes'].sort()
		  # ~ ltime = data['runtimes'][0]
		  # ~ if ltime < min_time:
			 # ~ faster = alg
			 # ~ min_time = ltime
		  if (alg == "MinReduct"):
		     str_add += str(data['size'])+','
		     str_add += str(data['nsol'])+','
		  str_add += str(data['runtime'])+',' # Select the lowest runtime
   # End line
   #str_add += faster
   f.write(str_add+'\n')
f.close()
