# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, urllib3, wikipedia, tempfile
from bs4 import BeautifulSoup
from urllib import urlopen
from io import StringIO
from threading import Thread
from gtts import gTTS
from googletrans import Translator
cl = LINETCR.LINE()
cl.login(token="EoB8ZHHukR5B6XYgAuma.apGNZMzba418M2CeQxD9/G.gcWcqLOM8kQNULkpMxRQGfnG2MClR+WVbVyMEeLo3TI=")
cl.loginResult()

ki1 = LINETCR.LINE()
ki1.login(token="EoRrJ7tye8FQarygx2h7.VlpYu+Q6jGzsicHOptxRPW.acUdejhDzXHwLZQftewce6f1PLt3gRrV0kbM9kqGOOc=")
ki1.loginResult()

ki2 = LINETCR.LINE()
ki2.login(token="Eoanj57G8zVmnx1Lbcq0.+ZViS46tqNx/xW3+/xvqWa.7OEC6oc00qyDxg4oyNPkxUPR6cp4NQtisWXcXsisb04=")
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token="EoTaHjbFSm5Q4uSw9nD8.TDGC/4U6kG8mrZHlHb4Xsa.5GnU4dc+9495v9xtFbXwBQbj8Mkh1Tf9eo/QyyHDPQA=")
ki3.loginResult()

ki4 = LINETCR.LINE()
ki4.login(token="Eov6BKJXHfTv7j3CRHU5.aOeodX8FNJewWK5vf5P9fq.LnPl7aQDvd/bjbou+L2w1lvh/ioHsSUQYDfd/swfrZA=")
ki4.loginResult()

ki5 = LINETCR.LINE()
ki5.login(token="EoD4mpmx79uzg09jbML1.efbujRuyG0q0ahbGcSYguq.DxbEGtvtTXAKEePt4fLUXH8jRjh7VG+5CUM0fAPAWAw=")
ki5.loginResult()

ki6 = LINETCR.LINE()
ki6.login(token="EoxwAg1N3lSmzFfZ0RX3.7f74kMOPgNIBSGT6+sawqW.zNL95ZZiregvvKd9pBWeCNQEvFK8pQVNb3TtBibAGEQ=")
ki6.loginResult()

ki7 = LINETCR.LINE()
ki7.login(token="Eokv7n7uoq4tsmQWREkf.PqUHiCpv2pBtz8Q0TEIqxW.AgPVyVnLoG7UHyzHyQX/ICM4cQapp9zRSY2uGr95du8=")
ki7.loginResult()

ki8 = LINETCR.LINE()
ki8.login(token="EoxWhUuk78IXHPBgYgbe.nMGqEcQDlP6dAl/gilNatG.90ay26S0VfNPti2ZmKGDVlu6FJ3ivCsIUSVDa6kmBEA=")
ki8.loginResult()

ki9 = LINETCR.LINE()
ki9.login(token="EoluRsFVIBC6WfNecGja.XeTFQ55WYwSmXh4n0wOhcG.Zl36VJU8INIcSFmmXsMSXyUZW+gbjmQTgE6LxBQpCa4=")
ki9.loginResult()

