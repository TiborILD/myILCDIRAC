import sys, os, subprocess
import time 
import argparse, math
from string import Template
from time import gmtime, strftime
#from readin_maps import readin_maps
#from readin_maps import * 
from get_nevts_inIx import * 

fR = file("runSimSplit.py","r")
lines = fR.read()
fR.close()

def submitSimSplitJobs(inChannel, infile, inJob, delta):
   '''
        Submit all SimSplitJobs for all files, or just for a selected file, jobs range.
   '''
   nEvtsArray=get_nevts_inIx(inChannel)
   nfiles= len(nEvtsArray)
   strinChannel= str(inChannel)
   print "submitSimSplitJobs.py nfiles ",nfiles, "inChannel=", inChannel

   if infile is not None:
     print 'infile=', infile
     maxfile = int(infile) +1
   else:
     infile =  1
     maxfile = nfiles

   evtsPerRun = 200
#Here loop over all available generator files i:
   strevtsprun = str(evtsPerRun)
   if int(infile) > nfiles:
      print "Impossible:  infile  ", infile, " > Max Files", nfiles
      sys.exit(-1)
   for iFile in range(int(infile),maxfile,1):
       striFile = str(iFile)
       nevents= nEvtsArray[iFile] 
       nJobs = nevents/evtsPerRun
       if (nevents%evtsPerRun >9):
           nJobs = nJobs +1
       snJobs = str(nJobs)
       if inJob is not None:
          maxJob = int(inJob) +  1
          if delta is not None:
             maxJob = int(inJob) + int(delta)
       else:
          inJob = 1
          maxJob = nJobs
       if int(inJob) > nJobs:
         print "Impossible:  inJob  ", inJob, " > Max Jobs", nJobs
         sys.exit(-1)
       delta = 0
       print "iFile : Evts - corrected nJobs= ",iFile, nevents, nJobs
       for ijob in range(int(inJob),maxJob,1):
          print 'ijob = ', ijob
          evtStart = (ijob-1)*evtsPerRun + 1
          fstevt = str(evtStart)
          sijob = str(ijob)
          t= Template(lines)
          if os.path.exists("runSimSplit.Tmp.py"):
             os.remove("runSimSplit.Tmp.py")
          fT = file("runSimSplit.Tmp.py","w")
          fT.write(t.substitute(idChannel=strinChannel,ixnfile=striFile,startevt=fstevt,evtsPerRun=strevtsprun,xJobs=snJobs, xjob=sijob))
          fT.close()
          print iFile, fstevt, sijob
          f2 = subprocess.call("python runSimSplit.Tmp.py", shell=True)

if __name__ == "__main__":
  """ Submit MC-simulation job.

      inChannel = reqId, ifile, ijob, delta (n-consecutive jobs)
  """
  parser = argparse.ArgumentParser()
  parser.add_argument("-c","--inChannel", dest='inChannel', help="MC-Id, mandatory parameter!!!")
  parser.add_argument("-i","--ifile", dest='ifile', help="File index")
  parser.add_argument("-j","--inJob", dest='inJob', help="Job index")
  parser.add_argument("-d","--delta", dest='delta', help="nJobs index")
  args = parser.parse_args()
  print args

  submitSimSplitJobs(args.inChannel,args.ifile,args.inJob,args.delta)
