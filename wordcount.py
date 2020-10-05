# put your code here.
#for key, value in my_dict.items():
#print("key = {}, value = {}".format(key, value))



def word_count(file):
    file = open(file)
    words_list = []
    for line in file:
        line = line.rstrip()
        words = line.split(' ')
        for word in words:
            words_list.append(word)
    words_dic = make_dic(words_list)
    for key, value in words_dic.items():
        print("{} {}".format(key, value))
    
def make_dic(words):
            checking_words = {}
            for word in words:
                checking_words[word] = checking_words.get(word,0) + 1
            return checking_words

