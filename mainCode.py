from googletrans import Translator
import difflib
import wikipedia
import random
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import json
import numpy as np
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
#import configure
#import infermedica_api

#api = infermedica_api.API(app_id='4c39c00d', app_key='164e3a42dc81ef64720517b97f4adb44')
# print(api.info())

# new libraries

sr = pd.read_csv('final dataset.csv.csv', engine='python')
sr = np.array(sr)
dis = sr[:, 1]
symp = sr[:, 2]

dis = np.array(dis)
symp = np.array(symp)

# greeting file
gr = pd.read_csv('Greeting Dataset.csv', engine='python')
gr = np.array(gr)
gd = gr[:, 0]

# thankyou file
tu = pd.read_csv('ThankYou.csv', engine='python')
tu = np.array(tu)
td = gr[:, 0]

# welcome file
wc = pd.read_csv('Welcome Dataset.csv', engine='python')
wc = np.array(wc)
wd = wc[:, 0]

# age file
ag = pd.read_csv('AGE Dataset.csv', engine='python')
ag = np.array(ag)
ad = ag[:, 0]

# bye file
by = pd.read_csv('BYE Dataset.csv', engine='python')
by = np.array(by)
bd = by[:, 0]

# name file
nm = pd.read_csv('Name Dataset.csv', engine='python')
nm = np.array(nm)
nd = nm[:, 0]


def stopWords(text):
    # text is a sentence
    stopw = set(stopwords.words('english'))
    filtered = []
    words = word_tokenize(text)
    for i in words:
        if i not in stopw:
            filtered.append(i)
    return filtered


def stemming(text):
    # text could be a sent or word
    ps = PorterStemmer()
    empty = []
    for w in text:
        empty.append(w)
    return empty


def getName(text):
    # text is a/many sentence
    # takes the user response and returns name of the user
    filtered = stopWords(text)
    stemmed = stemming(filtered)
# print("stemmed",stemmed)
    tag = nltk.pos_tag(stemmed)
    # print(tag)
    noun = []
    for i in range(len(tag)):
        # print(tag[i][1])
        if ((str(tag[i][1]) == 'NN' or str(tag[i][1]) == 'NNP') and str(tag[i][0]) != 'name'):
            noun.append(tag[i][0])
# print(noun)
##    chunkGram = r"""Chunk: {<NN+>*}  """
##    chunkParser = nltk.RegexpParser(chunkGram)
##    chunked = chunkParser.parse(tag)
# print(chunked)
# for i in chunked:
# if i != ('name', 'NN'):
##            name = i
# print('i=',i[0])
##
# print(name[0])
    return noun


def greet():
    k = random.randint(0, 50)
    print(gd[k % 13])


def askName(pre,pointer):
    if(pointer==2):
        k = random.randint(0, 50)
        lan = nd[k % 6]
        if (pre == '2'):
            lan = translator.translate(lan, dest='hi')
            print(lan.text)
            return (lan.text)
        
        if pre == '3':
            lan = translator.translate(lan, dest='mr')
            print(lan.text)
            return (lan.text)
        
        if pre == '1':
            print(nd[k % 6])
            return(nd[k%6])


def askAge(pre,pointer):
    if pointer==3 :
        k = random.randint(0, 50)
        lan = ad[k % 6]
    #print('PLease enter your age - ')

        if pre == '2':
            lan = translator.translate(lan, dest='hi')
            print(lan.text)
            return(lan.text)
        if pre == '3':
            lan = translator.translate(lan, dest='mr')
            print(lan.text)
            return(lan.text)
        if pre == '1':
            print(ad[k % 6])
            return(ad[k % 6])


def getAge(text):
    # text is a sentence(string)
    # expected output: age in number
    filtered = stopWords(text)
    for i in filtered:
        try:
            age = int(i)
        except Exception as e:
            continue
    return age


def askGender(pre):
    if pre == '2':
        lan = translator.translate('Are you a Male or a Female?', dest='hi')
        print(lan.text)
        return(lan.text)
    if pre == '3':
        lan = translator.translate('Are you a Male or a Female?', dest='mr')
        print(lan.text)
        return(lan.text)
    if pre == '1':
        print('Are you a Male or a Female?')
        return('Are you a Male or a Female?')

   

