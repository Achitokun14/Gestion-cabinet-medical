from tkinter import * 
from tkinter import messagebox
import mysql.connector

from tkinter import ttk
from tkinter import *
import mysql.connector as ms
import tkinter.messagebox as tm
import tkinter as tk


import time




window=Tk()   #Creer la fenetre de login--------------------------------------------------------------
window.title("Medical Management System ")
window.geometry('925x500+200+130')
window.resizable(1,1)
window.configure(bg='#fff')
window.iconbitmap("C:/Users/PC/Desktop/projX/patient.ico")

#######-----------------------------------------MY SQL-------------------------------------
pssw="alaoui.1999"
database="medical"

#Call database medical
mydb = mysql.connector.connect(host="localhost",user="root",password=pssw,database=database)
mycursor = mydb.cursor()


mycursor.execute("create database if not exists medical;")
mycursor.execute("CREATE TABLE IF NOT EXISTS `utilisateurs` (`id` int NOT NULL AUTO_INCREMENT,`nom` varchar(25) NOT NULL,`email` varchar(50) NOT NULL,`numero` varchar(10) NOT NULL,`password` varchar(50) NOT NULL,PRIMARY KEY (`id`));")
mycursor.execute("CREATE TABLE IF NOT EXISTS `consultation_initial` (`id_consiltation_inial` int NOT NULL AUTO_INCREMENT,`poids` float NOT NULL,`taille` float NOT NULL,`temperature` int NOT NULL,`Glycemie` float NOT NULL,`pression` float NOT NULL,`allergie` char(3) COLLATE utf8mb4_general_ci NOT NULL,`imc` char(20) COLLATE utf8mb4_general_ci DEFAULT NULL,`douleur` char(3) COLLATE utf8mb4_general_ci DEFAULT NULL,`maladies_chroniques` char(3) COLLATE utf8mb4_general_ci DEFAULT NULL,`interpretation_imc` char(30) COLLATE utf8mb4_general_ci DEFAULT NULL,PRIMARY KEY (`id_consiltation_inial`));")
mycursor.execute("CREATE TABLE IF NOT EXISTS consultation_fin (id_consultation INT PRIMARY KEY AUTO_INCREMENT, id_patient INT, consultation_final TEXT, ordonnance TEXT, situation_dossier CHAR(15) NOT NULL, constraint fk_info_patient FOREIGN KEY(id_patient) REFERENCES info_patient(id_patient) on delete cascade);")
mydb.commit()



def close():
   frame.quit()
#######-----------------------------------------Fin fonction quit programme-------------------------------------

def precedent():
            global valeur
            valeur = "Recommencer la fonction"
            window.destroy()

#######-----------------------------------------Gestion d'acces-------------------------------------
def singin():
    
    utilisateur = function.get()
    psw = password.get()
    try:
        mycursor.execute("SELECT * FROM utilisateurs WHERE nom = %s", (utilisateur,))  
        docteur = mycursor.fetchone()

    except:
        messagebox.showerror('incorrect',"Password or function wrong")
    try:
        if psw==docteur[4] and utilisateur=='admin' or utilisateur=='ADMIN' or utilisateur=='Admin' :
            linefram2.destroy()
            linefram.destroy()
            bottonconnect.destroy()
            Label(frame,text="'HELLO,Admin'",fg='#57a1f8',bg='white',font=("Microsoft YaJei UI Light",23,"bold")).grid(row=6, column=1)
            Button(frame,width=39,pady=7,text="Ajouter patient",bg='#57a1f8',fg="white",border=0,command=docpatient).grid(row=7 , column=1)
            Button(frame,width=39,pady=7,text="Consultation initial",bg='#57a1f8',fg="white",border=0,command=consiltinitial).grid(row=8 , column=1)
            Button(frame,width=39,pady=7,text="Fermer l'application",bg='#C70039',fg="white",border=0,command=close).grid(row=13 , column=1)
            Button(frame,width=39,pady=7,text="Voir les patient",bg='#57a1f8',fg="white",border=0).grid(row=9 , column=1)
            Button(frame,width=39,pady=7,text="Ajouter utilisateur",bg='#57a1f8',fg="white",border=0,command=register).grid(row=11 , column=1)
            Button(frame,width=39,pady=7,text="Changer Password",bg='#57a1f8',fg="white",border=0,command=changepass).grid(row=10 , column=1)
            Button(frame,width=39,pady=7,text="Consultation final",bg='#57a1f8',fg="white",border=0,command=Consfinal).grid(row=12 , column=1)


        elif psw==docteur[4] and utilisateur=='docteur' or utilisateur=='Docteur' or utilisateur=='DOCTEUR' :
            linefram2.destroy()
            linefram.destroy()
            bottonconnect.destroy()
            Label(frame,text="'HELLO Docteur'",fg='#57a1f8',bg='white',font=("Microsoft YaJei UI Light",23,"bold")).grid(row=6, column=1)
            Button(frame,width=39,pady=7,text="Ajouter patient",bg='#57a1f8',fg="white",border=0,command=docpatient).grid(row=7 , column=1)
            Button(frame,width=39,pady=7,text="Consultation initial",bg='#57a1f8',fg="white",border=0,command=consiltinitial).grid(row=8 , column=1)
            Button(frame,width=39,pady=7,text="Voir les patient",bg='#57a1f8',fg="white",border=0).grid(row=9 , column=1)
            Button(frame,width=39,pady=7,text="Ajouter utilisateur",bg='#57a1f8',fg="white",border=0,command=register,state=DISABLED).grid(row=11 , column=1)
            Button(frame,width=39,pady=7,text="Changer Password",bg='#57a1f8',fg="white",border=0,command=changepass).grid(row=10 , column=1)
            Button(frame,width=39,pady=7,text="Fermer l'application",bg='#C70039',fg="white",border=0,command=close).grid(row=12 , column=1)
            Button(frame,width=39,pady=7,text="Consultation final",bg='#57a1f8',fg="white",border=0,command=Consfinal).grid(row=13 , column=1)


        elif psw==docteur[4] and utilisateur=='reception' or utilisateur=='Reception' or utilisateur=='RECEPTION' :
            linefram2.destroy()
            linefram.destroy()
            bottonconnect.destroy()
            Label(frame,text="'HELLO'",fg='#57a1f8',bg='white',font=("Microsoft YaJei UI Light",23,"bold")).grid(row=6, column=1)
            Button(frame,width=39,pady=7,text="Ajouter patient",bg='#57a1f8',fg="white",border=0,command=docpatient).grid(row=7 , column=1)
            Button(frame,width=39,pady=7,text="Consultation initial",bg='#57a1f8',fg="white",border=0,command=consiltinitial,state=DISABLED).grid(row=8 , column=1)
            Button(frame,width=39,pady=7,text="Voir les patient",bg='#57a1f8',fg="white",border=0).grid(row=9 , column=1)
            Button(frame,width=39,pady=7,text="Ajouter utilisateur",bg='#57a1f8',fg="white",border=0,command=register,state=DISABLED).grid(row=9 , column=1)
            Button(frame,width=39,pady=7,text="Changer Password",bg='#57a1f8',fg="white",border=0,command=changepass).grid(row=10 , column=1)
            Button(frame,width=39,pady=7,text="Consultation final",bg='#57a1f8',fg="white",border=0,command=Consfinal).grid(row=11 , column=1)
            Button(frame,width=39,pady=7,text="Fermer l'application",bg='#C70039',fg="white",border=0,command=close).grid(row=12 , column=1)



        else:
            messagebox.showerror('Incorrect',"Password wrong")
    
    except:
        messagebox.showerror('Incorrect',"Fonction incorrect")

