# Python Task Level, 6 :
# Create a function that takes a sentence and word and remove the word from the sentence


# get string
my_sentence = input('Please type a Sentence : ')
my_word = input("type a word to remove from the sentence : ")

# make the sentence without the word
new_sentence = ''
for word in my_sentence.split():
    if word != my_word:
        new_sentence += word + ' ' 
        
# output new sentence
print(f'New Sentence is: {new_sentence[:-1]}')

        
        