def sorry(pre):
    if pre == '2':
        lan = translator.translate(
            'I\'m sorry I could not understand that. Let\'s try again.', dest='hi')
        print(lan.text)
    if pre == '3':
        lan = translator.translate(
            'I\'m sorry I could not understand that. Let\'s try again.', dest='mr')
        print(lan.text)
    if pre == '1':
        print('I\'m sorry I could not understand that. Let\'s try again.')


def getGender(text):
    # text is a sentence(string)
    # expected output: 'Male' or 'Female'
    filtered = stopWords(text)
    flag = 0
    for i in filtered:
        if i.lower() == 'male' or i.lower() == 'female':
            gender = i
            flag = 1
    if flag != 1:
        return 0
    else:
        return gender


def smokeAndAlc(pre,pointer):

    if pointer==5:
        if pre == '2':
            ans1 = translator.translate('Do you smoke?', dest='hi')
            print(ans1.text)
            return(ans1.text)
        if pre == '3':
            ans1 = translator.translate('Do you smoke?', dest='mr')
            print(ans1.text)
            return(ans1.text)
        if pre == '1':
            print('Do you smoke?')
            return('Do you smoke?')

    if pointer==6:
       
        if pre == '2':
            ans1 = translator.translate('Do you consume alcohol?', dest='hi')
            print(ans1.text)
            return(ans1.text)
        if pre == '3':
            ans1 = translator.translate('Do you consume alcohol?', dest='mr')
            print(ans1.text)
            return(ans1.text)
        if pre == '1':
            print('Do you consume alcohol?')
            return('Do you consume alcohol?')


def extDisease():
    print('Before we ask you your symptoms, we would like to know your health status.')
    print('If yout have any existing Medical Conditions or Problems, please provide them here.')
    print('If you dont, you can reply with a \'no\'')
    inp = input()
    tok = word_tokenize(inp)
    fl = 0
    for i in tok:
        stem = stemming(i)
        for i in tok:
            if 'no' in tok:
                fl = 1
                break
    if fl == 0:
        return inp
    else:
        return 'Nothing Severe'


def getSymptoms(pre,filt):
    

    # compare input with csv file with filtered sentence
    i1 = i2 = i3 = 0
    max1 = 0
    max2 = 1
    max3 = 2
    for i in range(symp.size):
        sequence = difflib.SequenceMatcher(isjunk=None, a=filt, b=symp[i])
        diff = sequence.ratio()*100
        if(diff > max1):
            max3 = max2
            max2 = max1
            max1 = diff
            i1 = i
        elif(diff > max2):
            max3 = max2
            max2 = diff
            i2 = i
        elif(diff > max3):
            max3 = diff
            i3 = i



    if(pre == '2'):
        temp = translator.translate('Diagnosed Diseases are : ', dest='hi')
        print(temp.text)
        if(i1 != i2 != i3):
            print(dis[i1])
            print(dis[i2])
            print(dis[i3])
            return(temp.text + dis[i1] +' '+ dis[i2] +' '+ dis[i3])
        else:
            print(dis[i1])
            return(temp.text + dis[i1])


    if(pre == '3'):
        temp = translator.translate('Diagnosed Diseases are : ', dest='mr')
        print(temp.text)
        if(i1 != i2 != i3):
            print(dis[i1])
            print(dis[i2])
            print(dis[i3])
            return(temp.text + dis[i1] + ' '+ dis[i2] +' '+ dis[i3])
        else:
            print(dis[i1])
            return(temp.text + dis[i1])


    if(pre == '1'):
        print('Diagnosed Diseases are:')
        if(i1 != i2 != i3):
            print(dis[i1])
            print(dis[i2])
            print(dis[i3])
            return('Diagnosed Diseases might be: ' + dis[i1] +' '+ dis[i2] +' '+ dis[i3])
        else:
            print(dis[i1])
            return('Diagnosed Diseases might be: ' + dis[i1])
    


translator = Translator()


