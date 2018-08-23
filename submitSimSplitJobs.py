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


"""
#  submitSimSplitJobs.sys.argv[1:])
#  submitSimSplitJobs.sys.argv[1], infile=-1, inJob=-1, delta=0)
#  submitSimSplitJobs.sys.argv[1],*kwargs)
  if len(sys.argv) == 2:
    print sys.argv[1]
  elif len(sys.argv) == 3:
    print sys.argv[1], sys.argv[2]
  elif len(sys.argv) == 4:
    print sys.argv[1], sys.argv[2], sys.argv[3]
  elif len(sys.argv) == 5 :
    print sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
  else :
    print "usage: python submitSimSplit_any.py  inChannel ifile ijob (e.g.:  106608 1 33)"
    sys.exit(-1)
==============================================================
def presentation(title, **kwargs):
    print ('---- %s ----' %(title))

    name=kwargs.get('name', None)
    firstname=kwargs.get('firstname', None)

    if (name and firstname):
        print('mon nom est %s, %s %s' %(name, firstname, name))
    elif (firstname and not(name)):
        print('Mon prenom est %s' %(firstname))
    elif (not(firstname) and name):
        print('Mon nom est %s' %(name))
    else:
        print('Je ne suis personne...')

if __name__ == "__main__":
    presentation('Prenom+nom', firstname='James', name='Bond')
    presentation('Seulement un prenom', firstname='James')
    presentation('Seulement un nom', name='Bond')
    presentation('ni nom, ni prenom')




===============================================================
# Avec *args
def traitement(a_remplacer, remplacant, *args):
    for idx, fichier in enumerate(args):
        content = ""
        with open(fichier, 'r') as fichier_only:
            for line in fichier_only.readlines():
                line = line.replace(a_remplacer, remplacant)
                content += line

        with open(fichier, 'w') as fichier_only:
            fichier_only.write(content)

if __name__ == '__main__':
    traitement('riri', 'fifi', 'fichier1.txt')
    traitement('toto', 'tata', 'fichier1.txt', 'fichier2.txt', 'fichiern.txt')  # le nombre d'arguments est variable
    liste_fichiers=['fichier3.txt', 'fichier4.txt', 'fichiers5.txt'] 
    traitement('fifi', 'loulou', *liste_fichiers) # mais on peut aussi passer une liste,  sans traitement, grace a l'operateur (*)
"""
