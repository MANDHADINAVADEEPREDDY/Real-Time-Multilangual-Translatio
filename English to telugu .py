from translate import Translator
translator= Translator(from_lang="english",to_lang="telugu")
translation = translator.translate("Goodmorning")
print (translation)