ki10 = LINETCR.LINE()
ki10.login(token="EoQW0fWuribDJDJRBTCa.XIBZSHhwVEi2szZJfJwo/G.0Vu2NC0IMsGRgSttKg/vSJz9ngGwx/lGkaqdUqt1GgM=")
ki10.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')
helpMessage ="""     ─┅═✥हईທຮຮๅજईह✥═┅─

─┅═✥s̵ᴇʟғʙᴏᴛ ᴛʜᴀɪʟᴀɴᴅ✥═┅─
                     
❂͜͡☆➣ 『Me』
❂͜͡☆➣ 『Id』
❂͜͡☆➣ 『Wc』
❂͜͡☆➣ 『Mc:』
❂͜͡☆➣ 『Mid』
❂͜͡☆➣ 『BBc:』
❂͜͡☆➣ 『Gift』
❂͜͡☆➣ 『Mid @』
❂͜͡☆➣ 『Cn: Display Name』
❂͜͡☆➣ 『Cc: Clock Name』
❂͜͡☆➣ 『Hack @』
❂͜͡☆➣ 『Tl: text』
❂͜͡☆➣ 『Auto join: on/off』
❂͜͡☆➣ 『Auto add: on/off』
❂͜͡☆➣ 『Auto leave: on/off』
❂͜͡☆➣ 『Clock: on/off』
❂͜͡☆➣ 『Share on』
❂͜͡☆➣ 『Add message: text』
❂͜͡☆➣ 『Message:』
❂͜͡☆➣ 『Add comment: text』
❂͜͡☆➣ 『Comment: 』
❂͜͡☆➣ 『Cbroadcast text』
❂͜͡☆➣ 『Gbroadcast text』
❂͜͡☆➣ 『Reject』
 
──┅═✥===========✥═┅──

                 SELFBOT

          PHET HACK BOT
            
──┅═✥===========✥═┅──

❂͜͡☆➣ 『Creator 』
❂͜͡☆➣ 『Gn: text 』
❂͜͡☆➣ 『Invite:on 』
❂͜͡☆➣ 『Invite: mid』 
❂͜͡☆➣ 『Allgift 』
❂͜͡☆➣ 『All mid』
❂͜͡☆➣ 『Cancel』
❂͜͡☆➣ 『Link on/off』
❂͜͡☆➣ 『Spam on/off』
❂͜͡☆➣ 『ginfo』
❂͜͡☆➣ 『Myginfo』
❂͜͡☆➣ 『Gurl』
❂͜͡☆➣ 『Glist』
❂͜͡☆➣ 『Set』
❂͜͡☆➣ 『Phet: Tag』
❂͜͡☆➣ 『Gcancel:』
❂͜͡☆➣ 『Masuk Join』
❂͜͡☆➣ 『Sa:yang』
❂͜͡☆➣ 『Beb』
❂͜͡☆➣ 『Cinta』
❂͜͡☆➣ 『Sayang: 』
❂͜͡☆➣ 『P:ulang』
❂͜͡☆➣ 『Ban @』
❂͜͡☆➣ 『Uban @』
❂͜͡☆➣ 『Ban 』
❂͜͡☆➣ 『Unban』
❂͜͡☆➣ 『Comment :』
❂͜͡☆➣ 『Banlist』
❂͜͡☆➣ 『Cekban』
❂͜͡☆➣ 『Clear ban』
❂͜͡☆➣ 『Kill @ Fuck @』
❂͜͡☆➣ 『Speed / Sp』
❂͜͡☆➣ 『Hack @2@3@4』
❂͜͡☆➣ 『Ambilin @』
❂͜͡☆➣ 『Sampul @』
❂͜͡☆➣ 『Copy @』
❂͜͡☆➣ 『Mycopy @』
❂͜͡☆➣ 『Keluar :@』
❂͜͡☆➣ 『music』
❂͜͡☆➣ 『.reboot』
❂͜͡☆➣ 『Wikipedia』
❂͜͡☆➣ 『Cleanse』
❂͜͡☆➣ 『Bot Speed』
❂͜͡☆➣ 『P1-P36 link on/off』
 
  
──┅═✥===========✥═┅──

❂͜͡☆➣ 『Key』
❂͜͡☆➣ 『Qr on/off』
❂͜͡☆➣ 『Backup on/off』
❂͜͡☆➣ 『Protect On/off』
❂͜͡☆➣ 『Namelock On/off』

    
        ─┅═✥ᵀᴴᴬᴵᴸᴬᴺᴰ✥═┅─

      [By. เพชร ทีมทดลองบอท]

──┅═✥============✥═┅──"""
helpMessage2 ="""
╔═════════════════
║       ✟ New function ✟
╠═════════════════
╠➩〘Help protect〙
╠➩〘Help self〙
╠➩〘Help grup〙
╠➩〘Help set〙
╠➩〘Help media〙
╠➩〘Speed〙
╠➩〘Status〙
╚═════════════════

╔═════════════════
║       ✟ New function ✟
╠═════════════════
╠➩〘Protect on/off〙
╠➩〘Qr on/off〙
╠➩〘Invit on/off〙
╠➩〘Cancel on/off〙
╚═════════════════

╔═════════════════
║       ✟ New function ✟
╠═════════════════
╠➩〘Me〙
╠➩〘Myname: 〙
╠➩〘Mybio: 〙
╠➩〘Myname〙
╠➩〘Mybio〙
╠➩〘Mypict〙
╠➩〘Mycover〙
╠➩〘My,copy @〙
╠➩〘Mybackup〙
╠➩〘Getgrup image〙
╠➩〘Getmid @〙
╠➩〘Getprofile @〙
╠➩〘Getcontact @〙
╠➩〘Getinfo @〙
╠➩〘Getname @〙
╠➩〘Getbio @〙
╠➩〘Getpict @〙
╠➩〘Getcover @〙
╠➩〘Mention〙
╠➩〘Lurk on/off〙
╠➩〘Lurkers〙
╠➩〘Mimic on/off〙
╠➩〘Micadd @〙
╠➩〘Micdel @〙
╠═════════════════
║       ✟ New function ✟
╠═════════════════
╠➩〘Contact on/off〙
╠➩〘Autojoin on/off〙
╠➩〘Autoleave on/off〙
╠➩〘Autoadd on/off〙
╠➩〘Like me〙
╠➩〘Like friend〙
╠➩〘Like on〙
╠➩〘Respon on/off〙
╠➩〘Read on/off〙
╠➩〘Simisimi on/off〙
╠═════════════════
║       ✟ New function ✟
╠═════════════════
╠➩〘Link on/off〙
╠➩〘Url〙
╠➩〘Cancel〙
╠➩〘Gcreator〙
╠➩〘Ki'ck @〙
╠➩〘Ulti @〙
╠➩〘Cancel〙
╠➩〘Gname: 〙
╠➩〘Gbroadcast: 〙
╠➩〘Cbroadcast: 〙
╠➩〘Infogrup〙
╠➩〘Gruplist〙
╠➩〘Friendlist〙
╠➩〘Blocklist〙
╠➩〘Ba'n @〙
╠➩〘U'nban @〙
╠➩〘Clearban〙
╠➩〘Banlist〙
╠➩〘Contactban〙
╠➩〘Midban〙
╠═════════════════
║       ✟ New function ✟
╠═════════════════
╠➩〘Kalender〙
╠➩〘tr-id 〙
╠➩〘tr-en 〙
╠➩〘tr-jp 〙
╠➩〘tr-ko 〙
╠➩〘say-id 〙
╠➩〘say-en 〙
╠➩〘say-jp 〙
╠➩〘say-ko 〙
╠➩〘profileig 〙
╠➩〘checkdate 〙
╚═════════════════
"""
helpMessage3 ="""
╔══════════════════════
║       ✦เปิด/ปิดข้อความต้อนรับ✦
╠══════════════════════
║✰ Hhx1 on ➠เปิดข้อความต้อนรับ
║✰ Hhx1 off ➠ปิดข้อความต้อนรับ
║✰ Hhx2 on ➠เปิดข้อความออกกลุ่ม
║✰ Hhx2 off ➠เปิดข้อความออกกลุ่ม
║✰ Hhx3 on ➠เปิดข้อความคนลบ
║✰ Hhx3 off ➠เปิดข้อความคนลบ
║✰ Mbot on ➠เปิดเเจ้งเตือนบอท
║✰ Mbot off ➠ปิดเเจ้งเตือนบอท
║✰ M on ➠เปิดเเจ้งเตือนตนเอง
║✰ M off ➠ปิดเเจ้งเตือนตนเอง
║✰ Tag on ➠เปิดกล่าวถึงเเท็ค
║✰ Tag off ➠ปิดกล่าวถึงเเท็ค
║✰ Kicktag on ➠เปิดเตะคนเเท็ค
║✰ Kicktag off ➠ปิดเตะคนเเท็ค
╚══════════════════════
╔══════════════════════
║         ✦โหมดตั้งค่าข้อความ✦
╠══════════════════════
║✰ Hhx1˓: ➠ไส่ข้อความต้อนรับ
║✰ Hhx2˓: ➠ไส่ข้อความออกจากกลุ่ม
║✰ Hhx3˓: ➠ไส่ข้อความเมื่อมีคนลบ
╚══════════════════════
╔══════════════════════
║       ✦โหมดเช็คตั้งค่าข้อความ✦
╠══════════════════════
║✰ Hhx1 ➠เช็คข้อความต้อนรับ
║✰ Hhx2 ➠เช็คข้อความคนออก
║✰ Hhx3 ➠เช็คข้อความคนลบ
╚══════════════════════"""

