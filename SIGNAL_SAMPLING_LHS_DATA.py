################################################################################################
# SIGNAL SAMPLING OF MULTIPLE EVENTS FROM MULTIPLE GEOLOGICAL BASINS WITH MULTIPLE INTENSITIES #
############  USING LATIN HYPERCUBE SAMPLING ADAPTED TO THE PROBLEMATIC ENCOUNTERED ############
################################################################################################
from math import *
# Liste des graphs à tracer :
# 3D scatter graph de toute la DATABASE PGA,PGV,fc
# 3D scatter graph de toute la DATABASE PGA,PGV,fc avec une distinction de la représentation par bassin
# 2D scatter graph avec colorbar de toute la DATABASE PGA, PGV, fc
# 2D scatter graph avec colorbar de toute la DATABASE PGA, PGV, fc avec une distinction de la représentation par bassin

# LHS sampling PGA PGV FC
# => 5 tirages à 3 variables
# 3D scatter graph du tirage PGA,PGV,fc
# 3D scatter graph du tirage PGA,PGV,fc avec une distinction de la représentation par bassin
# 2D scatter graph avec colorbar du tirage PGA, PGV, fc
# 2D scatter graph avec colorbar du tirage PGA, PGV, fc avec une distinction de la représentation par bassin

# LHS sampling BASIN EVENT PGA PGV FC
# => 5 tirages à 5 variables
# 3D scatter graph du tirage PGA,PGV,fc
# 3D scatter graph du tirage PGA,PGV,fc avec une distinction de la représentation par bassin
# 2D scatter graph avec colorbar du tirage PGA, PGV, fc
# 2D scatter graph avec colorbar du tirage PGA, PGV, fc avec une distinction de la représentation par bassin


def read_signal_data(inpfile):
    DATA = []
    INDEX = []
    BASIN = []
    EVENT = []
    PGA_TOT_H = []
    PGV_TOT_H = []
    FC_TOT_H = []
    source = open(inpfile,'r')
    A = source.readlines()
    # for i in range(0,len(A)):
    for i in range(1,len(A)):
        INDEX.append(float(i))
        BASIN.append(A[i].split()[6])
        # BASIN.append(float(1))
        EVENT.append(A[i].split()[1])
        # EVENT.append(float(2))
        PGA_TOT_H.append(float(A[i].split()[15]))
        PGV_TOT_H.append(float(A[i].split()[17]))
        FC_TOT_H.append(float(A[i].split()[3]))
    DATA = [INDEX,BASIN,EVENT,PGA_TOT_H,PGV_TOT_H,FC_TOT_H]
    return DATA
    
def write_total_signals(DATA,outpfile):
    wrfile = open(outpfile,'w')
    for i in range (0,len(DATA[0])):
        txt0 = DATA[0][i]
        txt1 = DATA[1][i]
        txt2 = DATA[2][i]
        txt3 = DATA[3][i]
        txt4 = DATA[4][i]
        txt5 = DATA[5][i]
        wrfile.write(str(txt0))
        wrfile.write('    ')
        wrfile.write(str(txt1))
        wrfile.write('    ')
        wrfile.write(str(txt2))
        wrfile.write('    ')
        wrfile.write(str(txt3))
        wrfile.write('    ')
        wrfile.write(str(txt4))
        wrfile.write('    ')
        wrfile.write(str(txt5))
        wrfile.write('\n')
    wrfile.close()
    
def read_LHS_sampling(inpfile):
    VARS = []
    VAR1 = []
    VAR2 = []
    VAR3 = []
    VAR4 = []
    VAR5 = []
    source = open(inpfile,'r')
    A = source.readlines()
    for i in range(0,len(A)):
        VAR1.append(A[i].split()[0])
        VAR2.append(A[i].split()[1])
        VAR3.append(A[i].split()[2])
        VAR4.append(A[i].split()[3])
        VAR5.append(A[i].split()[4])
    VARS = [VAR1,VAR2,VAR3,VAR4,VAR5]
    return VARS

