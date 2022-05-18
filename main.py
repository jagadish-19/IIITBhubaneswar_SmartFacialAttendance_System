
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgb
import tkinter.simpledialog as tsd
import cv2,os
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time



def if_path_exists(path):
    dirct = os.path.dirname(path)
    if not os.path.exists(dirct):
        os.makedirs(dirct)



def tick():
    time_string = time.strftime('%H:%M:%S')
    clk.config(text=time_string)
    clk.after(200,tick)



def contactus():
    msgb._show(title='Contact us', message="Please contact us on : 'b318019@iiit-bh.ac.in, b318011@iiit-bh.ac.in' ")



def check_for_haarcascadefile():
    present = os.path.isfile("haarcascade_frontalface_default.xml")
    if present:
        pass
    else:
        msgb._show(title='Important files missing', message='Kindly contact us for help')
        window.destroy()



def save_pwd():
    if_path_exists("TrainingImageLabel/")
    present1 = os.path.isfile("TrainingImageLabel\psd.txt")
    if present1:
        ft = open("TrainingImageLabel\psd.txt", "r")
        key = ft.read()
    else:
        master.destroy()
        new_pwd = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_pwd == None:
            msgb._show(title='No Password Entered', message='Password is not set yet!! Please try again')
        else:
            ft = open("TrainingImageLabel\psd.txt", "w")
            ft.write(new_pwd)
            msgb._show(title='Password Registered', message='New password has been registered successfully!!')
            return
    op = (old.get())
    newp= (new.get())
    nnewp = (nnew.get())
    if (op == key):
        if(newp == nnewp):
            tfx = open("TrainingImageLabel\psd.txt", "w")
            tfx.write(newp)
        else:
            msgb._show(title='Error', message='Please Confirm new password again!!!')
            return
    else:
        msgb._show(title='Wrong Password', message='Please enter the correct old password.')
        return
    msgb._show(title='Password Changed', message='Password has been changed !!')
    master.destroy()



def change_pwd():
    global master
    master = tk.Tk()
    master.geometry("400x160")
    master.resizable(False,False)
    master.title("Change Password")
    master.configure(background="white")
    ltb4 = tk.Label(master,text='    Enter Old Password',bg='white',font=('times', 12, ' bold '))
    ltb4.place(x=10,y=10)
    global old
    old=tk.Entry(master,width=25 ,fg="black",relief='solid',font=('times', 12, ' bold '),show='*')
    old.place(x=180,y=10)
    ltb5 = tk.Label(master, text='   Enter New Password', bg='white', font=('times', 12, ' bold '))
    ltb5.place(x=10, y=45)
    global new
    new = tk.Entry(master, width=25, fg="black",relief='solid', font=('times', 12, ' bold '),show='*')
    new.place(x=180, y=45)
    ltb6 = tk.Label(master, text='Confirm New Password', bg='white', font=('times', 12, ' bold '))
    ltb6.place(x=10, y=80)
    global nnew
    nnew = tk.Entry(master, width=25, fg="black", relief='solid',font=('times', 12, ' bold '),show='*')
    nnew.place(x=180, y=80)
    cncl=tk.Button(master,text="Cancel", command=master.destroy ,fg="black"  ,bg="red" ,height=1,width=25 , activebackground = "white" ,font=('times', 10, ' bold '))
    cncl.place(x=200, y=120)
    sv1 = tk.Button(master, text="Save", command=save_pwd, fg="black", bg="#3ece48", height = 1,width=25, activebackground="white", font=('times', 10, ' bold '))
    sv1.place(x=10, y=120)
    master.mainloop()



def pwd():
    if_path_exists("TrainingImageLabel/")
    present1 = os.path.isfile("TrainingImageLabel\psd.txt")
    if present1:
        ft = open("TrainingImageLabel\psd.txt", "r")
        key = ft.read()
    else:
        new_pwd = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_pwd == None:
            msgb._show(title='No Password Entered', message='Password is not set!! Please try again later')
        else:
            ft = open("TrainingImageLabel\psd.txt", "w")
            ft.write(new_pwd)
            msgb._show(title='Password Registered', message='New password registered successfully!!')
            return
    password = tsd.askstring('Password', 'Enter Password', show='*')
    if (password == key):
        TrainFaces()
    elif (password == None):
        pass
    else:
        msgb._show(title='Wrong Password', message='You have entered the wrong password')



