from    matplotlib.pyplot  import *
import lhsmdu
import numpy
import pylab as pl

############### LATIN HYPERCUBE SAMPLING (UNIFORM DISTRIB W.O. CORRELATION)
nvaria = 3
ntirages = 600
dx = 1 / ntirages
l = lhsmdu.sample(nvaria,ntirages)

############### OPEN OUTPUT FILE - WRITE NORMALIZED SAMPLING
outpfile = 'Norm_LHsampling144.txt' 
wrfile = open(outpfile,'w')
# for ivar in range (nvaria):
    # txt0 = 'Var' + str(ivar+1)
    # wrfile.write(txt0)
    # if ivar == nvaria-1 : 
        # wrfile.write('\n')
        # break
    # wrfile.write('    ')
for itir in range (ntirages):
    for ivar in range (nvaria):
        txt1 = l[ivar,itir]
        wrfile.write(str(round(txt1,3)))
        if ivar == nvaria-1 : 
            wrfile.write('\n')
            break
        wrfile.write('   ')
wrfile.close()