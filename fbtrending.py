#! python3 
import webbrowser,requests,bs4,getpass

session = requests.Session()
res = session.get('https://www.facebook.com/search/trending-news/')
doc = bs4.BeautifulSoup(res.text,'lxml')

data={}

for x in doc.select('input'):
	data[x.get('name')] = x.get('value')
del data[None] 		
data['login']='Log In'


data['email'] = input('Enter your Facebook Email Id\n')
data['pass'] = getpass.getpass()
res = session.post('https://www.facebook.com/login.php?login_attempt=1&next=https%3A%2F%2Fwww.facebook.com%2Fsearch%2Ftrending-news%2F&lwv=101',data=data)
res.raise_for_status()
doc = bs4.BeautifulSoup(res.text,'lxml')
for x in doc.select('span')[-22:-2]:
	print(x.text)

