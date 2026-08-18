class WordDictionary:

    def __init__(self):
        self.data = {'_isWord': False}        

    def addWord(self, word: str) -> None:
        it = self.data
        if not word:
            return

        for c in word:
            if c not in it:
                it[c] = {'_isWord': False}

            it = it[c]
        it['_isWord'] = True
        

    def search(self, word: str) -> bool:
        i = 0

        def itsearch(it):
            nonlocal i, word
            if i >= len(word):
                return False
            word_end = (i == len(word) - 1)
        
            if word[i] == '.':
                its = [v for k, v in it.items() if k != '_isWord']

            elif word[i] not in it:
                return False
            else:
                its = [it[word[i]]]

            i = i + 1
            for subit in its:
                if word_end:
                    if subit['_isWord']:
                        return True
                else:
                    if itsearch(subit):
                        return True

            return False

        return itsearch(self.data)

            




