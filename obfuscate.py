import os
import io
import requests 
from bs4 import BeautifulSoup
from fnmatch import fnmatch

API_ENDPOINT = "https://tools.kodigen.com/online-tools/php-obfuscator"
tRoot = "php"
dRoot = "obfuscated"
pattern = "*.php"
targetPath = os.path.join(tRoot)

for targetPath, subdirs, files in os.walk(tRoot):
    for fileName in files:
        if fnmatch(fileName, pattern):
            target_file = os.path.join(targetPath, fileName)
            
            f = open(target_file, 'rb')
            file_code   = f.read()
            f.close()

            phpFiles    = os.path.join(targetPath, fileName)
            saveTo      = os.path.join(dRoot, targetPath)
            saveToPath  = os.path.join(dRoot, targetPath, fileName)
            
            if not os.path.exists(saveTo):
                os.makedirs(saveTo)

            params      = {'content':file_code, 'action': 'obfuscate'} 
            req         = requests.post(API_ENDPOINT, params)
            
            print(fileName+' <<< Working... ')
            with io.open(saveToPath, "w", encoding="utf-8") as file:
                soup            = BeautifulSoup(req.text, "html.parser")
                obfuscated_php  = soup.find('textarea', id='output').text
                file.write(obfuscated_php)
print('>>> OBFUSCATION COMPLETE <<<')