import re  # regular expression
import nltk
import string

original_text = """On 13 March 1815, six days before Napoleon reached Paris, the powers at the Congress of Vienna declared him an outlaw. Four days later, the United Kingdom, Russia, Austria, and Prussia mobilised armies to defeat Napoleon. Critically outnumbered, Napoleon knew that once his attempts at dissuading one or more members of the Seventh Coalition from invading France had failed, his only chance of remaining in power was to attack before the coalition mobilised.
Had Napoleon succeeded in destroying the existing coalition forces south of Brussels before they were reinforced, he might have been able to drive the British back to the sea and knock the Prussians out of the war. Crucially, this would have bought him time to recruit and train more men before turning his armies against the Austrians and Russians.
An additional consideration for Napoleon was that a French victory might cause French-speaking sympathisers in Belgium to launch a friendly revolution. Also, coalition troops in Belgium were largely second-line, as many units were of dubious quality and loyalty, and most of the British veterans of the Peninsular War had been sent to North America to fight in the War of 1812.
The initial dispositions of Wellington, the British commander, were intended to counter the threat of Napoleon enveloping the Coalition armies by moving through Mons to the south-west of Brussels. This would have pushed Wellington closer to the Prussian forces, led by Gebhard Leberecht von Blücher, but might have cut Wellington's communications with his base at Ostend. In order to delay Wellington's deployment, Napoleon spread false intelligence which suggested that Wellington's supply chain from the channel ports would be cut."""

# 1. PREPROCESSING THE TEXT

# replace line breaks w/ one space by using regular expression
original_text = re.sub(r'\s+', ' ', original_text)

# allows us to use methods like nltk.word_tokenize()
nltk.download('punkt')
# inconsequential words like "the, a, an, and, for" etc to remove from text
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')


# function to clean up the text
def preprocess(text):
    # a. make all the words lowercase
    formatted_text = text.lower()

    # b. place all the words individually into the list
    tokens = []
    for token in nltk.word_tokenize(formatted_text):
        tokens.append(token)

    # c. remove stop words and punctuation marks from the tokens list
    tokens = [word for word in tokens if word not in stopwords and word not in string.punctuation]

    # d. bring in the elements from the tokens list as a string
    formatted_text = ' '.join(element for element in tokens)

    return formatted_text


formatted_text = preprocess(original_text)

# 2. WORD FREQUENCY

# each word in formatted text is now given a frequency value and stored in the dictionary called word_frequency
word_frequency = nltk.FreqDist(nltk.word_tokenize(formatted_text))

# store the word with the highest frequency
highest_frequency = max(word_frequency.values())

# calculate the weight of each word in the previous dictionary
for word in word_frequency.keys():
    word_frequency[word] = (word_frequency[word] / highest_frequency)


# 3. SENTENCE TOKENIZATION


