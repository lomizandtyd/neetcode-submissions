class PrefixTree:

    def __init__(self):
        self.root = {'isWord': False}

    def insert(self, word: str) -> None:
        if not word:
            return

        n = self.root
        for c in word:
            if c not in n:
                n[c] = {'isWord': False}
            n = n[c]
        n['isWord'] = True

    def search(self, word: str) -> bool:
        n = self.root
        for c in word:
            if c not in n:
                return False
            n = n[c]

        return n['isWord']
        

    def startsWith(self, prefix: str) -> bool:
        n = self.root
        
        for c in prefix:
            if c not in n:
                return False
            n = n[c]

        return n['isWord'] or len(n) > 1