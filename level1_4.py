# Python Task Level, 4 :
# Create a function that takes a sentence and prints the sentence without duplicated words


# my Function
def del_duplicates(sentence):
    # output sentence without a duplicated words
    result = ''
    for s in range(len(sentence)-1):
        # check if 2 word not duplicated
        # use the first word
        if sentence[s] != sentence[s+1]:
            result += sentence[s]

    result += sentence[-1]
    print(result)
    

# get string
sentence = input('Please type a Sentence : ')
del_duplicates(sentence)

        
        
