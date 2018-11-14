# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 12:04:19 2017
class: word processing
@author: talen
"""
class wps:
    @classmethod
    def __ini__(self,astr):
        self.astr = astr
    
    def word_segmentation(self,astr):
        import jieba
        str_seg = list(jieba.cut(astr)
        return str_seg
    
    def prepro(self,files):
        report = [term for term in self.word_segmentation(files) if term != '\n']
        report1 = [term[:-1] if term.endswith('\n') else term for term in report]
        # report2 用于去掉句子开头的'\ufeff'
        report2 = [term.encode('utf-8').decode('utf-8-sig') for term in report1 if term != '\n']
        return report2
    
    def text_cleaning(self):
        chinese_sym = ['，','。','；','：','“','”',' ','（','）','、','！']
        chinese_stop_words = ['的','和','是','在','为']
        self.tmp1 = [term for term in self.word_segmentation(self.astr) if term not in chinese_sym]
        self.cleaned = [term for term in self.tmp1 if term not in chinese_stop_words]
        return self.cleaned
    
    def get_stat(self,n):
        import collections as cc
        self.tmp = cc.Counter(self.text_cleaning())
        print(self.tmp.most_common(n))
    
    
        
        
