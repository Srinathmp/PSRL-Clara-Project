#Linking the entities identified with the explanation to provide from documentation

from New_functions.interaction import conversation
import pyttsx3
# initialisation 
engine = pyttsx3.init()

#Customizing properties
engine.setProperty('voice', 'english+f4')
engine.setProperty('rate', 170)

### Using google text to speech
from gtts import gTTS
import os

# import socket

# def is_connected():
#     try:
#         # connect to the host -- tells us if the host is actually
#         # reachable
#         socket.create_connection(("1.1.1.1", 53))
#         return True
#     except OSError:
#         pass
#     return False

def recognise_and_explain(entities, lang, ask):
		### Include entities return, variable, operator
		
	#print(entities)

	## Creating dictionary of entity as key and function call as value
	# if(not is_connected()):
	# 	try:
	# 		if entities:
	# 			print("From the query obtained, the keyterms recognized are:")
	# 			engine.say("From the query obtained, the keyterms recognized are.....")
	# 			for i in range(len(entities)):
	# 				entities[i] = (entities[i].split(':')[0]).replace('_entity', '')
	# 				print(i+1,':=',entities[i])
	# 				engine.say(entities[i])

	# 			engine.runAndWait()
	# 			engine.say("To strengthen the conceptual understanding,")
	# 			engine.say("Please go through the detailed explanation of these.")
	# 			engine.runAndWait()
	# 			#print(entities)
	# 			reading = 1
	# 			while(reading):
	# 				for entity in entities:
	# 					print("\nTo continue reading about,",entity,"Press 1, else press any key to continue :\n")
	# 					reply = input()
	# 					if reply == '1':
	# 						if entity in list(entity_func_dict.keys()):
	# 							entity_func_dict[entity]()
	# 						else:
	# 							print("Sorry!...We don't have related documentation for,",entity,"keyterm\n")
	# 							engine.say("Sorry...")
	# 							engine.runAndWait()
	# 				print("\nIf you would like to revisit the keywords recognised, to read further,press 1, else press 0 to exit\n")
	# 				engine.say("To revisit the keywords recognised for explanation,press 1, else press 0 to exit")
	# 				engine.runAndWait()
	# 				reading = int(input())

	# 		else:
	# 			print("Sorry!...We couldn't interpret your query as related to programming OR explanation might be unavailable, please try again\n")
	# 			engine.say("Sorry...couldn't interpret your query, please try again")
	# 			engine.runAndWait()
	# 			print("\nPress 1 to try again, else 0 to exit\n")
	# 			ask = input()
	# 			return ask


	# 		print("\n***Happing Learning***\n")
	# 		engine.say("Have a Good day. Happy learning and coding")
	# 		engine.runAndWait()

	# 	except Exception as err:
	# 		print("Exception arose is,",err)
	# else:
	# 	# print("Using google speech\n")
	try:
		language = 'en'
		# rate for speed of speech(True - slow, False = fast) 
		rate = False 
		if entities:
			#engine.say("From the query obtained, the keyterms recognized are.....")
			speak = "From the query obtained, the keyterms recognized are."
			print("\nFrom the query obtained, the keyterms recognized are:")

			for i in range(len(entities)):
				entities[i] = (entities[i].split(':')[0]).replace('_entity', '')
				print(i+1,':=',entities[i])
				#engine.say(entities[i])
				speak += entities[i]
				speech_obj = gTTS(text = speak, lang = language, slow=rate)
				speech_obj.save('wit_bot.mp3')
				os.system("mpg321 wit_bot.mp3")

			speak = "To strengthen the conceptual understanding,"
			speak += "Please go through the detailed explanation of these."
			speech_obj = gTTS(text = speak, lang = language, slow=rate)
			speech_obj.save('wit_bot.mp3')
			os.system("mpg321 wit_bot.mp3")
			#print(entities)
			reading = 1
			while(reading):
				### Section to be modified(Total voice based)
				#-----------------------------------------------------------------
				#Function to perform casual interaction with the bot
				reading = conversation(entities, lang)
		else:
			if(ask < 3):
				speak = "Sorry...couldn't interpret your query, please try again"
				speech_obj = gTTS(text = speak, lang = language, slow=rate)
				speech_obj.save('wit_bot.mp3')
				os.system("mpg321 wit_bot.mp3")
				print("\nSorry!...We couldn't interpret your query as related to programming OR explanation might be unavailable, please try again\n")
			else:
				speak = "Sorry...couldn't interpret your query."
				speech_obj = gTTS(text = speak, lang = language, slow=rate)
				speech_obj.save('wit_bot.mp3')
				os.system("mpg321 wit_bot.mp3")

			ask = ask + 1
			return ask


		speak = "Have a Good day. Happy learning and coding!"
		speech_obj = gTTS(text = speak, lang = language, slow=rate)
		speech_obj.save('wit_bot.mp3')
		os.system("mpg321 wit_bot.mp3")
		# print("\n***Happing Learning***\n")
		sys.exit("\n***Happing Learning***\n")


	except Exception as err:
		print("Exception arose is,",err)
		


