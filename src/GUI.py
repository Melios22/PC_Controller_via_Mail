# import tkinter
import customtkinter 
from PIL import Image

class Popup(customtkinter.CTkToplevel):
    def __init__(self, self_title : str, path : str = None, **kwargs):
        super().__init__( **kwargs)
        self.geometry(f"{900}x{540}+{self.winfo_x() + 300}+{self.winfo_y() + 150}")
        self.title(self_title)
        self.resizable(False, False)
        self.focus_force()
        self.grab_set()

        self.type = path.split(".")[1]
        print(self.type)

        if (self.type in ["png", "jpg", "jpeg", "tiff", "bmp", "gif"]):
            self.image = customtkinter.CTkImage(Image.open(path), size=(900,540))
            self.image_label = customtkinter.CTkLabel(master=self, image=self.image, text="")
            self.image_label.pack()
            print(path)
            return
        
        if (self.type == "txt"):
            self.file = customtkinter.CTkScrollableFrame(master=self, width=900, height=540, fg_color="white")
            # read file
            data = []
            with open(path, "r") as f:
                for line in f :
                    line = line.replace("\n", "")
                    data.append(line)
                    print(data)
            
            for i in range(len(data)):
                self.file_label = customtkinter.CTkButton(master=self.file, text=data[i], width=900, height=50, fg_color="white", anchor="w", font=("Arial", 20), text_color="black", hover=0, border_color="black", border_width=2)
                self.file_label.pack()
            
            
            self.file.pack()
            
            return

    pass