KAC=[cl,ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
mid = cl.getProfile().mid
Amid1 = ki1.getProfile().mid
Amid2 = ki2.getProfile().mid
Amid3 = ki3.getProfile().mid
Amid4 = ki4.getProfile().mid
Amid5 = ki5.getProfile().mid
Amid6 = ki6.getProfile().mid
Amid7 = ki7.getProfile().mid
Amid8 = ki8.getProfile().mid
Amid9 = ki9.getProfile().mid
Amid10 = ki10.getProfile().mid

protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
mid = cl.getProfile().mid
Bots = ["u00f827ce6641038d7c9b6704a9777dfa",mid,Amid1,Amid2,Amid3,Amid4,Amid5,Amid6,Amid7,Amid8,Amid9,Amid10]
self = ["u00f827ce6641038d7c9b6704a9777dfa",mid,Amid1,Amid2,Amid3,Amid4,Amid5,Amid6,Amid7,Amid8,Amid9,Amid10]
admin = "u00f827ce6641038d7c9b6704a9777dfa"
admsa = "u00f827ce6641038d7c9b6704a9777dfa"
owner = "u00f827ce6641038d7c9b6704a9777dfa"
adminMID = "u00f827ce6641038d7c9b6704a9777dfa"
Creator="u00f827ce6641038d7c9b6704a9777dfa"
wait = {
    "alwayRead":False,
    "detectMention":True,    
    "kickMention":False,
    "steal":False,
    'pap':{},
    'invite':{},
    "spam":{},
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True, "members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':False,
    'message':"Thanks for add Me MY NAME IS PHET",
    "lang":"JP",
    "comment":"AutoLike by Phet",
    "commentOn":False,
    "acommentOn":False,
    "bcommentOn":False,
    "ccommentOn":False,
    "Protectcancl":False,
    "pautoJoin":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"༺ ㏒ Ᵽɧëȶ ㏒ ༻",
    "likeOn":False,
    "pname":False,
    "blacklist":{},
    "whitelist":{},
    "wblacklist":False,
    "dblacklist":False,
    "qr":False,
    "Backup":False,
    "protectionOn":False,
    "winvite":False,
    "ainvite":False,
    "binvite":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "Hhx1":False,
    "Hhx2":False,
    "Hhx3":False,
    "Notifed":False,
    "Notifedbot":False,
    "atjointicket":False,
    "pnharfbot":{},
    "pname":{},
    "pro_name":{},
	"posts":False,
	}

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
    
settings = {
    "simiSimi":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

blacklistFile='blacklist.txt'
pendinglistFile='pendinglist.txt'

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus


contact = ki1.getProfile()
backup = ki1.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki2.getProfile()
backup = ki2.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki3.getProfile()
backup = ki3.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki4.getProfile()
backup = ki4.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki5.getProfile()
backup = ki5.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki6.getProfile()
backup = ki6.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki7.getProfile()
backup = ki7.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki8.getProfile()
backup = ki8.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki9.getProfile()
backup = ki9.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki10.getProfile()
backup = ki10.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def sendImageWithUrl(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e
def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

def upload_tempimage(client):
    '''
        Upload a picture of a kitten. We don't ship one, so get creative!
    '''
    config = {
        'album': album,
        'name':  'bot auto upload',
        'title': 'bot auto upload',
        'description': 'bot auto upload'
    }

    print("Uploading image... ")
    image = client.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error
       
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)      

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False
def sendMessage(self, messageObject):
        return self.Talk.client.sendMessage(0,messageObject)

def sendText(self, Tomid, text):
        msg = Message()
        msg.to = Tomid
        msg.text = text

        return self.Talk.client.sendMessage(0, msg)

def sendImage(self, to_, path):
    M = Message(to=to_, text=None, contentType = 1)
    M.contentMetadata = None
    M.contentPreview = None
    M2 = self._client.sendMessage(0,M)
    M_id = M2.id
    files = {
       'file': open(path, 'rb'),
    }
    params = {
       'name': 'media',
       'oid': M_id,
       'size': len(open(path, 'rb').read()),
       'type': 'image',
       'ver': '1.0',
    }
    data = {
       'params': json.dumps(params)
    }
    r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
    if r.status_code != 201:
       raise Exception('Upload image failure.')
    return True

def sendImage2(self, to_, path):
    M = Message(to=to_,contentType = 1)
    M.contentMetadata = None
    M.contentPreview = None
    M_id = self._client.sendMessage(M).id
    files = {
       'file': open(path, 'rb'),
    }
    params = {
       'name': 'media',
       'oid': M_id,
       'size': len(open(path, 'rb').read()),
       'type': 'image',
       'ver': '1.0',
    }
    data = {
       'params': json.dumps(params)
    }
    r = cl.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
    if r.status_code != 201:
       raise Exception('Upload image failure.')
    return True

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))


        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                        try:
                            G = ki1.getGroup(op.param1)
                        except:
                            try:
                                G = ki2.getGroup(op.param1)
                            except:
                                try:
                                    G = ki3.getGroup(op.param1)
                                except:
                                    try:
                                        G = ki4.getGroup(op.param1)
				    except:
					try:
                                            G = ki5.getGroup(op.param1)
                                        except:
                                            pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        cl.updateGroup(G)
                    except:
                        try:
                            ki1.updateGroup(G)
                        except:
                            try:
                                ki2.updateGroup(G)
                            except:
                                try:
                                    ki2.updateGroup(G)
                                except:
                                    try:
                                        ki3.updateGroup(G)
                                    except:
                                        try:
                                            ki4.updateGroup(G)
                                        except:
                                            pass
                    if op.param2 in ken:
                        pass
                    else:
                        try:
                            ki1.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ki1.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ki2.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ki3.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ki4.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                                        cl.sendText(op.param1,"Group Name Lock")
                                        ki1.sendText(op.param1,"Haddeuh dikunci Pe'a")
                                        ki2.sendText(op.param1,"Wekawekaweka (Har Har)")
                                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                                        c.contentMetadata={'mid':op.param2}
                                        cl.sendMessage(c)

        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)



                if op.param3 in mid:
                    if op.param2 in Amid1:
                        G = ki1.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki1.updateGroup(X)
                        Ti = ki1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki1.updateGroup(X)
                        Ti = ki1.reissueGroupTicket(op.param1)

                if op.param3 in mid:
                    if op.param2 in Amid2:
                        X = ki2.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)

                if op.param3 in mid:
                    if op.param2 in Amid3:
                        X = ki3.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)

                if op.param3 in mid:
                    if op.param2 in Amid4:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)

                if op.param3 in mid:
                    if op.param2 in Amid5:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)

                if op.param3 in mid:
                    if op.param2 in Amid6:
                        G = ki6.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Amid7:
                        G = ki7.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Amid8:
                        G = ki8.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Amid9:
                        G = ki9.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Amid10:
                        G = ki10.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)



                if op.param3 in Amid1:
                    if op.param2 in Amid2:
                        X = ki2.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki2.updateGroup(X)
                        Ti = ki1.reissueGroupTicket(op.param1)
                        ki1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)

                if op.param3 in Amid2:
                    if op.param2 in Amid3:
                        X = ki3.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki3.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)

                if op.param3 in Amid3:
                    if op.param2 in Amid4:
                        X = ki4.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)

                if op.param3 in Amid4:
                    if op.param2 in Amid5:
                        X = ki5.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)

                if op.param3 in Amid5:
                    if op.param2 in Amid6:
                        X = ki6.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)

                if op.param3 in Amid6:
                    if op.param2 in Amid7:
                        X = ki7.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)

                if op.param3 in Amid7:
                    if op.param2 in Amid8:
                        X = ki8.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                if op.param3 in Amid8:
                    if op.param2 in Amid9:
                        X = ki9.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                if op.param3 in Amid9:
                    if op.param2 in Amid10:
                        X = ki10.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki7.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
                if op.param3 in Amid10:
                    if op.param2 in Amid1:
                        X = ki.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki.updateGroup(X)
                        Ti = ki.reissueGroupTicket(op.param1)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki.updateGroup(X)
                        Ti = ki.reissueGroupTicket(op.param1)

