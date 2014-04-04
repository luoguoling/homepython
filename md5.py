#author:luoguoling
import os,sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import hashlib,io
def calMd5(files):
    m = hashlib.md5()
    file = io.FileIO(files,'r')
    bytes = file.read(2048)
    while(bytes != b''):
        m.update(bytes)
        bytes = file.read(1024)
    file.close()
    md5value = m.hexdigest()
    return md5value
def findDirectory(path):
        for root,subFolders,files in os.walk(path):
                if 'weblog' in subFolders:
                        subFolders.remove('weblog')
                for filespath in files:
                        if 'laodao_ynvng_config.php' in files:
                                files.remove('laodao_ynvng_config.php')
#                       print os.path.join(root,filespath)
                        filepath = os.path.join(root,filespath)
#                       return filepath
#                       if not os.path.isdir(filepath):
#			temp = sys.stdout
#			sys.stdout = open('a.txt','w')
#			f = open('b.txt','w')
#			f.truncate()
#			os.remove('b.txt')
#			f.close()
#			sys.stdout = f
			so = file('b.txt','a+')
			os.dup2(so.fileno(),sys.stdout.fileno())
                        print  os.path.join(root,filespath), calMd5(filepath)
path = '/data/www'
findDirectory(path)