def clr():
    txt.delete(0, 'end')
    res = "1)Take Images  >>>  2)Save Profile"
    msg1.configure(text=res)


def clr2():
    txt2.delete(0, 'end')
    res = "1)Take Images  >>>  2)Save Profile"
    msg1.configure(text=res)



def TakeFaces():
    check_for_haarcascadefile()
    columns = ['SERIAL NO.', '', 'ID', '', 'NAME']
    if_path_exists("StudentDetails/")
    if_path_exists("TrainingImage/")
    serial = 0
    present = os.path.isfile("StudentDetails\StudentDetails.csv")
    if present:
        with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
            rdr1 = csv.reader(csvFile1)
            for l in rdr1:
                serial = serial + 1
        serial = (serial // 2)
        csvFile1.close()
    else:
        with open("StudentDetails\StudentDetails.csv", 'a+') as csvFile1:
            wrtr = csv.writer(csvFile1)
            wrtr.writerow(columns)
            serial = 1
        csvFile1.close()
    Id = (txt.get())
    name = (txt2.get())
    if ((name.isalpha()) or (' ' in name)):
        camera = cv2.VideoCapture(0)
        haarcascadePath = "haarcascade_frontalface_default.xml"
        detection = cv2.CascadeClassifier(haarcascadePath)
        sampleNum = 0
        while (True):
            ret, img = camera.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detection.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                
                sampleNum = sampleNum + 1
                
                cv2.imwrite("TrainingImage\ " + name + "." + str(serial) + "." + Id + '.' + str(sampleNum) + ".jpg",
                            gray[y:y + h, x:x + w])
                
                cv2.imshow('Taking Images', img)
            
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            
            elif sampleNum > 100:
                break
        camera.release()
        cv2.destroyAllWindows()
        res = "Images Taken for ID : " + Id
        row = [serial, '', Id, '', name]
        with open('StudentDetails\StudentDetails.csv', 'a+') as csvFile:
            wrtr = csv.writer(csvFile)
            wrtr.writerow(row)
        csvFile.close()
        msg1.configure(text=res)
    else:
        if (name.isalpha() == False):
            res = "Enter Correct name"
            message.configure(text=res)



def TrainFaces():
    check_for_haarcascadefile()
    if_path_exists("TrainingImageLabel/")
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    haarcascadePath = "haarcascade_frontalface_default.xml"
    detection = cv2.CascadeClassifier(haarcascadePath)
    faces, ID = getFacesAndLabels("TrainingImage")
    try:
        recognizer.train(faces, np.array(ID))
    except:
        msgb._show(title='No Registrations', message='Please Register someone first!!!')
        return
    recognizer.save("TrainingImageLabel\Trainner.yml")
    res = "Profile Saved Successfully"
    msg1.configure(text=res)
    message.configure(text='Total Registrations till now  : ' + str(ID[0]))



def getFacesAndLabels(path):
    
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    
    faces = []
    
    Ids = []
    
    for imagePath in imagePaths:
        
        pilImage = Image.open(imagePath).convert('L')
        
        faceNp = np.array(pilImage, 'uint8')
        # getting the Id from the image
        ID = int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(faceNp)
        Ids.append(ID)
    return faces, Ids



def TrackFaces():
    check_for_haarcascadefile()
    if_path_exists("Attendance/")
    if_path_exists("StudentDetails/")
    for k in trv.get_children():
        trv.delete(k)
    msg = ''
    i = 0
    j = 0
    recognizer = cv2.face.LBPHFaceRecognizer_create() 
    present3 = os.path.isfile("TrainingImageLabel\Trainner.yml")
    if present3:
        recognizer.read("TrainingImageLabel\Trainner.yml")
    else:
        msgb._show(title='Data Missing', message='Please click on Save Profile to reset data!!')
        return
    haarcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(haarcascadePath);

    camera = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', '', 'Name', '', 'Date', '', 'Time']
    present1 = os.path.isfile("StudentDetails\StudentDetails.csv")
    if present1:
        df = pd.read_csv("StudentDetails\StudentDetails.csv")
    else:
        msgb._show(title='Details Missing', message='Students details are missing, Kindly check!')
        camera.release()
        cv2.destroyAllWindows()
        window.destroy()
    while True:
        ret, im = camera.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['SERIAL NO.'] == serial]['NAME'].values
                ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values
                ID = str(ID)
                ID = ID[1:-1]
                bb = str(aa)
                bb = bb[2:-2]
                attendance = [str(ID), '', bb, '', str(date), '', str(timeStamp)]

            else:
                Id = 'Unknown'
                bb = str(Id)
            cv2.putText(im, str(bb), (x, y + h), font, 1, (255, 255, 255), 2)
        cv2.imshow('Taking Attendance', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
    present = os.path.isfile("Attendance\Attendance_" + date + ".csv")
    if present:
        with open("Attendance\Attendance_" + date + ".csv", 'a+') as csvFile1:
            wrtr = csv.writer(csvFile1)
            wrtr.writerow(attendance)
        csvFile1.close()
    else:
        with open("Attendance\Attendance_" + date + ".csv", 'a+') as csvFile1:
            wrtr = csv.writer(csvFile1)
            wrtr.writerow(col_names)
            wrtr.writerow(attendance)
        csvFile1.close()
    with open("Attendance\Attendance_" + date + ".csv", 'r') as csvFile1:
        rdr1 = csv.reader(csvFile1)
        for lines in rdr1:
            i = i + 1
            if (i > 1):
                if (i % 2 != 0):
                    iidd = str(lines[0]) + '   '
                    trv.insert('', 0, text=iidd, values=(str(lines[2]), str(lines[4]), str(lines[6])))
    csvFile1.close()
    camera.release()
    cv2.destroyAllWindows()


    
global key
key = ''

ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
day,month,year=date.split("-")

mont={'01':'January',
      '02':'February',
      '03':'March',
      '04':'April',
      '05':'May',
      '06':'June',
      '07':'July',
      '08':'August',
      '09':'September',
      '10':'October',
      '11':'November',
      '12':'December'
      }



window = tk.Tk()
window.geometry("1280x720")
window.resizable(True,False)
window.title("Attendance System")
window.configure(background='#262523')

frm1 = tk.Frame(window, bg="purple")
frm1.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)

