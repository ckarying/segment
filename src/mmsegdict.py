#-*- coding:utf-8 -*-
'''
Created on Jan 18, 2013

@author: kary
'''
import cPickle as pickle
from cbase import BaseDict
class MmsegDict(BaseDict):
    
    def __init__(self , trainpath = "" , code="utf-8" , picklepath = "dic"):
        BaseDict.__init__(self, trainpath, code, picklepath)
            
    def solve(self , l):
        chunkarray = l.strip().split(" ");
        for chunk in chunkarray:
            chunk = chunk.strip()
            if chunk in self._banlist or chunk =="":
                continue
            if self._dict.has_key(chunk):
                self._dict[chunk] = self._dict[chunk]+1
            else:
                self._dict[chunk] = 1
    
    def storage(self , picklepath):
        outfile = open(picklepath , "w")
        items = self._dict.items()
        items = sorted(items , key = lambda x : x[1])   #sorted by frequent
        pickle.dump(items, outfile)
        outfile.close()
        
        
if __name__ == "__main__":
    d = MmsegDict("pku_training.txt" , "gbk");
    d.run()