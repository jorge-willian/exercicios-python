import urllib
import urllib.request

print(f'''{"=" * 50}
{"EX114 - Site está acessível?".center(50)}
{"=" * 50}''')

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')    
except:
    print('\033[1;31mSite PUDIM não está aecessível\033[m')
else:
    print('\033[1;32mO site PUDIM está acessível\033[m')