#######------------------------------------------------------------------------------
def save():

    sql = "INSERT INTO info_patient (datenaiss, age,grps,situation_fam,email,numero_tel,add_patient,note,sexe,nom_prenom) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (edate_naissance.get(),eage.get(),eGroupsanguin.get(),esituation.get(),eEmail.get(),eTel.get(),eAdresse.get(),enote.get(),variable4.get(),enom_prenom.get())
    print("done")
    x=1
    while x==1 :
        Label(window, text = "PASSION ADDED" ,fg='white',background="#57a1f8").grid(row =4, column = 1)
        time.sleep(1)
        x=0

    mycursor.execute(sql, val)
    mydb.commit()
#######-----------------------------------------Save les info de patient-------------------------------------

def save2():

    mycursor = mydb.cursor()
    imc=float(epoids.get())/((float(etaille.get()))*(float(etaille.get())))
    if (imc<18.5) :
        interpretation_imc="maigreur"
    elif (imc>18.5) and (imc<24.9):
         interpretation_imc="Corpulence normale"
    elif (imc>24.9) and (imc<29.9):
         interpretation_imc="Surpoids"
    elif (imc>29.9) and (imc<40):
         interpretation_imc="Obésité modérée"
    else:
        interpretation_imc="Obésité morbide ou massive"
    print(imc)


    sql = "INSERT INTO consultation_initial (poids,taille,temperature,Glycemie,pression,allergie,imc,douleur,maladies_chroniques,interpretation_imc) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (epoids.get(),etaille.get(),etemerature.get(),eGlycémie.get(),ePression.get(),variable.get(),imc,variable2.get(),variable3.get(),interpretation_imc)
    print("done")

    
    Label(window, text = "Consultation initial bien ajouter" ,fg='white',background="#57a1f8").grid(row =4, column = 9)

    mycursor.execute(sql, val)

    mydb.commit()
#######-----------------------------------------save consultation initial and calcul imc -------------------------------------

def save3():
        sql = "INSERT INTO utilisateurs (nom,email,numero,password) VALUES (%s,%s,%s,%s)"
        val = (eutilisateur.get(),eemail.get(),enumero.get(),epassword.get())
        mycursor.execute(sql, val)
        mydb.commit()
        print("done")
#######----------------------------------------- add Utilisateur-----------------------------------------------

def save4():
    utilisateur = eutilisateur.get()
    psw = epassword.get()
    try:
        mycursor.execute("SELECT * FROM utilisateurs WHERE email = %s", (utilisateur,))  
        docteur = mycursor.fetchone()
    except:
        messagebox.showerror('incorrect',"Wrong password or function")
    try:    
        if psw==docteur[4] and utilisateur==docteur[2] :
            sql = "UPDATE utilisateurs SET password = (%s) WHERE password = (%s)"
            val =(enewpassword.get(),psw)
            mycursor.execute(sql,val)
            mydb.commit()
            messagebox.showinfo("Info",'Password modified')
    except Exception as e:
        messagebox.showerror('error', e)
#######-----------------------------------------update utilisateur---------------------------------------

