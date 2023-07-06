# Python Task Level, 5 :
# Create a function that takes a sentence and prints how many words in the sentence (do not count the spaces)


def count_words(sentence):
    # output sentence without a duplicated words
    count_words = 0
    ha = True

    for w in sentence:
        if w != ' ' and ha: # w is a letter not space
            count_words += 1
            ha = False
        elif w == ' ':
            ha = True

    print(f'Count of words is: {count_words}')

        
        
# get string
sentence = input('Please type a Sentence : ')
count_words(sentence)