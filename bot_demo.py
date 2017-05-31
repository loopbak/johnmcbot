#!/usr/bin/python
#testing
from itty import *
import urllib2
import json
import requests
requests.packages.urllib3.disable_warnings()
from requests.auth import HTTPBasicAuth
import base64
import random 
from tinydb import TinyDB, Query
#import acitoolkit.acitoolkit as aci

#def acishowepg():
#    # Login to APIC
#    description = ('Simple application that logs on to the APIC'
#                   ' and displays all of the EPGs.')
#    creds = aci.Credentials('apic', description)
#    args = creds.get()
#    session = aci.Session(args.url, args.login, args.password)
#    resp = session.login()
#    if not resp.ok:
#        print('%% Could not login to APIC')
#
#    # Download all of the tenants, app profiles, and EPGs
#    # and store the names as tuples in a list
#    data = []
#    tenants = aci.Tenant.get(session)
#    for tenant in tenants:
#        apps = aci.AppProfile.get(session, tenant)
#        for app in apps:
#            epgs = aci.EPG.get(session, app, tenant)
#            for epg in epgs:
#                data.append((tenant.name, app.name, epg.name))

    # Display the data downloaded
#    template = "{0:19} {1:20} {2:15}"
#    print(template.format("TENANT", "APP_PROFILE", "EPG"))
#    print(template.format("------", "-----------", "---"))
#    for rec in data:
#        print(template.format(*rec))
#    return data

def getpisense():
    url = 'https://dweet.io/get/latest/dweet/for/databears-pi1'
    r = requests.get(url)

    binary = r.content
    output = json.loads(binary)

    numthings = len(output["with"])

    for x in range(0, numthings):
             temp = output["with"][x]["content"]["temperature"] * 9/5 + 32
             pres = output["with"][x]["content"]["pressure"] * 0.0295301
             hum = output["with"][x]["content"]["humidity"]
             pres = round(pres,1)
             temp = round(temp,1)
             hum = round(hum,1)
             
    return temp,hum,pres

def brewpeets():
    r = requests.get('http://69946291.ngrok.io/brew')

def brewbluebottle():
    r = requests.get('http://ed799fe7.ngrok.io/brew')
    
def eventbriteorder():
      response = requests.get(
         "https://www.eventbriteapi.com/v3/users/me/owned_events/?status=live",
         headers = {
             "Authorization": "Bearer JX5ONBLMAVZ7EN2HQTPT",
         },
         verify = True,  # Verify SSL certificate
     )
      data = response.json()
      events = len(data['events'])
      eventid = []
      eventname = []
      for i in range(0, events):
        eventid.append(data['events'][i]['id'])
        eventname.append(data['events'][i]['name']['text'])
      return eventid,eventname

def randombear():
    db = TinyDB('beardb.json')
    bears = db.all()
    randomurl = random.choice(bears)
    return randomurl['url'] 

def countbears():
    db = TinyDB('beardb.json')
    bears = db.all()
    bearcount = len(bears)
    return bearcount

def merakigetdevices():

    url = 'https://n131.meraki.com/api/v0/networks/L_636696397319504780/devices'
    headers = {'X-Cisco-Meraki-API-Key': '158adab9d93235d072e3258a3644d3af3b346e21'}
    devicemodel = []
    deviceserial = []
    r = requests.get(url, headers=headers)

    binary = r.content
    output = json.loads(binary)

    numdevices = len(output)
    for x in range(0, numdevices):
        devicemodel.append(output[x]["model"])
        deviceserial.append(output[x]["serial"])
    return devicemodel,deviceserial

def cmxgetclients():

   storedCredentials = True
   username = 'learning'
   password = 'learning'
   restURL = 'https://msesandbox.cisco.com:8081/api/location/v2/clients/count'

   if not storedCredentials:
           username = raw_input("Username: ")
           password = raw_input("Password: ")
           storedCredentials = True

           print("----------------------------------")
           print("Authentication string: "+ username+":"+password)
           print("Base64 encoded auth string: " + base64.b64encode(username+":"+password))
           print("----------------------------------")

   try:
           request = requests.get(
           url = restURL,
           auth = HTTPBasicAuth(username,password),
           verify=False)

           parsed = json.loads(request.content)
           clientcount = parsed['count']
           return clientcount
   except requests.exceptions.RequestException as e:
           print(e)

