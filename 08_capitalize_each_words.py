def capitalize_words(sentence):
    return ' '.join(word.capitalize() for word in sentence.split(" "))

sentence = "hello world from python"
print("Capitalized sentence:", capitalize_words(sentence))
# Output: "Hello World From Python"

