import io
import re
from googletrans import Translator
import PyDictionary
import requests
import json
import apikey
import googletrans


def word_definition(keyword: str):
    Oxford_Api_key = apikey.Oxford_API_Key
    Oxford_API_Id = apikey.Oxfors_API_id
    app_key = Oxford_Api_key
    app_id = Oxford_API_Id
    language = 'en'
    word_id = f'{keyword}'
    fields = 'definitions'
    strictMatch = 'false'
    url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word_id.lower() + '?fields=' + fields + '&strictMatch=' "false"

    r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
    response = json.loads(r.text)

    try:
        try:
            def_list = []
            pos_list = []
            for x in response['results'][0]['lexicalEntries']:
                defi = x['entries'][0]['senses'][0]['definitions'][0]
                lexipos = x['lexicalCategory']['text']

                # pints out allthe definitions in order
                def_list.append(defi)
                # print(lexipos)#prints  out the poss in a relative order as  the definitions
                pos_list.append(lexipos)
            return [def_list[0:], pos_list[0:]]  # returns the defintion lists  and  poslist  accordingly
        except Exception  as e:
            return e
    except:
        try:
            definition = PyDictionary.PyDictionary.meaning(keyword)
            return definition
        except:
            return "This  word can not be found in dictionary"


def Pronunciation(keyword):
    try:
        Oxford_Api_key = apikey.Oxford_API_Key
        Oxford_API_Id = apikey.Oxfors_API_id

        app_key = Oxford_Api_key
        app_id = Oxford_API_Id
        language = 'en'
        word_id = f'{keyword}'
        fields = 'pronunciations'
        strictMatch = 'false'
        url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word_id.lower() + '?fields=' + fields + '&strictMatch=' "false"

        r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
        response = json.loads(r.text)
        word_id = response['results'][0]['id']
        lang = response['results'][0]['language']
        phonetic_notation_li = []
        dialectsssss = []
        phoneticSpelling = []
        pronunciation_file_list = []
        for x in response['results'][0]['lexicalEntries']:
            Pronunciation_file = x['entries'][0]['pronunciations'][0]['audioFile']
            phonetic_natation_address = x['entries'][0]['pronunciations'][0]['phoneticNotation']
            phonetic_spelling_address = x['entries'][0]['pronunciations'][0]['phoneticSpelling']
            dialects = x['entries'][0]['pronunciations'][0]['dialects']
            pronunciation_file_list.append(Pronunciation_file)
            phonetic_notation_li.append(phonetic_natation_address)
            phoneticSpelling.append(phonetic_spelling_address)
            dialectsssss.append(dialects)
        return [phonetic_notation_li[0], dialectsssss[0][0], phoneticSpelling[0], pronunciation_file_list[0]]
    except:
        return '{"Message"}: {"No word was found  matching your keyword\n-----------------------------------------------------------Please try again.Make  sure to spell all words correctly"} {keyword}'


def synonym(keyword):
    """This function will return the synonyms of a given word """
    try:
        Oxford_Api_key = apikey.Oxford_API_Key
        Oxford_API_Id = apikey.Oxfors_API_id

        app_key = Oxford_Api_key
        app_id = Oxford_API_Id
        language = 'en'
        word_id = f'{keyword}'
        fields = 'synonyms'
        strictMatch = 'false'
        url = 'https://od-api.oxforddictionaries.com/api/v2/thesaurus/' + language + '/' + word_id.lower() + '?fields=' + fields + '&strictMatch=' "false"
        r = requests.get(url, headers={"Accept": "application/json", 'app_id': app_id, 'app_key': app_key})
        print(r.text)
        response = json.loads(r.text)
        return response
    except:
        try:
            synonyms_of_keyword = PyDictionary.PyDictionary.synonym(f'{keyword}')
            return synonyms_of_keyword[:(len(synonyms_of_keyword))]
        except:
            pass


def antonym(keyword):
    try:
        Antonym = PyDictionary.PyDictionary.antonym(f'{keyword}')
        return Antonym
    except  Exception  as  e:
        print(e)
        return None


def Translate(keyword, target_lang):
    translate = googletrans.Translator(service_urls=[translate.googleapis.com])
    translated_word = translate.translate(text=keyword, dest=target_lang)
    return translated_word.text
    # simple_translate



def Language_detect(keytext):
    try:
        lang_detect = googletrans.Translator()
        lang_detect_2 = lang_detect.detect(text=keytext)
        return [lang_detect_2.lang, lang_detect_2.confidence]
    except:
        return   None
