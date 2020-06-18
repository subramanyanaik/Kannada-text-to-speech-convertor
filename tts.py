import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

from tkinter import *
import tkinter
kb = tkinter.Tk()


matras=['ಾ','ಿ','ೀ','ು','ೂ','ೃ','ೆ','ೇ','ೈ','ೊ','ೋ','ೌ' ,'ಂ']
buttons = [
'ಅ','ಆ','ಇ','ಈ','ಉ','ಊ','ಋ','ಎ','ಏ','ಐ','ಒ','ಓ','ಔ','ಅಂ','ಅಃ','BACK','SPACE',
    'ಕ',

 'ಖ ', 'ಗ', 'ಘ', 'ಙ', 'ಚ', 'ಛ', 'ಜ', 'ಝ','ಞ','ಟ','ಠ',

'ಡ', 'ಢ', 'ಣ', 'ತ','ENTER', 'ಥ', 'ದ', 'ಧ', 'ನ ', 'ಪ','ಫ','ಬ','ಭ','ಮ','ಯ',
    'ರ', 'ಲ', 'ವ', 'ಶ', 'ಷ', 'ಸ', 'ಹ', 'ಳ','ಾ','ಿ','ೀ','ು','ೂ','ೃ','ೆ','ೇ','ೈ','ೊ','ೋ','ೌ','ಂ'
]

