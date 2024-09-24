import urllib
import urllib.request
try:
    site = urllib.request.urlopen('https://www.youtube.com')
except:
    print('\033[31mVc não esta conectado ao youtube\033[m')
else:
    print('\033[32mVc esta conectado ao youtube\033[m')