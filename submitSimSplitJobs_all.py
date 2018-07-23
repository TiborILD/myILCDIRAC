#!/usr/bin/python

import sys, os, subprocess
import time 
from string import Template
from time import gmtime, strftime
from get_nevts_inIx import * 

fR = file("runSimSplit_all.py","r")
lines = fR.read()
fR.close()

def submitSimSplitJobs_all(inChannel):
   '''
        Submit simulation jobs for all events, in all ifiles in given inChannel
   '''
   nEvtsArray=get_nevts_inIx(inChannel)
   nfiles= len(nEvtsArray)
   strinChannel= str(inChannel)
   print "submitSimSplitJobs_all: nfiles ",nfiles, "inChannel=", inChannel

# simulation jobs with "evtsPerRun" (split input generator file per "evtsPerRun")
   evtsPerRun = 200
# loop over all available generator files "nfiles":
   strevtsprun = str(evtsPerRun)
   for iFile in range(1,nfiles,1):
       striFile = str(iFile)
       nevents= nEvtsArray[iFile] 
       nJobs = nevents/evtsPerRun
# if >9 events remained, create/submit another job
       if (nevents%evtsPerRun >9):
           nJobs = nJobs +1
       snJobs = str(nJobs)
       print "iFile : Evts - corrected nJobs= ",iFile, nevents, nJobs
       for ijob in range(1,nJobs+1,1):
          evtStart = (ijob-1)*evtsPerRun + 1
          fstevt = str(evtStart)
          sijob = str(ijob)
          t= Template(lines)
          if os.path.exists("runSimSplit_all_Tmp.py"):
             os.remove("runSimSplit_all_Tmp.py")
          fT = file("runSimSplit_all_Tmp.py","w")
          fT.write(t.substitute(idChannel=strinChannel,ixnfile=striFile,startevt=fstevt,evtsPerRun=strevtsprun,xJobs=snJobs, xjob=sijob))
          fT.close()
          print iFile, fstevt, sijob
          f2 = subprocess.call("python runSimSplit_all_Tmp.py", shell=True)
       if iFile < nfiles - 1 :
          print strftime("%Y-%m-%d %H:%M:%S", gmtime())
          print("Sleeping for 10 min between submissions of 2 input files ...")
          time.sleep(600)   # Delay for 1 minute (60 seconds)
          print strftime("%Y-%m-%d %H:%M:%S", gmtime())

if __name__ == "__main__":
  if len(sys.argv) !=2:
    print "usage: python submitSimSplit_all.py  inChannel (e.g.:  106608)"
    print sys.argv[1]
    sys.exit(-1)
  print sys.argv[1]
  submitSimSplitJobs_all(sys.argv[1])