#===========================================
        if op.type == 32:
            if not op.param2 in Bots:
                if wait["protectionOn"] == True: 
                    try:
                        klist=[ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                        kicker = random.choice(klist) 
                        G = kicker.getGroup(op.param1)
                        kicker.kickoutFromGroup(op.param1,[op.param2])
                        kicker.inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                       print e
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                        cl.sendText(op.param1, "Your invitation was declined\n\n[SELFBOT PHET HACK BOT]]\n\nhttp://line.me/ti/p/09T2waRE7l")
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        cl.sendText(op.param1, "Your invitation was declined\n\n[SELFBOT PHET HACK BOT]]\n\nhttp://line.me/ti/p/09T2waRE7l")
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
            if Amid1 in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ki1.rejectGroupInvitation(op.param1)
                        else:
                            ki1.acceptGroupInvitation(op.param1)
                    else:
                        ki1.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ki1.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki1.cancelGroupInvitation(op.param1, matched_list)
            if Amid2 in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ki2.rejectGroupInvitation(op.param1)
                        else:
                            ki2.acceptGroupInvitation(op.param1)
                    else:
                        ki2.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ki2.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki2.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 11:
            if not op.param2 in Bots:
              if wait["qr"] == True:  
                try:
                    klist=[ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                    kicker = random.choice(klist) 
                    G = kicker.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kicker.updateGroup(G)
                except Exception, e:
                    print e
        if op.type == 11:
            if not op.param2 in Bots:
              if wait["protectionOn"] == True:
                 try:                    
                    klist=[ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                    kicker = random.choice(klist) 
                    G = kicker.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kicker.updateGroup(G)
                    kicker.kickoutFromGroup(op.param1,[op.param2])
                    G.preventJoinByTicket = True
                    kicker.updateGroup(G)
                 except Exception, e:
                           print e
        if op.type == 13:
            G = cl.getGroup(op.param1)
            I = G.creator
            if not op.param2 in Bots:
                if wait["protectionOn"] == True:  
                    klist=[ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                    kicker = random.choice(klist)
                    G = kicker.getGroup(op.param1)
                    if G is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        kicker.cancelGroupInvitation(op.param1, gInviMids)
        if op.type == 19:
                if not op.param2 in Bots:
                    try:
                        gs = ki1.getGroup(op.param1)
                        gs = ki2.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            pass
                                
                    except Exception, e:
                        print e
                if not op.param2 in Bots:
                  if wait["Backup"] == True:
                    try:
                        random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e
                if not op.param2 in Bots:
                  if wait["protectionOn"] == True:  
                   try:
                       klist=[ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                       kicker = random.choice(klist)
                       G = kicker.getGroup(op.param1)
                       G.preventJoinByTicket = False
                       kicker.updateGroup(G)
                       invsend = 0
                       Ticket = kicker.reissueGroupTicket(op.param1)
                       kl1.acceptGroupInvitationByTicket(op.param1,Ticket)
                       time.sleep(0.1)
                       X = kicker.getGroup(op.param1)             
                       X.preventJoinByTicket = True
                       kl1.kickoutFromGroup(op.param1,[op.param2])
                       kicker.kickoutFromGroup(op.param1,[op.param2])
                       kl1.leaveGroup(op.param1)
                       kicker.updateGroup(X)
                   except Exception, e:
                            print e
                if not op.param2 in Bots:
                    try:
                        gs = ki1.getGroup(op.param1)
                        gs = ki2.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            pass
                                
                    except Exception, e:
                        print e
                if not op.param2 in Bots:
                  if wait["Backup"] == True:
                    try:
                        random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e
        if op.type == 19:              
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass                   
                    try:
                        ki1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki1.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki1.updateGroup(G)
                    Ti = ki1.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid1 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki2.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki2.updateGroup(X)
                    Ti = ki2.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)

                    X = ki1.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki1.updateGroup(X)
                    Ticket = ki1.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True


                if Amid2 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki3.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki3.updateGroup(X)
                    Ti = ki3.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)

                    X = ki2.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki2.updateGroup(X)
                    Ticket = ki2.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid3 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki4.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki4.updateGroup(X)
                    Ti = ki4.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)

                    X = ki3.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki3.updateGroup(X)
                    Ticket = ki3.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid4 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki5.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki5.updateGroup(X)
                    Ti = ki5.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)

                    X = ki4.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki4.updateGroup(X)
                    Ticket = ki4.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid5 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki6.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki6.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki6.updateGroup(X)
                    Ti = ki6.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)

                    X = ki5.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki5.updateGroup(X)
                    Ticket = ki5.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid6 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki7.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki7.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki7.updateGroup(X)
                    Ti = ki7.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)

                    X = ki6.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki6.updateGroup(X)
                    Ticket = ki6.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid7 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki8.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki8.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki8.updateGroup(X)
                    Ti = ki8.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)

                    X = ki7.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki7.updateGroup(X)
                    Ticket = ki7.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid8 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki9.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki9.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki9.updateGroup(X)
                    Ti = ki9.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)

                    X = ki8.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki8.updateGroup(X)
                    Ticket = ki8.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid9 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki10.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki10.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki10.updateGroup(X)
                    Ti = ki10.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)

                    X = ki9.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki9.updateGroup(X)
                    Ticket = ki9.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid10 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki1.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki1.updateGroup(X)
                    Ti = ki1.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)

                    X = ki10.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki10.updateGroup(X)
                    Ticket = ki10.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
        if op.type == 13:
            if mid in op.param3:
              if wait["pautoJoin"] == True:
                  cl.acceptGroupInvitation(op.param1)
              else:
                  cl.rejectGroupInvitation(op.param1)


        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to, "error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)

        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                cl.sendText(msg.to, "[ChatBOT] " + data['result']['response'].encode('utf-8'))
                                
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Dont Tag Me!! Im Busy",cName + " Ngapain Ngetag?",cName + " Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja","-_-","Alin lagi off", cName + " Kenapa Tag saya?","SPAM PC aja " + cName, "Jangan Suka Tag gua " + cName, "Kamu siapa " + cName + "?", "Ada Perlu apa " + cName + "?","Tenggelamkan tuh yang suka tag pake BOT","Tersummon -_-"]
                     ret_ = "[Auto Respond] " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  break            
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Dont Tag Me!! Im Busy",cName + ""]
                     ret_ = "[Auto] " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  msg.contentType = 7
                                  msg.text = ''
                                  msg.contentMetadata = {
                                                            'STKPKGID': '608',
                                                            'STKTXT': '[]',
                                                            'STKVER': '16',
                                                            'STKID':'5507'
                                                        }
                                  cl.sendMessage(msg)
                                  break
                    
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Dont Tag Me!! Im Busy",cName + " Ngapain Ngetag?",cName + " Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja","-_-","Alin lagi off", cName + " Kenapa Tag saya?","SPAM PC aja " + cName, "Jangan Suka Tag gua " + cName, "Kamu siapa " + cName + "?", "Ada Perlu apa " + cName + "?","Tenggelamkan tuh yang suka tag pake BOT","Tersummon -_-"]
                     ret_ = "[Auto Respond] " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  cl.kickoutFromGroup(msg.to,[msg.from_])
                                  break
            
            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Stealed"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.findAndAddContactsByMid(target)
                                contact = cl.getContact(target)
                                cu = cl.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
                                cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                                cl.sendImageWithUrl(msg.to,image)
                                cl.sendText(msg.to,"Cover " + contact.displayName)
                                cl.sendImageWithUrl(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass    
                                
            if wait["alwayRead"] == True:
                if msg.toType == 0:
                    cl.sendChatChecked(msg.from_,msg.id)
                else:
                    cl.sendChatChecked(msg.to,msg.id)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done deleted")
                        
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"Done already")

                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done done aded")
               
               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done deleted")

                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")

               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Help","คำสั่ง"]:
                print "\nHelp pick up..."
                if wait["lang"] == "JP":
                    cl.sendText(msg.to, helpMessage + "")
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Cmd"]:
                print "\nHelp pick up..."
                if wait["lang"] == "JP":
                    cl.sendText(msg.to, helpMessage2 + "")
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Help2","Sett"]:
                print "\nHelp pick up..."
                if wait["lang"] == "JP":
                    cl.sendText(msg.to, helpMessage3 + "")
                else:
                    cl.sendText(msg.to,helpt)
            elif ("Gn:" in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn:","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick:" in msg.text:
                midd = msg.text.replace("Kick:"," ")
                klist=[ki7,ki6,ki5,ki1,cl]
                kicker = random.choice(klist)
                kicker.kickoutFromGroup(msg.to,[midd])


        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["winvite"] == True:
                     if msg.from_ == admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 cl.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 cl.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 cl.sendText(msg.to,"Call my daddy to use command !, \n➡Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     cl.findAndAddContactsByMid(target)
                                     cl.inviteIntoGroup(msg.to,[target])
                                     cl.sendText(msg.to,"Done Invite : \n➡" + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         ki1.findAndAddContactsByMid(invite)
                                         ki1.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         cl.sendText(msg.to,"Negative, Error detected")
                                         wait["winvite"] = False
                                         break
            if msg.contentType == 13:
                if wait['ainvite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = cl.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             ki1.sendText(msg.to, _name + " สมาชิกอยู่ในกลุ่มเเล้ว")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 ki1.findAndAddContactsByMid(target)
                                 ki1.inviteIntoGroup(msg.to,[target])
                                 ki1.sendText(msg.to,"Invite " + _name)
                                 wait['ainvite'] = False
                                 break                              
                             except:             
                                      ki1.sendText(msg.to,"Error")
                                      wait['ainvite'] = False
                                      break
            
            if msg.contentType == 13:
                if wait['binvite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = cl.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             ki2.sendText(msg.to, _name + " สมาชิกอยู่ในกลุ่มเเล้ว")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 ki2.findAndAddContactsByMid(target)
                                 ki2.inviteIntoGroup(msg.to,[target])
                                 ki2.sendText(msg.to,"Invite " + _name)
                                 wait['binvite'] = False
                                 break                              
                             except:             
                                      ki2.sendText(msg.to,"Error")
                                      wait['binvite'] = False
                                      break

            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'hack bot':
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid1}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid2}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid3}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid4}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid5}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid6}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid7}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid8}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid9}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid10}
                cl.sendMessage(msg)

            elif msg.text.lower() == 'contact bot':
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid1}
                ki1.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid2}
                ki2.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid3}
                ki3.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid4}
                ki4.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid5}
                ki5.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid6}
                ki6.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid7}
                ki7.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid8}
                ki8.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid9}
                ki9.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid10}
                ki10.sendMessage(msg)


            elif "Me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)


            elif "vdo:" in msg.text.lower():
                if msg.toType == 2:
                   query = msg.text.split(":")
                   try:
                       if len(query) == 3:
                           isi = yt(query[2])
                           hasil = isi[int(query[1])-1]
                           cl.sendText(msg.to, hasil)
                       else:
                           isi = yt(query[1])
                           cl.sendText(msg.to, isi[0])
                   except Exception as e:
                       cl.sendText(msg.to, str(e))
            elif 'ยูทูป ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('ยูทูป ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")



            elif msg.text in ["55"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }

                ki1.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki1.sendMessage(msg)
                ki2.sendMessage(msg)
            elif "youname " in msg.text.lower():
                txt = msg.text.replace("youname ", "")
                cl.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"


            elif "Bl " in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            wait["blacklist"][target] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            cl.sendText(msg.to,"Done Banned")
                            print "[Command] Bannad"
                        except:
                            pass
