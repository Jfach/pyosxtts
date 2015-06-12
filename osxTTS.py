#OSX text to speech library
#Written by Faissal Bensefia
#Distributed under the MIT license
from os import *
import platform

if platform.system() != 'Darwin': #Check that this is running on OSX
	raise Exception("You must be running OSX!")

def speak(string,rate): #Outputs speech to the speakers, text is a string, rate is an integer
	system('say -r '+str(rate)+' "'+string+'"')

def export(string,rate,filename):#Outputs speech to a file
	system('say -r '+str(rate)+'-o "'+filename+'" "+string+"')
