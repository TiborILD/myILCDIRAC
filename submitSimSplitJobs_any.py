# ...........................
# python submitSimSplit_any.py

import sys, os, subprocess
import time 
from string import Template
from time import gmtime, strftime
#from readin_maps import readin_maps
#from readin_maps import * 
from get_nevts_inIx import * 

fR = file("runSimSplit_any.py","r")
lines = fR.read()
fR.close()



def submitSimSplitJobs_any(inChannel):
   global lines,l1, nfiles, nEvtsArray, evtsPerRun, fOut
   '''
        print "Wrong Channel Id !!!!" , inChannel
   '''
#   print nEvtsArray[0]
   nEvtsArray=get_nevts_inIx(inChannel)
   nfiles= len(nEvtsArray)
   strinChannel= str(inChannel)
   print "submitSimSplitJobs_any: nfiles ",nfiles, "inChannel=", inChannel
 


   evtsPerRun = 200
#   nfiles=6
#   event1= 36601
#   event1= 1
#   fstevt=str(event1)
#Here loop over all available generator files i:
   strevtsprun = str(evtsPerRun)
   for iFile in range(1,nfiles,1):
#   for iFile in range(nfiles,nfiles+1,1):
       striFile = str(iFile)
#       nevents= nEvtsArray[iFile] - (event1 - 1)
       nevents= nEvtsArray[iFile] 
       nJobs = nevents/evtsPerRun
       if (nevents%evtsPerRun >9):
           nJobs = nJobs +1
#       nJobs=49
       snJobs = str(nJobs)
       print "iFile : Evts - corrected nJobs= ",iFile, nevents, nJobs
       for ijob in range(1,nJobs+1,1):
#       for ijob in range(nJobs,nJobs+1,1):
          evtStart = (ijob-1)*evtsPerRun + 1
          fstevt = str(evtStart)
          sijob = str(ijob)
          t= Template(lines)
          if os.path.exists("runSimSplit_any_Tmp.py"):
             os.remove("runSimSplit_any_Tmp.py")
          fT = file("runSimSplit_any_Tmp.py","w")
          fT.write(t.substitute(idChannel=strinChannel,ixnfile=striFile,startevt=fstevt,evtsPerRun=strevtsprun,xJobs=snJobs, xjob=sijob))
          fT.close()
          print iFile, fstevt, sijob
          f2 = subprocess.call("python runSimSplit_any_Tmp.py", shell=True)
       if iFile < nfiles - 1 :
          print strftime("%Y-%m-%d %H:%M:%S", gmtime())
          print("Sleeping for 10 min between submissions of 2 input files ...")
          time.sleep(600)   # Delay for 1 minute (60 seconds)
          print strftime("%Y-%m-%d %H:%M:%S", gmtime())


if __name__ == "__main__":
  if len(sys.argv) !=2:
    print "usage: python submitSimSplit_any.py  inChannel (e.g.:  106608)"
    print sys.argv[1]
    sys.exit(-1)
  print sys.argv[1]
  submitSimSplitJobs_any(sys.argv[1])


