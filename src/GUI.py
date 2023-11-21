import tkinter as tk

import customtkinter
from PIL import Image, ImageTk


def Splash_Screen():
    def quit():
        for after_id in root.tk.eval("after info").split():
            root.after_cancel(after_id)
        root.after(1000, root.destroy)

    root = tk.Tk()
    _width = 900
    _height = 500
    root.geometry(f"{_width}x{_height}+{_width // 3}+{_height // 5}")
    root.title("PC Controller via Email")
    root.resizable(False, False)
    root.overrideredirect(True)
    gif_file = Image.open("assets\\yasuo.gif")
    size = gif_file.n_frames
    frames = []
    for i in range(size):
        gif_file.seek(i)
        photo = ImageTk.PhotoImage(gif_file)
        frames.append(photo)

    loop_frames = gif_file.info["duration"]
    gif_label = tk.Label(root, image=frames[0])
    gif_label.pack()

    def update(ind, counter):
        if counter < loop_frames * 2:
            frame = frames[ind]
            ind += 1
            if ind == size:
                ind = 0
            gif_label.config(image=frame)
            root.after(loop_frames, update, ind, counter + 1)
        else:
            quit()

    root.after(0, lambda: update(0, 0))
    root.protocol("WM_DELETE_WINDOW", quit)
    root.mainloop()


class Popup(customtkinter.CTkToplevel):
    def __init__(self, self_title: str, path: str = None, **kwargs):
        super().__init__(**kwargs)
        self.geometry(f"{900}x{540}+{self.winfo_x() + 350}+{self.winfo_y() + 150}")
        self.title(self_title)
        self.resizable(False, False)
        self.after(201, lambda: self.iconbitmap("assets\\icon4.ico"))
        self.focus_force()
        self.grab_set()

        self.type = path.split(".")[1]

        if self.type in ["png", "jpg", "jpeg", "tiff", "bmp", "gif"]:
            self.image = customtkinter.CTkImage(Image.open(path), size=(900, 540))
            self.image_label = customtkinter.CTkLabel(
                master=self, image=self.image, text=""
            )
            self.image_label.pack()
            return

        if self.type in ["txt", 'log']:
            self.file = customtkinter.CTkScrollableFrame(
                master=self,
                width=900,
                height=540,
                fg_color="#f3defa",
                scrollbar_button_color="#9b47ba",
                scrollbar_button_hover_color="#9b47ba",
            )

            with open(path, "r") as f:
                data = f.read()

            self.file.pack()
            label = customtkinter.CTkLabel(
                master=self.file,
                text=data,
                text_color="black",
                bg_color="#f3defa",
                width=900,
                height=500,
                justify="left",
                anchor="nw",
                font=("Lucida Console", 30),
            )
            label.pack(side="left")

            return

    pass


