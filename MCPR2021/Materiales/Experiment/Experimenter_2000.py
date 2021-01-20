#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands

algsDir = "/home/vladimir/VLADIMIR/VSI/Upload/Software/"
algs = ["MinReduct.jar","MinReduct.jar -max"]
algs_labels = ["noInfo","info"]
#algs = ["sRGA.jar","MILT.jar -alg PFRC"]
exp_fname = "exp_30x2000_MinReduct_info_vs_noInfo.csv"
units_folder = "/home/vladimir/VLADIMIR/VSI/Upload/Data/BM2000x30/"
table_fname  = "BM2000x30_out_join.csv"

# Create output folder
commands.getoutput("mkdir " + units_folder[0:-1] + '_out/')

# Load units
f = file(table_fname,'r')
f.readline() # Skipping the header
lineas = f.readlines()
f.close()
unidades=[]
lengths=[]

for linea in lineas:
   values = linea.split(',')
   unidades.append(values[0])
   lengths.append(values[8])
   #print (values[0], values[8])


# Load experiment order
expf = file(exp_fname,'r')
expf.readline() # Skipping the header
exp_list = expf.readlines()
expf.close()

for exp in exp_list:#[1055:]:
    data = exp.split(',')
    
    unidad = unidades[int(data[0])]
    reductSize = lengths[int(data[0])]
    alg_num = int(data[1])
    alg = algs[alg_num]
    if (alg_num == 1):
       alg += " %s" % reductSize
    repeat = int(data[2])
    comando = "java -jar " + algsDir +alg + " " + units_folder + unidad
    
    of_name = units_folder[0:-1] + '_out/'+ unidad.split('.')[0]+'_'+algs_labels[alg_num]+'_'+str(repeat)+'.txt'
    #print comando
    ofile = file(of_name,'w')    
    ofile.write(commands.getoutput(comando))
    ofile.close()
      
