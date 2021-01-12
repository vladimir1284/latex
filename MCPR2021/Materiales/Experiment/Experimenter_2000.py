#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands

algsDir = "/home/vladimir/VLADIMIR/VSI/Upload/Software/"
#algs = ["MinReduct.jar","MILT.jar -alg NC"]
algs = ["sRGA.jar","MILT.jar -alg PFRC"]
exp_fname = "exp_30x2000_MILTnc_vs_MinReduct.csv"
units_folder = "/home/vladimir/VLADIMIR/VSI/Upload/Data/BM2000x30/"
table_fname  = "/home/vladimir/VLADIMIR/VSI/Review3/Experiment/Sinteticas/BM2000x30.csv"

# Create output folder
commands.getoutput("mkdir " + units_folder[0:-1] + '_out/')

# Load units
f = file(table_fname,'r')
f.readline() # Skipping the header
lineas = f.readlines()
f.close()
unidades=[]

for linea in lineas:
   unidades.append(linea.split(',')[0])

# Load experiment order
expf = file(exp_fname,'r')
expf.readline() # Skipping the header
exp_list = expf.readlines()
expf.close()

for exp in exp_list:#[1055:]:
    data = exp.split(',')
    
    unidad = unidades[int(data[0])]
    alg = algs[int(data[1])]
    repeat = int(data[2])
    comando = "java -jar " + algsDir +alg + " " + units_folder + unidad
    
    of_name = units_folder[0:-1] + '_out/'+ unidad.split('.')[0]+'_'+alg.split('.')[0]+'_'+str(repeat)+'.txt'
    #print comando
    ofile = file(of_name,'w')    
    ofile.write(commands.getoutput(comando))
    ofile.close()
      
