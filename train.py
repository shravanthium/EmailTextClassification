import re
import math

labelRegister={}
stem=[]

def tokenize(text):
        clean =re.sub(r'[^a-zA-Z]', ' ',text.lower())
        return clean.split()
def wordlabelcount(label,word):
        count=0
        for (l,w,c) in sorted(stem):
                if(l==label and w==word):
                        count+=c
        return float(count)
def wordcount(word):
        count=0
        for (l,w,c) in sorted(stem):
                if(w==word):
                        count+=c
        return float(count)
                        
def wordinvlabelcount(label,word):
        count=0
        for (l,w,c) in sorted(stem):
                if(l==label and w==word):
                        continue
                count+=1
        return float(count)

def train(mail_id,label,text):
        labelRegister[mail_id]=label
        words = list(set((tokenize(text))))
        for word in words:
               stem.append((label,word,1))
                                
def classify(text):
        words=tokenize(text)
        length=len(words)
        labels=list(set(labelRegister.values()))
        total_doc_count=float(len(labelRegister))
        scores={}
        logsum=0
        label_doc_count={}
        labelProbability={}
                
        for label in labels:
                label_doc_count=float(labelRegister.values().count(label))
                label_inverse_count= float(len(labelRegister.values())-labelRegister.values().count(label))
                labelProbability[label]=label_doc_count/total_doc_count

                for word in words:
                        count=wordcount(word)
                        if(count==0):
                                continue
                        else:
                                wordprobability=float(wordlabelcount(label,word))/label_doc_count
                                wordinvprobability=float(wordinvlabelcount(label,word)/len(stem))
                                wordicity = wordprobability / (wordprobability + wordinvprobability)
                                wordicity = ( (1 * 0.5) + (count * wordicity) ) / ( 1 + count )
                                if (wordicity == 0):
                                        wordicity = 0.01
                                elif (wordicity == 1):
                                        wordicity = 0.99
                        #logsum += float(math.log(1 - wordicity) - math.log(wordicity))
                        logsum=wordicity
                scores[label] = logsum
        return scores

def extractWinner(scores):
        bestScore = 0
        bestLabel =None
        for label in scores:
            if (scores[label] > bestScore):
                bestScore = scores[label]
                bestLabel = label
        print bestLabel, bestScore

with open('train.txt','r') as f:
        
        for each in f.readlines():
                line= each.split('\t')	
                train(line[0],line[1],line[2])

with open('5000_clean.txt','r') as f:
        for each in f.readlines():
                line= each.split('\t')
                print line[1]
                scores=classify(line[1])
                extractWinner(scores)
        
#print labelRegister
#print stem

