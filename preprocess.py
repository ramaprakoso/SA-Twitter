import re,string
from nltk.tokenize import word_tokenize
#variabel global 
filename='tweet1clean.csv'
fname='stopword.txt'
class Preproses: 
	def __init__(self):
		pass
	def get_token(self,filename,fname):
		#open file tweet 
		with open(filename,"r") as f:
			data=f.read().split('\n')
		#open file kbba
	
			#remove url 
			tampung=[]
			for text in data: 
				rm=re.sub(r"http\S+", "", text)
				result=' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",rm).split())
				tampung.append(result)
			#stopword removing with token  
			stop=[unicode(x.strip(),'utf-8') for x in open(fname,'r').read().split('\n')]
			t=[]
			token=[word_tokenize(i) for i in tampung]
			for a in token: 
				for kata in a: 
					if kata not in stop: 
						t.append(kata)
			#slang 
		with open('kbba.txt','r') as k : 
			kbba=k.read().split('\n')	
			dic={}
			for i in kbba: 
				(key,val)=i.split('\t')
				dic[str(key)]=val
			print dic
			
if __name__=='__main__': 
	b=Preproses()
	print b.get_token(filename,fname)
		
