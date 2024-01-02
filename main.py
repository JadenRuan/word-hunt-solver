import json
import copy
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word) -> None:
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.end_of_word = True

    def search(self, word) -> bool:
        cur = self.root

        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.end_of_word
    
    def starts_with(self, prefix) -> bool:
        cur = self.root

        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True

f = open("words_dictionary.json")

all_english_words = json.load(f)
solutions = []
words = Trie()

for key in all_english_words: # Adds all valid english words to trie
    words.insert(key)


letters = input("Input board: ")
board = [letters[0:4], letters[4:8], letters[8:12], letters[12:16]]
directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]
visited_init = [[False, False, False, False], [False, False, False, False], [False, False, False, False], [False, False, False, False]]
def check(row, col, currWord, visited):
    visited_copy = copy.deepcopy(visited)
    if row < 0 or row > 3 or col < 0 or col > 3:
       return
    if visited_copy[row][col]:
       return
    visited_copy[row][col] = True
    currWord += board[row][col]

    if not(words.starts_with(currWord)): # If currWord is not a prefix exit out
        return 
    if words.search(currWord) and len(currWord) >= 3 and not(currWord in solutions):
        solutions.append(currWord)
    for direction in directions:
        check(row + direction[0], col + direction[1], currWord, visited_copy)
    return 0

for r in range(4):
    for c in range(4):
        check(r, c, '', visited_init)
solutions.sort(key=len)
print(solutions)
