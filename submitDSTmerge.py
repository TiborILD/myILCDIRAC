from DIRAC.Core.Base import Script
Script.parseCommandLine()
from ILCDIRAC.Interfaces.API.NewInterface.UserJob import UserJob
from ILCDIRAC.Interfaces.API.NewInterface.Applications import Marlin, OverlayInput, DDSim, SLCIOConcatenate
from ILCDIRAC.Interfaces.API.NewInterface.LCUtilityApplication import LCUtilityApplication
from ILCDIRAC.Interfaces.API.DiracILC import DiracILC
import os, sys, time 
import subprocess, commands
from get_nevts_inIx import *
from time import gmtime, strftime

fR = file("runDSTmerge.py","r")
lines = fR.read()
fR.close()


def submitDSTmerge(inChannel):

   inFilesList=[]
   ireq="I" + str(inChannel)
   nEvtsArray=get_nevts_inIx(inChannel)
   nfiles= len(nEvtsArray)
   strinChannel= str(inChannel)
   evtsPerRun=200
   nfmerge = 100 
   evtsPmerge = evtsPerRun*nfmerge

   text="No such file or directory"
#   text="Unknown"

   print "submitDSTmerge: nfiles ",nfiles, "inChannel=", inChannel
   if inChannel == '106485':
       lfnlist = file("ilc-user-k-kurca-MyProd_v02-00-01-E250-TDR_ws-higgs-I106485-rec-DST.lfns","r")
   elif inChannel == '106486':
       lfnlist = file("ilc-user-k-kurca-MyProd_v02-00-01-E250-TDR_ws-higgs-I106486-rec-DST.lfns","r")
   elif inChannel == '106551':
       lfnlist = file("ilc-user-k-kurca-MyProd_v02-00-01-E250-TDR_ws-WW_h-I106551-rec-DST.lfns","r")
   elif inChannel == '106552':
       lfnlist = file("ilc-user-k-kurca-MyProd_v02-00-01-E250-TDR_ws-WW_h-I106552-rec-DST.lfns","r")
   elif inChannel == '106559':
       lfnlist = file("ilc-user-k-kurca-MyProd_v02-00-01-E250-TDR_ws-sZe_sl-I106559-rec-DST.lfns","r")
   elif inChannel == '106560':
       lfnlist = file("ilc-user-k-kurca-MyProd_v02-00-01-E250-TDR_ws-sZe_sl-I106560-rec-DST.lfns","r")
   elif inChannel == '106561':
       lfnlist = file("ilc-user-k-kurca-MyProd_v02-00-01-E250-TDR_ws-sZe_sl-I106561-rec-DST.lfns","r")
   elif inChannel == '106562':
       lfnlist = file("ilc-user-k-kurca-MyProd_v02-00-01-E250-TDR_ws-sZe_sl-I106562-rec-DST.lfns","r")
   elif inChannel == '106563':
       lfnlist = file("ilc-user-k-kurca-MyProd_v02-00-01-E250-TDR_ws-sW_sl-I106563-rec-DST.lfns","r")
   elif inChannel == '106564':
       lfnlist = file("ilc-user-k-kurca-MyProd_v02-00-01-E250-TDR_ws-sW_sl-I106564-rec-DST.lfns","r")
   elif inChannel == '106565':
       lfnlist = file("ilc-user-k-kurca-MyProd_v02-00-01-E250-TDR_ws-sW_sl-I106565-rec-DST.lfns","r")
   elif inChannel == '106566':
       lfnlist = file("ilc-user-k-kurca-MyProd_v02-00-01-E250-TDR_ws-sW_sl-I106566-rec-DST.lfns","r")
   elif inChannel == '106571':
       lfnlist = file("ilc-user-k-kurca-MyProd_v02-00-01-E250-TDR_ws-sZnu_sl-I106571-rec-DST.lfns","r")
   elif inChannel == '106572':
       lfnlist = file("ilc-user-k-kurca-MyProd_v02-00-01-E250-TDR_ws-sZnu_sl-I106572-rec-DST.lfns","r")
   elif inChannel == '106573':
       lfnlist = file("ilc-user-k-kurca-MyProd_v02-00-01-E250-TDR_ws-ZZ_h-I106573-rec-DST.lfns","r")
   elif inChannel == '106574':
       lfnlist = file("ilc-user-k-kurca-MyProd_v02-00-01-E250-TDR_ws-ZZ_h-I106574-rec-DST.lfns","r")
   elif inChannel == '106575':
       lfnlist = file("ilc-user-k-kurca-MyProd_v02-00-01-E250-TDR_ws-ZZ_sl-I106575-rec-DST.lfns","r")
   elif inChannel == '106576':
       lfnlist = file("ilc-user-k-kurca-MyProd_v02-00-01-E250-TDR_ws-ZZ_sl-I106576-rec-DST.lfns","r")
   elif inChannel == '106577':
       lfnlist = file("ilc-user-k-kurca-MyProd_v02-00-01-E250-TDR_ws-WW_sl-I106577-rec-DST.lfns","r")
   elif inChannel == '106578':
       lfnlist = file("ilc-user-k-kurca-MyProd_v02-00-01-E250-TDR_ws-WW_sl-I106578-rec-DST.lfns","r")
   elif inChannel == '106607':
       lfnlist = file("ilc-user-k-kurca-MyProd_v02-00-01-E250-TDR_ws-Z_h-I106607-rec-DST.lfns","r")
   elif inChannel == '106608':
       lfnlist = file("ilc-user-k-kurca-MyProd_v02-00-01-E250-TDR_ws-Z_h-I106608-rec-DST.lfns","r")
   else :
        "Wrong Channel !!!! "