def signals_sampling_unif_PGAPGVFC(DATA,VARS,outpfile):
    OUT_OUT = []
    OUT_INDEX = []
    OUT_BASIN = []
    OUT_EVENT = []
    OUT_PGA = []
    OUT_PGV = []
    OUT_FC = []
    # Define the basin on the basis of the first variable
    wrfile = open(outpfile,'w')
    for i in range (0,len(VARS[0])):
        LHS_basin = VARS[0][i]
        LHS_event = VARS[1][i]
        LHS_PGA = VARS[2][i]
        LHS_PGV = VARS[3][i]
        LHS_FC = VARS[4][i]
        
        reduced_list_1 = DATA[0]
        reduced_list_2 = DATA[1]
        reduced_list_3 = DATA[2]
        reduced_list_4 = DATA[3]
        reduced_list_5 = DATA[4]
        reduced_list_6 = DATA[5]
        
        # Find the extreme intensities of the reduced lists
        pga_max = max(reduced_list_4)
        pgv_max = max(reduced_list_5)
        fc_max = max(reduced_list_6)
        pga_min = min(reduced_list_4)
        pgv_min = min(reduced_list_5)
        fc_min = min(reduced_list_6)

        
        # "De-normalization" of intensities sampling
        LHS_PGA_denorm = float(LHS_PGA)*(float(pga_max)-float(pga_min))+float(pga_min)
        LHS_PGV_denorm = float(LHS_PGV)*(float(pgv_max)-float(pgv_min))+float(pgv_min)
        LHS_FC_denorm = float(LHS_FC)*(float(fc_max)-float(fc_min))+float(fc_min)
        wrfile.write(str(LHS_PGA_denorm))
        wrfile.write('    ')
        wrfile.write(str(LHS_PGV_denorm))
        wrfile.write('    ')
        wrfile.write(str(LHS_FC_denorm))
        wrfile.write('\n')
        # Find the signal with the intensity the closest of the sample
        reduced_list_7 = []
        for n in range(0,len(reduced_list_1)):
            delta_x = LHS_PGA_denorm - float(reduced_list_4[n])
            delta_y = LHS_PGV_denorm - float(reduced_list_5[n])
            delta_z = LHS_FC_denorm - float(reduced_list_6[n])
            norm_delta = ((delta_x)**2+(delta_y)**2+(delta_z)**2)**(0.5)
            reduced_list_7.append(norm_delta)
        norm_delta_min = min(reduced_list_7)
        ind_min = reduced_list_7.index(norm_delta_min)
        
        # Fill the output list with the selected signals
        OUT_INDEX.append(reduced_list_1[ind_min])
        OUT_BASIN.append(reduced_list_2[ind_min])
        OUT_EVENT.append(reduced_list_3[ind_min])
        OUT_PGA.append(reduced_list_4[ind_min])
        OUT_PGV.append(reduced_list_5[ind_min])
        OUT_FC.append(reduced_list_6[ind_min])
    wrfile.close()
    print(pga_max)
    print(pgv_max)
    print(fc_max)
    print(pga_min)
    print(pgv_min)
    print(fc_min)
    OUT_OUT = [OUT_INDEX,OUT_BASIN,OUT_EVENT,OUT_PGA,OUT_PGV,OUT_FC]
    return OUT_OUT

def write_selected_signals(OUT_OUT,outpfile):
    wrfile = open(outpfile,'w')
    for i in range (0,len(OUT_OUT[0])):
        txt0 = OUT_OUT[0][i]
        txt1 = OUT_OUT[1][i]
        txt2 = OUT_OUT[2][i]
        txt3 = OUT_OUT[3][i]
        txt4 = OUT_OUT[4][i]
        txt5 = OUT_OUT[5][i]
        wrfile.write(str(txt0))
        wrfile.write('    ')
        wrfile.write(str(txt1))
        wrfile.write('    ')
        wrfile.write(str(txt2))
        wrfile.write('    ')
        wrfile.write(str(txt3))
        wrfile.write('    ')
        wrfile.write(str(txt4))
        wrfile.write('    ')
        wrfile.write(str(txt5))
        wrfile.write('\n')
    wrfile.close()



# File name
# inp_file_signal = "Signal_DATA.txt"
inp_file_signal = "DATAset.txt"
inp_file_LHS = "Norm_LHsampling600.txt"
out_file_signal = "TOTAL_SIGNAL_DATA_CF.txt"
out_file_sampl = "Signal_Sampling_CF600.txt"
out_file_plot = "Signal_Sampling_CF600.png"
temp_out = "TEMP_OUT_DENORMALIZED300.txt"

# Function execution
DATA = read_signal_data(inp_file_signal)
write_total_signals(DATA,out_file_signal)
VARS = read_LHS_sampling(inp_file_LHS)
OUT_OUT = signals_sampling_unif_PGAPGVFC(DATA,VARS,temp_out)
write_selected_signals(OUT_OUT,out_file_sampl)


