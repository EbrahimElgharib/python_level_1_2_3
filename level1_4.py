# Python Task Level, 4 :
# Create a function that takes a sentence and prints the sentence without duplicated words


# get string
my_sentence = input('Please type a Sentence : ')

# output sentence without a duplicated words
output_sentence = []

for w in my_sentence:
    if w not in output_sentence:
        output_sentence.append(w)

print('Output is:')
print(''.join(output_sentence))

        
        
