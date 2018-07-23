from DIRAC.Core.Base import Script
Script.parseCommandLine()

from ILCDIRAC.Interfaces.API.DiracILC import DiracILC
from ILCDIRAC.Interfaces.API.NewInterface.UserJob import UserJob
from ILCDIRAC.Interfaces.API.NewInterface.Applications import Marlin, OverlayInput, DDSim, SLCIOConcatenate
from ILCDIRAC.Interfaces.API.NewInterface.LCUtilityApplication import LCUtilityApplication
import sys, time 
from get_nevts_inIx import *
from time import gmtime, strftime

energy = 250
ILDConfigVer  = "v02-00-01"
ILCSoftVer    = "ILCSoft-02-00-01_gcc49"
detectorModel = "ILD_l5_o2_v02"
detModelSim   = "ILD_l5_v02"

inChannel=str($idChannel)
ireq="I" + inChannel
iFile=$ixnfile
mrgx1=$mrg1
mrgx2=$mrg2
mergeList=$mrglist
evtsPerMrg=$evtspmrg

#print mergeList[0]
#print mergeList

if mrgx1 < 10:
   mrgix1 = "00" + str(mrgx1)
elif (mrgx1>9 and mrgx1 < 100)  :
   mrgix1 = "0" + str(mrgx1)
else  :
   mrgix1 = str(mrgx1)

if mrgx2 < 10:
   mrgix2 = "00" + str(mrgx2)
elif (mrgx2>9 and mrgx2 < 100)  :
   mrgix2 = "0" + str(mrgx2)
else  :
   mrgix2 = str(mrgx2)

mrg_range=mrgix1 + "-" + mrgix2

if iFile < 10:
   ix = ".00" + str(iFile)
elif (iFile>9 and iFile < 100)  :
   ix = ".0" +str(iFile)
else  :
   ix = "." + str(iFile)

idin = ireq + ix 
print "runDSTmerge:", idin, ireq, ix, mrg_range, evtsPerMrg
if   ireq == "I106485" :
   infile = "E" + str(energy) + "-TDR_ws.Pqqh.Gwhizard-1_95.eL.pR." + idin
   chann ="higgs"
elif   ireq == "I106486" :
   infile = "E" + str(energy) + "-TDR_ws.Pqqh.Gwhizard-1_95.eR.pL." + idin
   chann ="higgs"
elif ireq == "I106551" :
   infile = "E" + str(energy) + "-TDR_ws.P4f_ww_h.Gwhizard-1_95.eL.pR." + idin
   chann ="WW_h"
elif ireq == "I106552" :
   infile = "E" + str(energy) + "-TDR_ws.P4f_ww_h.Gwhizard-1_95.eR.pL." + idin
   chann ="WW_h"
elif ireq == "I106559" :
   infile = "E" + str(energy) + "-TDR_ws.P4f_sze_sl.Gwhizard-1_95.eL.pL." + idin
   chann ="sZe_sl"
elif ireq == "I106560" :
   infile = "E" + str(energy) + "-TDR_ws.P4f_sze_sl.Gwhizard-1_95.eL.pR." + idin
   chann ="sZe_sl"
elif ireq == "I106561" :
   infile = "E" + str(energy) + "-TDR_ws.P4f_sze_sl.Gwhizard-1_95.eR.pR." + idin
   chann ="sZe_sl"
elif ireq == "I106562" :
   infile = "E" + str(energy) + "-TDR_ws.P4f_sze_sl.Gwhizard-1_95.eR.pL." + idin
   chann ="sZe_sl"
elif ireq == "I106563" :
   infile = "E" + str(energy) + "-TDR_ws.P4f_sw_sl.Gwhizard-1_95.eL.pL." + idin
   chann ="sW_sl"
elif ireq == "I106564" :
   infile = "E" + str(energy) + "-TDR_ws.P4f_sw_sl.Gwhizard-1_95.eL.pR." + idin
   chann ="sW_sl"
elif ireq == "I106565" :
   infile = "E" + str(energy) + "-TDR_ws.P4f_sw_sl.Gwhizard-1_95.eR.pR." + idin
   chann ="sW_sl"
