#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

experiment = "exp_30x2000_MILTnc_vs_MinReduct"
repeats = 1
units   = 500
algs    = 2

total = repeats*units*algs
dummy = range(total)
order = np.ones(total)

while(total>0):
    order[total-1] = dummy.pop(np.random.random_integers(0,total-1))
    total -= 1

lista = [] 
for unit in range(units):
    for alg in range(algs):
        for repeat in range(repeats):
            lista.append("%i,%i,%i"%(unit,alg,repeat))

ofile = file(experiment+'.csv','w')
ofile.write("unit,algorithm,repetition\n")
for ind in order:
   ofile.write(lista[int(ind)])
   ofile.write('\n')
    
ofile.close()
