import re
from collections import Counter

def word_frequency(text):
    """Takes a string, strips it of all whitespace, punctuation and special chars,
    and returns a dictionary with words as the key, and the number of times they
    appear as the value. Uses Counter from collections"""
    stripped_text = re.sub('[^a-zA-Z\ \'\n]+', '', text).lower().split()
    common_words = Counter(stripped_text)
    return common_words


if __name__ == '__main__':
    ignore_words_list = "a,able,about,across,after,all,almost,also,am,among,an,"\
    "and,any,are,as,at,be,because,been,but,by,can,cannot,could,dear,did,do,"\
    "does,either,else,ever,every,for,from,get,got,had,has,have,he,her,hers,him,"\
    "his,how,however,i,if,in,into,is,it,its,just,least,let,like,likely,may,me,"\
    "might,most,must,my,neither,no,nor,not,of,off,often,on,only,or,other,our,own,"\
    "rather,said,say,says,she,should,since,so,some,than,that,the,their,them,then,"\
    "there,these,they,this,tis,to,too,twas,us,wants,was,we,were,what,when,where,"\
    "which,while,who,whom,why,will,with,would,yet,you,your".split(',')

    #read in file to process and count words using word_frequency
    with open("sample.txt") as sample:
        text = sample.read()
        common_words = word_frequency(text)

    #remove words from common_words dict that are in ignore_words_list
    for word in ignore_words_list:
        del common_words[word]

    #uses Counter.most_common method to find the 20 most commons words
    most_common = common_words.most_common(20)

    for count, word in most_common:
        print(word, count)
