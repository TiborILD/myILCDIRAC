# Config a script to do sim with automatic splitting of input for any iChannel

from DIRAC.Core.Base import Script
Script.parseCommandLine()
from ILCDIRAC.Interfaces.API.NewInterface.UserJob import UserJob
from ILCDIRAC.Interfaces.API.NewInterface.Applications import DDSim, SLCIOSplit
from ILCDIRAC.Interfaces.API.DiracILC import DiracILC
import os, random
import get_nevts_inIx 

ILDConfigVer  = "v02-00-01"
ILCSoftVer    = "ILCSoft-02-00-01_gcc49"
detectorModel = "ILD_l5_o2_v02"

energy = 250

ireq="I" + str($idChannel)
iFile=$ixnfile
evtsPrun=$evtsPerRun
nJobs=$xJobs
#nJobs=4
evtStart=$startevt
ixjob=$xjob

print "ireq= ", ireq, " evtsPrun= ", evtsPrun, "1st event= ", evtStart, "ijob= ", ixjob, "nJobs= ", nJobs

if iFile < 10:
   ix = ".00" + str(iFile)
elif (iFile>9 and iFile < 100)  :
   ix = ".0" +str(iFile)
else  : 
   ix = "." + str(iFile)

lcinputpath  = "LFN:/ilc/prod/ilc/mc-dbd/generated/250-TDR_ws/4f/" 
idin = ireq + ix
if   ireq == "I106485" :
   infile = "E" + str(energy) + "-TDR_ws.Pqqh.Gwhizard-1_95.eL.pR." + idin
   lcinputpath  = "LFN:/ilc/prod/ilc/mc-dbd/generated/250-TDR_ws/higgs/" 
   chann ="higgs"
elif   ireq == "I106486" :
   infile = "E" + str(energy) + "-TDR_ws.Pqqh.Gwhizard-1_95.eR.pL." + idin
   lcinputpath  = "LFN:/ilc/prod/ilc/mc-dbd/generated/250-TDR_ws/higgs/" 
   chann ="higgs"
elif   ireq == "I106563" :
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
elif ireq == "I106551" :
   infile = "E" + str(energy) + "-TDR_ws.P4f_ww_h.Gwhizard-1_95.eL.pR." + idin
   chann ="WW_h"
elif ireq == "I106552" :
   infile = "E" + str(energy) + "-TDR_ws.P4f_ww_h.Gwhizard-1_95.eR.pL." + idin
   chann ="WW_h"
elif ireq == "I106607" :
   infile = "E" + str(energy) + "-TDR_ws.P2f_z_h.Gwhizard-1_95.eL.pR." + idin
   lcinputpath="LFN:/ilc/prod/ilc/mc-dbd/generated/250-TDR_ws/2f/"
   chann ="Z_h"
elif ireq == "I106608" :
   infile = "E" + str(energy) + "-TDR_ws.P2f_z_h.Gwhizard-1_95.eR.pL." + idin
   lcinputpath="LFN:/ilc/prod/ilc/mc-dbd/generated/250-TDR_ws/2f/"
   chann ="Z_h"

else:
     print "Wrong Channel Id !!!!" , inChannel

jobGrName="group_" + chann
print infile, jobGrName


genfile = infile + ".stdhep"
detModelSim = "ILD_l5_v02"
simOutfile = "s" + ILDConfigVer + ".m" + detModelSim + ".LQGSP_BERT." + infile 
jobGroup = idin + "_" + detModelSim
dirac = DiracILC(True,jobGroup+".rep")


# outputs to be saved onto grid SE
SIMoutput = []  

#RandSeed = random.randrange(11623, 99999)
if ixjob < 10:
   indx = "00" + str(ixjob)
elif (ixjob>9 and ixjob < 100)  :
   indx = "0" +str(ixjob)
else  :
   indx = str(ixjob)

jobname = "s" + idin + "_" + indx
#lcinputSIM  = "LFN:/ilc/prod/ilc/mc-dbd/generated/" + genfile
lcinputSIM  = lcinputpath + genfile
lcoutputSIM  = simOutfile + "_%s.SIM.slcio"%(indx)
print lcinputSIM
print jobname

SIMoutput.append(lcoutputSIM)

job = UserJob()
job.setName(jobname)
job.setJobGroup(jobGrName)
job.setILDConfig(ILDConfigVer)
job.setCPUTime(86400)
job.setOutputSandbox(["*.log","*.sh","*.py "])
#job.setOutputData(lcoutputSIM,OutputPath="MyTest/sim1",OutputSE="IN2P3-SRM")
job.setOutputData( SIMoutput,"MyProd_" + ILDConfigVer + "/E250-TDR_ws/" + chann + "/" +ireq+ "/sim","IN2P3-SRM")
job.setInputSandbox(["runSimSplit_any_Tmp.py"])
#job.setDestinationCE('lyogrid07.in2p3.fr')

job.dontPromptMe()
job.setBannedSites(['LCG.Tau.il'])
#job.setBannedSites(['LCG.IN2P3-CC.fr','LCG.DESYZN.de','LCG.DESY-HH.de','LCG.KEK.jp','OSG.UConn.us','LCG.Cracow.pl','OSG.MIT.us','LCG.Glasgow.uk','OSG.CIT.us','OSG.BNL.us','LCG.Brunel.uk','LCG.RAL-LCG2.uk','LCG.Oxford.uk','OSG.UCSDT2.us'])


sim = DDSim()
sim.setVersion(ILCSoftVer)
sim.setDetectorModel(detModelSim)
sim.setInputFile(lcinputSIM)
sim.setSteeringFile("ddsim_steer.py")
sim.setNumberOfEvents(evtsPrun)
sim.setEnergy(energy)
sim.setOutputFile(lcoutputSIM)
#sim.setRandomSeed(RandSeed)
sim.setStartFrom(evtStart)

simres = job.append(sim)
if not simres['OK']:
   print simres['Not ok appending ddsim to job']
   quit()

print SIMoutput

print job.submit(dirac)