d = {'ಅ':'a.mp3','ಆ':'aa.mp3','ಇ':'i.mp3','ಈ':'ii.mp3','ಉ':'u.mp3','ಊ':'uu.mp3',	'ಎ':'e.mp3','ಏ':'ee.mp3','ಐ':'ai.mp3','ಒ':'o.mp3','ಓ':'oo.mp3','ಔ':'au.mp3','ಅಂ':'am.mp3',
     ' ':'space.mp3','ಕ':'ka.mp3','ಕಾ':'kaa.mp3','ಕಿ':'ki.mp3','ಕೀ':'kii.mp3','ಕು':'ku.mp3','ಕೂ':'kuu.mp3',	'ಕೆ':'ke.mp3','ಕೇ':'kee.mp3','ಕೈ':'kai.mp3','ಕೊ':'ko.mp3','ಕೋ':'koo.mp3','ಕೌ':'kau.mp3','ಕಂ':'kam.mp3'
     ,'ಖ':'ka.mp3','ಖಾ':'kaa.mp3','ಖಿ':'ki.mp3','ಖೀ':'kii.mp3','ಖು':'ku.mp3','ಖೂ':'kuu.mp3','ಖೆ':'ke.mp3','ಖೇ':'kee.mp3','ಖೈ':'kai.mp3','ಖೊ':'ko.mp3','ಖೋ':'koo.mp3','ಖೌ':'kau.mp3','ಖಂ':'kam.mp3',
     'ಗ':'ga.mp3','ಗಾ':'gaa.mp3','ಗಿ':'gi.mp3','ಗೀ':'gii.mp3','ಗು':'gu.mp3','ಗೂ':'guu.mp3',	'ಗೆ':'ge.mp3','ಗೇ':'gee.mp3','ಗೈ':'gai.mp3','ಗೊ':'go.mp3','ಗೋ':'goo.mp3','ಗೌ':'gau.mp3','ಗಂ':'gam.mp3',
     'ಘ':'ga.mp3','ಘಾ':'gaa.mp3','ಘಿ':'gi.mp3','ಘೀ':'gii.mp3','ಘು':'gu.mp3','ಘೂ':'guu.mp3',	'ಘೆ':'ge.mp3','ಘೇ':'gee.mp3','ಘೈ':'gai.mp3','ಘೊ':'go.mp3','ಘೋ':'goo.mp3','ಘೌ':'gau.mp3','ಘಂ':'gam.mp3',
     'ಚ':'cha.mp3','ಚಾ':'chaa.mp3','ಚಿ':'chi.mp3','ಚೀ':'chii.mp3','ಚು':'chu.mp3','ಚೂ':'chuu.mp3',	'ಚೆ':'che.mp3','ಚೇ':'chee.mp3','ಚೈ':'chai.mp3','ಚೊ':'cho.mp3','ಚೋ':'choo.mp3','ಚೌ':'chau.mp3','ಚಂ':'cham.mp3',
  'ಛ':'cha.mp3','ಛಾ':'chaa.mp3','ಛಿ':'chi.mp3','ಛೀ':'chii.mp3','ಛು':'chu.mp3','ಛೂ':'chuu.mp3',	'ಛೆ':'che.mp3','ಛೇ':'chee.mp3','ಛೈ':'chai.mp3','ಛೊ':'cho.mp3','ಛೋ':'choo.mp3','ಛೌ':'chau.mp3','ಛಂ':'cham.mp3',  
  'ಜ':'ja.mp3','ಜಾ':'jaa.mp3','ಜಿ':'ji.mp3','ಜೀ':'jii.mp3','ಜು':'ju.mp3','ಜೂ':'juu.mp3',	'ಜೆ':'je.mp3','ಜೇ':'jee.mp3','ಜೈ':'jai.mp3','ಜೊ':'jo.mp3','ಜೋ':'joo.mp3','ಜೌ':'jau.mp3','ಜಂ':'jam.mp3',  
  'ಝ':'ja.mp3','ಝಾ':'jaa.mp3','ಝಿ':'ji.mp3','ಝೀ':'jii.mp3','ಝು':'ju.mp3','ಝೂ':'juu.mp3',	'ಝೆ':'je.mp3','ಝೇ':'jee.mp3','ಝೈ':'jai.mp3','ಝೊ':'jo.mp3','ಝೋ':'joo.mp3','ಝೌ':'jau.mp3','ಝಂ':'jam.mp3',
 'ಟ': 'Ta.mp3', 'ಟಾ':'Taaa.mp3', 'ಟಿ' : 'Ti.mp3' , 'ಟೀ' : 'Tiii.mp3', 'ಟು' : 'Tu.mp3' , 'ಟೂ':'Tuu.mp3', 'ಟೃ':'Tru.mp3', 'ಟೆ':'Te.mp3', 'ಟೇ':'Tay.mp3' ,'ಟೈ':'Tie.mp3', 'ಟೊ':'To.mp3', 'ಟೋ':'Toe.mp3', 'ಟೌ':'Tau.mp3', 'ಟಂ':'Tam.mp3',
'ಠ':'Tha.mp3', 'ಠಾ':'Taaa.mp3', 'ಠಿ' : 'Ti.mp3' , 'ಠೀ' : 'Tiii.mp3', 'ಠು' : 'Tu.mp3' , 'ಠೂ':'Tuu.mp3', 'ಠೃ':'Tru.mp3', 'ಠೆ':'Te.mp3', 'ಠೇ':'Tay.mp3' ,'ಠೈ':'Tie.mp3', 'ಠೊ':'To.mp3', 'ಠೋ':'Toe.mp3', 'ಠೌ':'Tau.mp3', 'ಠಂ':'Tam.mp3',
'ಡ':'Da.mp3', 'ಡಾ':'Daa.mp3', 'ಡಿ':'Di.mp3', 'ಡೀ':'Dee.mp3', 'ಡು':'Du.mp3', 'ಡೂ':'Duu.mp3', 'ಡೃ':'Dru.mp3', 'ಡೆ':'De.mp3', 'ಡೇ':'Day.mp3', 'ಡೈ':'Die.mp3', 'ಡೊ':'Do.mp3', 'ಡೋ':'Doo.mp3', 'ಡೌ':'Dau.mp3', 'ಡಂ':'Dam.mp3',
'ಢ':'Da.mp3', 'ಢಾ':'Daa.mp3', 'ಢಿ':'Di.mp3', 'ಢೀ':'Dee.mp3', 'ಢು':'Du.mp3', 'ಢೂ':'Duu.mp3', 'ಢೃ':'Dru.mp3', 'ಢೆ':'De.mp3', 'ಢೇ':'Day.mp3', 'ಢೈ':'Die.mp3', 'ಢೊ':'Do.mp3', 'ಢೋ':'Doo.mp3', 'ಢೌ':'Dau.mp3', 'ಢಂ':'Dam.mp3',
'ಣ':'Na.mp3', 'ಣಾ':'Naa.mp3', 'ಣಿ':'Ni.mp3', 'ಣೀ':'Nii.mp3', 'ಣು':'Nu.mp3', 'ಣೂ':'Nuu.mp3', 'ಣೃ':'Nru.mp3', 'ಣೆ':'Ne.mp3', 'ಣೇ':'Nee.mp3', 'ಣೈ':'Nai.mp3', 'ಣೊ':'No.mp3', 'ಣೋ':'Noo.mp3', 'ಣೌ':'Nau.mp3', 'ಣಂ':'Nam.mp3',
'ತ':'Taa.mp3', 'ತಾ':'Thaa.mp3', 'ತಿ':'Tii.mp3', 'ತೀ':'The.mp3', 'ತು':'Thu.mp3', 'ತೂ':'Thuu.mp3', 'ತೃ':'Thru.mp3', 'ತೆ':'Tee.mp3', 'ತೇ':'Tea.mp3', 'ತೈ':'Tai.mp3', 'ತೊ':'Tho.mp3', 'ತೋ':'Thoo.mp3', 'ತೌ':'Tauu.mp3', 'ತಂ':'Tamm.mp3',
'ಥ':'Taa.mp3', 'ಥಾ':'Thaa.mp3', 'ಥಿ':'Tii.mp3', 'ಥೀ':'The.mp3', 'ಥು':'Thu.mp3', 'ಥೂ':'Thuu.mp3', 'ಥೃ':'Thru.mp3', 'ಥೆ':'Tee.mp3', 'ಥೇ':'Tea.mp3', 'ಥೈ':'Tai.mp3', 'ಥೊ':'Tho.mp3', 'ಥೋ':'Thoo.mp3', 'ಥೌ':'Tauu.mp3', 'ಥಂ':'Tamm.mp3',
'ದ':'Dha.mp3', 'ದಾ':'Dhaa.mp3', 'ದಿ':'Dii.mp3', 'ದೀ':'Thee.mp3', 'ದು':'Dhu.mp3', 'ದೂ':'Dhuu.mp3', 'ದೃ':'Dhru.mp3', 'ದೆ':'Dhe.mp3', 'ದೇ':'Dhee.mp3', 'ದೈ':'Dai.mp3', 'ದೊ':'Dho.mp3', 'ದೋ':'Dhoo.mp3', 'ದೌ':'Dauu.mp3', 'ದಂ':'Damm.mp3',
'ಧ':'Dha.mp3', 'ಧಾ':'Dhaa.mp3', 'ಧಿ':'Dii.mp3', 'ಧೀ':'Thee.mp3', 'ಧು':'Dhu.mp3', 'ಧೂ':'Dhuu.mp3', 'ಧೃ':'Dhru.mp3', 'ಧೆ':'Dhe.mp3', 'ಧೇ':'Dhee.mp3', 'ಧೈ':'Dai.mp3', 'ಧೊ':'Dho.mp3', 'ಧೋ':'Dhoo.mp3', 'ಧೌ':'Dauu.mp3', 'ಧಂ':'Damm.mp3',
'ನ':'Nha.mp3', 'ನಾ':'Nhaa.mp3', 'ನಿ':'Nhi.mp3', 'ನೀ':'Nhii.mp3', 'ನು':'Nhu.mp3', 'ನೂ':'Nhuu.mp3', 'ನೃ':'Nhru.mp3', 'ನೆ':'Nhe.mp3', 'ನೇ':'Nhee.mp3', 'ನೈ':'Nhai.mp3', 'ನೊ':'Nho.mp3', 'ನೋ':'Nhoo.mp3', 'ನೌ':'Nhau.mp3', 'ನಂ':'Nham.mp3',
'ಪ':'Pa.mp3', 'ಪಾ':'Paa.mp3', 'ಪಿ':'Pi.mp3', 'ಪೀ':'Pee.mp3', 'ಪು':'Pu.mp3', 'ಪೂ':'Poo.mp3', 'ಪೃ':'Pru.mp3', 'ಪೆ':'Pe.mp3', 'ಪೇ':'Pay.mp3', 'ಪೈ':'Pai.mp3', 'ಪೊ':'Po.mp3', 'ಪೋ':'Poe.mp3', 'ಪೌ':'Pau.mp3', 'ಪಂ':'Pam.mp3',
'ಫ':'Pa.mp3', 'ಫಾ':'Paa.mp3', 'ಫಿ':'Pi.mp3', 'ಫೀ':'Pee.mp3', 'ಫು':'Pu.mp3', 'ಫೂ':'Poo.mp3', 'ಫೃ':'Pru.mp3', 'ಫೆ':'Pe.mp3', 'ಫೇ':'Pay.mp3', 'ಫೈ':'Pai.mp3', 'ಫೊ':'Po.mp3', 'ಫೋ':'Poe.mp3', 'ಫೌ':'Pau.mp3', 'ಫಂ':'Pam.mp3',
'ಬ':'Ba.mp3', 'ಬಾ':'Baa.mp3', 'ಬಿ':'Be.mp3', 'ಬೀ':'Bee.mp3', 'ಬು':'Bu.mp3', 'ಬೂ':'Boo.mp3', 'ಬೃ':'Bru.mp3', 'ಬೆ':'Bae.mp3', 'ಬೇ':'Bay.mp3', 'ಬೈ':'Bai.mp3', 'ಬೊ':'Bo.mp3', 'ಬೋ':'Bow.mp3', 'ಬೌ':'Bau.mp3', 'ಬಂ':'Bam.mp3',
'ಭ':'Ba.mp3', 'ಭಾ':'Baa.mp3', 'ಭಿ':'Be.mp3', 'ಭೀ':'Bee.mp3', 'ಭು':'Bu.mp3', 'ಭೂ':'Boo.mp3', 'ಭೃ':'Bru.mp3', 'ಭೆ':'Bae.mp3', 'ಭೇ':'Bay.mp3', 'ಭೈ':'Bai.mp3', 'ಭೊ':'Bo.mp3', 'ಭೋ':'Bow.mp3', 'ಭೌ':'Bau.mp3', 'ಭಂ':'Bam.mp3', 
'ಯ':'ya.mp3','ಯಾ':'yaa.mp3','ಯಿ':'yi.mp3','ಯೀ':'yii.mp3','ಯು':'yu.mp3','ಯೂ':'yuu.mp3','ಯೆ':'ye.mp3','ಯೇ':'yee.mp3','ಯೊ':'yo.mp3','ಯೋ':'yoo.mp3','ಯೈ':'yai.mp3','ಯೌ':'yau.mp3','ಯಂ':'yum.mp3',
'ರ':'ra.mp3','ರಾ':'raa.mp3','ರಿ':'ri.mp3','ರೀ':'rii.mp3','ರು':'ru.mp3','ರೂ':'ruu.mp3','ರೆ':'re.mp3','ರೇ':'ree.mp3', 'ರೊ':'ro.mp3','ರೋ':'roo.mp3','ರೈ':'rai.mp3','ರೌ':'rau.mp3','ರಂ':'rum.mp3',
'ಲ':'la.mp3','ಲಾ':'laa.mp3','ಲಿ':'li.mp3','ಲೀ':'lii.mp3','ಲು':'lu.mp3','ಲೂ':'luu.mp3','ಲೆ':'le.mp3','ಲೇ':'lee.mp3','ಲೊ':'lo.mp3','ಲೋ':'loo.mp3','ಲೈ':'lai.mp3','ಲೌ':'lau.mp3','ಲಂ':'lum.mp3',
'ವ':'va.mp3','ವಾ':'vaa.mp3','ವಿ':'vi.mp3','ವೀ':'vii.mp3','ವು':'vu.mp3','ವೂ':'vuu.mp3','ವೆ':'ve.mp3','ವೇ':'vee.mp3','ವೊ':'vo.mp3','ವೋ':'voo.mp3','ವೈ':'vai.mp3','ವೌ':'vau.mp3','ವಂ':'vum.mp3',
'ಶ':'sha.mp3','ಶಾ':'shaa.mp3','ಶಿ':'shi.mp3','ಶೀ':'shii.mp3','ಶು':'shu.mp3','ಶೂ':'shuu.mp3','ಶೆ':'she.mp3','ಶೇ':'shee.mp3','ಶೊ':'sho.mp3','ಶೋ':'shoo.mp3','ಶೈ':'shai.mp3','ಶೌ':'shau.mp3','ಶಂ':'shum.mp3',
'ಮ':'ma.mp3','ಮಾ':'maa.mp3','ಮಿ':'mi.mp3','ಮೀ':'mii.mp3','ಮು':'mu.mp3','ಮೂ':'muu.mp3','ಮೆ':'me.mp3','ಮೇ':'mee.mp3', 'ಮೊ':'mo.mp3','ಮೋ':'moo.mp3','ಮೈ':'mai.mp3','ಮೌ':'mau.mp3','ಮಂ':'mum.mp3',  
  
  
  
  
  'ಹ್':'h.mp3','ಹ':'ha.mp3','ಹಾ':'haa.mp3','ಹಿ':'he.mp3','ಹೀ':'hee.mp3','ಹು':
  'hu.mp3','ಹೃ':'hru.mp3','ಹೆ':'hay.mp3','ಹೇ':'hayy.mp3','ಹೈ':'hai.mp3','ಹೊ':'ho.mp3','ಹೋ':'hoo.mp3','ಹೌ':'hou.mp3','ಹಂ':'ham.mp3','ಹಃ':''
  ,'ಸ್':'s.mp3','ಸ':'sa.mp3','ಸಾ':'saa.mp3','ಸಿ':'se.mp3','ಸೀ':'see.mp3','ಸು':'su.mp3','ಸೂ':'suu.smp3','ಸೃ':'sru.mp3','ಸೆ':'say.mp3','ಸೇ':'sayy.mp3',
  'ಸೈ':'sai.mp3','ಸೊ':'so.mp3','ಸೋ':'soo.mp3','ಸೌ':'sou.mp3','ಸಂ':'sam.mp3','ಸಃ':'',
  'ಳ':'lda.mp3','ಳಾ':'ldaa.mp3','ಳಿ':'ldi.mp3','ಳೀ':'ldii.mp3','ಳು':'ldu.mp3','ಳೂ':'lduu.mp3','ಳೃ':'ldru.mp3','ಳೆ':'lde.mp3','ಳೇ':'ldee.mp3','ಳೈ':'ldai.mp3',
   'ಳೊ':'ldo.mp3','ಳೋ':'ldoo.mp3','ಳೌ':'ldou.mp3','ಳಂ':'ldam.mp3','ಳಃ':'','ಳ್':'ld.mp3'
 }
