import pyautogui
import tkinter
from tkinter import filedialog
from PIL import Image,Image,ImageTk
import subprocess
import os
import sys
import pygame
import time
import webbrowser

def btn1():
    size=pyautogui.size()
    size0=str(size)
    if size0 == 'Size(width=1440, height=900)':
        feedback.set('                                    屏幕分辨率正常')
    else:
        feedback.set('       请调节屏幕分辨率至1440,900（如需使用模拟键盘谱）')

def btn2():
    btnh1.place_forget()
    btnh2.place_forget()
    btnh3.place_forget()
    btnh4.place_forget()
    btnh5.place_forget()
    btnh6.place_forget()
    btnh7.place_forget()
    btnm1.place_forget()
    btnm2.place_forget()
    btnm3.place_forget()
    btnm4.place_forget()
    btnm5.place_forget()
    btnm6.place_forget()
    btnm7.place_forget()
    btnl1.place_forget()
    btnl2.place_forget()
    btnl3.place_forget()
    btnl4.place_forget()
    btnl5.place_forget()
    btnl6.place_forget()
    btnl7.place_forget()
    btn4.place_forget()
    btn5.place_forget()
    lab3.place_forget()
    lab4.place_forget()
    lab6.place_forget()
    btn8.place_forget()
    btn9.place_forget()
    btn11.place_forget()
    lab5.place(x=160,y=80)
    lab8.place(x=500,y=500)
    btn1.place(x=160, y=300, width=520, height=60)
    btn6.place(x=160, y=380, width=520, height=60)
    btn10.place(x=500,y=460,width=180,height=25)
    ent1.place(x=270,y=460,width=210,height=25)
    ent2.place(x=270,y=500,width=210,height=25)
    lab1.place(x=160,y=460)
    lab2.place(x=230,y=550)
    lab7.place(x=160,y=500)

def get_script():
    script_path = filepath.get()
    if not script_path: 
        feedback.set('                                  请先键入琴谱路径')
    else:
        feedback.set('                                 琴谱将于5秒后执行')
        root.after(5000,lambda:run_script(script_path))