frm2 = tk.Frame(window, bg="purple")
frm2.place(relx=0.51, rely=0.17, relwidth=0.38, relheight=0.80)

msg3 = tk.Label(window, text="IIIT Bhubaneswar Facial Attendance System" ,fg="white",bg="#262523" ,width=55 ,height=1,font=('times', 29, ' bold '))
msg3.place(x=10, y=10)

frm3 = tk.Frame(window, bg="pink")
frm3.place(relx=0.52, rely=0.09, relwidth=0.09, relheight=0.07)

frm4 = tk.Frame(window, bg="yellow")
frm4.place(relx=0.36, rely=0.09, relwidth=0.16, relheight=0.07)

datef = tk.Label(frm4, text = day+"-"+mont[month]+"-"+year+"  |  ", fg="orange",bg="#262523" ,width=55 ,height=1,font=('times', 22, ' bold '))
datef.pack(fill='both',expand=1)

clk = tk.Label(frm3,fg="orange",bg="#262523" ,width=55 ,height=1,font=('times', 22, ' bold '))
clk.pack(fill='both',expand=1)
tick()

hed2 = tk.Label(frm2, text="                       For New Registrations                       ", fg="black",bg="pink" ,font=('times', 17, ' bold ') )
hed2.grid(row=0,column=0)

hed1 = tk.Label(frm1, text="                       For Already Registered                       ", fg="black",bg="pink" ,font=('times', 17, ' bold ') )
hed1.place(x=0,y=0)