def register():
    global eutilisateur,eemail,enumero,epassword
    window=Tk()
    window.title("Ajouter Utilisateur")
    window.geometry('375x250+500+130')
    window.configure(bg="#fff")
    window.resizable(1,1)
    window.iconbitmap("C:/Users/PC/Desktop/projX/patient.ico")

    titre = Label(window, text = "Ajouter Utilisateur" ,fg="#1E90FF",background='white', font=("Microsoft YaJei UI Light",15,"bold"))
    titre.place(x = 85, y = 1)
    def on_enter(e):
            eutilisateur.delete(0,"end")
    def on_leave(e):
            name=eutilisateur.get()
            if name=="":
                eutilisateur.insert(0,'Fonction')
    eutilisateur = Entry(window,background='white',border=0,fg="black", relief="sunken")
    eutilisateur.place(x = 120, y = 40)
    eutilisateur.insert(0,"Fonction")

    eutilisateur.bind("<FocusIn>",on_enter)
    eutilisateur.bind("<FocusOut>",on_leave)
    Frame(window,width=120,height=1,bg="#1E90FF").place(x=115 , y=60)

    def on_enter(e):
            eemail.delete(0,"end")
            
    def on_leave(e):
        name=eemail.get()
        if name=="":
            eemail.insert(0,"Email d'utilisateur")
    eemail = Entry(window,background='white',border=0,fg="black", relief="sunken")
    eemail.place(x = 120, y = 80)
    eemail.insert(0, "Email d'utilisateur")

    eemail.bind("<FocusIn>",on_enter)
    eemail.bind("<FocusOut>",on_leave)
    Frame(window,width=120,height=1,bg="#1E90FF").place(x=115 , y=100)

    def on_enter(e):
        enumero.delete(0,"end")
            
    def on_leave(e):
        name=enumero.get()
        if name=="":
            enumero.insert(0,'Numero')

    enumero = Entry(window,background='white',border=0,fg="black", relief="sunken")
    enumero.place(x = 120, y = 120)
    enumero.insert(0, "Numero")

    enumero.bind("<FocusIn>",on_enter)
    enumero.bind("<FocusOut>",on_leave)
    Frame(window,width=120,height=1,bg="#1E90FF").place(x=115 , y=140)

    def on_enter(e):
            epassword.delete(0,"end")
            
    def on_leave(e):
        name=epassword.get()
        if name=="":
            epassword.insert(0,'Password')

    epassword = Entry(window,background='white',border=0,fg="black", relief="sunken")
    epassword.place(x = 120, y = 160)
    epassword.insert(0, "Password")
    epassword.bind("<FocusIn>",on_enter)
    epassword.bind("<FocusOut>",on_leave)
    Frame(window,width=120,height=1,bg="#1E90FF").place(x=115 , y=180)


    Button(window,width=20,pady=7,text="save" ,font=('Helvetica bold', 12,"bold"),bg='white',fg="#57a1f8",border=2,command=save3).place(x = 75, y = 200)


    window.mainloop()
#######-----------------------------------------ajouter utilisateur---------------------------------------------------------

def docpatient():
    global enom_prenom,eAdresse,eage,edate_naissance,eGroupsanguin,esituation,enote,eTel,eEmail,variable4
    window=Tk()
    window.title("info patient")
    window.geometry('375x500+500+130')
    window.configure(bg="#fff")
    window.resizable(1,1)
    window.iconbitmap("C:/Users/PC/Desktop/projX/patient.ico")

    titre = Label(window, text = "INFO PATIENT" ,fg="#1E90FF",background='white', font=("Microsoft YaJei UI Light",15,"bold"))
    titre.place(x = 110, y = 1)


    def on_enter(e):
        enom_prenom.delete(0,"end")
        
    def on_leave(e):
        name=enom_prenom.get()
        if name=="":
            enom_prenom.insert(0,'Nom et prénom')
    enom_prenom = Entry(window,background='white',border=0,fg="black", relief="sunken")
    enom_prenom.place(x = 120, y = 40)
    enom_prenom.insert(0, "Nom et prénom")

    enom_prenom.bind("<FocusIn>",on_enter)
    enom_prenom.bind("<FocusOut>",on_leave)
    Frame(window,width=120,height=1,bg="#1E90FF").place(x=115 , y=60)
    

    def on_enter(e):
        edate_naissance.delete(0,"end")
        
    def on_leave(e):
        name=edate_naissance.get()
        if name=="":
            edate_naissance.insert(0,'Date de naissance')
    edate_naissance = Entry(window,background='white',border=0,fg="black", relief="sunken")
    edate_naissance.place(x = 120, y = 70)
    edate_naissance.insert(0, "Date de naissance")

    edate_naissance.bind("<FocusIn>",on_enter)
    edate_naissance.bind("<FocusOut>",on_leave)
    Frame(window,width=120,height=1,bg="#1E90FF").place(x=115 , y=90)

    def on_enter(e):
        eage.delete(0,"end")
        
    def on_leave(e):
        name=eage.get()
        if name=="":
            eage.insert(0,'Age')

    eage = Entry(window,background='white',border=0,fg="black", relief="sunken")
    eage.place(x = 120, y = 100)
    eage.insert(0, "Age")

    eage.bind("<FocusIn>",on_enter)
    eage.bind("<FocusOut>",on_leave)
    Frame(window,width=120,height=1,bg="#1E90FF").place(x=115 , y=120)


    def on_enter(e):
        eGroupsanguin.delete(0,"end")
        
    def on_leave(e):
        name=eGroupsanguin.get()
        if name=="":
            eGroupsanguin.insert(0,'le Groupe sanguin')

    eGroupsanguin = Entry(window,background='white',border=0,fg="black", relief="sunken")
    eGroupsanguin.place(x = 120, y = 130)
    eGroupsanguin.insert(0, "le Groupe sanguin")
    eGroupsanguin.bind("<FocusIn>",on_enter)
    eGroupsanguin.bind("<FocusOut>",on_leave)
    Frame(window,width=120,height=1,bg="#1E90FF").place(x=115 , y=150)



    def on_enter(e):
        esituation.delete(0,"end")
        
    def on_leave(e):
        name=esituation.get()
        if name=="":
            esituation.insert(0,'situation Familial')

    esituation  = Entry(window,background='white',border=0,fg="black", relief="sunken")
    esituation.place(x = 120, y = 160)
    esituation.insert(0, "situation Familial")
    esituation.bind("<FocusIn>",on_enter)
    esituation.bind("<FocusOut>",on_leave)
    Frame(window,width=120,height=1,bg="#1E90FF").place(x=115 , y=180)


    def on_enter(e):
        eEmail.delete(0,"end")
        
    def on_leave(e):
        name=eEmail.get()
        if name=="":
            eEmail.insert(0,'Email')



    eEmail = Entry(window,background='white',border=0,fg="black", relief="sunken")
    eEmail.place(x = 120, y = 190)
    eEmail.insert(0, "Email")
    eEmail.bind("<FocusIn>",on_enter)
    eEmail.bind("<FocusOut>",on_leave)
    Frame(window,width=120,height=1,bg="#1E90FF").place(x=115 , y=210)


    def on_enter(e):
        eTel.delete(0,"end")
        
    def on_leave(e):
        name=eTel.get()
        if name=="":
            eTel.insert(0,'Numero de Tel')

    eTel = Entry(window,background='white',border=0,fg="black", relief="sunken")
    eTel.place(x = 120, y = 220)
    eTel.insert(0, "Numero de Tel")
    eTel.bind("<FocusIn>",on_enter)
    eTel.bind("<FocusOut>",on_leave)
    Frame(window,width=120,height=1,bg="#1E90FF").place(x=115 , y=240)



    def on_enter(e):
        eAdresse.delete(0,"end")
        
    def on_leave(e):
        name=eAdresse.get()
        if name=="":
            eAdresse.insert(0,'Adresse de patient')

    eAdresse = Entry(window,background='white',border=0,fg="black", relief="sunken")
    eAdresse.place(x = 120, y = 250)
    eAdresse.insert(0, "Adresse de patient")
    eAdresse.bind("<FocusIn>",on_enter)
    eAdresse.bind("<FocusOut>",on_leave)
    Frame(window,width=120,height=1,bg="#1E90FF").place(x=115 , y=270)


    def on_enter(e):
        enote.delete(0,"end")
        
    def on_leave(e):
        name=enote.get()
        if name=="":
            enote.insert(0,'Note')

    enote = Entry(window,background='white',border=0,fg="black", relief="sunken")
    enote.place(x = 120, y = 280)
    enote.insert(0, "Note")
    enote.bind("<FocusIn>",on_enter)
    enote.bind("<FocusOut>",on_leave)

    Frame(window,width=120,height=1,bg="#1E90FF").place(x=115 , y=300)

    variable4 = StringVar(window)
    variable4.set("sexe") 
    w = OptionMenu(window, variable4, "Male", "female ")
    w.place(x = 120, y = 310)

    Button(window,width=20,pady=7,text="save" ,font=('Helvetica bold', 12,"bold"),bg='white',fg="#57a1f8",border=2,command=save).place(x = 85, y = 420)
    window.mainloop()
