import random
import nltk
from ntlk.corpus import wordnet

nltk.download('wordnet')
nltk.download('punkt')

def synonym_replacement(text):
  words = nltk.word_tokenize(text)
  new_words = words.copy()

for i, word in enumerate(words):
  synonyms = wordnet.synsets(words)
  if synonyms:
    synonym  = random.choice(synonyms).lemmas()[0].name()
    new_words[i]  = synonym if synonym!= word else new_words[i]
return ' '.join(new_words)

text = "The cat sat on the mat"
augmented_text = synonym_replacement(text)
print(augmented_text)
