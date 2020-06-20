from pytube import  YouTube
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import *
from threading import *


# yt= YouTube("https://www.youtube.com/watch?v=VB0mn8Tgz2k")
#
# print(yt.title)
# print(yt.rating)
# print(yt.views)
#
# st= yt.streams.first()
# st.download()
# print("video downloaded !!")

font= ('verdana', 20)
file_size= 0


#oncomplete callback function

def complete(stream = None, file_path = None):
    print("download completed !")
    showinfo("message", "File has been downloaded")
    downloadBtn['text'] = "download"
    downloadBtn['state']= "active"
    urlField.delete(0,END)

#on progress callback function

def progess(stream = None, chunk = None, bytes_remaining = None):
    print("progress called...")
    percent = (100*(file_size - bytes_remaining)/file_size)
    downloadBtn['text'] = "{:00.0f}% downloaded".format(percent)





#download function.....
def startDownload(url):
    global file_size
    path_to_save= askdirectory()
    if path_to_save is NONE:
        return
    try:
        yt = YouTube(url)
        st = yt.streams.first()
        yt.register_on_complete_callback(complete)
        yt.register_on_progress_callback(progess)

        file_size= st.filesize
        st.download(output_path=path_to_save)


    except EXCEPTION as e:
        print(e)


def btnClicked():
    try:
        downloadBtn['text']= "please wait...."
        downloadBtn['state']= 'disabled'
        url= urlField.get()
        if url==' ':
            return
        print(url)
        thread=Thread(target=startDownload, args=(url,))
        thread.start()


    except EXCEPTION as e:
        print(e)


# gui coding
root= Tk()
root.title("Youtube downloader powered by iamvipintiwari")
# root.iconbitmap("img/icon.ico")
root.geometry("300x300")

# main icon section

# file= PhotoImage(file="img/youtube.jpg")
headingicon= Label(root)
headingicon.pack(side=TOP, pady=3)

#utl field

urlField= Entry(root, font=font, justify=CENTER)
urlField.pack(side=TOP, fill=X , pady=10)
urlField.focus()

#download button

downloadBtn= Button(root, text="Click to download", font= font, relief='ridge', command=btnClicked)
downloadBtn.pack(side=TOP, pady=20)

root.mainloop()