#######-----------------------------------------Fin DE CREATION DE INFO PATIENT WINDOW-------------------------------------

def on_enter(e):
    function.delete(0,"end")

def Consfinal():   

    global root


    root = Toplevel(window)
    root.title("CONSULTATION")
    root.iconbitmap("C:/Users/PC/Desktop/projX/patient.ico")


    width = 700                     #blan nadi
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.resizable(1, 1)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.config (bg="#A1A1A1")          #background color


    ID_PATIENT = StringVar()            #variables
    CONSULTATION = StringVar()          
    ORDONNANCE = StringVar()
    ST_DO = StringVar()

    def database_add() :
        connect = ms.connect(host="localhost",
        user="root",
        password=pssw ,
        database=database)
        con =connect.cursor()


        con.execute("CREATE TABLE IF NOT EXISTS consultation_fin (id_consultation INT PRIMARY KEY AUTO_INCREMENT, id_patient INT, consultation_final TEXT, ordonnance TEXT, situation_dossier CHAR(15) NOT NULL, constraint fk_info_patient FOREIGN KEY(id_patient) REFERENCES info_patient(id_patient) on delete cascade);")
        con.execute("select * from consultation_fin order by id_patient asc;")
        fetch = con.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        con.close()
        connect.close()



    def add_patient_info():
        if  ST_DO.get() == "" or ORDONNANCE.get() == "" or CONSULTATION.get() == "" or ID_PATIENT.get() == "" :
            result = tm.showwarning('', 'comleter les info s\'il vous plais', icon="warning")
        else:
            tree.delete(*tree.get_children())
            connect = ms.connect(host="localhost" ,user="root" ,passwd=pssw ,database=database)
            con =connect.cursor()
            con.execute("INSERT INTO consultation_fin (consultation_final, ordonnance, situation_dossier) VALUES(%s,%s,%s);", (str(CONSULTATION.get()),str(ORDONNANCE.get()),str(ST_DO.get())))
            connect.commit()
            con.execute("select * from consultation_fin order by id_consultation asc;")
            fetch = con.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))
            con.close()
            connect.close()
            ID_PATIENT.set("")  #empty the place-holders
            CONSULTATION.set("")  
            ORDONNANCE.set("")
            ST_DO.set("")

    def update_patient_info():
        if  ST_DO.get() == "" or ORDONNANCE.get() == "" or CONSULTATION.get() == "" or ID_PATIENT.get() == "":
            result = tm.showwarning('', 'comleter les info s\'il vous plais', icon="warning")
        else:
            tree.delete(*tree.get_children())
            connect = ms.connect(host="localhost" ,user="root" ,passwd=pssw ,database=database)
            con =connect.cursor()
            con.execute("UPDATE consultation_fin SET consultation_final = %s, ordonnance = %s, situation_dossier = %s where id_consultation=%s;", (str(CONSULTATION.get()),str(ORDONNANCE.get()),str(ST_DO.get()),str(consul_id)))
            connect.commit()
            con.execute("select * from consultation_fin order by id_consultation asc;")
            fetch = con.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))
            con.close()
            connect.close()
            ID_PATIENT.set("")  #empty the place-holders
            CONSULTATION.set("")  
            ORDONNANCE.set("")
            ST_DO.set("")

    def OnSelected(event):
        global consul_id, Update_window
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents["values"]
        consul_id = selecteditem[0]
        ID_PATIENT.set("")  #empty the place-holders
        CONSULTATION.set("")  
        ORDONNANCE.set("")
        ST_DO.set("")
        ID_PATIENT.set(selecteditem[1])  #assining values to place-holders
        CONSULTATION.set(selecteditem[2])  
        ORDONNANCE.set(selecteditem[3])
        ST_DO.set(selecteditem[4])
        Update_window = Toplevel(root)
        Update_window.title("correction des donnes")

        width = 600                         #blan zwin f resize
        height = 400
        screen_width = Update_window.winfo_screenwidth()
        screen_height = Update_window.winfo_screenheight()
        x = ((screen_width/2)+450) - (width/2)
        y = ((screen_height/2)+20) - (height/2)
        Update_window.geometry("%dx%d+%d+%d" % (width, height, x, y))
        Update_window.resizable(1, 1)
        if 'NewWindow' in globals():
            NewWindow.destroy()


        FormTitle = Frame(Update_window)                #debut
        FormTitle.pack(side=TOP)
        ConsForm = Frame(Update_window)
        ConsForm.pack(side=TOP, pady=10)
        RadioGroup = Frame(ConsForm)
        traitement = Radiobutton(RadioGroup, text="traitement", variable=ST_DO, value="traitement",  font=('arial', 14)).pack(side=LEFT)
        fermeture = Radiobutton(RadioGroup, text="fermeture", variable=ST_DO, value="fermeture",  font=('arial', 14)).pack(side=LEFT)

        lebel_correction = Label(FormTitle, text="correction des données", font=('arial', 16), bg="#db7f34",  width = 300)
        lebel_correction.pack(fill=X)
        lebel_id = Label(ConsForm, text="le ID de patient \n(vous pouvez parcourir \ndans le premier tableau)", font=('arial', 14), bd=5)
        lebel_id.grid(row=0, sticky=W)
        lebel_consultation = Label(ConsForm, text="consultation \'docteur\'", font=('arial', 14), bd=5)
        lebel_consultation.grid(row=1, sticky=W)
        lebel_sd = Label(ConsForm, text="situation du dossier", font=('arial', 14), bd=5)
        lebel_sd.grid(row=3, sticky=W)
        lebel_ordonnance = Label(ConsForm, text="ordonnance", font=('arial', 14), bd=5)
        lebel_ordonnance.grid(row=2, sticky=W)

        id_patient = Entry(ConsForm, textvariable=ID_PATIENT, font=('arial', 14))
        id_patient.grid(row=0, column=1)
        consultation = Entry(ConsForm, textvariable=CONSULTATION, font=('arial', 14))
        consultation.grid(row=1, column=1)
        ordonnance = Entry(ConsForm, textvariable=ORDONNANCE,  font=('arial', 14))
        ordonnance.grid(row=2, column=1)    
        RadioGroup.grid(row=3, column=1) 

        botton_upd_conn = Button(ConsForm, text="Update", width=50, command=update_patient_info)
        botton_upd_conn.grid(row=4, columnspan=2, pady=10)                  #fin

    def del_patient_info():
        if not tree.selection():
            result = tm.showwarning('', 'sélectionner quelque chose s\'il vous plaît!!', icon="warning")
        else:
            result = tm.askquestion('', 'vous etes sûr que vous voulez supprimer ce patient?', icon="warning")
            if result == 'yes':
                curItem = tree.focus()
                contents =(tree.item(curItem))
                selecteditem = contents['values']
                tree.delete(curItem)
                connect = ms.connect(host="localhost" ,user="root" ,passwd=pssw ,database=database)
                con =connect.cursor()
                con.execute("DELETE FROM consultation_fin WHERE id_consultation = %d;" % selecteditem[0])
                connect.commit()
                con.close()
                connect.close()
        

    def Add_New_Window():
        global NewWindow
        ID_PATIENT.set("")  #the place-holders
        CONSULTATION.set("")  
        ORDONNANCE.set("")
        ST_DO.set("")
        NewWindow = Toplevel(root)
        NewWindow.title("remplissage d'une consultation")

        width = 600             #blan nadi
        height = 400
        screen_width = NewWindow.winfo_screenwidth()
        screen_height = NewWindow.winfo_screenheight()
        x = ((screen_width/2) - 455) - (width/2)
        y = ((screen_height/2) + 20) - (height/2)
        NewWindow.resizable(1, 1)
        NewWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))

        if 'Update_Window' in globals():
            Update_window.destroy()


        FormTitle = Frame(NewWindow)                #debut
        FormTitle.pack(side=TOP)
        ConsForm = Frame(NewWindow)
        ConsForm.pack(side=TOP, pady=10)
        RadioGroup = Frame(ConsForm)
        traitement = Radiobutton(RadioGroup, text="traitement", variable=ST_DO, value="traitement",  font=('arial', 14)).pack(side=LEFT)
        fermeture = Radiobutton(RadioGroup, text="fermeture", variable=ST_DO, value="fermeture",  font=('arial', 14)).pack(side=LEFT)

        lebel_correction = Label(FormTitle, text="remplissage des données", font=('arial', 16), bg="#66ff66",  width = 300)
        lebel_correction.pack(fill=X)
        lebel_id = Label(ConsForm, text="le ID de patient \n(vous pouvez parcourir \ndans le premier tableau)", font=('arial', 14), bd=5)
        lebel_id.grid(row=0, sticky=W)
        lebel_consultation = Label(ConsForm, text="consultation \'docteur\'", font=('arial', 14), bd=5)
        lebel_consultation.grid(row=1, sticky=W)
        lebel_sd = Label(ConsForm, text="situation du dossier", font=('arial', 14), bd=5)
        lebel_sd.grid(row=3, sticky=W)
        lebel_ordonnance = Label(ConsForm, text="ordonnance", font=('arial', 14), bd=5)
        lebel_ordonnance.grid(row=2, sticky=W)

        id_patient = Entry(ConsForm, textvariable=ID_PATIENT, font=('arial', 14))
        id_patient.grid(row=0, column=1)
        consultation = Entry(ConsForm, textvariable=CONSULTATION, font=('arial', 14))
        consultation.grid(row=1, column=1)
        ordonnance = Entry(ConsForm, textvariable=ORDONNANCE,  font=('arial', 14))
        ordonnance.grid(row=2, column=1)    
        RadioGroup.grid(row=3, column=1)

        botton_upd_conn = Button(ConsForm, text="Save", width=50, command=add_patient_info)
        botton_upd_conn.grid(row=4, columnspan=2, pady=10)                  #fin

    #main parts
    pane = PanedWindow(root,orient=VERTICAL)
    pane.pack(fill=BOTH, expand=1)

    upper_container = Frame(pane)
    upper_container.pack()

    Top = Frame(upper_container, width=500, bd=1, relief=SOLID)
    Top.pack(side=TOP)
    Mid = Frame(upper_container, width=500)
    Mid.pack(side=TOP)
    MidLeft = Frame(Mid, width=10)
    MidLeft.pack(side=LEFT, pady=10)
    MidLeftPadding = Frame(Mid, width=37)
    MidLeftPadding.pack(side=LEFT)
    MidRight = Frame(Mid, width=100)
    MidRight.pack(side=RIGHT, pady=10)
    TableMargin = Frame(upper_container, width=500)
    TableMargin.pack(side=TOP)

    lbl_title = Label(Top, text="Gstion des consultation", bg= "#51afc0",font=('arial', 16), width=500)
    lbl_title.pack(fill=X)


    botton_add = Button(MidLeft, text="ajouter une consultation", bg="green", command=Add_New_Window)
    botton_add.pack(side=LEFT)
    botton_delete = Button(MidRight, text="supprimer une consultation", bg="red", command=del_patient_info)
    botton_delete.pack(side=RIGHT)

    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin,height=8 ,columns=("id_consultation","id_patient" ,"consultation_final", "ordonnance", "situation_dossier"), selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)

    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    style = ttk.Style(pane)
    style.theme_use("clam")
    tree["show"] = "headings"

    tree.heading('id_consultation', text="idconsultation", anchor=tk.CENTER)
    tree.heading('id_patient', text="idpatient", anchor=tk.CENTER)
    tree.heading('consultation_final', text="consultationfinal", anchor=tk.CENTER)
    tree.heading('ordonnance', text="ordonnance", anchor=tk.CENTER)
    tree.heading('situation_dossier', text="situationdossier", anchor=tk.CENTER)

    tree.column('#0', width=150, minwidth=20, anchor=tk.CENTER)
    tree.column('#1', width=150, minwidth=20, anchor=tk.CENTER)
    tree.column('#2', width=150, minwidth=20, anchor=tk.CENTER)
    tree.column('#3', width=150, minwidth=150, anchor=tk.CENTER)
    tree.column('#4', width=150, minwidth=150, anchor=tk.CENTER)
    tree.column('#5', width=150, minwidth=50, anchor=tk.CENTER)


    tree.pack()
    tree.bind('<Double-Button-1>', OnSelected)

    connect = ms.connect(host="localhost" ,user="root" ,passwd=pssw ,database=database)
    con =connect.cursor()
    con.execute("select * from info_patient order by id_patient asc") #leter add 'where dateRV=..input of day/month/year' or 'CIN=....'

    tree1 = ttk.Treeview(pane)
    tree1["show"] = "headings" #removes the first empty column

    style = ttk.Style(pane)
    style.theme_use("clam") #theme used ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')

    tree1["columns"]=("id_patient", "datenaiss", "age", "grps", "situation_fam", "email", "numero_tel", "add_patient", "note", "sexe", "nom_prenom") #name of columns 

    #define all columns
    tree1.column("id_patient", width=150, minwidth=20, anchor=tk.CENTER)
    tree1.column("datenaiss", width=150, minwidth=50, anchor=tk.CENTER)
    tree1.column("age", width=150, minwidth=20, anchor=tk.CENTER)
    tree1.column("grps", width=150, minwidth=20, anchor=tk.CENTER)
    tree1.column("situation_fam", width=150, minwidth=50, anchor=tk.CENTER)
    tree1.column("email", width=150, minwidth=50, anchor=tk.CENTER)
    tree1.column("numero_tel", width=150, minwidth=50, anchor=tk.CENTER)
    tree1.column("add_patient", width=150, minwidth=50, anchor=tk.CENTER)
    tree1.column("note", width=150, minwidth=50, anchor=tk.CENTER)
    tree1.column("sexe", width=150, minwidth=20, anchor=tk.CENTER)
    tree1.column("nom_prenom", width=150, minwidth=100, anchor=tk.CENTER)

    #defin heading names to all columns
    tree1.heading("id_patient", text="id_patient", anchor=tk.CENTER)
    tree1.heading("datenaiss", text="datenaiss", anchor=tk.CENTER)
    tree1.heading("age", text="age", anchor=tk.CENTER)
    tree1.heading("grps", text="grps", anchor=tk.CENTER)
    tree1.heading("situation_fam", text="situation_fam", anchor=tk.CENTER)
    tree1.heading("email", text="email", anchor=tk.CENTER)
    tree1.heading("numero_tel", text="numero_tel", anchor=tk.CENTER)
    tree1.heading("add_patient", text="add_patient", anchor=tk.CENTER)
    tree1.heading("note", text="note", anchor=tk.CENTER)
    tree1.heading("sexe", text="sexe", anchor=tk.CENTER)
    tree1.heading("nom_prenom", text="nom_prenom", anchor=tk.CENTER)

    i = 0
    for row in con :
        tree1.insert("", i, text="", values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))
        i += 1

    scroll = ttk.Scrollbar(pane, orient="horizontal")
    scroll.configure(command = tree1.xview)
    tree1.configure(xscrollcommand = scroll.set)
    scroll.pack(fill = X,side = BOTTOM)

    scroll = ttk.Scrollbar(pane, orient="vertical")
    scroll.configure(command = tree1.yview)
    tree1.configure(yscrollcommand = scroll.set)
    scroll.pack(fill = Y,side = RIGHT)

    tree1.pack()
    pane.add(upper_container)
    pane.add(tree1)

    if __name__ == '__main__':
        database_add()
        root.mainloop()