elif ireq == "I106566" :
   infile = "E" + str(energy) + "-TDR_ws.P4f_sw_sl.Gwhizard-1_95.eR.pL." + idin
   chann ="sW_sl"
elif ireq == "I106571" :
   infile = "E" + str(energy) + "-TDR_ws.P4f_sznu_sl.Gwhizard-1_95.eL.pR." + idin
   chann ="sZnu_sl"
elif ireq == "I106572" :
   infile = "E" + str(energy) + "-TDR_ws.P4f_sznu_sl.Gwhizard-1_95.eR.pL." + idin
   chann ="sZnu_sl"
elif ireq == "I106573" :
   infile = "E" + str(energy) + "-TDR_ws.P4f_zz_h.Gwhizard-1_95.eL.pR." + idin
   chann ="ZZ_h"
elif ireq == "I106574" :
   infile = "E" + str(energy) + "-TDR_ws.P4f_zz_h.Gwhizard-1_95.eR.pL." + idin
   chann ="ZZ_h"
elif ireq == "I106575" :
   infile = "E" + str(energy) + "-TDR_ws.P4f_zz_sl.Gwhizard-1_95.eL.pR." + idin
   chann ="ZZ_sl"
elif ireq == "I106576" :
   infile = "E" + str(energy) + "-TDR_ws.P4f_zz_sl.Gwhizard-1_95.eR.pL." + idin
   chann ="ZZ_sl"
elif ireq == "I106577" :
   infile = "E" + str(energy) + "-TDR_ws.P4f_ww_sl.Gwhizard-1_95.eL.pR." + idin
   chann ="WW_sl"
elif ireq == "I106578" :
   infile = "E" + str(energy) + "-TDR_ws.P4f_ww_sl.Gwhizard-1_95.eR.pL." + idin
   chann ="WW_sl"
elif ireq == "I106607" :
   infile = "E" + str(energy) + "-TDR_ws.P2f_z_h.Gwhizard-1_95.eL.pR." + idin
   chann ="Z_h"
elif ireq == "I106608" :
   infile = "E" + str(energy) + "-TDR_ws.P2f_z_h.Gwhizard-1_95.eR.pL." + idin
   chann ="Z_h"
else:
     print "Wrong Channel Id !!!!" , inChannel

jobGrName="group_" + chann

mrgOutfile = "m" + ILDConfigVer + ".m" + detectorModel + ".LQGSP_BERT." + infile
lcoutputMRG  = mrgOutfile + "_%s.DST.slcio"%(mrg_range)
print "runDSTmerge:  lcoutputMRG= ", lcoutputMRG

jobGroup = idin + "_" + detModelSim
dirac = DiracILC(True,jobGroup+".rep")

MRGoutput = []
# outputs to be saved onto grid SE
outpath="MyProd_" + ILDConfigVer + "/E250-TDR_ws/" + chann + "/" +ireq+ "/mrg"

jobname="m" + idin + "_" + str(mrgix1)
print jobname

job = UserJob()
job.setName(jobname)
job.setJobGroup(jobGrName)
job.setILDConfig(ILDConfigVer)
job.setCPUTime(6400)
job.setInputSandbox(["runDSTmerge_Tmp.py"])
job.setOutputSandbox( ["*.log","*.sh","*.py"] )
job.setInputData(mergeList)
#job.setInputData(mergeList[0])
#job.setOutputData( lcoutputMRG, outpath, "CERN-SRM" )
job.setOutputData( lcoutputMRG, outpath, "IN2P3-SRM" )
job.dontPromptMe()

slcioconcat = SLCIOConcatenate()
slcioconcat.setInputFile(mergeList)
#slcioconcat.setInputFile(mergeList[0])
slcioconcat.setNumberOfEvents(evtsPerMrg)
slcioconcat.setOutputFile( lcoutputMRG, outpath)
slcioconcat.setLogFile("merge.log")

mergejob = job.append(slcioconcat)
if not mergejob['OK']:
       print mergejob['Not ok appending slcioconcat to job']
       quit()

print job.submit(dirac)
