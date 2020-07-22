sentence = input("Enter a sentence: ")
result = {}
def counts(cumle):    
    for i in cumle:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result
print(counts(sentence))