class Widget(customtkinter.CTkButton):
    __WIDTH = 0
    __HEIGHT = 0
    __x = 3
    __y = 3

    __m_master = ""
    __sender_mail = ""
    __recive_mail = ""
    __reply_subject = ""
    __subject = ""
    __date = ""
    __attachment = ""

    def print_info(self):   
        print(self.__m_master)
        print(self.__sender_mail)
        print(self.__recive_mail)
        print(self.__subject)
        print(self.__date)
        print(self.__attachment)
    
    def attachment_event(self, command : str, attachment : str):
       
            self.popup = Popup(self_title=command, path=attachment, master=self)
            return 
    
    def home_button_event(self, m_master):
        for widget in m_master.widget_list:
            print(len(m_master.widget_list))
            widget.destroy()
        
        m_master.widget_label = Mail_page(master=m_master)
        m_master.widget_label.place(x=0,y=0)

        cur_len = len(m_master.widget_list)
        for i in range(cur_len):
            m_master.add_new_mail(sender_mail=m_master.widget_list[i].__sender_mail, subject=m_master.widget_list[i].__subject, date=m_master.widget_list[i].__date, reply_subject=m_master.widget_list[i].__reply_subject, attachment=m_master.widget_list[i].__attachment)
            print(len(m_master.widget_list))

        del m_master.widget_list[0 : cur_len ]
       
        pass
            
            

        
        


    def button_event(self, m_master, sender_mail : str, recive_mail : str, subject : str, date : str, reply_subject : str, attachment : str):
        for widget in m_master.widget_list:
            widget.pack_forget()


        self.white_space = customtkinter.CTkButton(master=m_master.widget_label, text="", width=self.__WIDTH, height= self.__HEIGHT/10, fg_color="white", anchor="w",corner_radius=10, hover=0, border_width=2, border_color="black")
        self.white_space.place(x=0,y=0)

        self.home_btn = customtkinter.CTkButton(master=self.white_space, text="Home", width=100, height=40, fg_color="white", anchor="w", font=("Arial", 20, "bold"), hover=True,text_color="black", border_width=2, hover_color="#2196F3", command=lambda: self.home_button_event(m_master=m_master))
        self.home_btn.place(x=5,y=5)

        self.info_space = customtkinter.CTkButton(master=m_master.widget_label, text="", width=self.__WIDTH, height= self.__HEIGHT/10, fg_color="white", anchor="w",corner_radius=10, hover=0, border_width=2, border_color="black")
        self.info_space.pack(padx=5, pady=5)

        self.from_letter = customtkinter.CTkButton(master=self.info_space, text="Email:", width=40, height=20, fg_color="white", anchor="w", font=("Arial", 20, "bold"), hover=0,text_color="black", border_width=0 )
        self.from_letter.place(x=3,y=12)

        self.sender_mail_zone = customtkinter.CTkButton(master=self.info_space, text=sender_mail, width=self.__WIDTH - self.__WIDTH/4, height=20, fg_color="white", anchor="w", font=("Arial", 20), hover=0,text_color="black", border_width=0  )
        self.sender_mail_zone.place(x=75 ,y=12)

        self.date_zone = customtkinter.CTkButton(master=self.info_space, text=date, width=self.__WIDTH/4, height=20, fg_color="white", anchor="e", font=("Arial", 20), hover=0, text_color="black", border_width=0 )
        self.date_zone.place(x=self.__WIDTH/4 * 3 - 2 * self.__x, y=12)

        self.subject_zone = customtkinter.CTkButton (master=m_master.widget_label, text="", width=self.__WIDTH, height=self.__HEIGHT/10 * 3, fg_color="white", anchor="w", font=("Arial", 20, "bold"), hover=0,text_color="black", border_width=2, border_color="black")
        self.subject_zone.pack(padx=5, pady=5)
        self.subject_letter = customtkinter.CTkButton(master=self.subject_zone, text="Subject:", width=40, height=20, fg_color="white", anchor="w", font=("Arial", 20, "bold"), hover=0,text_color="black", border_width=0  )
        self.subject_letter.place(x=3,y=12)

        self.subject_content = customtkinter.CTkButton(master=self.subject_zone, text=subject, width=self.__WIDTH - self.__WIDTH/4, height=20, fg_color="white", anchor="w", font=("Arial", 20), hover=0,text_color="black", border_width=0  )
        self.subject_content.place(x=120 ,y=12)
        
        self.break_line = customtkinter.CTkButton(master=m_master.widget_label, text="", width=self.__WIDTH, height=7, fg_color="black", anchor="w",corner_radius=20, hover=0, border_width=0, border_color="black")
        self.break_line.pack(padx=2, pady=2)

        self.reply_zone = customtkinter.CTkButton(master=m_master.widget_label, text="", width=self.__WIDTH, height=self.__HEIGHT/2 - 46, fg_color="white", anchor="w", font=("Arial", 20, "bold"), hover=0,text_color="black", border_width=2, border_color="black")
        self.reply_zone.pack(padx=5, pady=5)

        self.reply_from_letter = customtkinter.CTkButton(master=self.reply_zone, text="From:", width=40, height=20, fg_color="white", anchor="w", font=("Arial", 20, "bold"), hover=0,text_color="black", border_width=0  )
        self.reply_from_letter.place(x=3,y=12)

        self.reply_email = customtkinter.CTkButton(master=self.reply_zone, text=recive_mail, width=self.__WIDTH - self.__WIDTH/4, height=20, fg_color="white", anchor="w", font=("Arial", 20), hover=0,text_color="black", border_width= 0 )
        self.reply_email.place(x=80 ,y=12)

        self.reply_subject_letter = customtkinter.CTkButton(master=self.reply_zone, text="Subject:", width=40, height=20, fg_color="white", anchor="w", font=("Arial", 20, "bold"), hover=0,text_color="black", border_width=0  )
        self.reply_subject_letter.place(x=3,y=50)

        self.reply_subject = customtkinter.CTkButton(master=self.reply_zone, text=reply_subject, width=self.__WIDTH - self.__WIDTH/4, height=20, fg_color="white", anchor="w", font=("Arial", 20), hover=0,text_color="black", border_width= 0 )
        self.reply_subject.place(x=100 ,y=50)

        self.attachment_letter = customtkinter.CTkButton(master=self.reply_zone, text="Attachment:", width=40, height=20, fg_color="white", anchor="w", font=("Arial", 20, "bold"), hover=0,text_color="black", border_width=0  )
        self.attachment_letter.place(x=3,y=88)

        attachment_icon = customtkinter.CTkImage(Image.open("images/attachment.png"), size=(40,40))
        self.attachment = customtkinter.CTkButton(master=self.reply_zone, text=attachment, width=self.__WIDTH/4, height=20, fg_color="white", anchor="w", font=("Arial", 20),text_color="black", border_width= 2, corner_radius=10, border_color="black", image=attachment_icon, hover_color="#2196F3", command=lambda: self.attachment_event(command=subject, attachment=attachment))
        self.attachment.place(x=160 ,y=88)        
        
        
    def add_widget(self):

        self.mail_lb = customtkinter.CTkButton(master=self, text=self.__sender_mail, width=self.__WIDTH/3 - self.__x, height=self.__HEIGHT/10 - self.__y, fg_color="white", anchor="w", font=("Arial", 20), text_color="black", hover=0, corner_radius=0, command=lambda: self.button_event(m_master=self.__m_master, sender_mail=self.__sender_mail, recive_mail=self.__recive_mail, subject=self.__subject, reply_subject=self.__reply_subject, date=self.__date, attachment=self.__attachment))
        self.mail_lb.place(x=2,y=2)

        self.subject_lb = customtkinter.CTkButton(master=self, text=self.__subject, width=self.__WIDTH/3 - self.__x, height=self.__HEIGHT/10 - self.__y, fg_color="white", anchor="w", font=("Arial", 20), text_color="black", hover=0, corner_radius=0, command=lambda: self.button_event(m_master=self.__m_master, sender_mail=self.__sender_mail, recive_mail=self.__recive_mail, subject=self.__subject, reply_subject=self.__reply_subject, date=self.__date, attachment=self.__attachment))
        self.subject_lb.place(x=self.__WIDTH/3 + self.__x, y=2)
        # print(self.__date)

        self.date_lb = customtkinter.CTkButton(master=self, text=self.__date, width=self.__WIDTH/3 - self.__x, height=self.__HEIGHT/10 - self.__y, fg_color="white", anchor="e", font=("Arial", 20), text_color="black", hover=0, corner_radius=0, command=lambda: self.button_event(m_master=self.__m_master, sender_mail=self.__sender_mail, recive_mail=self.__recive_mail, subject=self.__subject, date=self.__date,reply_subject=self.__reply_subject, attachment=self.__attachment))
        self.date_lb.place(x=self.__WIDTH/3 * 2 - 2 * self.__x, y=2)

        
    def __init__(self, m_master, sender_mail : str, recive_mail : str, subject : str, date : str, attachment : str, reply_subject : str, **kwargs):   
        super().__init__( **kwargs)
       
        self.configure(text="", width=m_master.APP_WIDTH - self.__x, height=m_master.APP_HEIGHT/10 , fg_color="white", anchor="w",corner_radius=10, hover=0, border_width=2, border_color="black")
        (self.__WIDTH, self.__HEIGHT) = (m_master.APP_WIDTH - 20, m_master.APP_HEIGHT - m_master.APP_HEIGHT/15)

        self.__m_master = m_master
        self.__sender_mail = sender_mail
        self.__recive_mail = recive_mail
        self.__subject = subject
        self.__date = date
        self.__attachment = attachment
        self.__reply_subject = reply_subject
        
        self.add_widget()

        
