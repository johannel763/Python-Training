## Asks the user to entr a word

another = 'y' or 'Y'
letter_count = 0 
word_count = 0

while another != '':
    
    word = str(input('Enter another word: '))
    word_count += 1
    letter_count += len(word)
    avg_letters = letter_count / word_count
    another = str(input('Add another word? '))

print('Number of words: ', word_count)
print('Number of letters: ', letter_count)
print('Average lettes per word: ', round(avg_letters))
