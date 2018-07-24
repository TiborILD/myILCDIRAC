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

def submitSimSplitJobs_any(inChannel, infile, inJob):
   '''
        print "Wrong Channel Id !!!!" , inChannel
   '''
   nEvtsArray=get_nevts_inIx(inChannel)
   nfiles= len(nEvtsArray)
   strinChannel= str(inChannel)
   print "submitSimSplitJobs_any: nfiles ",nfiles, "inChannel=", inChannel

   evtsPerRun = 200
#Here loop over all available generator files i:
   strevtsprun = str(evtsPerRun)
   if int(infile) > nfiles:
      print "Impossible:  infile  ", infile, " > Max Files", nfiles
      sys.exit(-1)
   for iFile in range(int(infile),int(infile)+1,1):
       striFile = str(iFile)
       nevents= nEvtsArray[iFile] 
       nJobs = nevents/evtsPerRun
       if (nevents%evtsPerRun >9):
           nJobs = nJobs +1
       snJobs = str(nJobs)
       if int(inJob) > nJobs:
         print "Impossible:  inJob  ", inJob, " > Max Jobs", nJobs
         sys.exit(-1)
       delta = 1
       print "iFile : Evts - corrected nJobs= ",iFile, nevents, nJobs
       for ijob in range(int(inJob),int(inJob)+delta,1):
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

if __name__ == "__main__":
  if len(sys.argv) !=4:
    print "usage: python submitSimSplit_any.py  inChannel ifile ijob (e.g.:  106608 1 33)"
    print sys.argv[1], sys.argv[2], sys.argv[3]
    sys.exit(-1)
  print sys.argv[1], sys.argv[2], sys.argv[3]
  submitSimSplitJobs_any(sys.argv[1],sys.argv[2],sys.argv[3])
