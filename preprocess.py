import re,string
from nltk.tokenize import word_tokenize
filename='tweet1clean.csv'
sname='stopword.txt'
def preprocess(tweet):
	#hapus url 
	tweet=hapus_url(tweet) 
	#hapus tandabaca
	tweet=hapus_tanda(tweet)
	#hapus angka 
	tweet=hapus_angka(tweet)
	#token 
	token=tokenize(tweet)
	token=kbbi(token)
	token=stopwordDel(token)
	return token   
def hapus_url(tweet): 
	url=re.sub(r'http\S',"",tweet)
	return url 
def hapus_tanda(tweet):
	tb=re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)","",tweet)
	return tb
def hapus_angka(tweet): 
	angka=re.sub(r'\w*\d\w*', '',tweet).strip()
	return angka 
def tokenize(tweet): 
	token=word_tokenize(tweet)
	return token 
def stopwordDel(token):
	stopword=[word.strip('\n') for word in open('stopword.txt')] 
	noise=[noise.strip('\n').strip('\r') for noise in open('noise.txt')]
	tampung=[]
	for i in range(0,len(token)): 
		if token[i] not in stopword: 
			tampung.append(token[i])
	return tampung
def kbbi(token): 
	kbba=[kamus.strip('\n').strip('\r') for kamus in open('kbba.txt')]
	#ubah list menjadi dictionary 
	dic={}
	for i in kbba: 
		(key,val)=i.split('\t')
		dic[str(key)]=val
	#kbbi cocokan 
	final_string = ' '.join(str(dic.get(word, word)) for word in token).split()
	return final_string
 
if __name__=='__main__': 
	with open(filename,"r") as f:
			data=f.read()
			print preprocess(data) 
			
			
			#stopwordDel()	
		
		
			
	"""
	def get_token(self,filename,fname):
		#open file tweet 
		with open(filename,"r") as f:
			data=f.read().split('\n')
			tampung=[]
			for text in data: 
				#remove url
				result=re.sub(r"http\S+", "", text)
				#remove number 
				result=re.sub(r'\w*\d\w*', '',result).strip()
				#remove punctuation 
				result=' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",result).split())
				tampung.append(result) 
			#stopword removing with token  
			stop=[unicode(x.strip(),'utf-8') for x in open(fname,'r').read().split('\n')]
			t=[]
			token=[word_tokenize(i) for i in tampung]
			for i in token: 
				for kata in i: 
					if kata not in stop: 
						t.append(kata)
			return t
		with open('kbba.txt','r') as k : 
			kbba=k.read().split('\n')	
			dic={}
			for i in kbba: 
				(key,val)=i.split('\t')
				dic[str(key)]=val
			u=[]
			for word in t: 
				for kandidat in dic: 
					if kandidat in word: 
						word=word.replace(kandidat,dic[kandidat])
				print word
			print u
		"""
