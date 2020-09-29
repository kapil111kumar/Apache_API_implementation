#!/usr/bin/python

#import pyttsx3
import os,cgi
print "Content-Type: text/html\n"

f=cgi.FieldStorage()
x=f.getvalue('x')



#pyttsx3.speak("Hello everyone this is Ashish personal computer")
#pyttsx3.speak("What You want to open ?")

#pytts3tts.speak("What you want to Open : \n Press 1 for Chrome \n Press 2 for Windows Media Player \n Press 3 for Notepad \n Enter Your Choice : ")
#x=input("What You want to open : ")

#x = input("What you want to Open : \n Press 1 for Chrome \n Press 2 for Windows Media Player \n Press 3 for Notepad \n Enter Your Choice : ")
while(True):
#	x=input("Let me know your requirement : ")
	z=("launch" in x or "run" in x or "execute" in x or "start" in x)
	if ("dont" or "not" or "don't") in x:
		print("I want to know your requirement.")
	elif z and ("browser"  in x or "chrome" in x):
		y="start  chrome"
		print(y)
		os.system(y)

	elif z and ("player"  in x or "media" in x):
		y="start wmplayer"
		print(y)
		os.system(y)

	elif z and ("notepad"  in x or "editor" in x):
		y="notepad"
		print(y)
		os.system(y)

	elif ("quit"  in x or "exit" in x):
		break
	else:
		print("Invalid ", end='') #end argument to remove space from the print statement ending.
		print("Choice")

#print(y)
#os.system(y)

