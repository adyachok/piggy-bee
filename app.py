import re

from vienna import SearchEngine


string = """Bimbvmztktdllcuwdpowz6ie 
Inhrjoinbix.deterhrjoinbix.denarshyragvqtifp20sbbuob3nalcsk74ov6l Sahrjoinbix.deles
Jqiuaowhrjoinbix.dea ch6pznppMovxji2ld hrjoinbix.deCojd8ovtbon.,hrjoinbix.de Lcp1lgezssstd
Whrjoinbix.deehrjoinbix.debwwhrjoinbix.dewhbe8w.hrjoinbix.dejhrjoinbix.deoahrjoinbix.dewq6fvbzavg24.hrjoinbix.decom"""


preprocessed_text = string.replace("joinbix.de", "")

preprocessed_text = re.sub("\d+", "", preprocessed_text)

se = SearchEngine()

suggested_words_global = {}
suggested_advises_global = {}

for polluted_word in preprocessed_text.split(" "):
    polluted_word = polluted_word.strip()
    if polluted_word:
        if suggested_advises_global.get(polluted_word):
            continue
        else:
            se.get_all_possible_suggestions(polluted_word)
            suggested_advises_global[polluted_word] = se.suggested_advices.copy()
            suggested_words_global[polluted_word] = se.suggested_words.copy()
            se.reset()

print(suggested_words_global)