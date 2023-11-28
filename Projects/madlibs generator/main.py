import os

with open("Projects\madlibs generator\story.txt", "r" ) as f: # 'r' = read mode, 'w' = write 'a' = add
    story = f.read() # we are storing that content in var 'story'

os.system("cls")
words = set() # to store all of the words
start_of_word = -1 # when its == to -1, it means we havent yet found anyword, when its == to anything else we have found a word.

target_start = "<"
target_end = ">"

for i, char in enumerate(story): # enumerate give us access to the position as well as the elemeent at that position
    if char == target_start:
        start_of_word = i
    if char == target_end and target_start != -1:
        word = story[start_of_word: i + 1] # we use the slice method to give us the word we are looking for.
        words.add(word) # we add that to our word list
        start_of_word = -1 # it == -1 because we need to reset it, for the another word.

answers = {}

for word in words: # it loops thru our set and allows usr to enter their words and then it adds it to our dict 'answers'
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)