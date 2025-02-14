import pyautogui,tkinter,subprocess,os,sys,pygame

def btn1():
    size=pyautogui.size()
    size0=str(size)
    if size0 == 'Size(width=1440, height=900)':
        feedback.set('          屏幕分辨率正常')
    else:
        feedback.set('请调节屏幕分辨率至1440,900')

def get_script():
    script_path = filepath.get()
    if not script_path: 
        feedback.set('         请先键入琴谱路径')
    else:
        feedback.set('       琴谱将于5秒后执行')
        root.after(5000, lambda: run_script(script_path))

def run_script(script_path):
    try:
        root.iconify()
        result = subprocess.run(script_path, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        feedback.set('            琴谱执行成功')
        print("琴谱执行成功", result.stdout)
    except Exception as e:
        feedback.set('                发生错误')
        print(f"发生错误: {e}")

def btn3():
    feedback.set('         右上角窗口最大化')

def btn4():
    global oc
    oc=1
    print(oc+'，捕捉')

def btn5():
    global oc
    oc=0
    print(oc+'，不捕捉')

root = tkinter.Tk()
root.minsize(400,310)
root.maxsize(1440,900)
root.title('原琴辅助演奏beta-x64')

filepath = tkinter.StringVar()
feedback = tkinter.StringVar()
oc=0

realpath = os.path.dirname(os.path.realpath(sys.argv[0]))
print ('本程序将于'+realpath+'运行，加载中。。。')

btn1= tkinter.Button(root,text='屏幕测量',
                       font=('微软雅黑',15),
                       fg=('black'),bd=5,command=btn1)
btn1.place(x=40,y=40,width=320,height=40)

btn2 = tkinter.Button(root, text='自动演奏', font=('微软雅黑', 15), fg='black', bd=5, command=get_script)
btn2.place(x=40, y=160, width=320, height=40)

btn3= tkinter.Button(root,text='模拟原琴',
                       font=('微软雅黑',15),
                       fg=('black'),bd=5,command=btn3)
btn3.place(x=40,y=100,width=320,height=40)

btn4= tkinter.Button(root,text='键盘模拟开',
                       font=('微软雅黑',15),
                       fg=('black'),bd=5,command=btn4)
btn4.place(x=908,y=420,width=110,height=40)

btn5= tkinter.Button(root,text='键盘模拟关',
                       font=('微软雅黑',15),
                       fg=('black'),bd=5,command=btn5)
btn5.place(x=1028,y=420,width=110,height=40)

ent1 = tkinter.Entry(root,textvariable=filepath)
ent1.place(x=150,y=220,width=210,height=25)

lab1 = tkinter.Label(root,text="键入琴谱路径")
lab1.place(x=40,y=220)

lab2 = tkinter.Label(root,textvariable=feedback)
lab2.place(x=110,y=250)

lab3 = tkinter.Label(root,text="Created by qinmingming")
lab3.place(x=120,y=270)

pygame.init()

sound1 = pygame.mixer.Sound('音频文件\h1.mp3')  
sound2 = pygame.mixer.Sound('音频文件\h2.mp3')
sound3 = pygame.mixer.Sound('音频文件\h3.mp3')
sound4 = pygame.mixer.Sound('音频文件\h4.mp3')
sound5 = pygame.mixer.Sound('音频文件\h5.mp3')
sound6 = pygame.mixer.Sound('音频文件\h6.mp3')
sound7 = pygame.mixer.Sound('音频文件\h7.mp3')
sound8 = pygame.mixer.Sound('音频文件\m1.mp3')
sound9 = pygame.mixer.Sound('音频文件\m2.mp3')
sound10 = pygame.mixer.Sound('音频文件\m3.mp3')
sound11 = pygame.mixer.Sound('音频文件\m4.mp3')
sound12 = pygame.mixer.Sound('音频文件\m5.mp3')
sound13 = pygame.mixer.Sound('音频文件\m6.mp3')
sound14 = pygame.mixer.Sound('音频文件\m7.mp3')
sound15 = pygame.mixer.Sound('音频文件\l1.mp3')
sound16 = pygame.mixer.Sound('音频文件\l2.mp3')
sound17 = pygame.mixer.Sound('音频文件\l3.mp3')
sound18 = pygame.mixer.Sound('音频文件\l4.mp3')
sound19 = pygame.mixer.Sound('音频文件\l5.mp3')
sound20 = pygame.mixer.Sound('音频文件\l6.mp3')
sound21 = pygame.mixer.Sound('音频文件\l7.mp3')

def h1():
    sound1.play()
def h2():
    sound2.play()
def h3():
    sound3.play()
def h4():
    sound4.play()
def h5():
    sound5.play()
def h6():
    sound6.play()
def h7():
    sound7.play()
def m1():
    sound8.play()
def m2():
    sound9.play()
def m3():
    sound10.play()
def m4():
    sound11.play()
def m5():
    sound12.play()
def m6():
    sound13.play()
def m7():
    sound14.play()
def l1():
    sound15.play()
def l2():
    sound16.play()
def l3():
    sound17.play()
def l4():
    sound18.play()
def l5():
    sound19.play()
def l6():
    sound20.play()
def l7():
    sound21.play()

btnh1= tkinter.Button(root,text='do',font=('微软雅黑',15),fg=('black'),bd=5,command=h1)
btnh1.place(x=302,y=489,width=86,height=86)

btnh2= tkinter.Button(root,text='re',font=('微软雅黑',15),fg=('black'),bd=5,command=h2)
btnh2.place(x=427,y=489,width=86,height=86)

btnh3= tkinter.Button(root,text='mi',font=('微软雅黑',15),fg=('black'),bd=5,command=h3)
btnh3.place(x=552,y=489,width=86,height=86)

btnh4= tkinter.Button(root,text='fa',font=('微软雅黑',15),fg=('black'),bd=5,command=h4)
btnh4.place(x=677,y=489,width=86,height=86)

btnh5= tkinter.Button(root,text='so',font=('微软雅黑',15),fg=('black'),bd=5,command=h5)
btnh5.place(x=802,y=489,width=86,height=86)

btnh6= tkinter.Button(root,text='la',font=('微软雅黑',15),fg=('black'),bd=5,command=h6)
btnh6.place(x=927,y=489,width=86,height=86)

btnh7= tkinter.Button(root,text='ti',font=('微软雅黑',15),fg=('black'),bd=5,command=h7)
btnh7.place(x=1052,y=489,width=86,height=86)


btnm1= tkinter.Button(root,text='do',font=('微软雅黑',15),fg=('black'),bd=5,command=m1)
btnm1.place(x=302,y=591,width=86,height=86)

btnm2= tkinter.Button(root,text='re',font=('微软雅黑',15),fg=('black'),bd=5,command=m2)
btnm2.place(x=427,y=591,width=86,height=86)

btnm3= tkinter.Button(root,text='mi',font=('微软雅黑',15),fg=('black'),bd=5,command=m3)
btnm3.place(x=552,y=591,width=86,height=86)

btnm4= tkinter.Button(root,text='fa',font=('微软雅黑',15),fg=('black'),bd=5,command=m4)
btnm4.place(x=677,y=591,width=86,height=86)

btnm5= tkinter.Button(root,text='so',font=('微软雅黑',15),fg=('black'),bd=5,command=m5)
btnm5.place(x=802,y=591,width=86,height=86)

btnm6= tkinter.Button(root,text='la',font=('微软雅黑',15),fg=('black'),bd=5,command=m6)
btnm6.place(x=927,y=591,width=86,height=86)

btnm7= tkinter.Button(root,text='ti',font=('微软雅黑',15),fg=('black'),bd=5,command=m7)
btnm7.place(x=1052,y=591,width=86,height=86)


btnl1= tkinter.Button(root,text='do',font=('微软雅黑',15),fg=('black'),bd=5,command=l1)
btnl1.place(x=302,y=693,width=86,height=86)

btnl2= tkinter.Button(root,text='re',font=('微软雅黑',15),fg=('black'),bd=5,command=l2)
btnl2.place(x=427,y=693,width=86,height=86)

btnl3= tkinter.Button(root,text='mi',font=('微软雅黑',15),fg=('black'),bd=5,command=l3)
btnl3.place(x=552,y=693,width=86,height=86)

btnl4= tkinter.Button(root,text='fa',font=('微软雅黑',15),fg=('black'),bd=5,command=l4)
btnl4.place(x=677,y=693,width=86,height=86)

btnl5= tkinter.Button(root,text='so',font=('微软雅黑',15),fg=('black'),bd=5,command=l5)
btnl5.place(x=802,y=693,width=86,height=86)

btnl6= tkinter.Button(root,text='la',font=('微软雅黑',15),fg=('black'),bd=5,command=l6)
btnl6.place(x=927,y=693,width=86,height=86)

btnl7= tkinter.Button(root,text='ti',font=('微软雅黑',15),fg=('black'),bd=5,command=l7)
btnl7.place(x=1052,y=693,width=86,height=86)

def on_key_press(event):
    if event.char.lower() == 'q':
        if oc == 1:
            sound1.play()
    if event.char.lower() == 'w':
        if oc == 1:
            sound2.play()
    if event.char.lower() == 'e':
        if oc == 1:
            sound3.play()
    if event.char.lower() == 'r':
        if oc == 1:
            sound4.play()
    if event.char.lower() == 't':
        if oc == 1:
            sound5.play()
    if event.char.lower() == 'y':
        if oc == 1:
            sound6.play()
    if event.char.lower() == 'u':
        if oc == 1:
            sound7.play()

    if event.char.lower() == 'a':
        if oc == 1:
            sound8.play()
    if event.char.lower() == 's':
        if oc == 1:
            sound9.play()
    if event.char.lower() == 'd':
        if oc == 1:
            sound10.play()
    if event.char.lower() == 'f':
        if oc == 1:
            sound11.play()
    if event.char.lower() == 'g':
        if oc == 1:
            sound12.play()
    if event.char.lower() == 'h':
        if oc == 1:
            sound13.play()
    if event.char.lower() == 'j':
        if oc == 1:
            sound14.play()

    if event.char.lower() == 'z':
        if oc == 1:
            sound15.play()
    if event.char.lower() == 'x':
        if oc == 1:
            sound16.play()
    if event.char.lower() == 'c':
        if oc == 1:
            sound17.play()
    if event.char.lower() == 'v':
        if oc == 1:
            sound18.play()
    if event.char.lower() == 'b':
        if oc == 1:
            sound19.play()
    if event.char.lower() == 'n':
        if oc == 1:
            sound20.play()
    if event.char.lower() == 'm':
        if oc == 1:
            sound21.play()

root.bind('<Key>', on_key_press)

root.mainloop()