class Mail_page(customtkinter.CTkScrollableFrame):
    __info_lb = None
    def add_widget(self, master, sender_mail : str, recive_mail : str, subject : str, date : str, reply_subject : str, attachment : str):
        self.widget = Widget(master=self, m_master=master, sender_mail=sender_mail, recive_mail=recive_mail, subject=subject, date=date,reply_subject=reply_subject, attachment=attachment)
        if (self.widget not in master.widget_list):
            master.widget_list.append(self.widget)

        self.widget.pack(after=self.__info_lb, padx=0, pady=0)

        
        pass
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(width=master.APP_WIDTH - 13, height=master.APP_HEIGHT - master.APP_HEIGHT/15, fg_color="white",corner_radius=10, border_width=0, border_color="black")
        
        self.__info_lb = customtkinter.CTkButton(master=self,text="", width=master.APP_WIDTH - 13, height=master.APP_HEIGHT/10 , fg_color="white", anchor="w",corner_radius=10, hover=0, border_width=2, border_color="black")
        self.__info_lb.pack()

        self.from_letter = customtkinter.CTkButton(master=self.__info_lb, text="Email:", width=40, height=20, fg_color="white", anchor="w", font=("Arial", 20, "bold"), hover=0,text_color="black" )
        self.from_letter.place(x=3,y=12)

        self.subject_letter = customtkinter.CTkButton(master=self.__info_lb, text="Subject:", width=40, height=20, fg_color="white", anchor="w", font=("Arial", 20, "bold"), hover=0,text_color="black"  )
        self.subject_letter.place(x=master.APP_WIDTH/3 ,y=12)

        self.date_letter = customtkinter.CTkButton(master=self.__info_lb, text="Date:", width=40, height=20, fg_color="white", anchor="w", font=("Arial", 20, "bold"), hover=0, text_color="black" )
        self.date_letter.place(x=master.APP_WIDTH/3 * 3 - 150,y=12)
        
        
       
            

class App(customtkinter.CTk):
    APP_WIDTH = 1000
    APP_HEIGHT = 600
    self_email = "emailcontrolMMT@gmail.com"
    sender_email = ""
    widget_list = []
  
    def add_new_mail(self, sender_mail : str, subject : str, date : str, reply_subject : str,  attachment : str):
        self.widget_label.add_widget(master=self, sender_mail=sender_mail, subject=subject, recive_mail=self.self_email, date=date, attachment=attachment, reply_subject=reply_subject)
        
    
    def __init__(self):
        super().__init__()
        x = 300
        y = 100
        self.title("PC Controller via Email")
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{x}+{y}")
        # self.resizable(False, False)
        self.configure(fg_color="white")

        self.widget_label = Mail_page(master=self)
        self.widget_label.place(x=0, y=0)
        


if __name__ == "__main__":
    app = App()

    attachment_list = ["images\\Screenshot.png", "images\\List_Process.txt", "images\\App_Process.txt"]
    subject_list = ["Screenshot", "listProcess", "AppProcess"]
    for i in range(5):
        app.after(3000,app.add_new_mail(sender_mail="sender_mail" + str(i) + "@gmail.com", subject=subject_list[i % 3], date= str(i % 31) + "/" + str(i % 12) + "/2023", reply_subject="reply_subject" + str(i), attachment=attachment_list[i % 3]))
    app.mainloop()