def consiltinitial():
    global epoids,etaille,etemerature,eGlycémie,ePression,mchroniques,variable,variable2,variable3
    window=Tk()
    window.title("Consultation initial")
    window.geometry('375x500+500+130')
    window.configure(bg="#fff")
    window.resizable(False,False)
    window.iconbitmap("C:/Users/PC/Desktop/projX/patient.ico")

    titre = Label(window, text = "Consultation initial" ,fg="#1E90FF",background='white', font=("Microsoft YaJei UI Light",15,"bold"))
    titre.place(x =90, y = 1)


    def on_enter(e):
        epoids.delete(0,"end")
        
    def on_leave(e):
        poids=epoids.get()
        if poids=="":
            epoids.insert(0,'Poids par KG')
    epoids=Entry(window,background='white',border=0,fg="black", relief="sunken")
    epoids.place(x =120, y = 40)
    epoids.insert(0,"Poids par Kg")
    epoids.bind("<FocusIn>",on_enter)
    epoids.bind("<FocusOut>",on_leave)
    Frame(window,width=120,height=1,bg="#1E90FF").place(x=115 , y=60)

    def on_enter(e):
        etaille.delete(0,"end")
        
    def on_leave(e):
        taille=etaille.get()
        if taille=="":
            etaille.insert(0,'Taille par cm')
    etaille = Entry(window,background='white',border=0,fg="black", relief="sunken")
    etaille.place(x = 120,y=70)
    etaille.insert(0, "Taille par cm")
    etaille.bind("<FocusIn>",on_enter)
    etaille.bind("<FocusOut>",on_leave)

    Frame(window,width=120,height=1,bg="#1E90FF").place(x=115 , y=90)

    def on_enter(e):
        eFréquence_cardiaque.delete(0,"end")
    def on_leave(e):
        name=eFréquence_cardiaque.get()
        if name=="":
            eFréquence_cardiaque.insert(0,'Fréquence cardiaque')


    eFréquence_cardiaque = Entry(window,background='white',border=0,fg="black", relief="sunken")
    eFréquence_cardiaque.place(x = 120, y = 100)
    eFréquence_cardiaque.insert(0, "Fréquence_cardiaque")

    eFréquence_cardiaque.bind("<FocusIn>",on_enter)
    eFréquence_cardiaque.bind("<FocusOut>",on_leave)

    Frame(window,width=120,height=1,bg="#1E90FF").place(x=115 , y=120)

    def on_enter(e):
        eGlycémie.delete(0,"end")
    def on_leave(e):
        Glycémie=etemerature.get()
        if Glycémie=="":
            eGlycémie.insert(0,'Glycémie MMOL/L')

    eGlycémie   = Entry(window,background='white',border=0,fg="black", relief="sunken")
    eGlycémie.place(x = 120, y = 140)
    eGlycémie.insert(0, "Glycémie MMOL/L")
    eGlycémie.bind("<FocusIn>",on_enter)
    eGlycémie.bind("<FocusOut>",on_leave)
    Frame(window,width=120,height=1,bg="#1E90FF").place(x=115 , y=160)

    def on_enter(e):
        ePression.delete(0,"end")
    def on_leave(e):
        pression=ePression.get()
        if pression=="":
            ePression.insert(0,'Lhypertension artérielle par mmHg')
    ePression  = Entry(window,background='white',border=0,fg="black", relief="sunken")
    ePression.place(x = 115, y = 180)
    ePression.insert(0, "Lhypertension par mmHg")
    ePression.bind("<FocusIn>",on_enter)
    ePression.bind("<FocusOut>",on_leave)

    Frame(window,width=120,height=1,bg="#1E90FF").place(x=115 , y=200)




    def on_enter(e):
        etemerature.delete(0,"end")
        
    def on_leave(e):
        temerature=etemerature.get()
        if temerature=="":
            etemerature.insert(0,'Temperature par degre')

    etemerature = Entry(window,background='white',border=0,fg="black", relief="sunken")
    etemerature.place(x = 115, y = 220)
    etemerature.insert(0, "Temperature par degre")
    etemerature.bind("<FocusIn>",on_enter)
    etemerature.bind("<FocusOut>",on_leave)
    Frame(window,width=120,height=1,bg="#1E90FF").place(x=115 , y=240)

    variable = StringVar(window)
    variable.set("")
    variable2 = StringVar(window)
    variable2.set("")
    variable3 = StringVar(window)
    variable3.set("")

    lAllergie=Label(window,background="white",text = "Allergie---------------:",fg='#1E90FF').place(x = 100, y = 270)
    mAllergie = OptionMenu(window, variable, "oui", "non")
    mAllergie.place(x = 230, y = 270)

    ldouleur=Label(window,background="white",text = "La douleur------------:",fg='#1E90FF').place(x = 100, y = 320)
    mdouleur= OptionMenu(window, variable2, "oui", "non")
    mdouleur.place(x = 230, y = 320)

    chroniques=Label(window,background="white",text = "Maladies chroniques  :",fg='#1E90FF').place(x = 100, y = 370)
    mchroniques=OptionMenu(window, variable3, "oui", "non")
    mchroniques.place(x = 230, y = 370)

    Button(window,width=20,pady=7,text="save" ,font=('Helvetica bold', 10),bg='white',fg="#1E90FF",border=2,command=save2).place(x = 100, y = 440)
    mainloop()
