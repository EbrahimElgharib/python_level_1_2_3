# Python Task Level, 4 :
# Create a function that takes a sentence and prints the sentence without duplicated words


# Func for letters
def del_consecutive_letters(sentence):
    # output sentence without a duplicated words
    result = ''
    for s in range(len(sentence)-1):
        # check if 2 word not duplicated
        # use the first word
        if sentence[s] != sentence[s+1]:
            result += sentence[s]

    result += sentence[-1]
    print(result)
    
# Func for words
def del_consecutive_words(sentence):
    words_list = sentence.split(' ')
    no_duplicated_words = []
    
    for word in words_list:
        if word not in duplicated_words:
            duplicated_words.append(word)
        
    print(' '.join(no_duplicated_words))
    

# get string
sentence = input('Please type a Sentence : ')

# del_consecutive_letters(sentence)
del_consecutive_words(sentence)


        
        
