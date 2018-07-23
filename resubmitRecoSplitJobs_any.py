# ...........................
# python resubmitRecoSplitJobs_any.py

import sys, os, subprocess
import time 
from string import Template
from time import gmtime, strftime
#from readin_maps import * 
from get_nevts_inIx import *

fR = file("rerunRecoSplit_any.py","r")
lines = fR.read()
fR.close()

def resubmitRecoSplitJobs_any(inChannel, infile, inJob):
   '''
        print "Which Channel Id !!!!" , inChannel
   '''

   evtsPerRun=200
   nEvtsArray=get_nevts_inIx(inChannel)
   nfiles= len(nEvtsArray)
   strinChannel= str(inChannel)

#Here loop over any available generator file infile:
   for iFile in range(int(infile),int(infile)+1,1):
       striFile = str(iFile)
       nJobs    = nEvtsArray[iFile]
#Now loop over all events in input iFile   nJobs=nEvents/200 + 1
       evts=nEvtsArray[iFile]
       nJobs = evts/evtsPerRun
       if (evts%evtsPerRun >9):
           nJobs = nJobs +1
       nJobs = inJob 
       delta = 1
       snJobs = str(nJobs)
       sevts = str(evts)
       for ijob in range(int(nJobs),int(nJobs)+delta,1):
           sijob = str(ijob)
           print iFile , "Total evts= ", evts, "corrected nJobs= ", nJobs, "ijob= ", ijob
           t= Template(lines)
           if os.path.exists("rerunRecoSplit_any_Tmp.py"):
              os.remove("rerunRecoSplit_any_Tmp.py")
           fT = file("rerunRecoSplit_any_Tmp.py","w")
           fT.write(t.substitute(idChannel=strinChannel,iJob=sijob,ixnfile=striFile))
           fT.close()
           f2 = subprocess.call("python rerunRecoSplit_any_Tmp.py", shell=True)
       print strftime("%Y-%m-%d %H:%M:%S", gmtime())
       print iFile

if __name__ == "__main__":
  if len(sys.argv) !=4:
    print "usage: python resubmitRecoJobs_any.py  inChannel ifile ijob (e.g.:  106608 32  3)"
    print sys.argv[1], sys.argv[2], sys.argv[3]
    sys.exit(-1)
  print sys.argv[1], sys.argv[2], sys.argv[3]
  resubmitRecoSplitJobs_any(sys.argv[1],sys.argv[2], sys.argv[3])


