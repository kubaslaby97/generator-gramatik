from nltk.parse.generate import generate, demo_grammar
from nltk import CFG
grammar = CFG.fromstring(demo_grammar)
print(grammar)

for sentence in generate(grammar, n=10):
    print(' '.join(sentence))