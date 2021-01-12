from pylab import *
import csv

density = []
minreduct = []
milt_nc = []
milt_pfrc = []
min1s = []
max1s = []

with open('BM2000x30_out_join.csv', 'rb') as csvfile:
   reader = csv.DictReader(csvfile)
   for row in reader:
      density.append(float(row['Density']))
      #reducts.append(float(row['reducts']))
      #ct.append(float(row['CT_time'])/1000)
      minreduct.append(float(row['MinReduct'])/1000)
      milt_nc.append(float(row['MILT_NC'])/1000)
      milt_pfrc.append(float(row['MILT_PFRC'])/1000)

density = array(density)
minreduct = array(minreduct)
milt_nc = array(milt_nc)
milt_pfrc = array(milt_pfrc)


##################################################################################
# Create density beans
nbeans = 16
maxdens = max(density)
mindens = min(density)
delta = (maxdens - mindens)/(nbeans+1)
bins = linspace(mindens+delta, maxdens, nbeans)
digitized = digitize(density, bins)

dens_mean      = []
minreduct_mean       = []
minreduct_std        = []
milt_nc_mean        = []
milt_nc_std         = []
milt_pfrc_mean        = []
milt_pfrc_std         = []


for i in range(1,len(bins)):
   dens_mean.append(density[digitized==i].mean())
   minreduct_mean.append(minreduct[digitized==i].mean())
   minreduct_std.append(minreduct[digitized==i].std())
   milt_nc_mean.append(milt_nc[digitized==i].mean())
   milt_nc_std.append(milt_nc[digitized==i].std())
   milt_pfrc_mean.append(milt_pfrc[digitized==i].mean())
   milt_pfrc_std.append(milt_pfrc[digitized==i].std())


# Plot overall performance
# Use central value in x instead of mean
x = linspace(0.22,0.78,15)
img = figure(figsize=(6,4))
errorbar(x,milt_nc_mean,yerr=milt_nc_std,fmt='s-')
errorbar(x,milt_pfrc_mean,yerr=milt_pfrc_std,fmt='^-')
errorbar(x,minreduct_mean,yerr=minreduct_std,fmt='o-')
xlabels = ['%.2f'%i for i in x]
xticks(x, xlabels, rotation=60)
ylim(ymin=0)
grid('on')
xlabel('Mean density of 1\'s')
ylabel('Runtime (s)')
title('Runtime vs. density of 1\'s')
legend(('MILT (NC)','MILT (PFRC)','MinReduct'), loc=1)
subplots_adjust(bottom=0.15)
#show()
img.savefig('MinReduct_vs_milt.eps')
