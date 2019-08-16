#!/usr/bin/python
# -*- coding: UTF-8 -*-
from pymogile import Client,MogileFSError
import time,sys,getopt,os
def main(argv):
  mog_domain=''
  mog_trackers=''
  output_dir=''
  try:
    opts,args = getopt.getopt(argv,"d:t:o:",["domain=","trackers=","output-dir="])
  except getopt.GetoptError:
    print sys.argv[0] + ' -d <domain> -t <trackers> -o <output-dir>'  
  for opt,arg in opts:
    if opt in ("-d","--domain"):
          mog_domain=arg
    elif opt in ("-t","--trackers"):
          mog_trackers=arg
    elif opt in ("-o","--output-dir"):
          if arg[len(arg)-1] == '/':  
            output_dir=arg
          else:
            output_dir=arg + '/'
  if not os.path.exists(output_dir):
    os.makedirs(output_dir)
  datastore= Client(domain=mog_domain,trackers=mog_trackers.split(','))
  keys=datastore.keys()
  start=time.time()
  for index in range(len(keys)):
    print ('downloading: '+keys[index])
    file=open(output_dir+keys[index],'w')
    file.write(datastore.get_file_data(keys[index]))
    file.close()
  print 'dump completed'
  print ("time used : %.2f seconds" % (time.time() - start))
if __name__ == "__main__":
   main(sys.argv[1:])
