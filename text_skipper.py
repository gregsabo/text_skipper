import re, string, random

big_string = open("sources/self_help.txt", "r").read()

# title_trans=''.join(chr(c) if chr(c).isupper() or chr(c).islower() or chr(c) == "'" else ' ' for c in range(256))
# print "removing non letters"
# big_string = big_string.translate(title_trans)

words = big_string.rsplit()
# words = nltk.word_tokenize(big_string)

#open("analyze_random.txt", "w").write("".join(out_words))

CHAIN_LENGTH = 2

lexicon = {}
for i, word in enumerate(words):
    if i+CHAIN_LENGTH >= len(words):
        break
    word_pair = []
    for j in range(0, CHAIN_LENGTH):
        word_pair.append(words[i+j])
    word_pair = tuple(word_pair)
    if word_pair not in lexicon:
        lexicon[word_pair] = []
    lexicon[word_pair].append(words[i+CHAIN_LENGTH])

total = 0
for key, value in lexicon.items():
    total += len(value)

output = words[0:CHAIN_LENGTH]
current_pair = tuple(output)
for i in range(0, 2000):
    chosen = random.choice(lexicon[current_pair])
    
    current_pair = list(current_pair)[1:]
    current_pair.append(chosen)
    current_pair = tuple(current_pair)
    
    if chosen.endswith('.'):
        chosen += '\n'
    output.append(chosen)

print "\n=======================================\n"
print " ".join(output)
print "\n=======================================\n"
print "AVERAGE LENGTH:", float(total)/len(lexicon)
