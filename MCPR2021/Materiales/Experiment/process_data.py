from pylab import *
import csv

density = []
info = []
noInfo = []

with open('BM2000x30_out_info_vs_noInfo.csv', 'rb') as csvfile:
   reader = csv.DictReader(csvfile)
   for row in reader:
      density.append(float(row['Density']))
      #reducts.append(float(row['reducts']))
      #ct.append(float(row['CT_time'])/1000)
      info.append(float(row['info'])/1000)
      noInfo.append(float(row['noInfo'])/1000)

density = array(density)
info = array(info)
noInfo = array(noInfo)


##################################################################################
# Create density beans
nbeans = 16
maxdens = max(density)
mindens = min(density)
delta = (maxdens - mindens)/(nbeans+1)
bins = linspace(mindens+delta, maxdens, nbeans)
digitized = digitize(density, bins)

dens_mean      = []
info_mean      = []
info_std       = []
noInfo_mean    = []
noInfo_std     = []


for i in range(1,len(bins)):
   dens_mean.append(density[digitized==i].mean())
   info_mean.append(info[digitized==i].mean())
   info_std.append(info[digitized==i].std())
   noInfo_mean.append(noInfo[digitized==i].mean())
   noInfo_std.append(noInfo[digitized==i].std())


# Plot overall performance
# Use central value in x instead of mean
x = linspace(0.22,0.78,15)
img = figure(figsize=(5,5))
errorbar(x,noInfo_mean,yerr=noInfo_std,fmt='s-')
errorbar(x,info_mean,yerr=info_std,fmt='^-')
# ~ xlabels = ['%.2f'%i for i in x]
# ~ xticks(x, xlabels, rotation=60)
# ~ ylim(ymin=0)
grid('on')
xlabel('Mean density of 1\'s')
ylabel('Runtime (s)')
title('Runtime vs. density of 1\'s')
legend(('unknown k','known k'), loc=1)
subplots_adjust(bottom=0.15)
#show()
img.savefig('noInfo_vs_info.eps')
