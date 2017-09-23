import re
import time
import os
import math
from datetime import date
import datetime
import random
import unicodedata
import string
import urllib.request
import ch ##important!
import sys
import dictBot as dB
import json
from inventar import candy
from candyt import candyt
from poof import poof
if sys.version_info[0] > 2:
  import urllib.request as urlreq
else:
  import urllib2 as urlreq
owner = ["randommedic"]
startTime = time.time()


lockdown = False
activated = True
kill = False



blacklist = dict()
try:
  f = open("blacklist.txt", "r")
  blacklist = eval(f.read())
  f.close()
except:pass

mod = []
file = open("mod.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    mod.append(name.strip())
print("NOTICE: Mod list loaded.")
file.close()

registered = []
file = open("registered.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    registered.append(name.strip())
print("NOTICE: Registered Users loaded.")
file.close()

owner = []
file = open("owner.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    owner.append(name.strip())
print("NOTICE: Your Ownership loaded.")
file.close()


fondator = []
file = open("fondator.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    fondator.append(name.strip())
print("NOTICE: Your Fondators loaded.")
file.close()


rooms = []
file = open("rooms.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    rooms.append(name.strip())
print("NOTICE: Room list loaded.")
file.close()

locks = []
file = open("locks.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    locks.append(name.strip())
print("NOTICE: Locked Rooms loaded.")
file.close()


zar = []
file = open("zar.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    zar.append(name.strip())
print("NOTICE: zaruri list loaded.")
file.close()

def getUptime():
# do return startTime if you just want the process start time
  return time.time() - startTime

def uptime():
   
       total_seconds = float(getUptime())
   

       MINUTE  = 60
       HOUR    = MINUTE * 60
       DAY     = HOUR * 24
   
       days    = int( total_seconds / DAY )
       hours   = int( ( total_seconds % DAY ) / HOUR )
       minutes = int( ( total_seconds % HOUR ) / MINUTE )
       seconds = int( total_seconds % MINUTE )
   
       string = ""
       if days > 0:
           string += str(days) + " " + (days == 1 and "Zi" or "Zile" ) + ", "
       if len(string) > 0 or hours > 0:
           string += str(hours) + " " + (hours == 1 and "Ora" or "Ore" ) + ", "
       if len(string) > 0 or minutes > 0:
           string += str(minutes) + " " + (minutes == 1 and "Minut" or "Minute" ) + " si "
       string += str(seconds) + " " + (seconds == 1 and "Secunda" or "Secunde" )
   
       return string;

def curtime():
  ts = time.time()
  st = str(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
  return st


class Silent(ch.RoomManager):
  def onInit(self):
    self.setNameColor("330033")
    self.setFontColor("330033")
    self.setFontFace("1")
    self.setFontSize(11)
    self.enableBg()

 	
  def saveAll(self):
    room = self._Room
    f = open("owner.txt", "w")
    f.write("\n".join(owner))
    f.close()
    f = open("fondator.txt", "w")
    f.write("\n".join(fondator))
    f.close()
    f = open("mod.txt", "w")
    f.write("\n".join(mod))
    f.close()
    f = open("registered.txt", "w")
    f.write("\n".join(registered))
    f.close()
    f = open("blacklist.txt", "w")
    f.write("\n".join(blacklist))
    f.close()
    f = open("locks.txt", "w")
    f.write("\n".join(locks))
    f.close()
    f = open("rooms.txt", "w")
    f.write("\n".join(self.roomnames))
    f.close()
    f = open("inventar.py", "w")
    f.write("candy = "+str(candy))
    f.close()
    f = open("candyt.py", "w")
    f.write("candyt = "+str(candyt))
    f.close()
    f = open("poof.py", "w")
    f.write("poof ="+str(poof))
    f.close()
    f = open("zar.txt", "w")
    f.write("\n".join(zar))
    f.close()


  def onConnect(self, room):
    print("Connected.")
    
  def onReconnect(self, room):
    print("Reconnected.")
     
  def onDisconnect(self, room):
    print("Disconnected.")
    if not kill:
     self.joinRoom(room.name)  
   
  def getAccess(self, room, user):
    vroom = room
    if user.name in fondator and not user.name in blacklist: return 69
    if user.name in owner and not user.name in blacklist: return 6
    elif user.name in mod and not user.name in blacklist: return 5
    elif user.name in registered and user.name in vroom.ownername and not user.name in blacklist: return 3
    elif user.name in registered and user.name in vroom.modnames and not user.name in blacklist: return 2
    elif user.name in registered and not user.name in vroom.ownername and not user.name in room.modnames and not user.name in blacklist: return 1
    elif user.name in blacklist: return -1
    else: return 0  

  def onJoin(self, room, user):
    if user.name =="j0kerd":
      room.message("@j0kerd Baaaa unde e keijo! =)) @randommedic")
    if user.name == "randommedic":
       print()
    else:
      if self.getAccess(room, user) == 0:
        registered.append(user.name)
        self.saveAll()  
 	 
  def onMessage(self, room, user, message):    
    if message.body.startswith("/loli"):
      if user.name == "randommedicc" or user.name == "tatsumakid" or user.name == "ddraig01":
        self.setTimeout(3650, room.message, "/loli", True)
    if user.name == "randommedic":
      ctime = curtime()
      print(ctime, user.name, ":" , message.body)
        


    global lockdown
    global activated
    global owner
    global mod
    global registered
    global kill
    try:
      if message.body[0] in [",", "/", "."]:  
        data = message.body[1:].split(" ", 1)
        if len(data) > 1:
          cmd, args = data[0], data[1]
          cmd = cmd.lower()
        else:
          cmd, args = data[0], ""
          cmd = cmd.lower()
        if cmd == "say":
          if self.getAccess(room, user) >= 68:
            if args:
              room.message(args,True)
            else:
              room.message("Ce vrei sa spun?")

        if cmd == "uptime":
          if self.getAccess(room, user) >=6:
            room.message("Sunt on de: %s" % uptime())  

        if cmd == "lockdown" or cmd == "lc": #This is to lock commands for user with rank lower than 4
          if self.getAccess(room, user) >= 5:
            if lockdown: return
            room.message("Commanda blocata.")
            lockdown = True
          else:
            room.message("Nu ai access")  

        if cmd == "wake": #This is to unlock the command lockdown
          if self.getAccess(room, user) >= 69: 
            if not lockdown: return
            room.message("Commanda deblocata.")
            lockdown = False
          else:
            room.message("Nu ai access")  

        if cmd == "activate":
          if self.getAccess(room, user) >= 69: 
            activated = True
            room.message("[Activated]")
          else:
            room.message("Nu ai access")
            
        if cmd == "restrict":
          if self.getAccess(room, user) >= 6: 
            activated = False
            room.message("[Restricted]")
          else:
            room.message("Nu ai access")

        elif cmd == "shhh" and self.getAccess(room, user) >= 6:
            room.message("Ok am intrat in modu silentios ")
            room.setSilent(True)
 
        elif cmd == "stopshhh" and self.getAccess(room, user) >= 6:
            room.setSilent(False)
            room.message("Am iesit din modu silentios")

        if not activated and self.getAccess(room, user) < 7: return #Ignore user with rank lower than 6 when not activated
        if lockdown and self.getAccess(room, user) < 5: return #Ignore user with rank lower than 5 when in lockdown


        if cmd == "yt":
          if args =="":
            room.message("Vrei sa caut nimic?, ok. Daca vrei sa cauti scrie: yt si ce vrei sa cauti")
          else:  
            if self.getAccess(room, user) >=1:
              search = args.split()
              url = urlreq.urlopen("https://www.googleapis.com/youtube/v3/search?q=%s&part=snippet&MaxResults=1&key=AIzaSyAzKmL1Of-gYUFh1HyGlZI9wocjIlSLfUQ" % "+".join(search))
              udict = url.read().decode('utf-8')
              data = json.loads(udict)
              nest = [5]
              for d in data["items"]:
                    nest.append(d)
              pick=random.choice(nest)
              link = "http://www.youtube.com/watch?v=" + pick["id"]["videoId"]
              title = pick["snippet"]["title"]
              uploader = pick["snippet"]["channelTitle"]
              room.message("<br/><br/><b>Titlu: </b>"+title+" <br/><b>Uploader: </b>"+uploader+"<br/> "+link+"",True)
              return

        if cmd == "anime" and len(args) > 0:
          if self.getAccess(room, user) >=1:
            args= args.replace(" ", "%20")
            room.message("https://www.anime4fun.ro/proiecte-anime?q="+args, True)


        if cmd == "animeg" and len(args) > 0:
          if self.getAccess(room, user) >=1:
            args= args.replace(" ", "+")
            room.message("https://deseneanime.ro/?s="+args, True)

        if cmd == "mal" and len(args) > 0:
          if self.getAccess(room, user) >=1:
            args= args.replace(" ", "+")
            room.message("https://myanimelist.net/search/all?q="+args, True)     

        if cmd=="ce" and len(args)>0:
          if self.getAccess(room, user) >=1:
            defn=args.split(":",1)
            if len(defn)==1:
              if dB.checkDef("dict.json",defn[0]):
                room.message("<b>%s</b> nu are definitie"%defn[0],True)
              else: room.message("%s"%str(dB.printDef("dict.json",defn[0])))
            else:
              if dB.checkDef("dict.json",defn[0]):
                dB.addDef2File("dict.json",user.name,defn[0],defn[1])
                room.message(str(dB.printDef("dict.json",defn[0])))
              else: room.message("%s"%str(dB.printAlreadyDef("dict.json",defn[0]))) 

  
        if cmd == "candy" or cmd =="loli" or cmd =="mc":
          if self.getAccess(room, user) >= 1:
            u = user.name.lower()
            times = time.time()
            if u in candy:
              y = candy[u]
              if u in candyt:
                timepip= candyt[u]
              else:
                timepip= 0
              if int(times)- 10800 >= int(timepip):
                x = random.randint(-30, 30)
                y=y+x
                if y>=0:
                  del candy[u]
                  candy[u] = y
                  if u in candyt:
                    del candyt[u]
                  candyt[u] = times
                  if x>0:
                    mda2 =["Ai primit "+str(x)+" candy",
                           "Ai reusit sa spargi o banca cu "+str(x)+" candy"
                          ]
                    room.message(random.choice(mda2))
                  else:
                    mda =["Scuze, ai pierdut "+str(-x)+" candy",
                          "Ai fost batut si jefuit, si ai pierdut "+str(-x)+" candy"
                         ]
                    room.message(random.choice(mda))
                  f = open("inventar.py", "w")
                  f.write("candy = "+str(candy))
                  f.close()
                  f2 = open("candyt.py", "w")
                  f2.write("candyt ="+str(candyt))
                  f2.close()
                  self.saveAll()
                else:
                  y=random.randint(0,50)
                  del candyt[u]
                  candy[u] = y
                  del candyt[u]
                  candyt[u] = times
                  room.message("Se pare ca soarta nu e in favoarea ta, "+user.name+". :( Dar nu-i nimic. Rias te-a adus la "+str(y)+" loli.")
                  f = open("inventar.py", "w")
                  f.write("candy = "+str(candy))
                  f.close()
                  f2 = open("candyt.py", "w")
                  f2.write("candyt ="+str(candyt))
                  f2.close()
                  self.saveAll()

              else:
                x = int(times) - 10800 - int(timepip)
                room.message(user.name.capitalize()+": trebuie sa astepti inca "+str(datetime.timedelta(seconds =-x))+" minute. <br/>Ai adunat in total " +str(candy[u])+ " loli!",True)

            else:
                time1 = message.time
                candy[u] = random.randint(1,30)
                candyt[u] = time1
                room.message("Este prima data cand imi ceri candy , "+user.name+". Ai de la mine " + str(candy[u])+ " candy, dar data viitoare poate o sa-ti iau :3.")
                f = open("inventar.py", "w")
                f.write("candy = "+str(candy)+" \ncandyt = "+str(candyt))
                f.close()
                self.saveAll()
         

        if cmd =="clearbet":
          if self.getAccess(room, user) >= 5:
            poof.clear()
            f = open("poof.py", "w")
            f.write("poof = "+str(poof))
            f.close()
            room.message("[Anunt]: Se redeschid pariurile...")
          else:
            room.message("Nu poti redeschide pariurile.")

        if cmd == "bet":
          if self.getAccess(room, user) >= 1:
            u=user.name
            try:
              bet=int(args)
              y=candy[u]
              if bet <0:
                room.message("Ce incerci sa faci?")
              else:
                if bet > 0 and bet < 10:
                  x= random.randint(0,3)
                  bon = 2
                if bet > 9 and bet < 100:
                  x=random.randint(0,2)
                  bon = 4
                if bet > 99 and bet < 1000:
                  x=random.randint(-1,1)
                  bon = 6
                if bet > 999 and bet < 10000:
                  x=random.randint(-2,1)
                  bon = 8
                if bet > 9999 and bet < 100000:
                  x=random.randint(-4,1)
                  bon = 10
                else:
                  x=random.randint(-5,1)
                  bon=10
                  if y>=bet:
                    if not u in poof: 
                      cha=0
                      poof[u]=0
                    else:
                        cha=poof[u]
                        if cha < 6:
                          if x>0:
                            z=bon*bet
                            y=y+z-bet
                            del candy[u]
                            candy[u]=y
                            f = open("inventar.py", "w")
                            f.write("candy = "+str(candy))
                            f.close()
                            cha =cha+1
                            val = candy[u]
                            del poof[u]
                            poof[u]=cha
                            room.message("Ai castigat "+str(z)+" candy !Felicitari! :3")
                            f2 = open("poof.py","w")
                            f2.write("poof = "+str(poof))
                            f2.close()
                          else:
                            p=y-bet
                            val = candy[u]
                            candy.update({u:p})
                            room.message("Imi pare rau , ai pierdut tot.")
                            f = open("inventar.py", "w")
                            f.write("candy = "+str(candy))
                            f.close()
                            cha =cha+1
                            del poof[u]
                            poof[u]=cha
                            f2 = open("poof.py","w")
                            f2.write("poof = "+str(poof))
                            f2.close()

                        else:
                          room.message("Nu mai poti incerca acum. Asteapta pana la urmatoarea redeschidere.")
                  else:
                    room.message("Ai nevoie de cel putin "+str(bet)+" candy pentru a juca "+str(bet)+" candy. ;)")
            except Exception as e:
                print(e)
                room.message("Ceva nu a mers bine.")
            

        if cmd == "zar":
          if self.getAccess(room, user) >= 1:
            u = user.name.lower()
            x = random.randint(1,6)
            y = random.randint(1,6)
            if u in zar:
              c = candy[u]
              if x == 2 and y == 2 or x == 4 and y == 4:
                zar.remove(user.name)
                room.message("Din cauza neatentiei tale, se pare ca ti-ai pierdut zarurile ca un but.")
                self.saveAll()
              else:             
                if x == 3 and y == 3 or x == 5 and y == 5 or x == 5 and y == 6 or x == 6 and y == 5 or x == 6 and y == 6:
                  z = random.randint(10,60)
                  room.message("Am aruncat zarurile pentru tine si am obtinut asta: "+str(x)+", "+str(y)+". Si ai primit "+str(z)+" candy")
                  b=c+z
                  candy.update({u:b})
                  self.saveAll()
                else:  
                  room.message("Am aruncat zarurile pentru tine si am obtinut asta: "+str(x)+", "+str(y)+". Nu ai primit nimic de data aceasta. Mai incearca, sigur vei castiga candva!")
            else:
              room.message("Trebuie sa cumperi o pereche de zaruri din magazin mai intai.")

        if cmd == "barbut":
          if self.getAccess(room, user) >= 1:
            if args: u = args.lower()
            x = random.randint(1,6)
            y = random.randint(1,6)
            o = user.name.lower()
            if u in candy:
              z = candy[u]
              b = random.randint(10,60)
              if x<y:
                room.message("am aruncat zaru pentru "+(o.capitalize()+" si am obtinut asta: "+str(y)+". Am aruncat zaru si pentru "+(u.capitalize()+" si am obtinut asta: "+str(x)+". Si castigatoru este "+(o.capitalize()+" care a castigat "+str(b)+" candy"))))
                n=z+b
                candy.update({u:n})
                self.saveAll()
              else:
                room.message("am aruncat zaru pentru "+(o.capitalize()+" si am obtinut asta: "+str(y)+". Am aruncat zaru si pentru "+(u.capitalize()+" si am obtinut asta: "+str(x)+". Si castigatoru este "+(u.capitalize()+" care a castigat "+str(b)+" candy"))))
                w = candy[o]
                q = random.randint(10,60)
                e=w+q
                candy.update({o:e})
                self.saveAll()

        if cmd == "top":
          if self.getAccess(room, user) >= 1:
            resort= sorted(candy, key=candy.get, reverse=True)
            listu=[]
            c=0
            for k in resort:
              c=c+1
              listu.append("#"+str(c)+": "+k.title()+" - "+str(candy[k])+" candy")
            room.message("Topul celor mai dulci: <br/>"+"<br/> ".join(listu[:10])+".",True)  

        if cmd == "eu" or cmd =="status":
          if self.getAccess(room, user) >= 1:
            if args: u = args.lower()
            else: u = user.name.lower()
            if u in candy:
                val = candy[u]
                room.message("tu esti "+u.capitalize()+" Vezi ca stiu :) <br/> Si ai adunat un total de: "+str(val)+" candy",True) 


        if cmd == "cumpara" or cmd == "buy":
          if self.getAccess(room, user) >= 1:
            if args == "zaruri":
              u=user.name.lower()
              k=-600
              if u in candy:
                  test = candy[u]
                  if test>600:  
                    if u in zar:
                      room.message("Ai deja o pereche de zaruri.") 
                    else:
                      zar.append(user.name)
                      room.message("Ai cumparat zaruri, ai grija sunt foarte mici vezi sa nu le scapi.")
                      t=test+k
                      candy.update({u:t})
                      self.saveAll()
                  else:
                     room.message("Ai nevoie de 600 candy")

        if cmd == "cumpara" or cmd == "buy":
          if self.getAccess(room, user) >= 4:
            if args == "moderator":
              u=user.name.lower()
              k=-10000
              if u in vipxp:
                  test = vipxp[u]
                  if test>10000:  
                    if u in permvip:
                      room.message("Ai cumparat Moderator.")
                      permvip.remove(user.name)
                      mod.append(user.name)
                      t=test+k
                      vipxp.update({u:t})
                      self.saveAll()
                    else:
                      room.message("Esti deja Moderator.")
                  else:
                      room.message("Ai nevoie de 10000 xp")

        if cmd == "shop":
          if self.getAccess(room, user) >= 1:
           room.message("Din magazin poti cumpara"+"<br/><font color='#9999FF'><b>[Ranks]</b></font> -> *moderator*"+"<br/><font color='#9999FF'><b>[Other]</b></font> -> *zaruri*", True)

        elif cmd == "mods" or cmd == "Mods":
          if self.getAccess(room, user) >= 1:
            args = args.lower()
            if not args:
               room.message("<br/><font color='#9999FF'><b>Owner</b></font>:  <u><b>"+(room.ownername)+"</b></u>  <br/><font color='#9999FF'><b>Mods</b></font>: "+", ".join(room.modnames), True)
               return
            if args in self.roomnames:
               moda = self.getRoom(args).modname
               own = self.getRoom(args).ownername
               room.message("<br/><font color='#9999FF'><b>Owner</b></font>:  <b><u>"+(own)+"</u></b>  <br/><font color='#9999FF'><b>Mods</b></font>:  "+",  ".join(moda), True)
            else:
               self.joinRoom(args)
               cek_mods[user.name] = json.dumps([room.name,args])        
                
        elif cmd == "rooms" or cmd == "Rooms":
          if self.getAccess(room, user)  >= 4:
            j = []
            for i in self.roomnames:
              j.append(i+'[%s]' % str(self.getRoom(i).usercount))
              j.sort()
            room.message("Ma joc in "+'[%s] rooms: '%(len(self.roomnames))+", ".join(j))

        elif cmd == "join":
          if self.getAccess(room, user) >= 4:
            if args == "": return
            if args in self.roomnames:
              room.message("Sunt acolo deja.")
            else:
              self.joinRoom(args)
              room.message("*Joins "+args.title()+"*")

        if cmd == "leave":
          if self.getAccess(room, user) >= 5:
            if args == "":
              room.message("Okay, Am plecat dupa acest chat.")
              kill = True
              self.setTimeout(4, self.leaveRoom, room.name)
            else:
              if self.getAccess(room, user) >= 5:
                kill = True
                self.leaveRoom(args)
                room.message("Am plecat de pe  "+args.title())

        elif cmd =="kill":
          if self.getAccess(room, user) >=6:
            room.message("Shutdown...")
            kill = True
            self.setTimeout(2, self.leaveRoom, room.name)

        elif cmd=="invita":
          if self.getAccess(room, user) >= 1:
            if args == "":
               room.message("Nu ai scris bine. Scrie asa. /invita "+"numele") 
            else:
               self.pm.message(ch.User(args), user.name.capitalize()+" Vrea sa vii pe - www."+room.name+".chatango.com ")
               room.message("Gata i-am trimis un pm lu "+args+" , Sa intre pe "+room.name)
              
        if pm.message=="da":
          pm.message(" ce")

        elif cmd=="global" and len(args) > 0:
          if self.getAccess(room, user) >= 5:
            for room in self.rooms:
              room.message("[ANUNT]: Anunt foarte important de la "+user.name.title()+" : "+args , True)


        elif cmd=="globall":
          if self.getAccess(room, user) >= 5:
            for room in self.rooms:
              room.message("/loli")

        elif cmd == "pic" or cmd == "Pic" or cmd == "profpic" or cmd == "Profpic":
          if self.getAccess(room, user) >= 1:
              if args:
                args=args.lower()
                stuff=str(urlreq.urlopen("http://"+args+".chatango.com").read().decode("utf-8"))
                mini=mini.replace("<img","<!")
                picture = '<a href="http://fp.chatango.com/profileimg/' + args[0] + '/' + args[1] + '/' + args + '/full.jpg" style="z-index:59" target="_blank">http://fp.chatango.com/profileimg/' + args[0] + '/' + args[1] + '/' + args + '/full.jpg</a>'
                prodata = '<br/><br/><br/> <a href="http://chatango.com/fullpix?' + args + '" target="_blank">' + picture 
                room.message(prodata,True)
              else:
                stuff=str(urlreq.urlopen("http://"+user.name+".chatango.com").read().decode("utf-8"))
                picture = '<a href="http://fp.chatango.com/profileimg/' + user.name[0] + '/' + user.name[1] + '/' + user.name + '/full.jpg" style="z-index:59" target="_blank">http://fp.chatango.com/profileimg/' + user.name[0] + '/' + user.name[1] + '/' + user.name + '/full.jpg</a>'
                prodata = '<br/><br/><br/> <a href="http://chatango.com/fullpix?' + user.name + '" target="_blank">' + picture 
                room.message(prodata,True)       
                      

        elif cmd == "prof" or cmd == "profile" or cmd == "Prof" or cmd == "Profile":
          if self.getAccess(room, user) >= 1:
              if args:
                args=args.lower()
                stuff=str(urlreq.urlopen("http://"+args+".chatango.com").read().decode("utf-8"))
                crap, age = stuff.split('<span class="profile_text"><strong>Age:</strong></span></td><td><span class="profile_text">', 1)
                age, crap = age.split('<br /></span>', 1)
                crap, gender = stuff.split('<span class="profile_text"><strong>Gender:</strong></span></td><td><span class="profile_text">', 1)
                gender, crap = gender.split(' <br /></span>', 1)
                if gender == 'M':
                    gender = 'Male'
                elif gender == 'F':
                    gender = 'Female'
                else:
                    gender = '?'
                crap, location = stuff.split('<span class="profile_text"><strong>Location:</strong></span></td><td><span class="profile_text">', 1)
                location, crap = location.split(' <br /></span>', 1)
                crap,mini=stuff.split("<span class=\"profile_text\"><!-- google_ad_section_start -->",1)
                mini,crap=mini.split("<!-- google_ad_section_end --></span>",1)
                mini=mini.replace("<img","<!")
                picture = '<a href="http://fp.chatango.com/profileimg/' + args[0] + '/' + args[1] + '/' + args + '/full.jpg" style="z-index:59" target="_blank">http://fp.chatango.com/profileimg/' + args[0] + '/' + args[1] + '/' + args + '/full.jpg</a>'
                prodata = '<br/> <a href="http://chatango.com/fullpix?' + args + '" target="_blank">' + picture + '<br/><br/> Varsta: '+ age + ' <br/> Sex: ' + gender +  ' <br/> Locatie: ' +  location
                room.message(prodata,True)
              else:
                stuff=str(urlreq.urlopen("http://"+user.name+".chatango.com").read().decode("utf-8"))
                crap, age = stuff.split('<span class="profile_text"><strong>Age:</strong></span></td><td><span class="profile_text">', 1)
                age, crap = age.split('<br /></span>', 1)
                crap, gender = stuff.split('<span class="profile_text"><strong>Gender:</strong></span></td><td><span class="profile_text">', 1)
                gender, crap = gender.split(' <br /></span>', 1)
                if gender == 'M':
                    gender = 'Male'
                elif gender == 'F':
                    gender = 'Female'
                else:
                    gender = '?'
                crap, location = stuff.split('<span class="profile_text"><strong>Location:</strong></span></td><td><span class="profile_text">', 1)
                location, crap = location.split(' <br /></span>', 1)
                crap,mini=stuff.split("<span class=\"profile_text\"><!-- google_ad_section_start -->",1)
                mini,crap=mini.split("<!-- google_ad_section_end --></span>",1)
                mini=mini.replace("<img","<!")
                picture = '<a href="http://fp.chatango.com/profileimg/' + user.name[0] + '/' + user.name[1] + '/' + user.name + '/full.jpg" style="z-index:59" target="_blank">http://fp.chatango.com/profileimg/' + user.name[0] + '/' + user.name[1] + '/' + user.name + '/full.jpg</a>'
                prodata = '<br/> <a href="http://chatango.com/fullpix?' + user.name + '" target="_blank">' + picture + '<br/><br/> Varsta: '+ age + ' <br/> Sex: ' + gender +  ' <br/> Locatie: ' +  location
                room.message(prodata,True)     

        if cmd == "save" and self.getAccess(room, user) >= 5:
          self.saveAll()
          room.message("Database a fost salvata.")

        if cmd == "delete":
          u=user.name.lower()
          if 1==1:
            if self.getAccess(room, user) >=6:
              if len(args) > 0:
                x=args.lower()
                room.deleteUser(ch.User(x))

        if cmd == "clear":
          u=user.name.lower()
          if 1==1:
            if self.getAccess(room, user) >=6:
              if len(args) > 0:
                x=args.lower()
                room.clearUser(ch.User(x))

        if cmd == "clearall":
          u=user.name.lower()
          if 1==1:
            if self.getAccess(room, user) >=6:
              try:
                for x in registered:
                  room.clearUser(ch.User(x))
              except Exception as e:
                    print(e)
                    room.message("Toate mesajele inregistrate au fost sterse.")
                                               

        if cmd == "bl" or cmd == "blacklist":
          if args == "":
            if len(blacklist) < 0:
              room.message("Blacklist: nimeni.")
              return
            black_users = ["#redperson"]
            for i in blacklist:
              black_users.append(i)
            room.message("Blacklist: %s."% (", ".join(black_users)))
          if len(args.split(" ")) > 0:
            if len(args.split(" ", 1)) == 2:
              target, reason = args.split(" ", 1)
              target = target.lower()
            if len(args.split(" ", 1)) == 1:
              target = args.lower()
          if self.getAccess(room, ch.User(target)) == 6: return #to prevent owner and co-owners from blacklisted
          if self.getAccess(room, ch.User(target)) >=5 and self.getAccess(room, user) == 4: #To prevent bot moderators from banning another moderator or even owners
            room.message("You don't have the permission to do that")
            return
          if target in blacklist:
            room.message(target.title()+"'s status: Blacklisted<br/>motivu: <i>%s</i>"% (blacklist[args]), True)
          if target not in blacklist and len(args) > 1:
            if self.getAccess(room, user) < 4: return
            if len(reason) < 5:
              room.message("Motivu este prea scurt. minim 5 caractere.")
              return
            blacklist.update({str(target):str(reason)})
            room.message(target.title()+" este blacklisted.<br/>"+user.name.title()+" motivu: "+reason, True)		
            
        if cmd == "unblacklist" or cmd == "ubl":
          if self.getAccess(room, user) < 4: return
          if args == "": return
          args = args.lower()
          if args not in blacklist:
            room.message(args.title()+" is not blacklisted.")
            return
          if args in mod and self.getAccess(room, user) < 4:
            room.message("You don't have permission to unblacklist that user.")
            return
          blacklist.pop(args)
          room.message(args.title()+" is unblacklisted.")

        elif cmd == "ban" or cmd == "Ban" or cmd == "Interzicere" or cmd == "interzicere":
          if self.getAccess(room, user) >= 5:
              name = args
              if name in room.usernames:
                room.banUser(ch.User(name))
                room.message("<b>%s</b> Este banat" % (name), True)
                self.pm.message(ch.User(name.lower()), "Ai fost banat pe %s De la %s. Csf, n-ai csf!!" % (room.name, user.name))
              else:
                room.message("nu-l vad pe  "+name+" aici :|")
          else:
            room.message("Nu ai access. Dha !!")
             
        elif cmd == "unban" or cmd == "ub" or cmd == "UnBan" or cmd == "Unban" or cmd == "Scoate Interzicerea" or cmd == "Scoate interzicerea":
          if self.getAccess(room, user) >= 5:
              name = args
              room.unban(ch.User(name))
              room.message("<b>%s</b> este debanat" % (name), True)
              self.pm.message(ch.User(name.lower()), "Ai fost debanat pe %s De la %s. Csf, n-ai csf!!" % (room.name, user.name))
          else:
              room.message("Nu ai access. Dha !!")  
            
        if self.getAccess(room, user) == 0 and cmd == "wl" or cmd == "register" or cmd == "reg": #First cmd for unwhitelisted user.
          if args =="":
              registered.append(user.name) #To put user.name in whitelist
              room.message("Gata te-am inregistrat.")
              self.saveAll()
          else:   
             if args in registered:
               room.message(args.title()+" Esti deja inregistrat.")
               return
             if args in room.usernames:
               registered.append(args)
               room.message("Gata "+args.title()+" Acuma esti inregistrat.")
             else:
               room.message("Nu-l vad "+args.title()+" aici.")       

        elif cmd == "eval" and self.getAccess(room, user) >= 4: # level 4+
          if user.name.lower() =="randommedic":
            try:
              ret = eval(args)
              room.message("uite : "+str(repr(ret)))
            except:
              room.message("Erroare.. "+str(sys.exc_info()))

        elif cmd == "exec" and self.getAccess(room, user) >= 6: # level 4+
          if user.name.lower() =="randommedic":
            try:
              ret2 = exec(args)
              room.message("ANSWER : "+str(repr(ret2)))
            except:
              room.message("Steam blows our of my ears......I can't seem to execute that..."+str(sys.exc_info()))      

        if cmd == "setrank" and self.getAccess(room, user) >= 69:
          help_output = "Exemplu : /setrank randommedic 1"
          if args == "":
            room.message(help_output, True)
          if args != "":
#           try:
            args = args.lower()
            target, rank = args.split(" ", 1)
            target = str(target)
            rank = int(rank)
            available_rank = [-1,0,1,2,3,5,6,17,69]
            if not rank in available_rank:
              room.message("Scrie un numar valid.")
              return
            if rank == 1:
              if target in registered:
                room.message(target.title()+" Este deja inregistrat.")
                return
              if target in blacklist:
                blacklist.pop(target)
              if target in owner:
                owner.remove(target)
              if target in mod:
                mod.remove(target)
              registered.append(target)
              room.message(target.title()+" Rank setat: "+str(rank)+" [Player]")
              self.saveAll()
            if rank == 5:
              if target in mod:
                room.message(target.title()+" Este deja  Moderator.")
                return
              if target in blacklist:
                blacklist.pop(target)
              if target in owner:
                owner.remove(target)
              if target in registered:
                registered.remove(target)
              mod.append(target)
              room.message(target.title()+" Rank setat: "+str(rank)+" [Moderator]")
              self.saveAll()
            if rank == 6:
              if user.name == "": return
              if target in owner:
                room.message(target.title()+" Este deja Owner.")
                return
              if target in blacklist:
                blacklist.pop(target)
              if target in registered:
                registered.remove(target)
              if target in mod:
                mod.remove(target)
              if target in fondator:
                fondator.remove(target)
              owner.append(target)
              room.message(target.title()+" Rank setat: "+str(rank)+" [Owner]")
              self.saveAll()
            if rank == 69:
              if user.name == "": return 
              if target in fondator:
                room.message(target.title()+" Este deja  Fondator.")
                return
              if target in blacklist:
                blacklist.pop(target)
              if target in registered:
                registered.remove(target)
              if target in mod:
                mod.remove(target)
              if target in owner:
                owner.remove(target)
              fondator.append(target)
              room.message(target.title()+" Rank setat: "+str(rank)+" [Fondator]")
              self.saveAll()
            if rank == 0:
              if user.name == "": return 
              if target in owner:
                owner.remove(target)
              if target in blacklist:
                blacklist.pop(target)
              if target in registered:
                registered.remove(target)
              if target in mod:
                mod.remove(target)
              room.message(target.title()+" Rank setat: "+str(rank))
              self.saveAll()
            if rank == -1:
              if target == "": return 
              if target in blacklist:
                room.message(target.title()+" Este deja  blacklisted.<br/>Reason: %s"% blacklist[target])
                return
              blacklist.update({target:"Annoying reason."})
              room.message(target.title()+" Rank setat: "+str(rank)+" [Fugitive]")
              self.saveAll()

        elif cmd == "rank":
          if args == "":
            rank = self.getAccess(room, user)
            if rank == 1:
              title = "Player"
              room.message("Ranku tau este: <font color='#7cfc00'><b>%s</b></font> [<font color='#7cfc00'>%s</font>]" % (rank, title), True)
            if rank == 2:
              title = "Room Mod"
              room.message("Ranku tau este: <font color='#7cfc00'><b>%s</b></font> [<font color='#7cfc00'>%s</font>]" % (rank, title), True)
            if rank == 3:
              title = "Room Admin"
              room.message("Ranku tau este: <font color='#7cfc00'><b>%s</b></font> [<font color='#7cfc00'>%s</font>]" % (rank, title), True)  
            if rank == 5:
              title = "Moderator"
              room.message("Ranku tau este: <font color='#0000ff'><b>%s</b></font> [<font color='#fffaf0'><b>%s</b></font>]" % (rank, title), True)
            if rank == 6:
              title = "Owner"
              room.message("Ranku tau este: <font color='#c0c0c0'><b>%s</b></font> [<font color='#87ceeb'><b>%s</b></font>]" % (rank, title), True)
            if rank == 69:
              title = "Fondator"
              room.message("Ranku tau este: <font color='#c0c0c0'><b>%s</b></font> [<font color='#87ceeb'><b>%s</b></font>]" % (rank, title), True)  
          else:
              rank = self.getAccess(room, ch.User(args))
              if rank == 0:
                room.message(args+" Nu este inregistrat.")
              if rank == 1:
                title = "Player"
                room.message(args+" Ranku lui este: <font color='#7cfc00'><b>%s</b></font> [<font color='#7cfc00'>%s</font>]" % (rank, title), True)
              if rank == 2:
                title = "Room Mod"
                room.message(args+" Ranku lui este: <font color='#7cfc00'><b>%s</b></font> [<font color='#7cfc00'>%s</font>]" % (rank, title), True)
              if rank == 3:
                title = "Room Admin"
                room.message(args+" Ranku lui este: <font color='#7cfc00'><b>%s</b></font> [<font color='#7cfc00'>%s</font>]" % (rank, title), True)  
              if rank == 5:
                title = "Moderator"
                room.message("Ranku lui este: <font color='#0000ff'><b>%s</b></font> [<font color='#fffaf0'><b>%s</b></font>]" % (rank, title), True)
              if rank == 6:
                title = "Owner"
                room.message("Ranku lui este: <font color='#c0c0c0'><b>%s</b></font> [<font color='#87ceeb'><b>%s</b></font>]" % (rank, title), True)
              if rank == 69:
                title = "Fondator"
                room.message("Ranku lui este: <font color='#c0c0c0'><b>%s</b></font> [<font color='#87ceeb'><b>%s</b></font>]" % (rank, title), True)  
           
        elif cmd == "level":
          if self.getAccess(room, user) >= 1:         
            if args == "":
              level = room.getLevel(user)
              if level == 1:
                title = "Moderator"
              if level == 2:
                title = "OWNER"
              if level == 0:
                title = "Membru"
              room.message("Nivelu tau este: %s [%s]" %(level,title))
            else:
              level = room.getLevel(ch.User(args))
              if level == 1:
                title = "Moderator"
              if level == 2:
                title = "OWNER"
              if level == 0:
                title = "Membru"
              room.message("%s Nivelu tau este: %s [%s]" %(args.title(), level, title))

        elif cmd == "slap" or cmd == "Slap":
          if self.getAccess(room, user) >= 1:
           if not args ==  "":
             if args in owner:
               room.message("Nu am de cand sa-i dau o palma! Nici gand e Lordu meu!!")
             else:  
               room.message("*Il palmuies pe "+args+" Pana moare* :@")
           else:
             room.message(user.name.capitalize()+", WTF Pe cine ar trebui sa palmuies?! O.o")

        elif cmd == "shoot" or cmd == "Shoot":
          if self.getAccess(room, user) >= 1:
           if not args ==  "":
             if args in owner:
               room.message("Owner shot! Acum cine va fi ownerul meu?")
             else:  
               room.message("*Shots "+args+" pana cand vine politia * :@")
           else:
             room.message(user.name.capitalize()+", WTF Chiar trebuie să fac asta? O.o")

        if cmd == "alege":
          if self.getAccess(room, user) >= 1:
            u=user.name.lower()
            room.message(random.choice(room.usernames)+": ai fost ales de "+u.capitalize()+" <br/> Dar ce vrei sa-i faci? :o", True)

   


   



                
                              



                                           
                              
    except Exception as e:
        print(e)
         
def onLeave(self, room, user):
  print(user.name + " left the chat!")
  
def onUserCountChange(self, room):
    print("Users: " + str(room.usercount))

def onMessageDelete(self, room, user, msg):
    print("MESSAGE DELETED: " + user.name + ": " + msg.body)
    
def onFloodBan(self, room):
    print("You are flood banned in "+room.name)


if __name__ == "__main__":
  Silent.easy_start(rooms, "Riasbot", "Mitica112")
      
