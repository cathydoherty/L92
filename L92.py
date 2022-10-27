#Cathy Doherty
string = 'SPAM!HelloSPAM! worldSPAM!!'
def remove_substring(string, word):
    output = []
    index = 0
    while index < len(string):
        if string[index: index+ len(word)]==word:
            index += len(word)
        else:
            output.append(string[index])
            index+=1
    print("".join(output))
remove_substring(string, "SPAM!")
