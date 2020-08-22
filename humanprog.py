import pyttsx3 as talk
import os



talk.speak('Hello Harsh ...How can I help you?')
print("Hello Harsh ...How can I help you? " , end='')
while True:
#	print("What is the next task for me? "  , end='')
	p = input()



	if (("run" in p) or ("open" in p) or ("launch" in p))  and ("chrome" in p):
	  talk.speak("Ok.. Harsh ..I am launching  Chrome browser for you  ")
	  os.system("start chrome")
	  print("What is the next task for me? "  , end='')
	  talk.speak('What is the next task for me?')

	elif (("run" in p) or  ("open" in p ) or ("launch" in p)) and  (("notepad" in p) or ("editor" in p) ) :
		talk.speak('Ok.. Harsh ..I am launching notepad for you')
		os.system("notepad")
		print("What is the next task for me? "  , end='')
		talk.speak('What is the next task for me?')

	elif (("run" in p) or ("open" in p) or ("launch" in p)) and (("calculator" in p) or ("calc" in p)) :
	  talk.speak("Ok.. Harsh ..I am launching calculator for you   ")
	  os.system("calc")
	  print("What is the next task for me? "  , end='')
	  talk.speak('What is the next task for me?')

	elif (("run" in p) or ("open" in p) or ("launch" in p)) and (("msoffice" in p) or ("ms-office" in p) ) :
	  talk.speak("Ok.. Harsh ..I am launching Microsoft Office for you")
	  os.system("start winword")
	  print("What is the next task for me? "  , end='')
	  talk.speak('What is the next task for me?')

	elif (("run" in p) or ("open" in p) or ("launch" in p)) and ( ("windows" in p) and ("media" in p)) or ("player" in p):
	  talk.speak('Ok.. Harsh ..I am launching windows Media Player for you')
	  os.system("start wmplayer")
	  print("What is the next task for me? "  , end='')
	  talk.speak('What is the next task for me?')

	elif (("run" in p) or ("open" in p) or ("launch" in p)) and (("vlc" in p) or ("media" in p)) or ("player" in p) :
		talk.speak('Ok.. Harsh ..I am launching vlc Media Player for you')
		os.system("start vlc")
		print("What is the next task for me? "  , end='')
		talk.speak('What is the next task for me?')

	elif ("date" in p) or ("show" in p) or ("current" in p):
	  talk.speak("Ok.. I am displaying Today's date is ")
	  os.system("date")
	  print("What is the next task for me? "  , end='')
	  talk.speak('What is the next task for me?')

	elif  ("exit" in p)  or ("quit" in p):
		print("Bye Harsh, Have a good day!! ")
		talk.speak("ok . Bye Harsh, Have a good day!")
		break


	else:
		print("Sorry I can't do that")
		talk.speak("Sorry I can't do that")
		print("What is the next task for me? ",end = '' )
		talk.speak('What is the next task for me?')