from playsound import playsound
from pydub import AudioSegment
import scipy
from scipy.io import wavfile
import pygame
import os

def sound(s):
    listofwords=s.split(" ")
    for string in listofwords:
        l=[]
        for i in string:
            l.append(i)
        for i in range(len(l)):
            if(l[i] in matras):
                l[i-1]=l[i-1]+l[i]
                l[i]=0
        l=list(filter(None,l))
        temp= AudioSegment.empty()
        for i in l:
            s = AudioSegment.from_mp3(d[i])
            temp=temp+s
        
        temp.export("need1.wav",format='wav')
        temp
        
        
        
    
        fs, data = wavfile.read('need1.wav')
        fsp, datap = wavfile.read('space.wav')
        
        da=list(data)
        for i in range(len(da)):
            if (da[i] in range(-10,10)):
                da[i]=0
        da_new=list(filter(None,da))
                
        import numpy as np
        dat = np.array(da_new)
            
        wavfile.write("need3.wav",fs,dat)
        
        
    
        pygame.mixer.init(22000)
        sound=pygame.mixer.Sound("need3.wav")
        sound.play()
        import os
        os.remove("need3.wav")    











s="hi"
def select(value):
    global s
    if value == "BACK":
		# allText = entry.get()[:-1]
		# entry.delete(0, tkinter,END)
		# entry.insert(0,allText)

        entry.delete(len(entry.get())-1,tkinter.END)
		
    elif value == "SPACE":
        entry.insert(tkinter.END, ' ')
    elif value == " Tab ":
        entry.insert(tkinter.END, '    ')
    elif value=="ENTER":
        entry.insert(tkinter.END, '')
        s=entry.get()
        sound(s)
        
    else :
        entry.insert(tkinter.END,value)



