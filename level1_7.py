# Python Task Level, 6 :
# Create a function takes a sentence and a word and prints how many time the word used in the sentence


# get 
my_sentence = input('Please type a Sentence : ')
my_word = input("type a word : ")

# count the word in the sentence
count = 0
for word in my_sentence.split():
    if word == my_word:
        count += 1
        
# output new sentence
print(f'Count is: {count}')

        
        
