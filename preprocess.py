import nltk
import re 
from nltk.tokenize import word_tokenize

class Preprocess:
	def __init__(self): 
		self.simpan=[]
	def buka_file(self,filename): 
		with open(filename,"r") as f:
			data=f.read().split('\n')	
			return data
	def hapus_url(self,fdata):
		tampung=[]
		for text in fdata: 
			result = re.sub(r"http\S+", "", text)
			return tampung.append(result)
	def stopword(self,fname):
		stop=[unicode(x.strip(),'utf-8') for x in open(fname,'r').read().split('\n')]
		return stop
	def tokenize(self,data,stoped):
		#memilih stopwords 
		tampung=[]
		token=[word_tokenize(i) for i in data]
		for a in token : 
			for kata in a: 
				if kata not in stoped: 
					tampung.append(kata)
		return tampung
if __name__=='__main__': 
	b=Preprocess()
	data=b.buka_file('tweet1clean.csv')
	hapus=b.hapus_url(data)
	stop=b.stopword('stopword.txt')
	b.tokenize(hapus,stop)
	"""data=b.buka_file()
	stop=b.stopword('stopword.txt')
	tokenize(data,stop)"""
		
