import nltk
from nltk.tokenize import word_tokenize

def buka_file(filename): 
	with open(filename,"r") as f:
		data=f.read().split('\n')
		return data
def stopword(filename):
	stop=[unicode(x.strip(),'utf-8') for x in open(filename,'r').read().split('\n')]
	return stop
def tokenize(data,stoped):
	#memilih stopwords 
	tampung=[]
	token=[word_tokenize(i) for i in data]
	for a in token : 
		for kata in a: 
			if kata not in stoped: 
				tampung.append(kata)
	return tampung
def main(): 
	data=buka_file('tweet1clean.csv')
	stop=stopword('stopword.txt')
	print tokenize(data,stop)
	
if __name__=='__main__': 
	main()
