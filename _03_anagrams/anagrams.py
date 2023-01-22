"""
Create an anagram game!
"""
import random
import tkinter as tk

# TODO Use this dictionary of anagrams to create an anagrams GUI word game.
#  Look at 'anagrams_game_example.png' in this folder for an example.
word_anagrams = {
    "action": ["cation"],
    "agree": ["eager"],
    "calm": ["clam"],
    "charming": ["marching"],
    "clean": ["lance"],
    "cool": ["loco"],
    "creative": ["reactive"],
    "delight": ["lighted"],
    "earnest": ["eastern", "nearest"],
    "easy": ["ayes", "yeas"],
    "free": ["reef"],
    "great": ["grate"],
    "green": ["genre"],
    "grin": ["ring"],
    "hearty": ["earthy"],
    "idea": ["aide"],
    "ideal": ["ailed"],
    "keen": ["knee"],
    "lively": ["evilly", "vilely"],
    "lovely": ["volley"],
    "merit": ["miter", "remit", "timer"],
    "open": ["nope", "peon", "pone"],
    "prepared": ["dapperer"],
    "quiet": ["quite"],
    "refined": ["definer"],
    "restored": ["resorted", "rostered"],
    "reward": ["drawer", "redraw", "warder", "warred"],
    "rewarding": ["redrawing", "wardering"],
    "right": ["girth"],
    "secure": ["rescue"],
    "simple": ["impels"],
    "smile": ["limes", "miles", "slime"],
    "super": ["puers", "purse"],
    "tops": ["opts", "post", "pots", "spot", "stop"],
    "unreal": ["neural"],
    "wonderful": ["underflow"],
    "zeal": ["laze"]}

class Anagrams(tk.Tk):
    def __init__(self):
        super().__init__()
        self.info = tk.Label(self)
        self.info.place(relx=0, rely=0, relwidth=0.8, relheight=0.2)
        self.new_word = tk.Button(self, text="Get New Word!", command=self.gen_new_word)
        self.new_word.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.2)
        self.gen_new_word()
        self.correct = tk.Label(self)
        self.correct.place(relx=0, rely=0.8, relwidth=1, relheight=0.2)
    def gen_new_word(self):
        self.word = random.choice(list(word_anagrams.keys()))
        self.answers = word_anagrams[self.word]
        self.info.configure(text="Guess the " + str(len(self.answers)) + " anagram(s) for the word: " + self.word)
if __name__ == "__main__":
    app = Anagrams()
    app.title("Anagrams")
    app.geometry("500x250")
    app.mainloop()