#create input list of files to be merged ?!!!  only from existing files! ..... readin a list !!!
   allFilesList = []
   for line in lfnlist:
        allFilesList.append(line)
   lfnlist.close()
#   xfiles = 1 
#   for iFile in range(xfiles,xfiles+1,1):
   for iFile in range(1,nfiles,1):
       if iFile < 10:
          ix = ".00" + str(iFile)
       elif (iFile>9 and iFile < 100)  :
          ix = ".0" +str(iFile)
       else  :
          ix = "." + str(iFile)
    
       print str(ix) 
       idin = "I"+ str(inChannel) +  ix

       inFilesList = "inFilesList" + ix
       inFilesList = []
       for exprs in allFilesList:
            if idin in exprs:
               l1=exprs.strip()
               inFilesList.append(l1)
#               print exprs 
#               print l1
       ndstfiles = len(inFilesList) 
       print ndstfiles 
       for i in range (0,ndstfiles,nfmerge):
          m1=str(i+1)
          m2=str(i+nfmerge)
          print "Loopi:",i,ndstfiles 
          if (ndstfiles - i) < nfmerge :
            m2=str(ndstfiles)
            print(i,m2,ndstfiles )
          mrgrange = m1 + "-" + m2 
          xmergeList = "mergeList_" +idin + "_" + mrgrange 
          xmergeList = []
          xmergeList.append(inFilesList[i:i+nfmerge])
          print i, mrgrange
          xnfmerge = 0 
          mergeList = []
          # check the existence of file before adding to the final list of files to be merged
          for ifile in xmergeList[0]:
              status,output = commands.getstatusoutput("dirac-dms-lfn-replicas %s" %ifile)
#              print status, output
              if not text in output:
                 mergeList.append(ifile)
                 xnfmerge = xnfmerge +1
          evtsPmerge = evtsPerRun*xnfmerge
          print "mergeList:", i, mrgrange, xnfmerge, mergeList
          t= Template(lines)
          if os.path.exists("runDSTmerge_Tmp.py"):
             os.remove("runDSTmerge_Tmp.py")
          fT = file("runDSTmerge_Tmp.py","w")
          fT.write(t.substitute(idChannel=strinChannel,mrg1=m1,mrg2=m2,mrglist=str(mergeList),ixnfile=str(iFile),evtspmrg=str(evtsPmerge)))
          fT.close()
          fT1 = file("runDSTmerge_"+idin + "_" + m1 + ".py","w")
          fT1.write(t.substitute(idChannel=strinChannel,mrg1=m1,mrg2=m2,mrglist=str(mergeList),ixnfile=str(iFile),evtspmrg=str(evtsPmerge)))
          fT1.close()
          f2 = subprocess.call("python runDSTmerge_Tmp.py", shell=True)

if __name__ == "__main__":
  if len(sys.argv) !=2:
    print "usage: python submitDSTmerge (e.g.:  106653)"
    print sys.argv[1]
    sys.exit(-1)
  submitDSTmerge(sys.argv[1])

