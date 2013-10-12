#-*- coding:utf-8 -*-
'''
Created on Oct 11, 2013

@author: Kary
'''

class AtomParser(object):
    '''
    Atom Parser
    '''

    def __init__(self , parserstring = "" , code ="utf-8" , picklepath = "dic"):
        '''
        Constructor
        '''
        self._parserstring = parserstring
        self._banlist = [u'/', u'‘', u'’', u'、', u'’' 
                          u',', u'.' , u';' , u':' , u'!' , u'?' , u'<' , u'>' , u'"' ,
                          u'。' , u'，',u'；' , u'：' , u'？' , u'！' , u'《' , u'》'  , u'“' , u'”']
        self._state = [0 , 1 , 2 ]
        self._tag = ['S' , 'M' , 'E']
        self._res = []
        
    def run(self ):
        if self._parserstring.strip() == "":
            return 
        line = self._parserstring.strip()
        outline = self.parseline(line)
        print outline
        
    def parseline(self , line):
        if line.strip() == "":
            return []
        else:
            self._res = map(lambda ch : ch in self._banlist and [ch , self._tag[2]] or [ch , self._tag[1]] , line)
            return type(self._res[-1]) == type([]) and self._res or self._res + [[]]
        
    def getres(self):
        return self._res
    
if __name__ == '__main__':
    demo = AtomParser(u'我是陈康睿。')
    demo.run()