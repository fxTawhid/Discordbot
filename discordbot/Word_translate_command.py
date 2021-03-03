@client.command()
async  def word_translate(ctx,word,*,dest):
    """This command will  translate a given word into the provided destination language
    **Note that here destination language should be provided in ISO 639-1 language codes or ISO language names or upper or
    lowercase of that language name**.Be careful to spell the  name of the language correctly.
    **The full list of ISO 639-1 language codes and names can be found here:
    https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes """
    if len(dest)==2:
        try:
            kl=Dictionay_py.Translate(keyword=word,target_lang=dest)
            await ctx.send(kl)

        except Exception as e:
            print(f'Dear dev,\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n {ctx.author} has used destination language {dest} and keyword{word} which created a problem/error while translating')
            def check_if_target_destination_lang_exists(lang):
                """Checks out if the target language is supported ,if the lang is supported, then:
                ->check_if_target_destination_lang_exists(lang=zh-tw)
                True
                ->check_if_target_destination_lang_exists(lang=hkn)
                False
                """
                if lang  in  li:
                    return  True
                else:
                    return False

            def Check_if_word_exists(keyword):
                t=Dictionay_py.Language_detect(keytext=keyword)
                if  type(t)==list:
                    return  True
                elif type(t)==None:
                    return  False
                else:
                    return False

    elif  len(dest) >2:
        try:
            if dest == "Afrikaans" or "Afrikaans".lower() or "Afrikaans".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="af")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Albanian" or "Albanian".lower() or "Albanian".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="sq")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Amharic" or "Amharic".lower() or "Amharic".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="am")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')#\
            elif dest == "Arabic" or "Arabic".lower() or "Arabic".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="ar")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Armenian" or "Armenian".lower() or "Armenian".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="hy")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Azerbaijani" or "Azerbaijani".lower() or "Azerbaijani".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="az")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Basque" or "Basque".lower() or "Basque".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="eu")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Belarusian" or "Belarusian".lower() or "Belarusian".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="be")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Bosnian" or "Bosnian".lower() or "Bosnian".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="bs")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Bengali" or "Bengali".lower() or "Bengali".upper()  or  "Bangla"or  "bangla".lower()  or  "Bangla".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="bn")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Bulgarian" or "Bulgarian".lower() or "Bulgarian".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="bg")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Catalan" or "Catalan".lower() or "Catalan".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="ca")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Cebuano" or "Cebuano".lower() or "Cebuano".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="ceb")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Chichewa" or "Chichewa".lower() or "Chichewa".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="ny")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Chinese(Simplified)" or "Chinese(Simplified)".lower() or "Chinese(Simplified)".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="zh-cn")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Chinese(Traditional)" or "Chinese(Traditional)".lower() or "Chinese(Traditional)".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="zh-tw")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Corsican" or "Corsican".lower() or "Corsican".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="co")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Croatian" or "Croatian".lower() or "Croatian".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="hr")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Czech" or "Czech".lower() or "Czech".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="cs")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Danish" or "Danish".lower() or "Danish".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="da")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Dutch" or "Dutch".lower() or "Dutch".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="nl")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "English" or "English".lower() or "English".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="en")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}, and it is  already translated by you :D')
            elif dest == "Esperanto" or "Esperanto".lower() or "Esperanto".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="eo")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Estonian" or "Estonian".lower() or "Estonian".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="et")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Filipino" or "Filipino".lower() or "Filipino".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="tl")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Finnish" or "Finnish".lower() or "Finnish".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="fi")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "French" or "French".lower() or "French".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="fr")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Frisian" or "Frisian".lower() or "Frisian".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="fy")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Galician" or "Galician".lower() or "Galician".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="gl")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Georgian" or "Georgian".lower() or "Georgian".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="ka")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "German" or "German".lower() or "German".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="ge")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Greek" or "Greek".lower() or "Greek".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="el")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Gujarati" or "Gujarati".lower() or "Gujarati".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="gu")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Haitian Creole" or "Haitian Creole".lower() or "Haitian Creole".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="ht")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Hausa" or "Hausa".lower() or "Hausa".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="ha")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Afrikaans" or "Afrikaans".lower() or "Afrikaans".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="af")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Hawaiian" or "Hawaiian".lower() or "Hawaiian".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="haw")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Hebrew" or "Hebrew".lower() or "Hebrew".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="he")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Hindi" or "Hindi".lower() or "Hindi".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="hi")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Hmong" or "Hmong".lower() or "Hmong".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="hmn")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Hungarian" or "Hungarian".lower() or "Hungarian".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="hu")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Icelandic" or "Icelandic".lower() or "Icelandic".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="is")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Igbo" or "Igbo".lower() or "Igbo".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="ig")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Indonesian" or "Indonesian".lower() or "Indonesian".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="id")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Irish" or "Irish".lower() or "Irish".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="ga")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Italian" or "Italian".lower() or "Italian".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="it")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Japanese" or "Japanese".lower() or "Japanese".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="ja")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Javanese" or "Javanese".lower() or "Javanese".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="jw")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Kannada" or "Kannada".lower() or "Kannada".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="kn")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Kazakh" or "Kazakh".lower() or "Kazakh".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="kk")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Khmer" or "Khmer".lower() or "Khmer".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="km")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Korean" or "Korean".lower() or "Korean".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="ko")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Kurdish" or "Kurdish".lower() or "Kurdish".upper()  or "Kurmanji"  or "Kurmanji".upper() or "Kurmanji".lower():
                tr = Dictionay_py.Translate(keyword=word, target_lang="ku")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Kyrgyz" or "Kyrgyz".lower() or "Kyrgyz".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="ky")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Lao" or "Lao".lower() or "Lao".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="lo")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Latin" or "Latin".lower() or "Latin".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="la")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Latvian" or "Latvian".lower() or "Latvian".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="lv")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Lithuanian" or "Lithuanian".lower() or "Lithuanian".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="lt")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Luxembourgish'" or "Luxembourgish".lower() or "Luxembourgish".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="lb")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Macedonian" or "Macedonian".lower() or "Macedonian".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="mk")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Malagasy" or "Malagasy".lower() or "Malagasy".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="mg")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Malay" or "Malay".lower() or "Malay".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="ms")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Malayalam" or "Malayalam".lower() or "Malayalam".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="ml")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Maltese" or "Maltese".lower() or "maltese".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="mt")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Maori" or "Maori".lower() or "Maori".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="mi")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Marathi" or "Marathi".lower() or "Marathi".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="mr")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Mongolian" or "Mongolian".lower() or "Mongolian".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="mn")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Burmese" or "Burmese".lower() or "Burmese".upper() or "Myanmar" or "Myanmar".upper() or "Myanmar".lower():
                tr = Dictionay_py.Translate(keyword=word, target_lang="my")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Nepali" or "Nepali".lower() or "Nepali".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="ne")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Norwegian" or "Norwegian".lower() or "Norwegian".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="no")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Odia" or "Odia".lower() or "Odia".upper() or "Oriya" or "Oriya".upper() or "Oriya".lower():
                tr = Dictionay_py.Translate(keyword=word, target_lang="or")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Pashto" or "Pashto".lower() or "Pashto".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="ps")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Persian" or "Persian".lower() or "Persian".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="fa")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Polish" or "Polish".lower() or "Polish".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="pl")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Portuguese" or "Portuguese".lower() or "Portuguese".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="pt")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Punjabi" or "Punjabi".lower() or "Punjabi".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="pa")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Romanian" or "Romanian".lower() or "Romanian".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="ro")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Russian" or "Russian".lower() or "Russian".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="ru")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Samoan" or "Samoan".lower() or "Samoan".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="sm")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Scots Gaelic" or "Scots Gaelic".lower() or "Scots Gaelic".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="gd")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Serbian" or "Serbian".lower() or "Serbian".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="sr")
                await ctx.send(f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Serbian" or "Serbian".lower() or "Serbian".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="sr")
                await ctx.send(
                    f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Sesotho" or "Sesotho".lower() or "Sesotho".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="st")
                await ctx.send(
                    f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Shona" or "Shona".lower() or "Shona".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="sn")
                await ctx.send(
                    f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Sindhi" or "Sindhi".lower() or "Sindhi".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="sd")
                await ctx.send(
                    f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Sinhala" or "Sinhala".lower() or "Sinhala".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="si")
                await ctx.send(
                    f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Slovak" or "Slovak".lower() or "Slovak".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="sk")
                await ctx.send(
                    f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Slovenian" or "Slovenian".lower() or "Slovenian".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="sl")
                await ctx.send(
                    f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Somali" or "Somali".lower() or "Somali".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="so")
                await ctx.send(
                    f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Spanish" or "Spanish".lower() or "Spanish".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="es")
                await ctx.send(
                    f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Sundanese" or "Sundanese".lower() or "Sundanese".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="su")
                await ctx.send(
                    f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Swahili" or "Swahili".lower() or "Swahili".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="sw")
                await ctx.send(
                    f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Swedish" or "Swedish".lower() or "Swedish".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="sv")
                await ctx.send(
                    f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Tajik" or "Tajik".lower() or "Tajik".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="tg")
                await ctx.send(
                    f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Tamil" or "Tamil".lower() or "Tamil".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="ta")
                await ctx.send(
                    f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Telugu" or "Telugu".lower() or "Telugu".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="te")
                await ctx.send(
                    f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Thai" or "Thai".lower() or "Thai".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="th")
                await ctx.send(
                    f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Turkish" or "Turkish".lower() or "Turkish".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="tr")
                await ctx.send(
                    f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Ukrainian" or "Ukrainian".lower() or "Ukrainian".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="uk")
                await ctx.send(
                    f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Urdu" or "Urdu".lower() or "Urdu".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="ur")
                await ctx.send(
                    f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Uyghur" or "Uyghur".lower() or "Uyghur".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="ug")
                await ctx.send(
                    f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Uzbek" or "Uzbek".lower() or "Uzbek".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="uz")
                await ctx.send(
                    f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Vietnamese" or "Vietnamese".lower() or "Vietnamese".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="vi")
                await ctx.send(
                    f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Welsh" or "Welsh".lower() or "Welsh".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="cy")
                await ctx.send(
                    f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Xhosa" or "Xhosa".lower() or "Xhosa".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="xh")
                await ctx.send(
                    f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Yiddish" or "Yiddish".lower() or "Yiddish".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="yi")
                await ctx.send(
                    f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Yoruba" or "Yoruba".lower() or "Yoruba".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="yo")
                await ctx.send(
                    f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')
            elif dest == "Zulu" or "Zulu".lower() or "Zulu".upper():
                tr = Dictionay_py.Translate(keyword=word, target_lang="zu")
                await ctx.send(
                    f'Dear {ctx.author.mention} the translation for your query word {word} into {dest} is {tr}')

        except:
            em=discord.Embed(title="Sorry",description=f'```bash\nDear {ctx.author.mention} , please check that the spelling of your word is correct and the language destination you have chosen is correct and try   again.```')