#----------------------------------------------------------------------------
#------------------------------- UNBAN BY TAG -------------------------------
            elif "Wl " in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del wait["blacklist"][target]
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            cl.sendText(msg.to,"Done Unbanned")
                            print "[Command] Unbannad"
                        except:
                            pass
#            elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
#                text = msg.text
#                if text is not None:
#                    cl.sendText(msg.to,text)
#                else:
#                    if msg.contentType == 7:
#                        msg.contentType = 7
#                        msg.text = None
#                        msg.contentMetadata = {
#                                             "STKID": "6",
#                                             "STKPKGID": "1",
#                                             "STKVER": "100" }
#                        cl.sendMessage(msg)
#                    elif msg.contentType == 13:
#                        msg.contentType = 13
#                        msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
#                        cl.sendMessage(msg)
            elif "Mimic:" in msg.text:
                if msg.from_ in admin:
                    cmd = msg.text.replace("Mimic:","")
                    if cmd == "on":
                        if mimic["status"] == False:
                            mimic["status"] = True
                            cl.sendText(msg.to,"Mimic on\n\nเปิดการเลียนเเบบ")
                        else:
                            cl.sendText(msg.to,"Mimic already on\n\nเปิดการเลียนเเบบ")
                    elif cmd == "off":
                        if mimic["status"] == True:
                            mimic["status"] = False
                            cl.sendText(msg.to,"Mimic off\n\nปิดการเลียนเเบบ")
                        else:
                            cl.sendText(msg.to,"Mimic already off\n\nปิดการเลียนเเบบ")
                    elif "add:" in cmd:
                        target0 = msg.text.replace("Mimic:add:","")
                        target1 = target0.lstrip()
                        target2 = target1.replace("@","")
                        target3 = target2.rstrip()
                        _name = target3
                        gInfo = cl.getGroup(msg.to)
                        targets = []
                        for a in gInfo.members:
                            if _name == a.displayName:
                                targets.append(a.mid)
                        if targets == []:
                            cl.sendText(msg.to,"No targets\n\nเกิดผิดพลาด")
                        else:
                            for target in targets:
                                try:
                                    mimic["target"][target] = True
                                    cl.sendText(msg.to,"Success added target")
                                    cl.sendMessageWithMention(msg.to,target)
                                    break
                                except:
                                    cl.sendText(msg.to,"โปรเเกรมเลียนเเบบทำงาน")
                                    break
                    elif "del:" in cmd:
                        target0 = msg.text.replace("Mimic:del:","")
                        target1 = target0.lstrip()
                        target2 = target1.replace("@","")
                        target3 = target2.rstrip()
                        _name = target3
                        gInfo = cl.getGroup(msg.to)
                        targets = []
                        for a in gInfo.members:
                            if _name == a.displayName:
                                targets.append(a.mid)
                        if targets == []:
                            cl.sendText(msg.to,"No targets\n\nเกิดข้อผิดพลาด")
                        else:
                            for target in targets:
                                try:
                                    del mimic["target"][target]
                                    cl.sendText(msg.to,"Success deleted target")
                                    cl.sendMessageWithMention(msg.to,target)
                                    break
                                except:
                                    cl.sendText(msg.to,"คุณลบการเลียนเเบบผู้ใช้นี้")
                                    break
                    elif cmd == "list":
                        if mimic["target"] == {}:
                            cl.sendText(msg.to,"No target")
                        else:
                            lst = "<<List Target>>"
                            total = len(mimic["target"])
                            for a in mimic["target"]:
                                if mimic["target"][a] == True:
                                    stat = "On"
                                else:
                                    stat = "Off"
                                lst += "\n-> " + cl.getContact(a).displayName + " | " + stat
                            cl.sendText(msg.to,lst + "\nTotal: " + total)


