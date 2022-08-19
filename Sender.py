



def send_image():
    global image_name
    global image_path
    f = Fernet(key)
    fd = os.open(image_path.get(), os.O_RDONLY)
    size = os.path.getsize(image_path.get())
    read_bytes = os.read(fd, size)
    token = f.encrypt(read_bytes)
    print(size)
    data = "Image"+str(size)+"^"+image_name.get()
    s.send(str.encode(data))
    time.sleep(2)
    s.send(token)
    posts.destroy()




# connects ..................................................................................
def displays_conn():
    connec.destroy()
    print("IP address : ", ip_add.get(), "\nPort Number :", port_num.get())
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ip_add.get()
    port = port_num.get()
    s.connect((host, port))  # here we just connect the server
    messagebox.showinfo('Status', "Connection Established")
    s.send(key)



# menu ..................................................................................

def adjustWindow(window):
    w = 600  # width for the window size
    h = 600  # height for the window size
    ws = window.winfo_screenwidth()  # width of the screen
    hs = window.winfo_screenheight()  # height of the screen
    x = (ws / 2) - (w / 2)  # calculate x and y coordinates for the Tk window
    y = (hs / 2) - (h / 2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))  # set the dimensions of the screen and where it is placed
    window.resizable(False, False)  # disabling the resize option for the window
    # window.configure(background='#174873') # making the background white of the window


# validate the entry data and makes a new entry into the database


def menu():
    global root
    global key
    key = Fernet.generate_key()

    # global s
    root = Tk()
    adjustWindow(root)
    Label(root, text="Secure Data Transfer System Over The Network", width="500", height="2", font=("Calibri", 22, 'bold'), fg='white',
          bg='red').pack()
    Button(root, text='Connect', command=connects, fg="blue").place(x=50, y=150)
    Button(root, text='Disconnect', command=disconnects, fg="orange").place(x=250, y=150)
    Text_button = Button(root, text='Text Transfer', command=Text_transfer, fg="blue")
    Text_button.place(x=50, y=250)

    
   
    root.mainloop()


menu()
