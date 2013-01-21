#-*- coding:utf-8 -*-
'''
Created on Jan 18, 2013

@author: kary
'''
import codecs
import cPickle as pickle
import re
class BaseDict(object):
    '''
    This class is used to create the BaseDict for parsers
    '''
    def __init__(self , trainpath = "" , code="utf-8" , picklepath = "dic"):
        '''
        Constructor
        '''
        self._dict = {}
        self._banlist = [u'/', u'‘', u'’', u'、', u'’' 
                          u',', u'.' , u';' , u':' , u'!' , u'?' , u'<' , u'>' , u'"' ,
                          u'。' , u'，',u'；' , u'：' , u'？' , u'！' , u'《' , u'》'  , u'“' , u'”']
        self._trainpath = trainpath
        self._code = code
        self._picklepath = picklepath
    
    def run(self):
        if self._trainpath.strip() != "":
            self._dict = {}
            self.build( self._trainpath , self._code)
            self.storage(self._picklepath)
            
    def build(self , trainpath , code):
        infile = codecs.open(trainpath, 'r', code)
        for line in infile:
            line = line.strip()
            regular = re.compile(u'，|。|；|！|？')
            larray = regular.split(line.strip());
            for l in larray:
                if l.strip() == "":
                    continue
                self.solve(l)
        infile.close()
    
    def solve(self , string):
        pass
    
    def storage(self , picklepath):
        pass

class BaseParser():
    '''
    This class is used to parse the file with dictionary
    '''
    def __init__(self , _parsepath = "" , _code ="utf-8" , _picklepath = "dic", ):
        self._banlist = [u'/', u'‘', u'’', u'、', u'’' 
                          u',', u'.' , u';' , u':' , u'!' , u'?' , u'<' , u'>' , u'"' ,
                          u'。' , u'，',u'；' , u'：' , u'？' , u'！' , u'《' , u'》'  , u'“' , u'”']
        try:
            f = open(_picklepath , "rb")
            self._dict = pickle.load(f)
        except Exception , e:
            print "Error" , e
            return
        f.close()
        self._maxlevel = 2
        self._secdict = {}
        self._code = _code
        self._parsepath = _parsepath
                
    def run(self ):
        if self._parsepath.strip() != "":
            self.buildhash()
        infile = codecs.open(self._parsepath, "r", self._code)
        outfile = codecs.open("ans" , "w" , "gbk")
        for line in infile:
            outline = self.parseline(line)
            print outline
            outfile.write(outline.strip() + "\n");
        infile.close()
        outfile.close()
        
    def splitline(self , line):
        if line == "":
            return []
        else:
            res = map(lambda ch : ch in self._banlist and [ch] or ch , line)
            return type(res[-1]) == type([]) and res or res + [[]]
    
    def parseline(self , line):
        pass
    
if __name__ == '__main__':
    pass