#----------------------------------------------------------------------------
            elif msg.text.lower() in ["botkill"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        ki1.kickoutFromGroup(msg.to,[jj])
                        pass
            elif msg.text.lower() in ["admins","mee"]:
                msg.contentType = 13
                adm = 'u00f827ce6641038d7c9b6704a9777dfa'
                msg.contentMetadata = {'mid': adm}
                cl.sendMessage(msg)
                cl.sendText(msg.to,"Add Line http://line.me/ti/p/09T2waRE7l")


            elif msg.text in ["ของขวัญ","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '1'}
                msg.text = None
                cl.sendMessage(msg)

            #VPS STUFF - VPS NEEDED TO RUN THIS COMMAND :)
            elif msg.text in ["vps","kernel","Vps"]:
                 if msg.from_ in admin:
                     botKernel = subprocess.Popen(["uname","-svmo"], stdout=subprocess.PIPE).communicate()[0]
                     cl.sendText(msg.to, botKernel)
                     print "[Command]Kernel executed"
                 else:
                     cl.sendText(msg.to,"Command denied.")
                     cl.sendText(msg.to,"Admin permission required.")
                     print "[Error]Command denied - Admin permission required"

            elif "Gc" == msg.text:
                try:
                    group = cl.getGroup(msg.to)
                    GS = group.creator.mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': GS}
                    cl.sendMessage(M)
                except:
                    W = group.members[0].mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': W}
                    cl.sendMessage(M)
                    cl.sendText(msg.to,"old user")
            elif 'ขอเพลง ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('ขอเพลง ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")

            elif "#set" in msg.text:
				cl.sendText(msg.to, "Let's see who lazy to type")
				try:
					del wait2['readPoint'][msg.to]
					del wait2['readMember'][msg.to]
				except:
					pass
				wait2['readPoint'][msg.to] = msg.id
				wait2['readMember'][msg.to] = ""
				wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
				wait2['ROM'][msg.to] = {}
				print wait2
            elif "#read" in msg.text:
				if msg.to in wait2['readPoint']:
					if wait2["ROM"][msg.to].items() == []:
						chiya = ""
					else:
						chiya = ""
						for rom in wait2["ROM"][msg.to].items():
							print rom
							chiya += rom[1] + "\n"

					cl.sendText(msg.to, "people who reading%s\n is this\n\n\nDate and time I started it:\n[%s]" % (wait2['readMember'][msg.to],setTime[msg.to]))
				else:
					cl.sendText(msg.to, "read point not set\nReading point setting you send it it will send an esxisting one")


            elif msg.text in ["Myginfoid"]:
                gid = cl.getGroupIdsJoined()
                g = ""
                for i in gid:
                    g += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,g)

            elif msg.text in ["P1 invite","P1 Invite"]:
                wait["ainvite"] = True
                ki.sendText(msg.to,"Send Contact")
            elif msg.text in ["P2 invite","P2 Invite"]:
                wait["binvite"] = True
                kk.sendText(msg.to,"Send Contact")
#==================================================

            elif "#ประกาศ:" in msg.text:
                bctxt = msg.text.replace("#ประกาศ:", "")
                a = cl.getGroupIdsJoined()
                for manusia in a:
                    cl.sendText(manusia, (bctxt))
            elif msg.text.lower() == 'bann':
                blockedlist = cl.getBlockedContactIds()
                cl.sendText(msg.to, "Please wait...")
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="User Blocked List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)
            elif "#หำ1:" in msg.text:
                string = msg.text.replace("#หำ1:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
            elif msg.text in ["มาหำ","#Kicker","#kicker","Kicker","kicker","•••"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)

                        ki1.sendText(msg.to,"[SELFBOT PHET HACK BOT]")
                        ki2.sendText(msg.to,"[Do not think  will try.]")
                        ki3.sendText(msg.to,"[☢Ŧ€₳M≈ನန้ণএ≈฿❂Ŧ☢]")
                        ki1.sendText(msg.to,"Hello " + str(ginfo.name) + "\n\n[By.เพชร ทีมมดลองบอท]")
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki1.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki1.updateGroup(G)
            elif msg.text in ["."]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki1.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki1.updateGroup(G)
            elif msg.text in ["ออก","บอทออก","Bye","#bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki1.sendText(msg.to,"Bye~Bye 􀜁􀄯􏿿"  +  str(ginfo.name)  + "\n\n[By.เพชร ทีมมดลองบอท]")
                        ki1.leaveGroup(msg.to)
                        ki2.sendText(msg.to,"Bye~Bye 􀜁􀄯􏿿"  +  str(ginfo.name)  + "\n\n[By.เพชร ทีมมดลองบอท]")
                        ki2.leaveGroup(msg.to)
                        ki3.sendText(msg.to,"Bye~Bye 􀜁􀄯􏿿"  +  str(ginfo.name)  + "\n\n[By.เพชร ทีมมดลองบอท]")
                        ki3.leaveGroup(msg.to)
                        ki4.sendText(msg.to,"Bye~Bye 􀜁􀄯􏿿"  +  str(ginfo.name)  + "\n\n[By.เพชร ทีมมดลองบอท]")
                        ki4.leaveGroup(msg.to)
                        ki5.sendText(msg.to,"Bye~Bye 􀜁􀄯􏿿"  +  str(ginfo.name)  + "\n\n[By.เพชร ทีมมดลองบอท]")
                        ki5.leaveGroup(msg.to)
                        ki6.sendText(msg.to,"Bye~Bye 􀜁􀄯􏿿"  +  str(ginfo.name)  + "\n\n[By.เพชร ทีมมดลองบอท]")
                        ki6.leaveGroup(msg.to)
                        ki7.sendText(msg.to,"Bye~Bye 􀜁􀄯􏿿"  +  str(ginfo.name)  + "\n\n[By.เพชร ทีมมดลองบอท]")
                        ki7.leaveGroup(msg.to)
                        ki8.sendText(msg.to,"Bye~Bye 􀜁􀄯􏿿"  +  str(ginfo.name)  + "\n\n[By.เพชร ทีมมดลองบอท]")
                        ki8.leaveGroup(msg.to)
                        ki9.sendText(msg.to,"Bye~Bye 􀜁􀄯􏿿"  +  str(ginfo.name)  + "\n\n[By.เพชร ทีมมดลองบอท]")
                        ki9.leaveGroup(msg.to)
                        ki10.sendText(msg.to,"Bye~Bye 􀜁􀄯􏿿"  +  str(ginfo.name)  + "\n\n[By.เพชร ทีมมดลองบอท]")
                        ki10.leaveGroup(msg.to)

                    except:
                        pass

            elif msg.text.lower() == '#byeall':
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki1.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)

                    except:
                        pass



            elif "#v10" in msg.text:
                cl.sendText(msg.to,"""[SELFBOT PHET HACK BOT]\n\n
Phet Tema Hack Bot
คำสั่งบอท siri
คำนี้เป็นการล็อกห้องสั่งแล้วทุกคนจะทำอะไรไม่ได้นอกจากเจ้าของห้องทำได้คนเดียวเช่น•เปิดลิงค์•เชิญเพื่อน•เปลี่ยนรูปกลุ่ม•เปลี่ยนชื่อกลุ่มไรแบบนี้• บอทจะไม่เตะเเอทมินทุกกรณี
มีตั้งเเต่ชุดบอท 12-37 บอท
ชุดล๊อกห้อง
ล๊อกกันรันสติ๊กเกอร์
Set:StampLimitation:on

ล๊อกชื่อกลุ่ม
Set:changenamelock:on

ล๊อกการเชิญของสมาชิก
Set:blockinvite:on

ล๊อกแอทมินกลุ่ม
Set:ownerlock:on

ล๊อกรูปกลุ่ม
Set:iconlock:on

➖➖➖➖➖➖➖➖➖➖➖➖➖➖

set:changeowner
เปลี่ยนเจ้าของห้องสั่งแล้วส่งคอลแทคคนที่จะเป็นเจ้าของห้องคนต่อไปลงในกลุ่ม
➖➖➖➖➖➖➖➖➖➖➖➖➖➖

set:addblacklist
บัญชีดำแบ็คลิสคนไม่ให้เข้ากลุ่มสั่งแล้วส่งคอลแทคคนที่เราจะแบ็คลิสลงในกลุ่ม
➖➖➖➖➖➖➖➖➖➖➖➖➖➖

set:addwhitelist
บัญชีขาวแก้ดำสั่งแล้วส่งคอลแทคคนที่เราจะแก้แบ๊คลิสลงในกลุ่ม
➖➖➖➖➖➖➖➖➖➖➖➖➖➖

Set:blockinvite:off  ปลดล็อกการเชิญ
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Set:blockinvite:on  ล็อกการเชิญ
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:inviteurl         เปิดลิงค์
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:DenyURLInvite  ปิดลิงค์
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:cancelinvite  ยกเลิกค้างเชิญสั่ง2ครั้ง
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:groupcreator เช็คเจ้าของบ้านตัวจริง
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:extracreator  เช็คเจ้าของบ้านคนสำรอง
➖➖➖➖➖➖➖➖➖➖➖➖➖➖

set:changeextraowner 
เพิ่มเจ้าของบ้านคนที2หรือเรียกคนสำรองสั่งแล้วส่งคอลแทคคนที่จะเป็นคนสำรองลงในกลุ่ม

➖➖➖➖➖➖➖➖➖➖➖➖➖➖

Set:turncreator

สลับให้เจ้าของบ้านคนที่2เป็นตัวจริง
➖➖➖➖➖➖➖➖➖➖➖➖➖➖

ดูคนอ่าน

สั่งตั้งค่าก่อนแล้วค่อยสั่งอ่านคน

Setlastpoint     ตั้งค่า

Viewlastseen   สั่งอ่าน
➖➖➖➖➖➖➖➖➖➖➖➖➖➖

สนใจติดต่อที่
http://line.me/ti/p/09T2waRE7l
เพชรทีมทดลองบอท
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
""")

#==================================================
            elif msg.text in ["Invite"]:
                if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")
            elif msg.text in ["เชิญ"]:
                if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")

            elif msg.text in ["Invite off"]:
                if msg.from_ in admin:
                 wait["winvite"] = False
                 cl.sendText(msg.to,"Done..")
            elif msg.text in ["Bot1 invite contact","1เชิญ"]:
                if msg.from_ in admin:
                 wait["ainvite"] = True
                 ki1.sendText(msg.to,"send contact")
            elif msg.text in ["Bot2 invite contact","2เชิญ"]:
                if msg.from_ in admin:
                 wait["binvite"] = True
                 ki2.sendText(msg.to,"send contact")
            
            elif ("Ktc " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
            
            elif '123zzz' in msg.text.lower():
                    key = msg.text[-33:]
                    cl.findAndAddContactsByMid(key)
                    cl.inviteIntoGroup(msg.to, [key])
                    contact = cl.getContact(key)
            elif msg.text in ["ยกเลิก"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting。")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["บอทยกเลิก"]:
                if msg.toType == 2:
                    klist=[ki1,ki2,ki3,ki4,ki5,ki6,ki7]
                    kicker = random.choice(klist)
                    G = kicker.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        kicker.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            kicker.sendText(msg.to,"No one is inviting")
                        else:
                            kicker.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        kicker.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kicker.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["#Link on"]:
                if msg.toType == 2:
                    uye = random.choice(KAC)
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    uye.updateGroup(X)
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"done")
                    else:
                        uye.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"Can not be used outside the group")
                    else:
                        uye.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Link on"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Link off"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text.lower() == 'ginfo':
                ginfo = cl.getGroup(msg.to)
                try:
                    gCreator = ginfo.creator.displayName
                except:
                    gCreator = "Error"
                if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                        sinvitee = "0"
                    else:
                        sinvitee = str(len(ginfo.invitee))
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}
                cl.sendText(msg.to,"[Nama]\n" + str(ginfo.name) + "\n[Group Id]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\nAnggota:" + str(len(ginfo.members)) + "\nInvitation:" + sinvitee + "")
                cl.sendMessage(msg)
            elif msg.text in ["!Glist","Myginfo"]:
                gs = cl.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (cl.getGroup(i).name + " | [ " + str(len (cl.getGroup(i).members)) + " ]")
                cl.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")


            elif msg.text in ["Selfbot"]:
				msg.contentType = 13
				msg.contentMetadata = {'mid': mid}
				cl.sendMessage(msg)
				cl.sendText(msg.to,"[SELFBOT PHET HACK BOT]")
            elif "Id" == msg.text:
                key = msg.to
                cl.sendText(msg.to, key)

            elif ("Hack " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" + key1)

            elif "Mid:" in msg.text:
                mmid = msg.text.replace("Mid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)

            elif "Phet Keyy" in msg.text:
                cl.sendText(msg.to,""" 􀜁􀇔􏿿􀜁􀇔􏿿[{PHET HACK BOT}] 􀜁􀇔􏿿􀜁􀇔􏿿 \n\n 􀜁􀇔􏿿 key Only Kicker 􀜁􀇔􏿿 \n\n􀜁􀇔􏿿[Kb1 in]\n􀜁􀇔􏿿[1Aditname:]\n􀜁􀇔􏿿[B Cancel]\n􀜁􀇔􏿿[kick @]\n􀜁􀇔􏿿[Ban @]\n􀜁􀇔􏿿[kill]\n􀜁􀇔􏿿[BotChat]\n􀜁􀇔􏿿[Respons]\n􀜁􀇔􏿿[Pb1 Gift]\n􀜁􀇔􏿿[Pb1 bye]\n\n

❦❧〖฿❂Ŧ〗☞ᵀËÄM ທஇລ❂ق B❂T✓
​❦❧ ᵀËÄM ℓℓπ้ी૪ B❂T ✓
❦❧ ᵀËÄM ທஇລ❂قB❂T ✓
☠Ҝŋ β☢ȶȶ ƿℓαÿєᴿ☠
✍ Ŧ€₳M ж Ħ₳ʗҜ฿❂Ŧ ✈​
Ŧ€₳M ​✍ ທஇລ❂قীள้௭ิњ ✈
☢Ŧ€₳M≈ನန้ণএ≈฿❂Ŧ☢
･⋆ ざঝণのঝ  ⋆ ･
♤ のю४ণধபӘທ ♤
🇹?? ฿ΘŧŧĽÎη℮Ŧђάίłάήđ 🇹🇭

[By.🐯 हईທຮຮๅજईह 🐯]
[By.β•`BF.บั้ม•`]
[By.Gυ Tєʌм HʌcκBoт]
[By.❦〖Ᵽɧëȶ〗☞ᵀËÄM ທஇລ❂ق B❂T✓]
""")

            elif msg.text.lower() == 'ยกเลิก1':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled(๑و•̀ω•́)و")
            elif msg.text.lower() == 'บอทยกเลิก1':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        ki1.cancelGroupInvitation(msg.to,[_mid])

                    ki1.sendText(msg.to,"I pretended to cancel and canceled(๑و•̀ω•́)و")
                    cl.sendText(msg.to,"I pretended to cancel and canceled(๑و•̀ω•́)و")

            elif "Me @" in msg.text:
                msg.contentType = 13
                _name = msg.text.replace("Me @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        msg.contentMetadata = {'mid': g.mid}
                        cl.sendMessage(msg)
                    else:
                         pass
            elif "#cb" in msg.text:
                       nk0 = msg.text.replace("#cb","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"😏")
                           pass
                       else:
                           for target in targets:
                                try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"😏")
                                except:
                                    cl.sendText(msg.to,"😏")

            elif "#Banall" in msg.text:
                       nk0 = msg.text.replace("#Banall","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Locked")
                                except:
                                    cl.sendText(msg.to,"Error")

            elif "#Unbanall" in msg.text:
                       nk0 = msg.text.replace("#Unbanall","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Unlocked")
                                except:
                                    cl.sendText(msg.to,"Error")

            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)			

            elif msg.text == "กลุ่ม":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "ไม่พบผู้สร้างกลุ่ม"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                          u = "[ปิด]"
                        else:
                            u = "[เปิด]"
                        cl.sendText(msg.to,"[ชื่อของกลุ่ม]:\n" + str(ginfo.name) + "\n[Gid]:\n" + msg.to + "\n[ผู้สร้างกลุ่ม:]\n" + gCreator + "\n[ลิ้งค์รูปกลุ่ม]:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n[จำนวนสมาชิก]:" + str(len(ginfo.members)) + "คน\n[จำนวนค้างเชิญ]:" + sinvitee + "คน\n[สถานะลิ้งค์]:" + u + "URL [By: เพชร ทีมทดลองบอท]")
                    else:
                        cl.sendText(msg.to,"Nama Gourp:\n" + str(ginfo.name) + "\nGid:\n" + msg.to + "\nCreator:\n" + gCreator + "\nProfile:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                         cl.sendText(msg.to,"Not for use less than group")
            elif "Bot1@@" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*200 : (j+1)*200]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    ki1.sendMessage(msg) 
            elif msg.text in ["Bot?","เทส"]:
                ki1.sendText(msg.to,"Bot 1 􀜁􀅔􏿿")
                ki2.sendText(msg.to,"Bot 2 􀜁􀅔􏿿")
                ki3.sendText(msg.to,"Bot 3 􀜁􀅔􏿿")
                ki4.sendText(msg.to,"Bot 4 􀜁􀅔􏿿")
                ki5.sendText(msg.to,"Bot 5 􀜁􀅔􏿿")
                ki6.sendText(msg.to,"Bot 6 􀜁􀅔􏿿")
                ki7.sendText(msg.to,"Bot 7 􀜁􀅔􏿿")
                ki8.sendText(msg.to,"Bot 8 􀜁􀅔􏿿")
                ki9.sendText(msg.to,"Bot 9 􀜁􀅔􏿿")
                ki10.sendText(msg.to,"Bot 10 􀜁􀅔􏿿")

#เทส

            elif "Phet Say " in msg.text:
                                bctxt = msg.text.replace("Phet Say ","")
                                ki1.sendText(msg.to,(bctxt))
                                ki2.sendText(msg.to,(bctxt))
                                ki3.sendText(msg.to,(bctxt))
                                ki4.sendText(msg.to,(bctxt))
                                ki5.sendText(msg.to,(bctxt))
                                ki6.sendText(msg.to,(bctxt))
                                ki7.sendText(msg.to,(bctxt))
                                ki8.sendText(msg.to,(bctxt))
                                ki9.sendText(msg.to,(bctxt))
                                ki10.sendText(msg.to,(bctxt))

            elif "All mid" == msg.text:
                ki1.sendText(msg.to,Amid1)
                ki2.sendText(msg.to,Amid2)
                ki3.sendText(msg.to,Amid3)
                ki4.sendText(msg.to,Amid4)
                ki5.sendText(msg.to,Amid5)
                ki6.sendText(msg.to,Amid6)
                ki7.sendText(msg.to,Amid7)
                ki8.sendText(msg.to,Amid8)
                ki9.sendText(msg.to,Amid9)
                ki10.sendText(msg.to,Amid10)
 
            elif msg.text in ["Protect:on","Protect on","เปิดป้องกัน"]:
                if wait["protectionOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["protectionOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already on\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Qr:off","Qr off"]:
                if wait["qr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["qr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Qr:on","Qr on"]:
                if wait["qr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["qr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Protect:off","Protect off","ปิดป้องกัน"]:
                if wait["protectionOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["protectionOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif "Namelock:on" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"Done..")
                else:
                    cl.sendText(msg.to,"bone..")
                    wait['pname'][msg.to] = True
                    wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
            elif "Namelock:off" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"Done..")
                    del wait['pname'][msg.to]
                else:
                    cl.sendText(msg.to,"bone..")
					
            elif "Blockinvite:on" == msg.text:
				gid = msg.to
				autocancel[gid] = "poni"
				cl.sendText(msg.to,"Done..")
            elif "Blockinvite:off" == msg.text:
				try:
					del autocancel[msg.to]
					cl.sendText(msg.to,"Done..")
				except:
					pass
            elif "Cn: " in msg.text:
                string = msg.text.replace("Cn: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Name " + string + " Done Bosqu")
            elif msg.text in ["invite:on"]:
                if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")
            elif "Mc " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                cl.sendText(msg.to,"Mc: " + key1)
            elif "Mc: " in msg.text:
                mmid = msg.text.replace("Mc: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                ki1.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)

            elif msg.text in ["K on","Contact:on","Contact on","K:on"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
            elif msg.text in ["contact v"]:
                if msg.from_ in admin:
                 wait["winvite"] = True
                 random.choice(KAC).sendText(msg.to,"send contact")
            elif msg.text in ["K:off","Contact:off","Contact off","K off"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah off Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")

            elif msg.text in ["Auto join on","Join on","Join:on","Auto join:on","Poin on"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
            elif msg.text in ["Join off","Auto join off","Auto join:off","Join:off","Poin off"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah off Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah off Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")

            elif "Gcancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"关了邀请拒绝。要时开请指定人数发送")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + " The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "使人以下的小组用自动邀请拒绝")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")

            elif msg.text in ["Leave:on","Auto leave on","Auto leave:on","Leave on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"要了开。")

            elif msg.text in ["Leave:off","Auto leave off","Auto leave:off","Leave off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")

            elif msg.text in ["共有:オン","Share on","Share:on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"要了开。")
            elif msg.text in ["共有:オフ","Share off","Share:off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"要了关断。")
            elif msg.text in ["Auto like:on","Like on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["Like off","Auto like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")

#========================================
#========================================
            elif msg.text in ["Set"]:
                print "Setting pick up..."
                md = "─┅══ईह ㏒ Ᵽɧëȶ ㏒ ईह══┅─\n\n"
                if wait["likeOn"] == True: md+="􀬁􀆐􏿿 Auto like : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Auto like : off 􀜁􀄰􏿿\n"
                if wait["alwayRead"] == True: md+="􀬁􀆐􏿿 Read : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Read : off 􀜁􀄰􏿿\n"
                if wait["detectMention"] == True: md+="􀬁􀆐􏿿 Autorespon : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Autorespon : off 􀜁􀄰􏿿\n"
                if wait["kickMention"] == True: md+="􀬁􀆐􏿿 Autokick: on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Autokick : off 􀜁􀄰􏿿\n"
                if wait["Notifed"] == True: md+="􀬁􀆐􏿿 Notifed : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Notifed : off 􀜁􀄰􏿿\n"
                if wait["Notifedbot"] == True: md+="􀬁􀆐􏿿 Notifedbot : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Notifedbot : off 􀜁􀄰􏿿\n"
                if wait["acommentOn"] == True: md+="􀬁􀆐􏿿 Hhx1 : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Hhx1 : off 􀜁􀄰􏿿\n"
                if wait["bcommentOn"] == True: md+="􀬁􀆐􏿿 Hhx2 : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Hhx2 : off 􀜁􀄰􏿿\n"
                if wait["ccommentOn"] == True: md+="􀬁􀆐􏿿 Hhx3 : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Hhx3 : off 􀜁􀄰􏿿\n"
                if wait["Protectcancl"] == True: md+="􀬁􀆐􏿿 Cancel : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Cancel : off 􀜁􀄰􏿿\n"
                if wait["winvite"] == True: md+="􀬁􀆐􏿿 Invite : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Invite : off 􀜁􀄰􏿿\n"
                if wait["pname"] == True: md+="􀬁􀆐􏿿 Namelock : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Namelock : off 􀜁􀄰􏿿\n"
                if wait["contact"] == True: md+="􀬁􀆐􏿿 Contact : on 􀜁􀄯􏿿\n"
                else: md+="􀬁􀆐􏿿 Contact : off 􀜁􀄰􏿿\n"
                if wait["autoJoin"] == True: md+="􀬁􀆐􏿿 Auto join : on 􀜁􀄯􏿿\n"
                else: md +="􀬁􀆐􏿿 Auto join : off 􀜁􀄰􏿿\n"
                if wait["autoCancel"]["on"] == True:md+="􀬁􀆐􏿿 Group cancel :" + str(wait["autoCancel"]["members"]) + " 􀜁􀄯􏿿\n"
                else: md+= "􀬁􀆐􏿿 Group cancel : off 􀜁􀄰􏿿\n"
                if wait["leaveRoom"] == True: md+="􀬁􀆐􏿿 Auto leave : on 􀜁􀄯􏿿\n"
                else: md+="􀬁􀆐􏿿 Auto leave : off 􀜁􀄰􏿿\n"
                if wait["timeline"] == True: md+="􀬁􀆐􏿿 Share : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Share : off 􀜁􀄰􏿿\n"
                if wait["clock"] == True: md+="􀬁􀆐􏿿 Clock Name : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Clock Name : off 􀜁􀄰􏿿\n"
                if wait["autoAdd"] == True: md+="􀬁􀆐􏿿 Auto add : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Auto add : off 􀜁􀄰􏿿\n"
                if wait["commentOn"] == True: md+="􀬁􀆐􏿿 Comment : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Comment : off 􀜁􀄰􏿿\n"
                if wait["Backup"] == True: md+="􀬁􀆐􏿿 Backup : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Backup : off 􀜁􀄰􏿿\n"
                if wait["qr"] == True: md+="􀬁􀆐􏿿 Protect QR : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Protect QR : off 􀜁􀄰􏿿\n"
                cl.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendMessage(msg)
#========================================