lbl = tk.Label(frm2, text="Enter ID",width=20  ,height=1  ,fg="black"  ,bg="#00aeff" ,font=('times', 17, ' bold ') )
lbl.place(x=80, y=55)

txt = tk.Entry(frm2,width=32 ,fg="black",font=('times', 15, ' bold '))
txt.place(x=30, y=88)

lbl2 = tk.Label(frm2, text="Enter Name",width=20  ,fg="black"  ,bg="#00aeff" ,font=('times', 17, ' bold '))
lbl2.place(x=80, y=140)

txt2 = tk.Entry(frm2,width=32 ,fg="black",font=('times', 15, ' bold ')  )
txt2.place(x=30, y=173)

msg1 = tk.Label(frm2, text="1)Take Images  >>>  2)Save Profile" ,bg="#00aeff" ,fg="black"  ,width=39 ,height=1, activebackground = "yellow" ,font=('times', 15, ' bold '))
msg1.place(x=7, y=230)

message = tk.Label(frm2, text="" ,bg="#00aeff" ,fg="black"  ,width=39,height=1, activebackground = "yellow" ,font=('times', 16, ' bold '))
message.place(x=7, y=450)

lbl3 = tk.Label(frm1, text="Attendance",width=20  ,fg="black"  ,bg="#00aeff"  ,height=1 ,font=('times', 17, ' bold '))
lbl3.place(x=100, y=115)

res=0
present = os.path.isfile("StudentDetails\StudentDetails.csv")
if present:
    with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
        rdr1 = csv.reader(csvFile1)
        for l in rdr1:
            res = res + 1
    res = (res // 2) - 1
    csvFile1.close()
else:
    res = 0
message.configure(text='Total Registrations till now  : '+str(res))



mbar = tk.Menu(window,relief='ridge')
fmenu = tk.Menu(mbar,tearoff=0)
fmenu.add_command(label='Change Password', command = change_pwd)
fmenu.add_command(label='Contact Us', command = contactus)
fmenu.add_command(label='Exit',command = window.destroy)
mbar.add_cascade(label='Help',font=('times', 29, ' bold '),menu=fmenu)



trv= ttk.Treeview(frm1,height =13,columns = ('name','date','time'))
trv.column('#0',width=82)
trv.column('name',width=130)
trv.column('date',width=133)
trv.column('time',width=133)
trv.grid(row=2,column=0,padx=(0,0),pady=(150,0),columnspan=4)
trv.heading('#0',text ='ID')
trv.heading('name',text ='NAME')
trv.heading('date',text ='DATE')
trv.heading('time',text ='TIME')



scrl=ttk.Scrollbar(frm1,orient='vertical',command=trv.yview)
scrl.grid(row=2,column=4,padx=(0,100),pady=(150,0),sticky='ns')
trv.configure(yscrollcommand=scrl.set)



clrbtn = tk.Button(frm2, text="Clear", command=clr  ,fg="black"  ,bg="#ea2a2a"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
clrbtn.place(x=335, y=86)
clrbtn2 = tk.Button(frm2, text="Clear", command=clr2  ,fg="black"  ,bg="#ea2a2a"  ,width=11 , activebackground = "white" ,font=('times', 11, ' bold '))
clrbtn2.place(x=335, y=172)    
tkImg = tk.Button(frm2, text="Take Images", command=TakeFaces  ,fg="white"  ,bg="blue"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
tkImg.place(x=30, y=300)
trnImg = tk.Button(frm2, text="Save Profile", command=pwd ,fg="white"  ,bg="blue"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
trnImg.place(x=30, y=380)
trkImg = tk.Button(frm1, text="Take Attendance", command=TrackFaces  ,fg="black"  ,bg="yellow"  ,width=35  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
trkImg.place(x=30,y=50)
quitWindow = tk.Button(frm1, text="Quit", command=window.destroy  ,fg="black"  ,bg="red"  ,width=35 ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
quitWindow.place(x=30, y=450)



window.configure(menu=mbar)
window.mainloop()


