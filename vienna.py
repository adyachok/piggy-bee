from enchant import Dict


class SearchEngine(object):
    """Class process combination of characters step-by-step and checks is the combination is a word or possible word.
    Possible words are stored in suggested_words set. Possible advices are stored in suggested_advices.
    Algorithm assumes that it is possible to build a word just following from beginning to the end of "polluted" word.
    """

    def __init__(self):
        self.DICT = Dict("en_US")
        self.suggested_advices = set()
        self.suggested_words = set()

    def reset(self):
        self.suggested_advices = set()
        self.suggested_words = set()

    def get_advices(self, variant):
        variant = variant.lower()
        return [adv for adv in self.DICT.suggest(variant) if adv.lower().startswith(variant)]

    def is_variant_word(self, variant):
        return self.DICT.check(variant)

    def get_suggestions(self, poluted_word, variant=None, index=None):
        if not variant:
            start = poluted_word[0]
            for i, ch in enumerate(poluted_word):
                if i == 0:
                    continue
                v = start + ch
                suggested_advices = self.get_advices(v)
                if len(suggested_advices):
                    self.suggested_advices.update(suggested_advices)
                    if self.is_variant_word(v):
                        self.suggested_words.add(v)
                    self.get_suggestions(poluted_word, variant=v, index=i)
        else:
            for j in range(index + 1, len(poluted_word)):
                v = variant + poluted_word[j]
                suggested_advices = self.get_advices(v)
                if len(suggested_advices):
                    self.suggested_advices.update(suggested_advices)
                    if self.is_variant_word(v):
                        self.suggested_words.add(v)
                    self.get_suggestions(poluted_word, variant=v, index=j)

    def get_all_possible_suggestions(self, poluted_word):
        # Exclude 2 last characters from search area
        for i in range(len(poluted_word[:-2])):
            word = poluted_word[i:]
            self.get_suggestions(word)


if __name__ == '__main__':
    se = SearchEngine()
    se.get_all_possible_suggestions('jreghrearhrds')
    print(se.suggested_words)
    print(se.suggested_advices)