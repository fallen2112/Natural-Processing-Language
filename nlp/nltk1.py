#tokenizing


from nltk import sent_tokenize,word_tokenize
example_text ="Hello Mr. Smith,How Are You.I m fine."
print(sent_tokenize(example_text))
print(word_tokenize(example_text))