#######-----------------------------------------Fin DE CREATION DE CONSULTATION INITIAL PATIENT WINDOW-----------------
def changepass():
    window=Tk()
    window.title("Change password")
    window.geometry('375x250+500+130')
    window.configure(bg="#fff")
    window.resizable(False,False)
    window.iconbitmap("C:/Users/PC/Desktop/projX/patient.ico")
    global epassword,eutilisateur,enewpassword
    titre = Label(window, text = "Change password" ,fg="#1E90FF",background='white', font=("Microsoft YaJei UI Light",15,"bold"))
    titre.place(x = 85, y = 1)
    def on_enter(e):
            eutilisateur.delete(0,"end")
    def on_leave(e):
            name=eutilisateur.get()
            if name=="":
                eutilisateur.insert(0,"Email d'utilisateur")
    eutilisateur = Entry(window,background='white',border=0,fg="black", relief="sunken")
    eutilisateur.place(x = 120, y = 60)
    eutilisateur.insert(0, "Email d'utilisateur")

    eutilisateur.bind("<FocusIn>",on_enter)
    eutilisateur.bind("<FocusOut>",on_leave)
    Frame(window,width=120,height=1,bg="#1E90FF").place(x=115 , y=80)


    def on_enter(e):
            epassword.delete(0,"end")
            
    def on_leave(e):
        name=epassword.get()
        if name=="":
            epassword.insert(0,'Password')

    epassword = Entry(window,background='white',border=0,fg="black", relief="sunken")
    epassword.place(x = 120, y = 100)
    epassword.insert(0, "Password")
    epassword.bind("<FocusIn>",on_enter)
    epassword.bind("<FocusOut>",on_leave)
    Frame(window,width=120,height=1,bg="#1E90FF").place(x=115 , y=120)

    def on_enter(e):
            enewpassword.delete(0,"end")
            
    def on_leave(e):
        enewpassword=epassword.get()
        if enewpassword=="":
            epassword.insert(0,'Password')

    enewpassword = Entry(window,background='white',border=0,fg="black", relief="sunken")
    enewpassword.place(x = 120, y = 140)
    enewpassword.insert(0, "Nouveaux password")
    enewpassword.bind("<FocusIn>",on_enter)
    enewpassword.bind("<FocusOut>",on_leave)
    Frame(window,width=120,height=1,bg="#1E90FF").place(x=115 , y=160)
    
        
    Button(window,width=20,pady=7,text="save" ,font=('Helvetica bold', 12,"bold"),bg='white',fg="#57a1f8",border=2,command=save4).place(x = 75, y = 200)


    window.mainloop()
