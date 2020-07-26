#Linking the entities identified with the explanation to provide from documentation

from New_functions.interaction import conversation

### Using google text to speech
from gtts import gTTS
import sys
from playsound import playsound

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
	try:
		if lang == 'py':
			prog_lang = 'Python'
			from Documentation.python_doc_testing import documentation_list
			#Storing the list of all the available documentations in the used programming language
			all_docs = documentation_list()
		elif lang == 'c':
			prog_lang = 'C language'
			from Documentation.doc_testing import documentation_list
			#Storing the list of all the available documentations in the used programming language
			all_docs = documentation_list()
		language = 'en'
		# rate for speed of speech(True - slow, False = fast) 
		rate = False 
		if entities:
			if 'available_documentation:available_documentation' in entities:
				speak = "Displaying the list of available documentations."
				speech_obj = gTTS(text = speak, lang = language, slow=rate)
				speech_obj.save('wit_bot.mp3')
				playsound('wit_bot.mp3', True)
				print("Displaying the list of available documentations\n")
				if lang == 'py':
					from Documentation.python_doc_testing import available_documentation
					available_documentation()
				elif lang == 'c':
					from Documentation.doc_testing import available_documentation
					available_documentation()
				print("\nIf you wish to read from any of these, press 1 and you will be redirected to ask query, else press 0 exit.\n")
				your_wish = input()
				if (your_wish == '0'):
					speak = "Have a good day. Happy Learning and coding."
					speech_obj = gTTS(text = speak, lang = language, slow=rate)
					speech_obj.save('wit_bot.mp3')
					playsound('wit_bot.mp3', True)
					sys.exit("\n***Happy Coding!!!***\n")

				ask = 2
				return ask

			### Check whether the entities recognised are relevant to the programming language that he is working on
			### Stored in another list 
			relevant_entities = []
			speak = "From the query obtained, the keyterms recognized, relevant to."+prog_lang+"are."
			print("\nFrom the query obtained, the keyterms recognized relevant to the",prog_lang,"are:")

			for i in range(len(entities)):
				entities[i] = (entities[i].split(':')[0]).replace('_entity', '')
				flag = 0 ### Represents entity found not relevant to the programming language that the user is using
				for doc in all_docs:
					# print("entity: ", entities[i])
					# print("Docs : ", doc)
					if entities[i] in doc:
						flag = 1
						break
				if flag:
					print('=>',entities[i])
					speak += entities[i]
					speech_obj = gTTS(text = speak, lang = language, slow=rate)
					speech_obj.save('wit_bot.mp3')
					playsound('wit_bot.mp3', True)
					relevant_entities.append(entities[i])

			speak = "To strengthen the conceptual understanding,"
			speak += "Please go through the detailed explanation of these."
			speech_obj = gTTS(text = speak, lang = language, slow=rate)
			speech_obj.save('wit_bot.mp3')
			
			playsound('wit_bot.mp3', True)
			
			reading = 1
			while(reading):
				#Function to perform casual interaction with the bot
				reading = conversation(relevant_entities, lang)
		else:
			if(ask < 3):
				speak = "Sorry...couldn't interpret your query, please try again"
				print("\nSorry!...We couldn't interpret your query as related to programming OR explanation might be unavailable, please try again\n")
			else:
				speak = "Sorry...couldn't interpret your query."
				print("Sorry...couldn't interpret your query")
			speech_obj = gTTS(text = speak, lang = language, slow=rate)
			speech_obj.save('wit_bot.mp3')
			playsound('wit_bot.mp3', True)

			ask = ask + 1
			return ask


		speak = "Have a Good day. Happy learning and coding!"
		speech_obj = gTTS(text = speak, lang = language, slow=rate)
		speech_obj.save('wit_bot.mp3')
		playsound('wit_bot.mp3', True)
		sys.exit("\n***Happy Learning***\n")


	except Exception as err:
		print("Exception arose is,",err)
		


