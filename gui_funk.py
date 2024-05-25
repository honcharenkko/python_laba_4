import customtkinter as ctk
import sqlite3
from PIL import Image



app = ctk.CTk()
app.geometry("600x500")
app.title("IMS")



conn = sqlite3.connect('kunden.db')
cur = conn.cursor()

Id = None
Name = None
Count = None
Category = None
Country = None
Weight = None
nam = None
pasw = None

def neue_ding():
    def help_win_ding():
        def send_data():
            Name = name_enter.get()
            Count = count_enter.get()
            Category = category_enter.get()
            Country = country_enter.get()
            Weight = weight_enter.get()
            sql_query = f"INSERT INTO Dinge (Name, Count, Category, Country, Weight) VALUES (?, ?, ?, ?, ?)"
            values = (Name, Count, Category, Country, Weight)
            cur.execute(sql_query, values)
            # Підтвердження змін у базі даних
            conn.commit()

            help_win.destroy()

        help_win = ctk.CTkToplevel(app)
        help_win.geometry("500x300")

        help_name = ctk.CTkLabel(help_win, text="Додати товар", font=("Bauhaus",33))
        help_name.pack(pady =(10, 0))
            #Створення фреймів
        big_frame = ctk.CTkFrame(master=help_win, width=450, height=200, fg_color="transparent")
        big_frame.pack(pady = (10,10))
        
        left_frame = ctk.CTkFrame(master=big_frame, fg_color="transparent")
        left_frame.grid(row = 0, column =0, padx =10)
        right_frame = ctk.CTkFrame(master=big_frame, fg_color="transparent")
        right_frame.grid(row = 0, column =1, padx =10)
            #Заповнення лівої сторони
        name_label = ctk.CTkLabel(left_frame, text="Name:", font=("Bauhaus",18))
        name_enter = ctk.CTkEntry(left_frame)
        name_label.grid(row = 1, column =0, pady =10, sticky="w")
        name_enter.grid(row = 1, column =1, pady =10, padx =10)

        count_label = ctk.CTkLabel(left_frame, text="Count:", font=("Bauhaus",18))
        count_enter = ctk.CTkEntry(left_frame)
        count_label.grid(row = 2, column =0, pady =10, sticky="w")
        count_enter.grid(row = 2, column =1, pady =10, padx =10)

        weight_label = ctk.CTkLabel(left_frame, text="Weight:", font=("Bauhaus",18))
        weight_enter = ctk.CTkEntry(left_frame)
        weight_label.grid(row = 3, column =0, pady =10, sticky="w")
        weight_enter.grid(row = 3, column =1, pady =10, padx =10)

            #Заповнення правої сторони
        category_label = ctk.CTkLabel(right_frame, text="Category:", font=("Bauhaus",18))
        category_enter = ctk.CTkOptionMenu(right_frame, values=["food", "tech", "cloth"])
        category_label.grid(row = 0, column =0, pady =10, sticky="w")
        category_enter.grid(row = 0, column =1, pady =10, padx =10)

        country_label = ctk.CTkLabel(right_frame, text="Country:", font=("Bauhaus",18))
        country_enter = ctk.CTkOptionMenu(right_frame, values=["USA", "JP", "UA"])
        country_label.grid(row = 1, column =0, pady =10, sticky="w")
        country_enter.grid(row = 1, column =1, pady =10, padx =10)



        conf_btn = ctk.CTkButton(help_win, text="Confirm", font=("Bauhaus",18), command=send_data)
        conf_btn.pack(pady= 20)
    help_win_ding()



def warning():
    def close_warn():
        warn.destroy()
    warn = ctk.CTkToplevel(app)

    warn_lable = ctk.CTkLabel(warn, text="Введені данні некоректні")
    warn_btn = ctk.CTkButton(warn, text="OK", command=close_warn)

    warn_lable.pack()
    warn_btn.pack()

def login_user(username, password):
    if not isinstance(username, str) or not isinstance(password, (str, int)):
        warning()
        raise TypeError('Данні введені некоректно')
    else:
        cur.execute("SELECT * FROM kunden WHERE nickname=? AND password=?", (username, password))
        user = cur.fetchone()
        conn.commit()
        return user is not None


def add_arb(nam, pasw):
        if not nam or not pasw:
            warning()
            raise ValueError('Пусті данні')
        else:
            cur.execute("SELECT * FROM kunden WHERE nickname=?", (nam))
            existing_user = cur.fetchone()

        if existing_user:
            warning()
            raise ValueError('Користувач вже є')
        else:
            cur.execute("INSERT INTO kunden (nickname, password) VALUES (?, ?)", (nam, pasw))
            conn.commit()
            kun.destroy()
