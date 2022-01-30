#! /usr/bin/python

import sys
import os

os.system('rm -r practica_creativa2')

os.system('git clone https://github.com/JaimeMadridAlonso/parte3.git')

os.system('cd practica_creativa2/bookinfo/src/reviews && docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build')
