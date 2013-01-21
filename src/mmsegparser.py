# -*- coding:utf-8 -*-
import codecs
from cbase import BaseParser
import cPickle as pickle
'''
Created on Jan 18, 2013

@author: kary
'''
class MmsegPaeser(BaseParser):
    '''
    This class is used to parse the file with dictionary
    '''
    def __init__(self , _parsepath = "" , _code ="utf-8" , _picklepath = "dic", ):
        BaseParser.__init__(self, _parsepath, _code, _picklepath)
            
    def buildhash(self):
        for item in self._dict:
            if item[0].strip() in self._banlist or item[0].strip() == "":
                continue
            if self._secdict.has_key(item[0][0]):
                self._secdict[item[0][0]] = self._secdict[item[0][0]] + [item]
            else:
                self._secdict[item[0][0]] = [item]
                
    def parsestr(self , string):
        res = []
        tmpstr = ""
        while len(string.strip()) != 0:
            candidatelist = self.search(string[0] , string , 0)
            candidatelist = self.select(candidatelist)
            if len(candidatelist):
                res = res + (tmpstr and [tmpstr] or [])
                res = res + candidatelist[-1]
                finishedstr = reduce(lambda l , r : l + r , candidatelist[-1])
                string = string[len(finishedstr) : ]
                tmpstr = ""
            else:
                tmpstr = tmpstr + string[0]
                string = string[1:]
        return res
    
    def parseline(self , line):
        res = self.splitline(line.strip())
        partline = ""
        outline = ""
        for ch in res:
            if type(ch) == type([]):
                res = self.parsestr(partline)
                outline = outline + (res and reduce(lambda l , r:  l +"\t" +r , res) or "")
                if ch: 
                    outline = outline + '\t' + ch[0] + '\t'
                partline = ""
            else:
                partline = partline + ch
        return outline.strip()
    
    def search(self , ch , string , level):
        if len(string.strip()) == 0:
            return []
        candidatelist = []
        if self._secdict.has_key(ch):
            for item in self._secdict[ch]:
                if string.startswith(item[0]):
                    newstr = string[len(item[0]):]
                    if level <self._maxlevel and len(newstr) > 0:
                        backtrack = self.search(newstr[0] , newstr , level+1)
                        if backtrack == []:
                            candidatelist = candidatelist + [[item[0]]]
                        else:
                            for candidate in backtrack:
                                candidatelist = candidatelist + [[item[0]]+candidate]
                    else:
                        candidatelist = candidatelist + [[item[0]]]
        return candidatelist


    def select(self , candidatelist):
        candidatelist = sorted(candidatelist , key = lambda candidate : 
                               [sum(map(lambda item : len(item) , candidate)) ,    #rule1
                               sum(map(lambda item : len(item) , candidate))*1.0/len(candidate) ,   #rule2
                               sum(map(lambda item:(len(item) - sum(map(lambda x :len(x) , candidate))*1.0/len(candidate))**2 ,
                                          candidate))/len(candidate) * -1.0],  #rule3
                               )
        return candidatelist
    
if __name__ == '__main__':
    p = MmsegPaeser("test" , "gbk")
    p.run()
