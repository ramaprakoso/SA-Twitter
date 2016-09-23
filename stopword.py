import nltk
from nltk.tokenize import word_tokenize

with open("tweet1clean.csv","r") as myfile: 
	data=myfile.read().split('\n')
	print data
stop_words=[unicode(x.strip(),'utf-8') for x in open('stopword.txt','r').read().split('\n')]
token=word_tokenize(kalimat)

tampung=[]
for kata in token: 
	if kata not in stop_words:
		tampung.append(kata)
print tampung