class Widget(customtkinter.CTkButton):
    __WIDTH = 0
    __HEIGHT = 0
    __x = 3
    __y = 3

    __m_master = None
    __sender_mail = ""
    __recive_mail = ""
    __reply_subject = ""
    __subject = []
    __date = ""
    __attachment = []

    def attachment_event(self, command: str, attachment: str):
        self.popup = Popup(self_title=command, path=attachment, master=self)
        return

    def home_button_event(self, m_master):
        for widget in m_master.widget_list:
            widget.destroy()

        m_master.widget_label = Mail_page(master=m_master)
        m_master.widget_label.place(x=0, y=0)

        cur_len = len(m_master.widget_list)
        for i in range(cur_len):
            m_master.add_new_mail(
                sender_mail=m_master.widget_list[i].__sender_mail,
                subject=m_master.widget_list[i].__subject,
                date=m_master.widget_list[i].__date,
                reply_subject=m_master.widget_list[i].__reply_subject,
                attachment=m_master.widget_list[i].__attachment,
            )

        del m_master.widget_list[0:cur_len]

        pass

    def button_event(
        self,
        m_master,
        sender_mail: str,
        recive_mail: str,
        subject: [],
        date: str,
        reply_subject: str,
        attachment: [],
    ):
        for widget in m_master.widget_list:
            widget.pack_forget()

        self.white_space = customtkinter.CTkButton(
            master=m_master.widget_label,
            text="",
            width=self.__WIDTH + 15,
            height=self.__HEIGHT / 10 + 3,
            fg_color="#f3defa",
            anchor="w",
            corner_radius=0,
            hover=0,
            border_width=2,
            border_color="black",
        )
        self.white_space.place(x=0 + 2, y=0)
        home_icon = customtkinter.CTkImage(Image.open("assets/home.png"), size=(40, 40))
        self.home_btn = customtkinter.CTkButton(
            master=self.white_space,
            text="",
            width=50,
            height=50,
            fg_color="#f3defa",
            anchor="w",
            font=("Arial", 20, "bold"),
            hover=False,
            text_color="black",
            border_width=2,
            hover_color="#2196F3",
            image=home_icon,
            border_color="black",
            corner_radius=0,
            command=lambda: self.home_button_event(m_master=m_master),
        )
        self.home_btn.place(x=5, y=3)

        self.info_space = customtkinter.CTkButton(
            master=m_master.widget_label,
            text="",
            width=self.__WIDTH,
            height=self.__HEIGHT / 10,
            fg_color="#f3defa",
            anchor="w",
            corner_radius=0,
            hover=0,
            border_width=2,
            border_color="black",
        )
        self.info_space.pack(padx=5, pady=5)

        self.from_letter = customtkinter.CTkButton(
            master=self.info_space,
            text="Email:",
            width=40,
            height=20,
            fg_color="#f3defa",
            anchor="w",
            font=("Arial", 20, "bold"),
            hover=0,
            text_color="black",
            border_width=0,
        )
        self.from_letter.place(x=3, y=12)

        self.sender_mail_zone = customtkinter.CTkButton(
            master=self.info_space,
            text=sender_mail,
            width=self.__WIDTH - self.__WIDTH / 4,
            height=20,
            fg_color="#f3defa",
            anchor="w",
            font=("Arial", 20),
            hover=0,
            text_color="black",
            border_width=0,
        )
        self.sender_mail_zone.place(x=75, y=12)

        self.date_zone = customtkinter.CTkButton(
            master=self.info_space,
            text=date,
            width=self.__WIDTH / 4,
            height=20,
            fg_color="#f3defa",
            anchor="e",
            font=("Arial", 20),
            hover=0,
            text_color="black",
            border_width=0,
        )
        self.date_zone.place(x=self.__WIDTH / 4 * 3 - 2 * self.__x, y=12)

        self.subject_zone = customtkinter.CTkScrollableFrame(
            master=m_master.widget_label,
            width=self.__WIDTH - 20,
            height=170,
            fg_color="#f3defa",
            corner_radius=0,
            border_width=2,
        )
        self.subject_zone._scrollbar.configure(height=0)
        self.subject_zone.pack()

        self.subject_letter = customtkinter.CTkButton(
            master=self.subject_zone,
            text="Content:",
            width=40,
            height=20,
            fg_color="#f3defa",
            anchor="nw",
            font=("Arial", 20, "bold"),
            hover=0,
            text_color="black",
            border_width=0,
        )
        self.subject_letter.pack(side="top", fill="x", expand=True)

        for i in range(len(subject)):
            customtkinter.CTkButton(
                master=self.subject_zone,
                text="> " + str(subject[i]),
                width=self.__WIDTH / 10,
                height=20,
                fg_color="#f3defa",
                anchor="nw",
                font=("Arial", 20),
                hover=0,
                text_color="black",
                border_width=0,
            ).pack(side="top", fill="x", expand=True)

        self.break_line = customtkinter.CTkButton(
            master=m_master.widget_label,
            text="",
            width=self.__WIDTH,
            height=7,
            fg_color="black",
            anchor="w",
            corner_radius=20,
            hover=0,
            border_width=0,
            border_color="black",
        )
        self.break_line.pack(padx=2, pady=2)

        self.reply_zone = customtkinter.CTkButton(
            master=m_master.widget_label,
            text="",
            width=self.__WIDTH,
            height=self.__HEIGHT / 2 - 35,
            fg_color="#f3defa",
            anchor="w",
            font=("Arial", 20, "bold"),
            hover=0,
            text_color="black",
            border_width=2,
            border_color="black",
            corner_radius=0,
        )
        self.reply_zone.pack(padx=5, pady=0)

        self.reply_from_letter = customtkinter.CTkButton(
            master=self.reply_zone,
            text="From:",
            width=40,
            height=20,
            fg_color="#f3defa",
            anchor="w",
            font=("Arial", 20, "bold"),
            hover=0,
            text_color="black",
            border_width=0,
        )
        self.reply_from_letter.place(x=3, y=12)

        self.reply_email = customtkinter.CTkButton(
            master=self.reply_zone,
            text=recive_mail,
            width=self.__WIDTH - self.__WIDTH / 4,
            height=20,
            fg_color="#f3defa",
            anchor="w",
            font=("Arial", 20),
            hover=0,
            text_color="black",
            border_width=0,
        )
        self.reply_email.place(x=80, y=12)

        self.reply_subject_letter = customtkinter.CTkButton(
            master=self.reply_zone,
            text="Content:",
            width=40,
            height=20,
            fg_color="#f3defa",
            anchor="w",
            font=("Arial", 20, "bold"),
            hover=0,
            text_color="black",
            border_width=0,
        )
        self.reply_subject_letter.place(x=3, y=50)

        self.reply_subject = customtkinter.CTkButton(
            master=self.reply_zone,
            text="reply_subject",
            width=self.__WIDTH - self.__WIDTH / 4,
            height=20,
            fg_color="#f3defa",
            anchor="w",
            font=("Arial", 20),
            hover=0,
            text_color="black",
            border_width=0,
        )
        self.reply_subject.place(x=100, y=50)

        self.attachment_zone = customtkinter.CTkScrollableFrame(
            master=self.reply_zone,
            width=self.__WIDTH - 21,
            height=140,
            fg_color="#f3defa",
            corner_radius=0,
            border_width=2,
            border_color="black",
        )
        self.attachment_zone._scrollbar.configure(height=0)
        self.attachment_zone.place(x=0, y=100)
        self.attachment_letter = customtkinter.CTkButton(
            master=self.attachment_zone,
            text="Attachment:",
            width=40,
            height=20,
            fg_color="#f3defa",
            anchor="w",
            font=("Arial", 20, "bold"),
            hover=0,
            text_color="black",
            border_width=0,
        )
        self.attachment_letter.grid(row=0, column=0, sticky="w")

        attachment_icon = customtkinter.CTkImage(
            Image.open("assets/attach.png"), size=(30, 30)
        )

        self.attach_space = [customtkinter.CTkButton] * 9
        self.attachment = [customtkinter.CTkButton] * 9

        row, col = (1, 0)

        for i in range(len(attachment)):
            self.new_attachment = str(attachment[i]).split("\\")[-1]
            self.attach_space[i] = customtkinter.CTkButton(
                master=self.attachment_zone,
                text="",
                width=self.__WIDTH / 5,
                height=50,
                fg_color="#f3defa",
                anchor="nw",
                font=("Arial", 20),
                hover=0,
                border_width=0,
                corner_radius=0,
            )
            self.attach_space[i].grid(row=row, column=col)  # Place the first widget

            self.attachment[i] = customtkinter.CTkButton(
                master=self.attach_space[i],
                text=self.new_attachment,
                width=self.__WIDTH / 10,
                height=20,
                fg_color="#4c0f66",
                anchor="nw",
                font=("Arial", 20),
                text_color="white",
                hover=0,
                border_width=2,
                border_color="black",
                image=attachment_icon,
                command=lambda i=i: self.attachment_event(
                    command=subject[i], attachment=attachment[i]
                ),
            )
            self.attachment[i].grid(row=row, column=col)
            col += 1  # Increment column count for the next widget
            if col == 4:  # If three widgets are placed, move to the next row
                row += 1
                col = 0

    def add_widget(self):
        self.mail_lb = customtkinter.CTkButton(
            master=self,
            text=self.__sender_mail,
            width=self.__WIDTH / 3 - self.__x,
            height=self.__HEIGHT / 10 - self.__y,
            fg_color="#f3defa",
            anchor="w",
            font=("Arial", 20),
            text_color="black",
            hover=0,
            corner_radius=0,
            command=lambda: self.button_event(
                m_master=self.__m_master,
                sender_mail=self.__sender_mail,
                recive_mail=self.__recive_mail,
                subject=self.__subject,
                reply_subject=self.__reply_subject,
                date=self.__date,
                attachment=self.__attachment,
            ),
        )
        self.mail_lb.place(x=2, y=2)
        self.content = ""
        for i in range(len(self.__subject)):
            self.content += str(self.__subject[i])
            self.content += " "

        self.content = self.content[:30] + "..."

        self.subject_lb = customtkinter.CTkButton(
            master=self,
            text=self.content,
            width=self.__WIDTH / 3 - self.__x,
            height=self.__HEIGHT / 10 - self.__y,
            fg_color="#f3defa",
            anchor="w",
            font=("Arial", 20),
            text_color="black",
            hover=0,
            corner_radius=0,
            command=lambda: self.button_event(
                m_master=self.__m_master,
                sender_mail=self.__sender_mail,
                recive_mail=self.__recive_mail,
                subject=self.__subject,
                reply_subject=self.__reply_subject,
                date=self.__date,
                attachment=self.__attachment,
            ),
        )
        self.subject_lb.place(x=self.__WIDTH / 3 + self.__x, y=2)

        self.date_lb = customtkinter.CTkButton(
            master=self,
            text=self.__date,
            width=self.__WIDTH / 3 - self.__x,
            height=self.__HEIGHT / 10 - self.__y,
            fg_color="#f3defa",
            anchor="e",
            font=("Arial", 20),
            text_color="black",
            hover=0,
            corner_radius=0,
            command=lambda: self.button_event(
                m_master=self.__m_master,
                sender_mail=self.__sender_mail,
                recive_mail=self.__recive_mail,
                subject=self.__subject,
                date=self.__date,
                reply_subject=self.__reply_subject,
                attachment=self.__attachment,
            ),
        )
        self.date_lb.place(x=self.__WIDTH / 3 * 2 - 2 * self.__x, y=2)

    def __init__(
        self,
        m_master,
        sender_mail: str,
        recive_mail: str,
        subject: [],
        date: str,
        attachment: [],
        reply_subject: str,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.configure(
            text="",
            width=m_master.APP_WIDTH - self.__x,
            height=m_master.APP_HEIGHT / 10,
            fg_color="#f3defa",
            anchor="w",
            corner_radius=0,
            hover=0,
            border_width=2,
            border_color="black",
        )
        (self.__WIDTH, self.__HEIGHT) = (
            m_master.APP_WIDTH - 20,
            m_master.APP_HEIGHT - m_master.APP_HEIGHT / 15,
        )

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

    def add_widget(
        self,
        master,
        sender_mail: str,
        recive_mail: str,
        subject: [],
        date: str,
        reply_subject: str,
        attachment: [],
    ):
        self.widget = Widget(
            master=self,
            m_master=master,
            sender_mail=sender_mail,
            recive_mail=recive_mail,
            subject=subject,
            date=date,
            reply_subject=reply_subject,
            attachment=attachment,
        )
        if self.widget not in master.widget_list:
            master.widget_list.append(self.widget)

        self.widget.pack(after=self.__info_lb, padx=5, pady=5)

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(
            width=master.APP_WIDTH,
            height=master.APP_HEIGHT - master.APP_HEIGHT / 15,
            fg_color="#f3defa",
            corner_radius=0,
            border_width=0,
            border_color="black",
        )

        self.__info_lb = customtkinter.CTkButton(
            master=self,
            text="",
            width=master.APP_WIDTH - 13,
            height=master.APP_HEIGHT / 10,
            fg_color="#f3defa",
            anchor="w",
            corner_radius=0,
            hover=0,
            border_width=3,
            border_color="black",
        )
        self.__info_lb.pack(pady=1)

        self.from_letter = customtkinter.CTkButton(
            master=self.__info_lb,
            text="Email",
            width=40,
            height=20,
            fg_color="#f3defa",
            anchor="w",
            font=("Arial", 20, "bold"),
            hover=0,
            text_color="black",
        )
        self.from_letter.place(x=3, y=12)

        self.subject_letter = customtkinter.CTkButton(
            master=self.__info_lb,
            text="Content",
            width=40,
            height=20,
            fg_color="#f3defa",
            anchor="w",
            font=("Arial", 20, "bold"),
            hover=0,
            text_color="black",
        )
        self.subject_letter.place(x=master.APP_WIDTH / 3, y=12)

        self.date_letter = customtkinter.CTkButton(
            master=self.__info_lb,
            text="Date",
            width=40,
            height=20,
            fg_color="#f3defa",
            anchor="w",
            font=("Arial", 20, "bold"),
            hover=0,
            text_color="black",
        )
        self.date_letter.place(x=master.APP_WIDTH / 3 * 3 - 80, y=12)


class App(customtkinter.CTk):
    APP_WIDTH = 1000
    APP_HEIGHT = 600
    self_email = "emailcontrolMMT@gmail.com"
    sender_email = ""
    widget_list = []

    def add_new_mail(
        self,
        sender_mail: str,
        subject: [],
        date: str,
        reply_subject: str,
        attachment: [],
    ):
        self.widget_label.add_widget(
            master=self,
            sender_mail=sender_mail,
            subject=subject,
            recive_mail=self.self_email,
            date=date,
            attachment=attachment,
            reply_subject=reply_subject,
        )

    def __init__(self):
        super().__init__()
        x = 300
        y = 100
        self.title("PC Controller via Email")
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{x}+{y}")
        self.resizable(False, False)
        self.configure(fg_color="#f3defa")
        # self.focus_force()
        self.after(201, lambda: self.iconbitmap("assets\\icon4.ico"))
        self.widget_label = Mail_page(master=self)
        self.widget_label.place(x=0, y=0)


# if __name__ == "__main__":
#     # Splash_Screen()
#     app = App()

#     cmd_list = [
#         "screenshot a",
#         "webcam b",
#         "keylog 10",
#         "screenshot a",
#         "webcam b",
#         "keylog 10",
#         "screenshot a",
#         "webcam b",
#         "keylog 10",
#     ]
#     cmd_list = [i.split(" ") for i in cmd_list]

#     attachment_list = [
#         "Files\\Pictures\\a.png",
#         "Files\\Pictures\\b.png",
#         "Files\\Keylog.txt",
#         "Files\\Pictures\\a.png",
#         "Files\\Pictures\\b.png",
#         "Files\\Keylog.txt",
#         "Files\\Pictures\\a.png",
#         "Files\Pictures\\b.png",
#         "Files\\Keylog.txt",
#     ]
#     for i in range(10):
#         app.add_new_mail(
#             sender_mail="SenderEmail",
#             subject=cmd_list,
#             date="Date",
#             reply_subject="ReplySubject",
#             attachment=attachment_list,
#         )
#     app.mainloop()
