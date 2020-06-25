

#import subprocess

#out0 = subprocess.check_output("cd ..", shell = True)
#print(out0)

#out1 = subprocess.check_output("git init", shell=True)
#print(out1)

#out2 = subprocess.check_output(["git", "add", "tp.py"])
#print(out2)

#out3 = subprocess.check_output("git status", shell=True)
#print(out3)

#out4 = subprocess.check_output(["git", "commit", "-m", "'adding tp.py'"])
#print(out4)

#cmd = subprocess.Popen('cmd.exe /K cd /')

import os
#os.system("start cmd")
#os.system("git init")

#os.system("git add readME.txt")
#os.system("git status")
#os.system("git rm --cached -f tp.py")
#o = os.system('dir C:')
#print(o)
#os.system('git commit -m "adding readME"')

#import subprocess
#process = subprocess.Popen('cmd /k ', shell=True, stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=None)
#process.stdin.write(b"dir C:")                 #passing command
#stdOutput,stdError = process.communicate()
#print(stdOutput)
#process.stdin.close()

os.system('git init')
os.system('git pull https://github.com/ame-madhekar-7/sorceres-code2.git')
os.system('git add readME.txt')
os.system('git commit -m "adding readME.txt"')
os.system('git remote add origin https://github.com/ame-madhekar-7/sorceres-code2.git')
os.system('git push -u origin master')