def HosoPop():

    varRow = 2
    varColumn = 0

    for button in buttons:

        command = lambda x=button: select(x)
		
        if button == "SPACE" or button == "SHIFT" or button == "BACK":
            tkinter.Button(kb,text= button,width=8,height=2, bg="#380318", fg="#ffffff",
                activebackground = "#ffffff", activeforeground="#380318", relief='raised', padx=1,
                pady=1, bd=1,command=command).grid(row=varRow,column=varColumn)

        else:
            tkinter.Button(kb,text= button,width=8,height=2, bg="#3c4987", fg="#ffffff",
                activebackground = "#ffffff", activeforeground="#3c4987", relief='raised', padx=1,
                pady=1, bd=1,command=command).grid(row=varRow,column=varColumn)


        varColumn +=1 

        if varColumn > 16 and varRow == 2:
            varColumn = 0
            varRow+=1
        if varColumn > 16 and varRow == 3:
            varColumn = 0
            varRow+=1
        if varColumn > 16 and varRow == 4:
            varColumn = 0
            varRow+=1


def keyboard():
    kb.title("Kannada keyboard")
    kb.resizable(0,0)
	
    

    label1 = Label(kb,text='               ').grid(row=0,columnspan=15)

    global entry
    entry = Entry(kb,width=100)
    entry.grid(row=1,columnspan=16)
	# entry.pack()

    entry.bind("<Button-1>", lambda e: HosoPop())

    kb.mainloop()
    


   
    
button1 = tk.Button(text='Keyboard',command=keyboard, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)
root.mainloop()