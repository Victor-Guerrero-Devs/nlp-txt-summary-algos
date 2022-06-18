# freq_based_algo

## about
- most basic of algorithms 
- takes a text 
- counts the frequency of words within said text 
- gives them a score based on their frequency 
- sentences are given a score based on scores 
from the words they contain 
- sentences with the highest score are used 
for the summary


## math
- find the word with the highest frequency 
- give each word a score by dividing their 
frequency number by the highest frequency one 

Example: "artificial" is the highest frequency 
word and shows up 4 times in the text. "brain" 
shows up 3 times in the text. 

3 / 4 = 0.75 

0.75 = the score (or **weight**) of "brain"

1.00 = the score of "artificial"

- now that we have the weight of every word, 
we take each sentence 1 by 1 and add together
the weight (score) of each word they contain 
- the sum is the score of the sentence 

Example: "The brain is artificial" (0.75 + 1 = 1.75)

- the sentences with the highest scores will 
be used for the summary; the rest are discarded. 

