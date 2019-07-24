import tkinter
import cv2
import PIL.Image
import PIL.ImageTk
import os

rectangle = None
press_x, press_y = 0, 0
directory = './zadania/'

window_x, window_y = None, None

def open_file(name):
    global rectangle, press_x, press_y, window_x, window_y

    window = tkinter.Tk()
    
    cv_img = cv2.imread(name)
    height, width, no_channels = cv_img.shape

    max_height = 950

    resize_factor = 1

    if height > max_height:
        resize_factor = max_height/height
        width, height = int(resize_factor*width), max_height
        cv_img = cv2.resize(cv_img, (width, height))

    if window_x is not None:
        window.geometry('%dx%d+%d+%d' % (width, height, window_x, window_y))

    canvas = tkinter.Canvas(window, width=width, height=height)
    canvas.pack()

    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
    canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)

    def on_mouse_down(event):
        global rectangle, press_x, press_y
        x, y = event.x, event.y
        press_x, press_y = x, y
        rectangle = canvas.create_rectangle(x, y, x, y, fill=None, width=2, outline='red')


    def on_mouse_up(event):
        flag = True
        while flag:
            flag = False
            for i in range(len(RectangleList)):
                r = RectangleList[i]
                x1,y1,x2,y2 = canvas.coords(r)
                x3,y3,x4,y4 = canvas.coords(rectangle)

                if x1 < x4 and x2 > x3 and y2 > y3 and y1 < y4:
                    flag = True
                    canvas.delete(r)
                    del RectangleList[i]
                    break
        RectangleList.append(rectangle)


    def on_mouse_move(event):
        global rectangle
        x1, y1 = press_x, press_y
        x2, y2 = event.x, event.y
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        canvas.coords(rectangle, x1, y1, x2, y2)

    def on_key_release(event):
        global i, window_x, window_y
        if event.char == '\r':
            
            window_x, window_y = window.winfo_x(), window.winfo_y()
            for rectangle in RectangleList:
                x1,y1,x2,y2 = canvas.coords(rectangle)
                
                width, height = int(x2-x1), int(y2-y1)

                x1 = int(x1/resize_factor)
                x2 = int(x2/resize_factor)
                y1 = int(y1/resize_factor)
                y2 = int(y2/resize_factor)

                img = cv2.imread(name)
                crop = img[y1:y2, x1:x2]
                crop = cv2.resize(crop, (width, height))
                n = len([item for item in os.listdir(directory) if os.path.isfile(os.path.join(directory, item))])+1
                cv2.imwrite("./zadania/zadanie-%03d.png" % n, crop)


            window.destroy()

    def on_closing():
        exit()


    RectangleList = []
    window.bind('<Button-1>', on_mouse_down)
    window.bind('<ButtonRelease-1>', on_mouse_up)
    window.bind('<B1-Motion>', on_mouse_move)
    window.bind("<KeyRelease>", on_key_release)
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.after(50, lambda: window.focus_force())
    window.mainloop()
