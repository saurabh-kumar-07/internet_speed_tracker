from tkinter import *
import speedtest

def test_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6  # in Mbps
    upload_speed = st.upload() / 10**6  # in Mbps
    result_label.config(text=f"Download Speed: {download_speed:.2f} Mbps\nUpload Speed: {upload_speed:.2f} Mbps")

sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x200")
sp.config(bg="blue")


test_button = Button(sp, text="Test Speed", command=test_speed)
test_button.pack(pady=20)

result_label = Label(sp, text="")
result_label.pack()

sp.mainloop()