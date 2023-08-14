from googletrans import Translator
from zen_python import string_zen

translator = Translator()


result = translator.translate(string_zen, dest="ru")
print(result.text)
