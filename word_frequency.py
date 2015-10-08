import re
from collections import Counter

def word_frequency(text):
    """Takes a string, strips it of all whitespace, punctuation and special chars,
    and returns a dictionary with words as the key, and the number of times they
    appear as the value. Uses Counter from collections"""
    stripped_text = re.sub('[^a-zA-Z\ \'\n]+', '', text).lower().split()
    common_words = Counter(stripped_text)
    return common_words

def max_reduced_to_50(count_dict):
    """Takes a dictionary with counts as values, and returns a dict with a max
    key value count of 50, and each count reduced at the same percentage and
    rounded. If the max count < 50, it returns the same dict. It's probably
    needlessly complex, but I'm tired"""
    values_list = []
    multiplier = float()
    for count in count_dict.values():
        values_list.append(count)
    max_count = max(values_list)
    print(max_count * 10)
    if max_count < 51:
        return count_dict
    else:
        multiplier = max_count / 50
        print(multiplier)
        for word in count_dict:
            count_dict[word] = round(count_dict[word] / multiplier)
        return count_dict

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

    #calls max_reduced_to_50 to check if counts should be reduced
    #uses Counter.most_common method to find the 20 most commons words
    most_common = max_reduced_to_50(common_words).most_common(20)

    for word, count in most_common:
        print(word.ljust(15, " "), "#" * count)