def cmxgetbeacons():

   storedCredentials = True
   username = 'learning'
   password = 'learning'
   restURL = 'https://msesandbox.cisco.com:8081/api/location/v1/beacon/count'

   if not storedCredentials:
           username = raw_input("Username: ")
           password = raw_input("Password: ")
           storedCredentials = True

           print("----------------------------------")
           print("Authentication string: "+ username+":"+password)
           print("Base64 encoded auth string: " + base64.b64encode(username+":"+password))
           print("----------------------------------")

   try:
           request = requests.get(
           url = restURL,
           auth = HTTPBasicAuth(username,password),
           verify=False)

           parsed = json.loads(request.content)
           beaconcount = parsed
           return beaconcount
   except requests.exceptions.RequestException as e:
           print(e)


def cmxgetclientmac():

   storedCredentials = True
   username = 'learning'
   password = 'learning'
   restURL = 'https://msesandbox.cisco.com:8081/api/location/v2/clients'
   clientmac = []
   if not storedCredentials:
           username = raw_input("Username: ")
           password = raw_input("Password: ")
           storedCredentials = True

           print("----------------------------------")
           print("Authentication string: "+ username+":"+password)
           print("Base64 encoded auth string: " + base64.b64encode(username+":"+password))
           print("----------------------------------")

   try:
           request = requests.get(
           url = restURL,
           auth = HTTPBasicAuth(username,password),
           verify=False)

           parsed = json.loads(request.content)
           clientcount = len(parsed)
           for x in range(0, clientcount):
               clientmac.append(parsed[x]["macAddress"])
           return clientmac
   except requests.exceptions.RequestException as e:
           print(e)

def sendSparkGET(url):
    """
    This method is used for:
        -retrieving message text, when the webhook is triggered with a message
        -Getting the username of the person who posted the message if a command is recognized
    """
    request = urllib2.Request(url,
                            headers={"Accept" : "application/json",
                                     "Content-Type":"application/json"})
    request.add_header("Authorization", "Bearer "+bearer)
    contents = urllib2.urlopen(request).read()
    return contents
    
def sendSparkPOST(url, data):
    """
    This method is used for:
        -posting a message to the Spark room to confirm that a command was received and processed
    """
    request = urllib2.Request(url, json.dumps(data),
                            headers={"Accept" : "application/json",
                                     "Content-Type":"application/json"})
    request.add_header("Authorization", "Bearer "+bearer)
    contents = urllib2.urlopen(request).read()
    return contents
    

