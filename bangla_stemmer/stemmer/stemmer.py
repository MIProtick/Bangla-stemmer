from os.path import dirname, abspath
from typing import Dict, List
import re

from ..resources import grammar

# d = dirname(dirname(abspath(__file__)))

class BanglaStemmer:

    first_dict: Dict[str,List[str]]
    second_dict: Dict[str,List[str]]
    third_dict: Dict[str,List[str]]
    fourth_dict: Dict[str,List[str]]

    def __init__(self):
        self.grammarParser()

    def grammarParser(self):
        self.first_dict = grammar.sp_initial_dict
        self.second_dict = grammar.con_rep_dict
        self.third_dict = grammar.obv_rep_dict
        self.fourth_dict = grammar.sp_final_dict

    def checklen(self, word):
        skip_wrd = ['া', 'ি', 'ী', 'ু', 'ূ', 'ৃ', 'ে', 'ৈ', 'ো', 'ৌ']
        len = 0
        for ltr in word:
            if ltr in skip_wrd:
                pass
            else:
                len += 1
        return len

    def dot_replace(self, word, initial_index, rplc):
        wrd = word[0:initial_index]
        for i in range(len(rplc)):
            if rplc[i] == '.':
                wrd += word[initial_index + i]
            else:
                wrd += rplc[i]
        return wrd

    def dirrect_replace(self, word, initial_index, rplc):
        wrd = word[0:initial_index]
        wrd += rplc
        return wrd

    def apply_frth_rule(self, word):
        grep = word
        for rules in self.fourth_dict:
            result = re.search(rules, word)
            if result:
                print('applied fourth rules..')
                initial_index = result.span()[0]
                final_index = result.span()[1]
                wordlen = len(word)
                if final_index == wordlen:
                    rigid_wordlen = self.checklen(grep[0:initial_index])
                    if rigid_wordlen > 1:
                        rplc = self.fourth_dict[rules][1]
                        if '.' in rplc:
                            grep = self.dot_replace(word, initial_index, rplc)
                        else:
                            grep = self.dirrect_replace(word, initial_index, rplc)
                    elif rigid_wordlen == 1:
                        rplc = self.fourth_dict[rules][0]
                        if '.' in rplc:
                            grep = self.dot_replace(word, initial_index, rplc)
                        else:
                            grep = self.dirrect_replace(word, initial_index, rplc)
                    else:
                        pass
                else:
                    pass
                break
            else:
                pass
        return grep

    def apply_thrd_rule(self, word):
        grep = word
        for rules in self.third_dict:
            result = re.search(rules, word)
            if result:
                print('applied third rules..')
                initial_index = result.span()[0]
                final_index = result.span()[1]
                wordlen = len(word)
                if final_index == wordlen:
                    rigid_wordlen = self.checklen(grep[0:initial_index])
                    if rigid_wordlen > 1:
                        rplc = self.third_dict[rules][1]
                        if '.' in rplc:
                            grep = self.dot_replace(word, initial_index, rplc)
                        else:
                            grep = self.dirrect_replace(word, initial_index, rplc)
                    elif rigid_wordlen == 1:
                        rplc = self.third_dict[rules][0]
                        if '.' in rplc:
                            grep = self.dot_replace(word, initial_index, rplc)
                        else:
                            grep = self.dirrect_replace(word, initial_index, rplc)
                    else:
                        pass
                else:
                    pass
                break
            else:
                pass
        grep = self.apply_frth_rule(grep)
        return grep

    def apply_scnd_rule(self, word):
        grep = word
        for rules in self.second_dict:
            result = re.search(rules, word)
            if result:
                print('applied second rules..')
                initial_index = result.span()[0]
                final_index = result.span()[1]
                wordlen = len(word)
                if final_index == wordlen:
                    rigid_wordlen = self.checklen(grep[0:initial_index])
                    if rigid_wordlen > 1:
                        rplc = self.second_dict[rules][1]
                        if '.' in rplc:
                            grep = self.dot_replace(word, initial_index, rplc)
                        else:
                            grep = self.dirrect_replace(word, initial_index, rplc)
                    elif rigid_wordlen == 1:
                        rplc = self.second_dict[rules][0]
                        if '.' in rplc:
                            grep = self.dot_replace(word, initial_index, rplc)
                        else:
                            grep = self.dirrect_replace(word, initial_index, rplc)
                    else:
                        pass
                else:
                    pass
                break
            else:
                pass
        grep = self.apply_thrd_rule(grep)
        return grep

    def apply_frst_rule(self, word):
        grep = word
        for rules in self.first_dict:
            result = re.search(rules, word)
            if result:
                print('applied first rules..')
                initial_index = result.span()[0]
                final_index = result.span()[1]
                wordlen = len(word)
                if final_index == wordlen:
                    rigid_wordlen = self.checklen(grep[0:initial_index])
                    if rigid_wordlen > 1:
                        rplc = self.first_dict[rules][1]
                        if '.' in rplc:
                            grep = self.dot_replace(word, initial_index, rplc)
                        else:
                            grep = self.dirrect_replace(word, initial_index, rplc)
                    elif rigid_wordlen == 1:
                        rplc = self.first_dict[rules][0]
                        if '.' in rplc:
                            grep = self.dot_replace(word, initial_index, rplc)
                        else:
                            grep = self.dirrect_replace(word, initial_index, rplc)
                    else:
                        pass
                else:
                    pass
                break
            else:
                pass
        grep = self.apply_scnd_rule(grep)
        return grep

    def stem(self, wordarg):
        stemlist = []
        stemword = ''
        if isinstance(wordarg, list):
            for word in wordarg:
                stemlist.append(self.apply_frst_rule(word))
            return stemlist
        elif isinstance(wordarg, str):
            stemword = self.apply_frst_rule(wordarg)
            return stemword
        
