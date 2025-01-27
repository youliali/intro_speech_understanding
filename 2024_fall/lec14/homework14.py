import datetime, gtts, bs4, random, speech_recognition

def what_time_is_it(lang, filename):
    '''
    Tell me what time it is.
    
    Parameters:
    lang (str) - language in which to speak
    filename (str) - the filename into which the audio should be recorded
    '''
    #raise RuntimeError("You need to write this part!")
    (data, time) = datetime.datetime.now().isoformat().split("T")
    (hour, minutes, seconds) = time.split(":")
    if lang=="en":
        text = hour+" hours and "+minutes+" minutes"
    elif lang =="ja":
        text = hour+"時"+minutes+"分です"
    elif lang=="zh":
        text = "现在是"+hour+"点"+"分"
    else:
        text="I'm sorry, I don't know that language"
    gtts.gTTS(text,lang=lang).save(filename)
    
    
def tell_me_a_joke(lang, audiofile):
    '''
    Tell me a joke.
    
    @params:
    filename (str) - filename containing the database of jokes
    lang (str) - language
    audiofile (str) - audiofile in which to record the joke
    '''
    #raise RuntimeError("You need to write this part!")
    filename = 'jokes_%s.txt'%(lang)
    with open(filename) as f:
        jokes = f.readlines()
    jokes = random.choice(jokes)
    print(joke.strip())
    gtts.gTTS(joke.strip(), lang=lang).save(audiofile)

def what_day_is_it(lang, audiofile):
    '''
    Tell me what day it is.

    @params:
    lang (str) - language in which to record the date
    audiofile (str) - filename in which to read the date
    
    @returns:
    url (str) - URL that you can look up in order to see the calendar for this month and year
    '''
    #raise RuntimeError("You need to write this part!")
    today = datetime.date.today()
    year = today.year
    month = today.month
    day = today.day
    weekday = today.isoweekday()
    if lang=="en":
        weekdays=['','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        months=['','January','February','March','April','May','June','July','August','September','October','November'

def personal_assistant(lang, filename):
    '''
    Listen to the user, and respond to one of three types of requests:
    What time is it?
    What day is it?
    Tell me a joke!
    
    @params:
    lang (str) - language
    filename (str) - filename in which to store the result
    '''
    raise RuntimeError("You need to write this part!")