@post('/')
def index(request):
    """
    When messages come in from the webhook, they are processed here.  The message text needs to be retrieved from Spark,
    using the sendSparkGet() function.  The message text is parsed.  If an expected command is found in the message,
    further actions are taken. i.e.
    /batman    - replies to the room with text
    /batcave   - echoes the incoming text to the room
    /batsignal - replies to the room with an image
    """
    webhook = json.loads(request.body)
    print webhook['data']['id']
    result = sendSparkGET('https://api.ciscospark.com/v1/messages/{0}'.format(webhook['data']['id']))
    result = json.loads(result)
    msg = ''
    if webhook['data']['personEmail'] != bot_email:
        in_message = result.get('text', '').lower()
        in_message = in_message.replace(bot_name, '')
        if 'databears' in in_message or "favorite" in in_message:
            msg = "I Love Databears!"
        elif 'brew coffee peets' in in_message:
              brewpeets()
              msg = 'Epic Coffee on the way!'
        elif 'brew coffee blue bottle' in in_message:
              brewbluebottle()
              msg = 'Epic Coffee on the way!'
        elif 'trainingdaystatus' in in_message:
            eventid,eventname = eventbriteorder()
            for i in range(0, len(eventid)):
                for x in eventname:
                    response = requests.get(
                    "https://www.eventbriteapi.com/v3/reports/attendees/?event_ids=%s" % (eventid[i], ),
                    headers = {
                    "Authorization": "Bearer JX5ONBLMAVZ7EN2HQTPT",
                    },
                    verify = True,
                    )
                data = response.json()
                msg += 'Event Name:'
                msg += eventname[i]
                msg += u'\n'
                msg += 'Event ID:'
                msg += eventid[i]
                msg += u'\n'
                msg += 'Total Attendees:'
                msg += str(data['totals']['num_attendees'])
                msg += u'\n'
                msg += 'Total Orders:'                  
                msg += str(data['totals']['num_orders'])
                msg += u'\n'
                msg += u'\n'
        elif 'trainingdayreg' in in_message:
            eventid,eventname = eventbriteorder()
            msg += "<h1>Training Day Registrations</h1>"
            for i in range(0, len(eventid)):
                    response = requests.get(
                    "https://www.eventbriteapi.com/v3/events/%s/orders" % (eventid[i], ),
                    headers = {
                    "Authorization": "Bearer JX5ONBLMAVZ7EN2HQTPT",
                    },
                    verify = True,
                    )
                    data = response.json()
                    numorders = len(data['orders'])
                    msg += "<h2>"
                    msg += eventname[i]
                    msg += "</h2>"
                    msg += u'\n\n'
                    for i in range(0, numorders):
                        msg += 'Name:'
                        msg += data['orders'][i]['name']
                        msg += u'\n'
                        msg += data['orders'][i]['email']
                        msg += u'\n\n'
        elif 'what do we do?' in in_message:
            msg = "<h1>We Hunt We Fight We WIN!<h1>"
        elif 'jimmyjams' in in_message:
            msg = "Im all about the Jimmy Jams!"
        elif 'merakidevices' in in_message:
            devicemodel,deviceserial = merakigetdevices()
            for i in range(0, len(devicemodel)):
                msg += 'Model:'
                msg += devicemodel[i]
                msg += u'\t'
                msg += 'Serial:'
                msg += deviceserial[i]                  
                msg += u'\n'
        elif 'cmxactiveclients' in in_message:
            clientcount = cmxgetclients()
            msg = "Active Clients for DevNetCampus>DevNetBuilding>DevNetZone>Zone1: %s" % clientcount
        elif 'cmxactivebeacons' in in_message:
            beaconcount = cmxgetbeacons()
            msg = "Active Beacons for DevNetCampus>DevNetBuilding>DevNetZone>Zone1: %s" % beaconcount
        elif 'cmxclientmac' in in_message:
            clientmac = cmxgetclientmac()
            for i in clientmac:
                msg += i
                msg += u'\n'
        elif 'help' in in_message:
            msg = "I only do pre sales you should call Cisco TAC at 1 800 553 2447"
        elif 'howmanybears' in in_message:
            bearcount = countbears()
            msg = bearcount
        elif 'randombear' in in_message:
            randomurl = randombear()
            sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": randomurl})
        elif 'dancingbears' in in_message:
            print "Databears get Funky!"
            sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": bat_signal})
        elif 'hulabears' in in_message:
            print "Databears get Funky!"
            sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": hula_bears})
        elif 'sharonbday' in in_message:
            sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": happy_bday})
        elif 'snorlax' in in_message:
            sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": snorlax})
        elif 'sparkboard' in in_message:
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": sparkboard})
             msg = "You really need to collaborate on Spark Board, this is what you get with Surface Hub or Google Jamboard"
        elif 'laserfocus' in in_message: 
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": laserfocus})
        elif 'manatee' in in_message:
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": manatee})
        elif 'raiders' in in_message:
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": raiders})
        elif 'touchdown' in in_message:
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": touchdown})
        elif 'osupokes' in in_message:
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": osu1})
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": osu2})
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": touchdown})
        elif 'micdrop' in in_message:
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": micdrop})
        elif 'agile' in in_message:
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": agile}) 
        elif 'ghettoblaster' in in_message:
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": ghettoblaster})
        elif 'coffee' in in_message:
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": coffee})
        elif 'jailbreak' in in_message:
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": jailbreak})
        elif 'welcometotheinternet' in in_message:
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": welcometotheinternet})
        elif 'somuchwin' in in_message:
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": somuchwin})
        elif 'mindblown' in in_message: 
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": mindblown})
        elif 'ready for a beer' in in_message:
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": beerpour})
        elif 'ready for a drink' in in_message:
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": drinkpour})
        elif 'dashboard' in in_message:
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": dashboard})
        elif 'rickrolled' in in_message:
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": rickrolled})
        elif 'walrusagrees' in in_message:
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": walrusagrees})
        elif 'happy friday' in in_message:
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": happyfriday})
        elif 'moscow mule' in in_message:
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": moscowmule})
        elif 'kieferkiefer' in in_message:
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": worry})
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": freakout})
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": nope})
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": diva})
        elif 'tablerabbit' in in_message:
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": glasslicker})
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": nathandog})
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": puglicker})
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": toiletpug})
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": wiperpug})
        elif 'wordvomit' in in_message:
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": elfvomit})
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": wordvomit})
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": babyvomit})
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": passout})
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": boring})
             sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": wrapitup})
        elif 'getpisense' in in_message:
             temp,hum,pres = getpisense()
             msg += "Temperature:"
             msg += str(temp)
             msg += "F"
             msg += "\n"
             msg += "Pressure:"
             msg += str(pres)
             msg += "in"
             msg += "\n"
             msg += "Humidity:"
             msg += str(hum)
             msg += '%'
             msg += "\n"
             msg += "See this in real time at:https://freeboard.io/board/sG-SNI"
#        elif 'acishowepg' in in_message:
#             epgdata = acishowepg()
#             msg += "ACI EPG's for: sandboxapicdc.cisco.com\n"
#             for epg in epgdata:
#	         msg += "\t**Tenant:**\t"
#                 msg += epg[0]
#                 msg += "\tApp Profile:\t"
#                 msg += epg[1]
#                 msg += "\tEPG:\t"
#                 msg += epg[2]
#                 msg += '\n'
        if msg != None:
            print msg
            sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "text": msg})
    return "true"



