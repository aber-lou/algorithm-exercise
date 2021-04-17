class Trie {
private:
    vector<Trie*> children;
    bool isWord;

    Trie* searchPrefix(string prefix) {
        Trie *node = this;
        for(char ch: prefix){
            ch -= 'a';
            if(node->children[ch] == nullptr) {
                return nullptr;
            }
            node = node->children[ch];
        }
        return node;
    }

public:
    Trie() : children(26), isWord(false) {}

    void insert(string word) {
        Trie *node = this;
        for(char ch : word){
            ch -= 'a';
            if(node->children[ch] == nullptr) {
                node->children[ch] = new Trie();
            }
            node = node->children[ch];
        }
        node->isWord = true;
    }

    bool search(string word) {
        Trie *node = this->searchPrefix(word);
        return node != nullptr && node->isWord;
    }

    bool startsWith(string prefix) {
        return this->searchPrefix(prefix) != nullptr;
    }
};