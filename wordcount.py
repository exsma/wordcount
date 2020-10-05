# put your code here.
#for key, value in my_dict.items():
#print("key = {}, value = {}".format(key, value))


def word_count(file):
    file = open(file)
    words_list = []
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for line in file:
        line = line.rstrip()
        words = line.split(' ')
        for word in words:
            no_punctuation = ""
            for char in word:
                if char not in punctuation:
                    no_punctuation = no_punctuation + char
            words_list.append(no_punctuation)
    words_dic = make_dic(words_list)
    for key, value in words_dic.items():
        print("{} {}".format(key, value))
    
def make_dic(words):
            checking_words = {}
            for word in words:
                checking_words[word] = checking_words.get(word,0) + 1
            return checking_words

