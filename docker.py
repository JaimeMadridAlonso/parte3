#! /usr/bin/python

import sys
import os

if len(sys.argv)==2:
  if sys.argv[1]=='1':
    os.system('docker-compose -f docker-compose.yml up --build')
  elif sys.argv[1]=='2':
    os.system('docker-compose -f docker-compose2.yml up --build')
  elif sys.argv[1]=='3':
    os.system('docker-compose -f docker-compose3.yml up --build')
  else:
    print("Elige un valor del 1-3")
else:
  print("El comando correcto es 'python3 docker.py X' siendo X un valor del 1-3")
