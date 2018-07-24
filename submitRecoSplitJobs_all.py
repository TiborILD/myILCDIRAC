# python submitRecoSplitJobs_all.py

import sys, os, subprocess
import time 
from string import Template
from time import gmtime, strftime
#from readin_maps import * 
from get_nevts_inIx import *

fR = file("runRecoSplit_all.py","r")
lines = fR.read()
fR.close()

def submitRecoSplitJobs_all(inChannel):
   '''
        print "Which Channel Id !!!!" , inChannel
   '''

   evtsPerRun=200
   nEvtsArray=get_nevts_inIx(inChannel)
   nfiles= len(nEvtsArray)
   strinChannel= str(inChannel)

#Here loop over all available generator files i:
   for iFile in range(1,nfiles,1):
       striFile = str(iFile)
       nJobs    = nEvtsArray[iFile]
#Now loop over all events in input iFile   nJobs=nEvents/200 + 1
       evts=nEvtsArray[iFile]
       nJobs = evts/evtsPerRun
       if (evts%evtsPerRun >9):
           nJobs = nJobs +1
       snJobs = str(nJobs)
       sevts = str(evts)
       for ijob in range(1,nJobs+1,1):
           sijob = str(ijob)
           print iFile , "Total evts= ", evts, "corrected nJobs= ", nJobs, "ijob= ", ijob
           t= Template(lines)
           if os.path.exists("runRecoSplit_all_Tmp.py"):
              os.remove("runRecoSplit_all_Tmp.py")
           fT = file("runRecoSplit_all_Tmp.py","w")
           fT.write(t.substitute(idChannel=strinChannel,iJob=sijob,ixnfile=striFile))
           fT.close()
           f2 = subprocess.call("python runRecoSplit_all_Tmp.py", shell=True)
       print strftime("%Y-%m-%d %H:%M:%S", gmtime())
       print iFile
       if iFile < nfiles - 1 :
          print("Sleeping for 10 min between submissions of 2 input files ...")
          time.sleep(600)   # Delay for 1 minute (60 seconds)
          print strftime("%Y-%m-%d %H:%M:%S", gmtime())


if __name__ == "__main__":
  if len(sys.argv) !=2:
    print "usage: python submitRecoJobs_all.py  inChannel (e.g.:  106608)"
    print sys.argv[1]
    sys.exit(-1)
  print sys.argv[1]
  submitRecoSplitJobs_all(sys.argv[1])