####CHANGE THESE VALUES#####
bot_email = "johnmcbot@sparkbot.io"
bot_name = "JohnMcBot"
bearer = "MGYzYTI4MWEtYWZiNi00MzAzLWIxZGYtZmE3MWUyOTg4YmUxYjg2MDM2NTgtZWFk"
bat_signal  = "http://www.gifbin.com/bin/163563561.gif"
happy_bday = "http://bestanimations.com/Holidays/Birthday/funnybithdaygifs/funny-star-wars-darth-vaderdancing--happy-birthday-gif.gif"
hula_bears = "http://i.imgur.com/Bz2n7KR.gif"
snorlax = "https://media.giphy.com/media/11g5IteO9JjpgA/giphy.gif"
sparkboard = "https://media.giphy.com/media/14wPFMQBn66xwI/giphy.gif"
laserfocus = "https://media.giphy.com/media/ruCg20L6H72TK/giphy.gif"
manatee = "https://media.giphy.com/media/6kbx5578gUAJa/giphy.gif"
raiders = "https://media.giphy.com/media/3ofT5yXYtGFv7G3I5O/giphy.gif"
touchdown = "https://media.giphy.com/media/1434lafyjzMk1y/source.gif"
osu1 = "https://media.giphy.com/media/291XZD4vUtiuY/giphy.gif"
osu2 = "https://media.giphy.com/media/14skUVRkuqgekg/source.gif"
micdrop = "https://media.giphy.com/media/Yt3aZ6wj8AXJK/giphy.gif"
agile = "https://media.giphy.com/media/n3FEnZX92MekM/giphy.gif"
ghettoblaster = "https://media.giphy.com/media/WI17euXijqDqU/giphy.gif"
coffee = "https://media.giphy.com/media/oZEBLugoTthxS/giphy.gif"
jailbreak = "https://media.giphy.com/media/mdyergNCRWFGM/giphy.gif"
welcometotheinternet = "https://media.giphy.com/media/zthJViY229AMU/giphy.gif"
somuchwin = "http://s2.quickmeme.com/img/0f/0ff49113f737f6725161e579f345863f0a8b6d82d260aca7a3726c18b760b024.jpg"
mindblown = "http://www.reactiongifs.com/r/2013/10/tim-and-eric-mind-blown.gif"
beerpour = "https://media.giphy.com/media/5xtDartUauedjBiErJK/giphy.gif"
drinkpour = "https://media.giphy.com/media/RuU7Q2mH0n8ac/giphy.gif"
dashboard = "https://media.giphy.com/media/eYog10JH32Aa4/giphy.gif"
rickrolled = "https://media.giphy.com/media/SdYKdGBtnTVnO/giphy.gif"
walrusagrees = "https://media.giphy.com/media/DhFI6BYOHRORq/giphy.gif"
happyfriday = "https://media.giphy.com/media/sTczweWUTxLqg/giphy.gif"
moscowmule = "https://media.giphy.com/media/bs4TCToe1x7gY/giphy.gif"
worry = "https://media.giphy.com/media/bEVKYB487Lqxy/giphy.gif"
freakout = "https://media.giphy.com/media/FwpecpDvcu7vO/giphy.gif"
nope = "https://media.giphy.com/media/6h4z4b3v6XWxO/giphy.gif"
diva = "https://media.giphy.com/media/xThuWhoaNyNBjTGERa/giphy.gif"
glasslicker = "https://media.giphy.com/media/ZB9f1T1hb6jHG/giphy.gif"
nathandog = "https://media.giphy.com/media/XK9Fpj6DWXNdK/giphy.gif"
puglicker = "https://media.giphy.com/media/NGALQBUgvmVTa/giphy.gif"
toiletpug = "https://media.giphy.com/media/qwpe4N4nulVWU/giphy.gif"
wiperpug = "https://media.giphy.com/media/M5ycS0IuXyOdO/giphy.gif"
wordvomit = "https://media.giphy.com/media/hJAtglT8jOzPW/giphy.gif"
elfvomit = "https://media.giphy.com/media/Uw9ohPF8uUik/giphy.gif"
babyvomit = "https://media.giphy.com/media/12P6AnN6DcQj1S/giphy.gif"
passout = "https://media.giphy.com/media/LTYT5GTIiAMBa/giphy.gif"
boring = "https://media.giphy.com/media/z9sFrQMfEME5a/giphy.gif"
wrapitup = "https://media.giphy.com/media/4PvmF62Tl3KLe/giphy.gif"
run_itty(server='wsgiref', host='0.0.0.0', port=10010)
