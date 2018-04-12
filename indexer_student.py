# -*- coding: utf-8 -*-
"""
Created on Sat Jul  5 11:38:58 2014

@author: zzhang

Modified: Kate Pellegrino
Partner: Zane Fadul

Date: 23 March 2018

"""
import pickle


class Index:
    def __init__(self, name):
        self.name = name
        self.msgs = []
        self.index = {}
        self.total_msgs = 0
        self.total_words = 0

    def get_total_words(self):
        return self.total_words

    def get_msg_size(self):
        return self.total_msgs

    def get_msg(self, n):
        return self.msgs[n]

    # append string m to self.msgs and increment self.total_msgs
    def add_msg(self, m):
        self.msgs.append(m)
        self.total_msgs += 1

    def add_msg_and_index(self, m):
        self.add_msg(m)
        line_at = self.total_msgs - 1
        self.indexing(m, line_at)

    # implement
    # split a string m (loacted at line numbe I) into individual words and then
    #   updates dictionary self.index which is a mapping from words to their
    #   frequencies.
    def indexing(self, m, l):
        temp_l = m.split(" ")
        # self.total_words += len(temp_l)
        for word in temp_l:
            if word in self.index.keys():
                self.index[word].append(l)  
            else:
                self.index[word] =  [l]

    # implement: query interface
    # search(term) - returns a list of tuples which specify each line number
    #   (and line) in which term appears.


    '''
    return a list of tupple. if index the first sonnet (p1.txt), then
    call this function with term 'thy' will return the following:
    [(7, " Feed'st thy light's flame with self-substantial fuel,"),
    (9, ' Thy self thy foe, to thy sweet self too cruel:'),
    (9, ' Thy self thy foe, to thy sweet self too cruel:'),
    (12, ' Within thine own bud buriest thy content,')]

    '''

    def search(self, term):
        msgs = []
        for word in self.index.keys():
            # indices = self.index[term]
            # msgs = [(i, self.msgs[i]) for i in indices]
            if term == word:
                for element in self.index[word]:
                    msgs.append((element, self.msgs[element].rstrip()))
        return msgs


class PIndex(Index):
    def __init__(self, name):
        super().__init__(name)
        roman_int_f = open('roman.txt.pk', 'rb')
        self.int2roman = pickle.load(roman_int_f)
        roman_int_f.close()
        self.load_poems()

        # implement: 1) open the file for read, then call
        # the base class's add_msg_and_index
    def load_poems(self):
        f = open('AllSonnets.txt', 'r')
        for line in f:
            self.add_msg_and_index(line) 
        f.close()
        """ lines = open(self.name, 'r').readlines()
            for l in lines:
                self.add_msg_and_index(l.rstrip())"""
        return

        # implement: p is an integer, get_poem(1) returns a list,
        # each item is one line of the 1st sonnet
    def get_poem(self, p):
        """ p_str = self.int2roman[p] + '.'
            p_next_str = self.int2roman[p+1]
            [(go_line, m)] = self.search(p_str)
            poem = []
            end = self.get_msg_size()
            while go_line < end:
                this_line = self.get_msg(go_line)
                if this_line == p_next_str:
                    break
                poem.append(this_line)
                go_line += 1
            return poem """
        poem = []
        num = self.int2roman[p]
        num = num + '.'
        line = self.search(num + "\n")
        actual_num = int(line[0][0])
        j = 0
        while self.msgs[j + 5].rstrip() != "":
            poem.append(self.msgs[actual_num + j].rstrip())
            j += 1
        return poem


if __name__ == "__main__":
    sonnets = PIndex("AllSonnets.txt")
    # the next two lines are just for testing
    for j in sonnets.get_poem(8):
        print(j)
    print('\n------------------------------------------------------------------\n')
    for i in sonnets.search('five'):
       print(i)
