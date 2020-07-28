import sys
import requests
import json
from New_functions.Recorder import record_audio, read_audio
import shlex 
import subprocess
import readline

# Wit speech API endpoint
API_ENDPOINT = 'https://api.wit.ai/speech'

# Wit.ai api access token
wit_access_token = '5XSGMLPWESNYCRXTTPNLDGO2AZMR5GSX'

#-----------------------------------------------------------------
curl_request = """curl \
 -H 'Authorization: Bearer 5XSGMLPWESNYCRXTTPNLDGO2AZMR5GSX' \
 'https://api.wit.ai/message?v=20200623&q="""

def text_clean(text):
    for i in text:
        if(i==' '):
            text = text.replace(' ','%20')
    return text

def rlinput(prompt, prefill=''):
   readline.set_startup_hook(lambda: readline.insert_text(prefill))
   try:
      return input(prompt)
   finally:
      readline.set_startup_hook()
#-----------------------------------------------------------------
def RecognizeSpeech_during_interaction(AUDIO_FILENAME, num_seconds):

    # record audio of specified length in specified audio file
    record_audio(num_seconds, AUDIO_FILENAME)

    # reading audio
    audio = read_audio(AUDIO_FILENAME)

    # defining headers for HTTP request
    headers = {'authorization': 'Bearer ' + wit_access_token,
               'Content-Type': 'audio/wav'}

    # making an HTTP post request
    resp = requests.post(API_ENDPOINT, headers = headers,
                         data = audio)
    #print('Http post request=',resp)
    # converting response content to JSON format
    data = json.loads(resp.content)
    #print('data dictionary = ',data['entities'].keys())
    # get text from data
    received_audio_input = 0
    response = []
    try:
        text = data['text']
        text = text.replace("\'","")
        received_audio_input = 1
    except:
        print('\nThere was some issue recording your query, please try again\n')
        return response
    #-----------------------------------------------------------
    if(received_audio_input==1):
        #processing the returned text
        default_value = text
        print("\n***Note : You can edit your response inplace below, if this is not what you said, else press enter key to proceed***\n")
        print('Did you say?')
        stuff = rlinput("", default_value)
        text = stuff
        sample_text = text_clean(text)
        sample_text = sample_text.replace("\'", "")
        # print('original text = ',text)
        if sample_text == "":
            sys.exit("\n**You didn't give any query**\n")

        final_request = curl_request+sample_text+"'"
        # print('curl_request = ',final_request)
        sub_list = shlex.split(final_request)
        #-----------------------------------------------------------
        #Sending request to api again
        #-----------------------------------------------------------
        process = subprocess.Popen(sub_list,
                             stdout=subprocess.PIPE, 
                             stderr=subprocess.PIPE,
                             universal_newlines=True)
        stdout, stderr = process.communicate()
        # print('standard output=',stdout)
        # print('final output=',type(stdout))
        final_dict =json.loads(stdout)
        print(final_dict)
        if final_dict['intents']:
        	response.append(final_dict['intents'][0]['name'])
        else:
        	response.append(None)
        if final_dict['traits']:
        	response.append(final_dict['traits']['wit$on_off'][0]['value'])
        else:
        	response.append(None)
    #-----------------------------------------------------------
    # print("\nYour final query: {}".format(text))
    # return the entity list
    return response