def run_script(script_path):
    if script_path[-4:] == '.exe':
        try:
            root.iconify()
            result = subprocess.run(script_path, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            feedback.set('                                     琴谱执行成功')
            print("琴谱执行成功", result.stdout)
        except Exception as e:
            feedback.set('                                         发生错误')
            print(f"发生错误: {e}")
    elif script_path[-4:] == '.txt':  
        try:
            length = float(s.get())
            root.iconify()
            with open(script_path,'r',encoding='utf-8') as file:
                file_content = file.read()
            keys = [file_content[i:i+5] for i in range(0, len(file_content), 5) if len(file_content[i:i+5]) == 5]
            for key in keys:
                pyautogui.hotkey(*key)
                time.sleep(length)
            feedback.set('                                     琴谱执行成功')
            print("琴谱执行成功")
        except Exception as e:
            feedback.set('                                         发生错误')
            print(f"发生错误: {e}")
    elif script_path[-3:] == '.py':
        try:
            root.iconify()
            result = subprocess.run(['python', script_path], capture_output=True, text=True)
            feedback.set('                                     琴谱执行成功')
            print("琴谱执行成功", result.stdout)
        except Exception as e:
            feedback.set('                发生错误')
            print(f"发生错误: {e}")
    else:
        try:
            root.iconify()
            result = subprocess.run(script_path, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            feedback.set('                                     琴谱执行成功')
            print("琴谱执行成功", result.stdout)
        except Exception as e:
            feedback.set('                               发生错误,且格式未知')
            print(f"发生错误: {e}")
def btn3():
    btn4.place_forget()
    btn5.place_forget()
    btn1.place_forget()
    btn6.place_forget()
    ent1.place_forget()
    ent2.place_forget()
    lab1.place_forget()
    lab2.place_forget()
    lab3.place_forget()
    lab4.place_forget()
    lab5.place_forget()
    btn8.place_forget()
    btn9.place_forget()
    btn10.place_forget()
    lab7.place_forget()
    lab8.place_forget()
    btn11.place_forget()
    lab6.place(x=160,y=80)
    btnh1.place(x=302,y=489,width=86,height=86)
    btnh2.place(x=427,y=489,width=86,height=86)
    btnh3.place(x=552,y=489,width=86,height=86)
    btnh4.place(x=677,y=489,width=86,height=86)
    btnh5.place(x=802,y=489,width=86,height=86)
    btnh6.place(x=927,y=489,width=86,height=86)
    btnh7.place(x=1052,y=489,width=86,height=86)
    btnm1.place(x=302,y=591,width=86,height=86)
    btnm2.place(x=427,y=591,width=86,height=86)
    btnm3.place(x=552,y=591,width=86,height=86)
    btnm4.place(x=677,y=591,width=86,height=86)
    btnm5.place(x=802,y=591,width=86,height=86)
    btnm6.place(x=927,y=591,width=86,height=86)
    btnm7.place(x=1052,y=591,width=86,height=86)
    btnl1.place(x=302,y=693,width=86,height=86)
    btnl2.place(x=427,y=693,width=86,height=86)
    btnl3.place(x=552,y=693,width=86,height=86)
    btnl4.place(x=677,y=693,width=86,height=86)
    btnl5.place(x=802,y=693,width=86,height=86)
    btnl6.place(x=927,y=693,width=86,height=86)
    btnl7.place(x=1052,y=693,width=86,height=86)
    btn4.place(x=908,y=420,width=110,height=40)
    btn5.place(x=1028,y=420,width=110,height=40)

def btn4():
    global oc
    oc=1

def btn5():
    global oc
    oc=0

def btn7():
    btnh1.place_forget()
    btnh2.place_forget()
    btnh3.place_forget()
    btnh4.place_forget()
    btnh5.place_forget()
    btnh6.place_forget()
    btnh7.place_forget()
    btnm1.place_forget()
    btnm2.place_forget()
    btnm3.place_forget()
    btnm4.place_forget()
    btnm5.place_forget()
    btnm6.place_forget()
    btnm7.place_forget()
    btnl1.place_forget()
    btnl2.place_forget()
    btnl3.place_forget()
    btnl4.place_forget()
    btnl5.place_forget()
    btnl6.place_forget()
    btnl7.place_forget()
    btn4.place_forget()
    btn5.place_forget()
    btn4.place_forget()
    btn5.place_forget()
    btn1.place_forget()
    btn6.place_forget()
    btn10.place_forget()
    ent1.place_forget()
    ent2.place_forget()
    lab1.place_forget()
    lab2.place_forget()
    lab5.place_forget()
    lab6.place_forget()
    lab7.place_forget()
    lab8.place_forget()
    lab4.place(x=160,y=80)
    lab3.place(x=160,y=160)
    btn8.place(x=160,y=300,width=650,height=60)
    btn9.place(x=160,y=380,width=650,height=60)
    btn11.place(x=160,y=460,width=650,height=60)

def btn8():
    url1 = 'https://www.bilibili.com/video/BV1Dnepe4EjA'
    webbrowser.open(url1)

def btn9():
    url2 = 'https://space.bilibili.com/1302740287'
    webbrowser.open(url2)

def select_file():
    file_selection=filedialog.askopenfilename()
    ent1.delete(0,tkinter.END)
    ent1.insert(0,file_selection)

def exit_script():
    root.destroy()

def load_image(path):
    image = Image.open(path)
    photo = ImageTk.PhotoImage(image)
    return photo

root = tkinter.Tk()
root.minsize(1175,800)
root.minsize(0,0)
root.title('原琴辅助演奏2.0-winx64')
root.configure(background='white')
root.geometry('1175x800+120+20')

filepath = tkinter.StringVar()
feedback = tkinter.StringVar()
oc = 0
s = tkinter.StringVar()
image_path = r'程序资源\background.png'
photo = load_image(image_path)

realpath = os.path.dirname(os.path.realpath(sys.argv[0]))
print ('本程序将于'+realpath+'运行，加载中。。。')

piclab = tkinter.Label(root,image=photo,background='white')
piclab.image = photo
piclab.place(x=160, y=40)

btn1= tkinter.Button(root,text='屏幕测量',
                       font=('微软雅黑',15),
                       fg=('black'),bd=5,background='white',command=btn1)
btn1.place(x=160, y=300, width=520, height=60)

btn2 = tkinter.Button(root, text='自动演奏',
                      font=('微软雅黑', 10),
                      fg='black', bd=5,background='white',command=btn2)
btn2.place(x=40, y=380, width=80, height=80)

btn3 = tkinter.Button(root,text='模拟原琴',
                       font=('微软雅黑',10),
                       fg=('black'),bd=5,background='white',command=btn3)
btn3.place(x=40,y=470,width=80,height=80)

btn4 = tkinter.Button(root,text='键盘监测开',
                       font=('微软雅黑',15),
                       fg=('black'),bd=5,background='white',command=btn4)
btn4.place(x=908,y=420,width=110,height=40)

btn5 = tkinter.Button(root,text='键盘监测关',
                       font=('微软雅黑',15),
                       fg=('black'),bd=5,background='white',command=btn5)
btn5.place(x=1028,y=420,width=110,height=40)

btn6 = tkinter.Button(root, text='开始演奏',
                      font=('微软雅黑', 15),
                      fg='black', bd=5,background='white',command=get_script)
btn6.place(x=160, y=380, width=520, height=60)

btn7 = tkinter.Button(root,text='首页',
                       font=('微软雅黑',10),
                       fg=('black'),bd=5,background='white',command=btn7)
btn7.place(x=40,y=290,width=80,height=80)

btn8 = tkinter.Button(root,text='使用说明',
                       font=('微软雅黑',15),
                       fg=('black'),bd=5,background='white',command=btn8)
btn8.place(x=160,y=300,width=650,height=60)

btn9 = tkinter.Button(root,text='交流反馈',
                       font=('微软雅黑',15),
                       fg=('black'),bd=5,background='white',command=btn9)
btn9.place(x=160,y=380,width=650,height=60)

btn10 = tkinter.Button(root,text='选择文件',
                       font=('微软雅黑',12),
                       fg=('black'),bd=5,background='white',command=select_file)
btn10.place(x=500,y=460,width=180,height=25)

btn11 = tkinter.Button(root,text='退出程序',
                       font=('微软雅黑',15),
                       fg=('black'),bd=5,background='white',command=exit_script)
btn11.place(x=160,y=460,width=650,height=60)

ent1 = tkinter.Entry(root,textvariable=filepath)
ent1.place(x=270,y=460,width=210,height=25)

ent2 = tkinter.Entry(root,textvariable=s)
ent2.place(x=270,y=500,width=210,height=25)

lab1 = tkinter.Label(root,text="键入琴谱路径",background='white')
lab1.place(x=160,y=460)

lab2 = tkinter.Label(root,textvariable=feedback,background='white')
lab2.place(x=230,y=550)

lab3 = tkinter.Label(root,text="Created by qinmingming",font=('微软雅黑',15,'bold italic'),background='white')
lab3.place(x=160,y=160)

lab4 = tkinter.Label(root,text="欢迎使用《原琴辅助演奏2.0-winx64》",font=('微软雅黑',30,'bold italic'),background='white')
lab4.place(x=160,y=80)

lab5 = tkinter.Label(root,text="自动演奏",font=('微软雅黑',30,'bold'),background='white')
lab5.place(x=160,y=80)

lab6 = tkinter.Label(root,text="模拟原琴",font=('微软雅黑',30,'bold'),background='white')
lab6.place(x=160,y=80)

lab7 = tkinter.Label(root,text="键入音距(文本琴谱)",background='white')
lab7.place(x=160,y=500)

lab8 = tkinter.Label(root,text="(支持浮点数、整数)",background='white')
lab8.place(x=500,y=500)

btn4.place_forget()
btn5.place_forget()
btn1.place_forget()
btn6.place_forget()
btn10.place_forget()
ent1.place_forget()
ent2.place_forget()
lab1.place_forget()
lab2.place_forget()
lab5.place_forget()
lab6.place_forget()
lab7.place_forget()
lab8.place_forget()

pygame.init()

sound1 = pygame.mixer.Sound(r'程序资源\h1.mp3')  
sound2 = pygame.mixer.Sound(r'程序资源\h2.mp3')
sound3 = pygame.mixer.Sound(r'程序资源\h3.mp3')
sound4 = pygame.mixer.Sound(r'程序资源\h4.mp3')
sound5 = pygame.mixer.Sound(r'程序资源\h5.mp3')
sound6 = pygame.mixer.Sound(r'程序资源\h6.mp3')
sound7 = pygame.mixer.Sound(r'程序资源\h7.mp3')
sound8 = pygame.mixer.Sound(r'程序资源\m1.mp3')
sound9 = pygame.mixer.Sound(r'程序资源\m2.mp3')
sound10 = pygame.mixer.Sound(r'程序资源\m3.mp3')
sound11 = pygame.mixer.Sound(r'程序资源\m4.mp3')
sound12 = pygame.mixer.Sound(r'程序资源\m5.mp3')
sound13 = pygame.mixer.Sound(r'程序资源\m6.mp3')
sound14 = pygame.mixer.Sound(r'程序资源\m7.mp3')
sound15 = pygame.mixer.Sound(r'程序资源\l1.mp3')
sound16 = pygame.mixer.Sound(r'程序资源\l2.mp3')
sound17 = pygame.mixer.Sound(r'程序资源\l3.mp3')
sound18 = pygame.mixer.Sound(r'程序资源\l4.mp3')
sound19 = pygame.mixer.Sound(r'程序资源\l5.mp3')
sound20 = pygame.mixer.Sound(r'程序资源\l6.mp3')
sound21 = pygame.mixer.Sound(r'程序资源\l7.mp3')

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

btnh1= tkinter.Button(root,text='do',font=('微软雅黑',15),fg=('black'),bd=5,command=h1,background='white')
btnh1.place(x=302,y=489,width=86,height=86)

btnh2= tkinter.Button(root,text='re',font=('微软雅黑',15),fg=('black'),bd=5,command=h2,background='white')
btnh2.place(x=427,y=489,width=86,height=86)

btnh3= tkinter.Button(root,text='mi',font=('微软雅黑',15),fg=('black'),bd=5,command=h3,background='white')
btnh3.place(x=552,y=489,width=86,height=86)

btnh4= tkinter.Button(root,text='fa',font=('微软雅黑',15),fg=('black'),bd=5,command=h4,background='white')
btnh4.place(x=677,y=489,width=86,height=86)

btnh5= tkinter.Button(root,text='so',font=('微软雅黑',15),fg=('black'),bd=5,command=h5,background='white')
btnh5.place(x=802,y=489,width=86,height=86)

btnh6= tkinter.Button(root,text='la',font=('微软雅黑',15),fg=('black'),bd=5,command=h6,background='white')
btnh6.place(x=927,y=489,width=86,height=86)

btnh7= tkinter.Button(root,text='ti',font=('微软雅黑',15),fg=('black'),bd=5,command=h7,background='white')
btnh7.place(x=1052,y=489,width=86,height=86)


btnm1= tkinter.Button(root,text='do',font=('微软雅黑',15),fg=('black'),bd=5,command=m1,background='white')
btnm1.place(x=302,y=591,width=86,height=86)

btnm2= tkinter.Button(root,text='re',font=('微软雅黑',15),fg=('black'),bd=5,command=m2,background='white')
btnm2.place(x=427,y=591,width=86,height=86)

btnm3= tkinter.Button(root,text='mi',font=('微软雅黑',15),fg=('black'),bd=5,command=m3,background='white')
btnm3.place(x=552,y=591,width=86,height=86)

btnm4= tkinter.Button(root,text='fa',font=('微软雅黑',15),fg=('black'),bd=5,command=m4,background='white')
btnm4.place(x=677,y=591,width=86,height=86)

btnm5= tkinter.Button(root,text='so',font=('微软雅黑',15),fg=('black'),bd=5,command=m5,background='white')
btnm5.place(x=802,y=591,width=86,height=86)

btnm6= tkinter.Button(root,text='la',font=('微软雅黑',15),fg=('black'),bd=5,command=m6,background='white')
btnm6.place(x=927,y=591,width=86,height=86)

btnm7= tkinter.Button(root,text='ti',font=('微软雅黑',15),fg=('black'),bd=5,command=m7,background='white')
btnm7.place(x=1052,y=591,width=86,height=86)


btnl1= tkinter.Button(root,text='do',font=('微软雅黑',15),fg=('black'),bd=5,command=l1,background='white')
btnl1.place(x=302,y=693,width=86,height=86)

btnl2= tkinter.Button(root,text='re',font=('微软雅黑',15),fg=('black'),bd=5,command=l2,background='white')
btnl2.place(x=427,y=693,width=86,height=86)

btnl3= tkinter.Button(root,text='mi',font=('微软雅黑',15),fg=('black'),bd=5,command=l3,background='white')
btnl3.place(x=552,y=693,width=86,height=86)

btnl4= tkinter.Button(root,text='fa',font=('微软雅黑',15),fg=('black'),bd=5,command=l4,background='white')
btnl4.place(x=677,y=693,width=86,height=86)

btnl5= tkinter.Button(root,text='so',font=('微软雅黑',15),fg=('black'),bd=5,command=l5,background='white')
btnl5.place(x=802,y=693,width=86,height=86)

btnl6= tkinter.Button(root,text='la',font=('微软雅黑',15),fg=('black'),bd=5,command=l6,background='white')
btnl6.place(x=927,y=693,width=86,height=86)

btnl7= tkinter.Button(root,text='ti',font=('微软雅黑',15),fg=('black'),bd=5,command=l7,background='white')
btnl7.place(x=1052,y=693,width=86,height=86)

btnh1.place_forget()
btnh2.place_forget()
btnh3.place_forget()
btnh4.place_forget()
btnh5.place_forget()
btnh6.place_forget()
btnh7.place_forget()
btnm1.place_forget()
btnm2.place_forget()
btnm3.place_forget()
btnm4.place_forget()
btnm5.place_forget()
btnm6.place_forget()
btnm7.place_forget()
btnl1.place_forget()
btnl2.place_forget()
btnl3.place_forget()
btnl4.place_forget()
btnl5.place_forget()
btnl6.place_forget()
btnl7.place_forget()

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
