#!/usr/bin/env python

from pprint import pprint, pformat
import time, datetime
import sys, subprocess, commands
from DIRAC.Core.Base.Script import parseCommandLine
parseCommandLine()
from DIRAC.WorkloadManagementSystem.Client.JobMonitoringClient import JobMonitoringClient

jobMon = JobMonitoringClient()

def validate_date(d):
    try:
      datetime.datetime.strptime(d, "%Y-%m-%d %H:%M:%S")
      return True
    except ValueError:
      return False

def jobStat(idone):
#ret = jobMon.getJobsSites([3465870])
#ret = jobMon.getJobs({'JobName':'sI106551.050_057', 'Owner':'kurca'})
   ts = time.gmtime()
   print(time.strftime("%X", ts))
   print(time.strftime("%c", ts))
   myts = str(time.strftime("%d", ts)) + str(time.strftime("%m", ts))  + str(time.strftime("%y", ts))
   print myts
   
   if int(idone) == 1 :
      ret = jobMon.getJobs({'Status':'Done', 'Owner':'kurca'})
      fTX = file("jobsStatDone_"+myts+".txt","a")
   else:
      ret = jobMon.getJobs({'MinorStatus':'Maximum of reschedulings reached', 'Owner':'kurca'})
      fTX = file("jobsStatMax3_"+myts+".txt","a")

   print "idone = ",  idone
   print fTX
   if not ret['OK']:
      print "Error", ret['Message']

   jobIDs = ret['Value']
   njobs = len(jobIDs)
   print "range:", len(jobIDs)
#   print jobIDs

   outlist = []
   for indx in range(0,njobs,1):
     sublist=[]
     jobid = int(jobIDs[indx])
     ret3 = jobMon.getJobAttribute(jobid,'JobName')
     ret4 = jobMon.getJobAttribute(jobid,'Site')
     ret5 = jobMon.getJobAttribute(jobid,'StartExecTime')
     ret6 = jobMon.getJobAttribute(jobid,'EndExecTime')
     ret7 = jobMon.getJobAttribute(jobid,'RescheduleCounter')

     jobname   = ret3['Value']
     sitename  = ret4['Value']
     strtex    = ret5['Value']
     endex     = ret6['Value']
     reschdcnt = ret7['Value']

     if validate_date(strtex)and validate_date(endex):
        t1=time.mktime(datetime.datetime.strptime(strtex, "%Y-%m-%d %H:%M:%S").timetuple())
        t2=time.mktime(datetime.datetime.strptime(endex, "%Y-%m-%d %H:%M:%S").timetuple())
     else:
        t1=0
        t2=0
     print jobid, jobname, sitename ,strtex, endex, t2-t1
     if int(idone) == 1 :
        sublist.append(jobid)
        sublist.append(jobname)
        sublist.append(sitename)
        sublist.append(strtex)
        sublist.append(endex)
        sublist.append(reschdcnt)
        sublist.append(str(t2-t1))
        outstring = str(jobid)+ "," + jobname + "," + sitename + "," + strtex + "," + endex + "," + str(reschdcnt) + "," + str(t2-t1)
     else:
        sublist.append(jobname)
        outstring =  jobname 

     print outstring 
     fTX.write(outstring + "\n")
                    
if __name__ == "__main__":
  if len(sys.argv) !=2:
    print "usage: python jobStat.py  1  [(Done),  any other (Max3reschedulings)]"
    sys.exit(-1)
  print sys.argv[1]
  jobStat(sys.argv[1])
 