def neue_kunde():
    global kun, nam, pasw
    kun = ctk.CTkToplevel()
    kun.geometry("400x300")
    kun.title("Add Arbeiter")


    add_lable = ctk.CTkLabel(kun, text="Додати нового користувача", font=("Bauhaus",26))
    add_lable.pack(pady = 10)
    fr1 = ctk.CTkFrame(master=kun, fg_color="transparent")
    fr1.pack()
    arb_name = ctk.CTkLabel(fr1, text="Nik:", font=("Bauhaus",18))
    arb_pass = ctk.CTkLabel(fr1, text="Password:", font=("Bauhaus",18))

    arb_name_ent = ctk.CTkEntry(fr1)
    arb_pass_ent = ctk.CTkEntry(fr1)

    arb_name.grid(row = 0, column = 0, sticky = "w",padx = 5, pady =5)
    arb_name_ent.grid(row = 0, column = 1)
    arb_pass.grid(row = 1, column = 0, sticky = "w", padx = 5)
    arb_pass_ent.grid(row = 1, column = 1)

    conf_arb =ctk.CTkButton(kun, text="Add", command=lambda: add_arb(nam, pasw))
    conf_arb.pack(pady = 10)
    nam = arb_name_ent.get()
    pasw = arb_pass_ent.get()
#AUTENTIFICATION WINDOW

def autentification():
    def login_btn():
        global username, password
        username = name_blank.get()
        password = password_blank.get()
        if login_user(username, password):
            main_txt.destroy()
            name_blank.destroy()
            password_blank.destroy()
            log_btn.destroy()
            frame.destroy()
            mainwind()
        elif username == None or password == None:
            warning()
            raise TypeError('Данні введені некоректно')  
            
        else:
            warning()
            raise TypeError('Данні введені некоректно')
        

    main_txt = ctk.CTkLabel(app, text="WELCOME",font=("Bauhaus",33))
    main_txt.pack(pady= (140, 0))

    name_blank = ctk.CTkEntry(app, width=200, height=35, corner_radius=15)
    name_blank.pack(pady = 10)
    password_blank = ctk.CTkEntry(app, width=200, height=35, corner_radius=15)
    password_blank.pack(pady = (0, 10))
    frame = ctk.CTkFrame(master=app, width=200, height=50, fg_color = 'transparent')
    frame.pack()

    log_btn = ctk.CTkButton(frame, text= "Log in", width= 80, command=login_btn)
    log_btn.pack()

def upp_it_com(new_count, object_name):
    table_name = 'Dinge'
    try:
        conn = sqlite3.connect('kunden.db')
        cur = conn.cursor()
        cur.execute(f"UPDATE {table_name} SET count = ? WHERE name = ?", (new_count, object_name))
        conn.commit()
    except sqlite3.Error as e:
        print("Помилка при оновленні товару:", e)
    finally:
        sett_win.destroy()

def del_btn_com(object_name):
    table_name = 'Dinge'
    try:
        conn = sqlite3.connect('kunden.db')
        cur = conn.cursor()
        cur.execute(f"DELETE FROM {table_name} WHERE name = ?", (object_name,))
        conn.commit()
    except sqlite3.Error as e:
        print("Помилка при видаленні товару:", e)
    finally:
        sett_win.destroy()

def sett_com():
    global sett_win
    sett_win = ctk.CTkToplevel(app)
    sett_win.geometry("500x300")
    
    # Отримання імен предметів з бази даних
    cur.execute("SELECT name from Dinge")
    nik = cur.fetchall()
    items = [item[0] for item in nik]
    
    # Створення вікна з опціями для вибору предмету
    sel_it = ctk.CTkOptionMenu(sett_win, values=items)
    sel_it.pack()
    
    # Створення інтерфейсу для введення даних
    ccnt_lab = ctk.CTkLabel(sett_win, text="Count")
    ccnt = ctk.CTkEntry(sett_win)
    ccnt_lab.pack()
    ccnt.pack()
    
    # Створення кнопки для видалення предмету
    del_btn = ctk.CTkButton(sett_win, text="Видалити товар", command=lambda: del_btn_com(sel_it.get()))
    corect_btn = ctk.CTkButton(sett_win, text="Редагувати товар", command=lambda: upp_it_com( ccnt.get(),sel_it.get()))
    del_btn.pack(pady=(10, 10))
    corect_btn.pack()
    
    


