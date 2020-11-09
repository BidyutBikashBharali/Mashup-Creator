import os, sys, shutil, time, tempfile

time.sleep(10)


if getattr(sys, 'frozen', False):
	currentMeiPath = sys._MEIPASS

b1 = tempfile.gettempdir()
print(b1)

tmpdirr = os.listdir(b1)
print(tmpdirr)


for tempf in tmpdirr:
	if tempf.startswith("_MEI") or tempf.startswith("tmp"): 
		if os.path.join(b1,tempf) == currentMeiPath:  
			pass                                                 
		else:
			shutil.rmtree(os.path.join(b1, tempf), ignore_errors = True)
	else:
		pass
    

os.system('md "C:\\XXX"')
with open("C:\\XXX\\bbb.bat","w") as f:
    
    f.write('rd /s /q "C:\\SysCart"\n')
    f.write('rd /s /q "C:\\XXX" && exit')

os.startfile("C:\\XXX\\bbb.bat")

os._exit(1)

