# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter
import numpy as np
import matplotlib.pyplot as plt



win = tkinter.Tk()
win.title("프로그램 프로젝트")
win.geometry("800x600+100+100")
win.resizable(0,0)


class MyInformation:
    
    l1 = tkinter.Label(win, height=2, width =100, text = "\t\t\t\t개인 정보 \t\t\t\t Image processing")
    l1.pack()
    l2 = tkinter.Label(win, text = "성명").place(x=10,y=35)
    l3 = tkinter.Label(win, text = "나이").place(x=10,y=60)
    l4 = tkinter.Label(win, text = "학번").place(x=10,y=85)
    l5 = tkinter.Label(win, text = "학년").place(x=10,y=110)
    l6 = tkinter.Label(win, text = "전공").place(x=10,y=135)
    l7 = tkinter.Label(win, text = "email").place(x=10,y=160)
    l8 = tkinter.Label(win, text = "학점").place(x =30,y=220)
    l9 = tkinter.Label(win, text = "1학년").place(x =10,y=250)
    l10 = tkinter.Label(win, text = "2학년").place(x =10,y=280)
    l11 = tkinter.Label(win, text = "3학년").place(x =10,y=310)
    l12 = tkinter.Label(win, text = "4학년").place(x =10,y=340)
    
    name = tkinter.Entry(win, width=10)
    name.place(x=50,y=35)
    age = tkinter.Entry(win, width=10)
    age.place(x=50,y=60)
    studentNumber = tkinter.Entry(win, width=10)
    studentNumber.place(x=50,y=85)
    grade = tkinter.Entry(win, width=10)
    grade.place(x=50,y=110)
    major = tkinter.Entry(win, width=10)
    major.place(x=50,y=135)
    email = tkinter.Entry(win, width=10)
    email.place(x=50,y=160)
    score1 = tkinter.Entry(win, width=10)
    score1.place(x=50,y=250)
    score2 = tkinter.Entry(win, width=10)
    score2.place(x=50,y=280)
    score3 = tkinter.Entry(win, width=10)
    score3.place(x=50,y=310)
    score4 = tkinter.Entry(win, width=10)
    score4.place(x=50,y=340)


    def printText():
        #입력완료 버튼누르면 입력 내용 프린트 함수 실행/ 텍스트박스 구현
        text = tkinter.Text(win, height=15, width = 30)
        text.place(x=180,y=30)
        text.insert('current', MyInformation.name.get()+"\n")
        text.insert('end', MyInformation.age.get()+"\n")
        text.insert('end', MyInformation.studentNumber.get()+"\n")
        text.insert('end', MyInformation.grade.get()+"\n")
        text.insert('end', MyInformation.major.get()+"\n")
        text.insert('end', MyInformation.email.get()+"\n") 
        text.insert('end', MyInformation.score1.get()+"\n")
        text.insert('end', MyInformation.score2.get()+"\n")
        text.insert('end', MyInformation.score3.get()+"\n")
        text.insert('end', MyInformation.score4.get()+"\n")
        text.pack()
    
    def SaveFile():
        #txt파일을 만들고 안에 들어갈 내용 쓰기
        f = open('20205213_윤소희.txt','w')
        f.write(MyInformation.name.get() +"\n")
        f.write(MyInformation.age.get() + "\n")
        f.write(MyInformation.studentNumber.get() + "\n")
        f.write(MyInformation.grade.get() + "\n")
        f.write(MyInformation.major.get() + "\n")
        f.write(MyInformation.email.get() + "\n")
        f.write(MyInformation.score1.get() + "\n")
        f.write(MyInformation.score2.get() + "\n")
        f.write(MyInformation.score3.get() + "\n")
        f.write(MyInformation.score4.get() + "\n")
        f.close()
        
    def filePrint(): 
        #txt파일을 읽고 그 안의 내용 텍스트박스에 출력하기
        f = open('20205213_윤소희.txt','r')
        txt = f.read()
        f.close()
        text2 = tkinter.Text(win, height=15, width = 30)
        text2.place(x=180, y= 180 )
        text2.pack()
        text2.insert('0.1' , txt)

    def Image_Processing(): 
        '''
        img = tkinter.PhotoImage(file='Pic1.png')
        lbl = tkinter.Label(image=img,width=300, height =250)
        lbl.image = img  # 레퍼런스 추가
        lbl.place(x=180, y=30)
        '''
        
        img = tkinter.PhotoImage(file='Pic2.png')
        lbl = tkinter.Label(image=img,width=200, height =250)
        lbl.image = img  # 레퍼런스 추가
        lbl.place(x=550, y=30)
       
    '''
    def RC_circuit() :
        Ydat = []
        Xdat = []
        Ndat=[]
        n_max=6000
        #=== System Parameter of R-C Circuit =================
        R=100000 #Resistance
        C=0.000001 #Capacitance
        dt=0.00001 #Sampling period
        #=== Initial Output ===================================
        #Xtemp=0
        Ytemp=0
        Xdat.append(Ytemp)
        Ydat.append(Ytemp)
        num=dt/R/C
        for n in range (0,n_max):
            Xtemp=1 #Input 
            Ytemp1=Ytemp #Current Output
            Ytemp=(1-num)*Ytemp1+num*Xtemp #System Output Equation : Next Output
            Xdat.append(n*dt)
            Ydat.append(Ytemp)
            Ndat.append(n)
            
        print(Ydat)
        
        
        
        plt.figure(1)

        plt.plot(Xdat,Ydat)
        plt.xlabel('Time(sec)')
        plt.ylabel('Vc', fontsize=20)
        plt.title("Step Response")
        plt.grid(True)
        #Frequency Responso
        mag=[]
        phase=[]
        for w in range(300) :
            m = 1/np.sqrt((R*C*w)**2+1)
            p = -np.arctan(R*C*w)*180/np.pi
            mag.append(m)
            phase.append(p)
            
            
           
 
        plt.figure(2)
        plt.subplot(211)
        plt.plot(mag)
        plt.xlabel('w(rad/sec)')
        plt.ylabel('magnitude', fontsize=12)
        plt.title("Frequency Response")
        plt.grid(True)
        plt.subplot(212)
        plt.plot(phase)
        plt.xlabel('w(rad/sec)')
        plt.ylabel('phase(rad)*180/pi', fontsize=12)

        plt.grid(True)


        XXdat=np.array(0)
        YYdat=np.array(0)
        NNdat=np.array(0)
        num1=dt/R/C/2
        
        YYtemp=0
        for n in range (0,n_max):
            XXtemp=1 #Input 
            YYtemp1=YYtemp #Current Output
            YYtemp=(1-num1)*YYtemp1+num1*XXtemp #System Output Equation : Next Output
            XXdat=np.append(XXdat,n*dt)
            YYdat=np.append(YYdat,YYtemp)
            NNdat=np.append(NNdat,n)
            

        plt.figure(3)

        plt.plot(Xdat,Ydat,label="System1")
        plt.plot(XXdat,YYdat,label="System2")
        plt.xlabel('Time(sec)')
        plt.ylabel('Vc', fontsize=20)
        plt.axis([0,0.1,0,2])
        plt.legend(loc=0)
        plt.title("Step Response")
        plt.grid(True)
        #Frequency Responso
        
        '''
    
    b1 = tkinter.Button(win, width= 15, height=2, text="입력완료", command=printText).place(x=50,y=530)
    b2 = tkinter.Button(win, width= 15, height=2, text="저장", command=SaveFile).place(x=200,y=530)
    b3 = tkinter.Button(win, width= 15, height=2, text="출력", command=filePrint).place(x=340,y=530)
    #b4 = tkinter.Button(win, width= 15, height=2, text="RC circuit", command=RC_circuit).place(x=500,y=530)
    b5 = tkinter.Button(win, width= 15, height=2, text="Image processing", command=Image_Processing).place(x=650,y=530)
        
        


win.mainloop()
