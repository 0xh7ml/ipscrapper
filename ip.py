from urllib.request import urlopen as html
ip = input("Enter your Ip :-")
url = 'http://ipinfo.io/'+ip+'/geo?token=0b6776a4b59afd' #add your token here
r= html(url).read().decode('utf-8')
print(r)