def mainwind():
    def item_select():
        for widget in scrollable_frame.winfo_children():
            widget.destroy()

        cur.execute("SELECT name from Dinge")
        nik = cur.fetchall()
        my_array0 = [i + 1 for i in range(len(nik))]
        my_array = [item[0] for item in nik]

        cur.execute("SELECT count from Dinge")
        nik1 = cur.fetchall()
        my_array1 = [item[0] for item in nik1]
        conn.commit()


        x = 0
        for item0, item, item1 in zip(my_array0, my_array, my_array1):
            x =x+1
            new_frame = ctk.CTkFrame(master=scrollable_frame, fg_color="#343638")
            new_frame.pack(pady = 10)


            label0 = ctk.CTkLabel(new_frame, text=item0, width=10)
            label0.grid(row = 0, column =0, padx= (5, 0), sticky="w")
            label = ctk.CTkLabel(new_frame, text=item, width=100)
            label.grid(row = 0, column =1, padx= (5,90), sticky="w")  
            label1 = ctk.CTkLabel(new_frame, text=item1)
            label1.grid(row = 0, column =2, padx= (270,5), sticky="e")
        

    def search_object():
        for widget in scrollable_frame.winfo_children():
            widget.destroy()
        # Отримання даних з поля вводу
        serch = serch_ent.get()

        # Виконання SQL-запиту для пошуку об'єкта
        sql_query = "SELECT name, count FROM Dinge WHERE name LIKE ?"
        values = (serch + '%',)

        try:
            cur.execute(sql_query, values)
            results = cur.fetchall()
            names_tuple = tuple(result[0] for result in results)
            counts_tuple = tuple(result[1] for result in results)
            if names_tuple:

                x = 0
                for name, count in zip(names_tuple, counts_tuple):
                    x =x+1
                    new_frame = ctk.CTkFrame(master=scrollable_frame, fg_color="#343638")
                    new_frame.grid(row=x, column = 0, pady = 10, sticky="ew")
                    label = ctk.CTkLabel(new_frame, text=name, width=100, )
                    label.grid(row = 0, column =0, padx= (10,90), sticky="e")  
                    label1 = ctk.CTkLabel(new_frame, text=count)
                    label1.grid(row = 0, column =1, padx= (330,5))
            else:
                new_frame1 = ctk.CTkFrame(master=scrollable_frame, fg_color="#343638")
                new_frame1.grid(pady = 10)
                lab = ctk.CTkLabel(new_frame1, text = "Товару не знайдено")
                lab.grid()

        except sqlite3.Error as e:
            new_frame2 = ctk.CTkFrame(master=scrollable_frame, fg_color="#343638")
            new_frame2.grid(pady = 10)
            showerror= ctk.CTkLabel(new_frame2, text = "Помилка при виконанні запиту: ")
            showerror.grid()


    neue_kunde_img = ctk.CTkImage(Image.open("new-account.png"), size=(30, 30))
    neue_dinge_img = ctk.CTkImage(Image.open("add-product.png"), size=(30, 30))
    serch_img = ctk.CTkImage(Image.open("search.png"), size=(25, 25))
    update_img = ctk.CTkImage(Image.open("refresh.png"), size=(30, 30))
    sett_img = ctk.CTkImage(Image.open("settings.png"), size = (30, 30))
    def_txt = 'Пошук...'

    frame_sett_name = ctk.CTkFrame(master=app, width= 570, fg_color="transparent", bg_color="transparent")
    frame_sett_name.pack()
    sett_btn =ctk.CTkButton(master=frame_sett_name, image=sett_img,text="", command= sett_com,
                              corner_radius=15, height= 40, width=40, bg_color="transparent")
    sett_btn.grid(row = 0, column =0, sticky = 'e', padx =(0, 0))
    serch_txt = ctk.CTkLabel(master=frame_sett_name, text='Інвентар товарів', font=("Bauhaus",26))
    serch_txt.grid(pady=(10, 0), padx =(300,0),row = 0, column = 1)

    serch_frame = ctk.CTkFrame(master=app, height=50, width= 570, fg_color="transparent")
    serch_frame.pack(pady = 10)


    serch_ent = ctk.CTkEntry(serch_frame, height= 50, width = 570, corner_radius=15, bg_color="transparent")
    serch_ent.insert(0, def_txt)
    serch_ent.grid(row= 0, column= 0)

    
    serch_btn = ctk.CTkButton(serch_frame, image=serch_img,text="", command=search_object, 
                              corner_radius=15, height= 40, width=40, bg_color="#343638")
    serch_btn.grid(row= 0, column= 0, sticky = 'e', padx = 10)
    scrollable_frame = ctk.CTkScrollableFrame(app, width=550, height=300)
    scrollable_frame.pack()

    but_frame = ctk.CTkFrame(master=app, fg_color="transparent")
    but_frame.pack(pady = 10)
    neue_kunde_btn = ctk.CTkButton(but_frame, image=neue_kunde_img, text="", command=neue_kunde)
    neue_kunde_btn.grid(row =0, column =0, padx=(0, 50))

    neue_dinge_btn =ctk.CTkButton(but_frame, image=neue_dinge_img, text='', command=neue_ding)
    neue_dinge_btn.grid(row =0, column =2, padx=(50, 0))
    
    update_serch_btn = ctk.CTkButton(but_frame, image=update_img, text="", command=item_select)
    update_serch_btn.grid(row =0, column =1)



#MAIN WINDOW

autentification()




app.mainloop()