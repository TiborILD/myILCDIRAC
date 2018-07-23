# script to do reco for ANY ifile, ijob for defined Id channels

from DIRAC.Core.Base import Script
Script.parseCommandLine()
from ILCDIRAC.Interfaces.API.NewInterface.UserJob import UserJob
from ILCDIRAC.Interfaces.API.NewInterface.Applications import DDSim, Marlin
from ILCDIRAC.Interfaces.API.DiracILC import DiracILC
import os, random
import get_nevts_inIx

ILDConfigVer  = "v02-00-01"
ILCSoftVer    = "ILCSoft-02-00-01_gcc49"
detectorModel = "ILD_l5_o2_v02"

energy = 250
evtsPerRun = 201 # Marlin (201) - ddsim(200)  different loops ???

ireq="I" + str($idChannel)
iFile=$ixnfile
ixjob=$iJob

if iFile < 10:
   ix = ".00" + str(iFile)
elif (iFile>9 and iFile < 100) :
   ix = ".0" + str(iFile)
else  : 
   ix = "." + str(iFile)

idin = ireq + ix

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

genfile = infile + ".stdhep"
print genfile, jobGrName

detModelSim = "ILD_l5_v02"
simOutfile = "s" + ILDConfigVer + ".m" + detModelSim + ".LQGSP_BERT." + infile 
recOutfile = "r" + ILDConfigVer + ".m" + detectorModel + ".LQGSP_BERT." + infile

jobGroup = idin + "_" + detModelSim
dirac = DiracILC(True,jobGroup+".rep")

if ixjob < 10:
   indx = "00" + str(ixjob)
elif (ixjob>9 and ixjob < 100)  :
   indx = "0" +str(ixjob)
else  :
   indx = str(ixjob)


RECoutput = []  
# outputs to be saved onto grid SE

jobname = "r" + idin + "_" + str(indx)
print jobname

lcoutputSIM  = simOutfile + "_%s.SIM.slcio"%(indx) 
lcinputREC = "/ilc/user/k/kurca/MyProd_" + ILDConfigVer + "/E250-TDR_ws/" + chann + "/" + ireq +"/sim/" + lcoutputSIM
print lcinputREC

# Marlin
lcoutputDST  = recOutfile + "_%s.DST.slcio"%(indx) 
lcoutputREC  = recOutfile + "_%s.REC.slcio"%(indx) 

ma = Marlin()
ma.setVersion(ILCSoftVer)
ma.setDetectorModel(detectorModel)
ma.setEnergy(energy)
ma.setSteeringFile("MarlinStdReco.xml")
ma.setExtraCLIArguments(" --constant.DetectorModel=%s "%(detectorModel) )
ma.setLogFile("marlin.log")
ma.setInputFile([lcoutputSIM])
ma.setNumberOfEvents(evtsPerRun)
ma.setOutputDstFile(lcoutputDST)
ma.setOutputRecFile(lcoutputREC)

RECoutput.append(lcoutputDST)
RECoutput.append(lcoutputREC)

job = UserJob()
job.setName(jobname)
job.setJobGroup(jobGrName)
job.setILDConfig(ILDConfigVer)
job.setCPUTime(86400)
job.setInputData([lcinputREC])
job.setInputSandbox(["runRecoSplit_any_Tmp.py"])
job.setOutputSandbox(["*.log","*.sh","MarlinStdRecoParsed.xml","marlin*.xml","*.py "])
#job.setOutputSandbox(["*.log","*.sh","MarlinStdRecoParsed.xml","marlin*.xml","*.py ","*.root"])
#job.setDestinationCE('lyogrid07.in2p3.fr')

job.dontPromptMe()
job.setBannedSites(['LCG.QMUL.uk'])
#job.setBannedSites(['LCG.IN2P3-CC.fr','LCG.DESYZN.de','LCG.DESY-HH.de','LCG.KEK.jp','OSG.UConn.us','LCG.Cracow.pl','OSG.MIT.us','LCG.Glasgow.uk','OSG.CIT.us','OSG.BNL.us','LCG.Brunel.uk','LCG.RAL-LCG2.uk','LCG.Oxford.uk','OSG.UCSDT2.us'])

# run Malrin reco jobs
mares = job.append(ma)
if not mares['OK']:
        print mares['Not ok appending Marlin to job']
        quit()

job.setOutputData( RECoutput,"MyProd_" + ILDConfigVer + "/E250-TDR_ws/" + chann + "/" +ireq+ "/rec","IN2P3-SRM")
print RECoutput

print job.submit(dirac)