def myfunc(inp, pointer):
    global translator
    translator = Translator()
    global pre
    global language
    global opt
    global res1
    global res2
    # Starting the conversation
    if pointer == 0:
        print('Which language would you prefer - 1.English 2.Hindi 3.Marathi')
        return 'Which language would you prefer - 1.English 2.Hindi 3.Marathi'

    if pointer == 1:
        pre = inp
        language = pre
        if pre == '2':
            greet1 = translator.translate(
                'I am Groot, your personal health assistant.', dest='hi')
            print(greet1.text)
            # return greet1.text
            greet2 = translator.translate(
                'I will help you find out about your health.', dest='hi')
            print(greet2.text)
            # return greet2.text
            greet3 = translator.translate(
                'Do you want 1. Medical information or 2. Check your symptoms:', dest='hi')
            print(greet3.text)
            return greet3.text

        elif pre == '3':
            greet1 = translator.translate(
                'I am Groot, your personal health assistant.', dest='mr')
            # print(greet1.text)
            # return greet1.text
            greet2 = translator.translate(
                'I will help you find out about your health.', dest='mr')
            # print(greet2.text)
            # return greet2.text
            greet3 = translator.translate(
                'Do you want 1. Medical information or 2. Check your symptoms:', dest='mr')
            # print(greet3.text)
            return greet3.text

        else:
            print('I\'m Groot, your personal health assistant.')
            print(
                "I can help you find out what is going on with a simple symptom assessment.")
            print('Do you want 1. Medical information or 2. Check your symptoms:')
            return 'Do you want 1. Medical information or 2. Check your symptoms:'

    if pointer == 2:
        imp = inp
        opt = imp
        if pointer == 2:
            if(imp == '1'):
                if(language == '2'):
                    tt = translator.translate(
                        'Name a medical term you need information about - ', dest='hi')
                    print(tt.text)
                    return tt.text

                elif(language == '3'):
                    tt = translator.translate(
                        'What information do you need - ', dest='mr')
                    print(tt.text)
                    return tt.text

                elif(pre == '1'):
                    print('Name a medical term you need information about - ')
                    return 'Name a medical term you need information about - '

            
            ######################################################################################################################
            
            
            elif imp == '2':
            
                if(pointer==2 ):
                    ufName = askName(language,pointer)
                    return ufName


    if pointer==3 and opt == '2':
        ufName = inp
        print('Done taking the name')
        ufAge = askAge(language,pointer)
        return ufAge

    if pointer==4:
        ufAge = inp
        print('Done taking the age')
        ufGender = askGender(language)
        return ufGender

    if pointer==5:
        ufGender=inp
        sa = smokeAndAlc(language,pointer)
        return sa

    if pointer==6:
      
        inp1 = inp
        for i in inp1:
            stem = stemming(i)
            if 'yes' in stem or 'yea' in stem or 'yeah' in stem:
                res1 = 1
        
        sa = smokeAndAlc(language,pointer)
        return sa

    calc = 0

    if pointer==7:
        res2=0
        inp2 = inp
        for i in inp2:
            stem = stemming(i)
            if 'yes' in stem or 'yea' in stem or 'yeah' in stem:
                res2 = 1
            if language=='2':
                greet1 = translator.translate('Okay. Can you please describe your symptoms?', dest='hi')
                print(greet1.text)
                # return greet1.text
                return greet1.text


            if language=='3':
                greet1 = translator.translate('Okay. Can you please describe your symptoms?', dest='mr')
                print(greet1.text)
                # return greet1.text
                return greet1.text

            else:
                return('Okay. Can you please describe your symptoms?')


    #calc = (res1*10)+res2

    if pointer==8:

        filtered = stopWords(inp)
        stemmed = stemming(filtered)
        filt = stopWords(inp)
        Sym = getSymptoms(language,filt)    
        return Sym



            #########################################################################################################################


    if pointer == 3 and opt == '1':
        if(language == '2'):
            inp1 = inp
            text1 = translator.translate(inp1)
            print(text1.text)
            # return text1.text
            final = (translator.translate(wikipedia.summary(
            text1.text, sentences=2), dest='hi'))
            print(final.text)
            return final.text

        elif(language == '3'):
            inp1 = inp
            text1 = translator.translate(inp1)
            print(text1.text)
            final = (translator.translate(wikipedia.summary(
            text1.text, sentences=2), dest='mr'))
            print(final.text)
            return final.text

        elif(pre == '1'):
            inp1 = inp
            print(wikipedia.summary(inp1, sentences=2))
            return wikipedia.summary(inp1, sentences=2)
                
                
                
                
                