def on_leave(e):
    name=function.get()
    if name=="":
        function.insert(0,'Function')
img1 = PhotoImage(file= 'C:/Users/PC/Desktop/projX/patient.png')
smaller_image = img1.subsample(6, 6)

Label(window,image=smaller_image,bg='white').place(x=70,y=50)


frame = Frame(window,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text="Sign in",fg='#57a1f8',bg='white',font=("Microsoft YaJei UI Light",23,"bold"))
heading.place(x=100,y=5)

function=Entry(frame,width=25,fg='black',border=0,bg="white",font=("Microsoft YaJei UI Light",11))
function.place(x=30,y=80)
function.insert(0, "Function")
function.bind("<FocusIn>",on_enter)
function.bind("<FocusOut>",on_leave)

linefram=Frame(frame,width=295,height=2,bg="black")
linefram.place(x=25,y=107)


def on_enter(e):
    password.delete(0,"end")
def on_leave(e):
    name=password.get()
    if name=="":
        password.insert(0,'Mot de pass')


password=Entry(frame,width=25,fg='black',border=0,bg="white",font=("Microsoft YaJei UI Light",11))
password.place(x=30,y=150)
password.insert(0, "Mot de pass")
password.bind("<FocusIn>",on_enter)
password.bind("<FocusOut>",on_leave)
if password.get() != "Mot de pass":
    password.configure(show='*')


linefram2=Frame(frame,width=295,height=2,bg="black")
linefram2.place(x=25,y=177)

bottonconnect=Button(frame,width=39,pady=7,text="Connect",bg='#57a1f8',fg="white",border=0,command=singin)
bottonconnect.place(x=35,y=204)

window.mainloop()
