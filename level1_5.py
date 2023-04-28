# Python Task Level, 4 :
# Create a function that takes a sentence and prints the sentence without duplicated words


# get string
my_sentence = input('Please type a Sentence : ')

# output sentence without a duplicated words
count_words = 0
ha = True

for w in my_sentence:
    if w != ' ' and ha: # w is a letter not space
        count_words += 1
        ha = False
    elif w == ' ':
        ha = True

print(f'Count of words is: {count_words}')

        
        
