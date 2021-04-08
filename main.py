""" saya Mochamad Mufid Abiyyu
	mengerjakan TP3 dalam 
	mata kuliah DPBO untuk keberkahanNya maka
	saya tidak melakukan kecurangan seperti
	yang telah dispesifikasikan.Aamiin. """
# Import library
from tkinter import *
from tkinter import messagebox
import sqlite3

# bikin window
root = Tk()
root.title("TP3")
# bikin label judul dan deskripsi aplikasi
labelJudul = Label(root, text = "Form Data Mahasiswa", padx="10", pady="5")
labelJudul.config(font=("Segoe UI", 18))
labelJudul.pack()

labelDesc = Label(root, text="Ini aplikasi kumpulan data mahasiswa", padx="10")
labelDesc.pack()
# bikin frame
frameForm = LabelFrame(root, text="Masukan data", padx="5", pady="10")
frameForm.pack(padx="10", pady="10")
# connect db
conn = sqlite3.connect("mahasiswa.db")

c = conn.cursor()

# c.execute(""" CREATE TABLE mhs (
#             nim integer,
#             nama text,
#             jk text,
#             prodi text,
#             hobi text
#             )""")


# fungsi menambah data
def add():

    gabung = StringVar()
    cek = 0
    # penggabungan string untuk checkbox
    if(cek == 0):
        if(hobiButton1.get() != "0"): 
            gabung = hobiButton1.get()
            cek = 1
    else:
        if(hobiButton1.get() != "0"):
            gabung += " , " + hobiButton1.get()

    if(cek == 0):
        if(hobiButton2.get() != "0"):
            gabung = hobiButton2.get()
            cek = 1
    else:
        if(hobiButton2.get() != "0"):
            gabung += " , " + hobiButton2.get()

    if(cek == 0):
        if(hobiButton3.get() != "0"):
            gabung = hobiButton3.get()
            cek = 1
    else:
        if(hobiButton3.get() != "0"):
            gabung += " , " + hobiButton3.get()
            
    if(cek == 0):
        if(hobiButton4.get() != "0"):
            gabung = hobiButton4.get()
            cek = 1
    else:
        if(hobiButton4.get() != "0"):
            gabung += " , " + hobiButton4.get()
            
            
    # connect db
    conn = sqlite3.connect("mahasiswa.db")

    c = conn.cursor()
    # cek jika ada masukan yang kosong
    if(NIM.get() == "" or name.get() == ""):
        messagebox.showinfo("Pop-up", "Data harus terisi semua")
    else:
        # jika semua terisi maka insert
        c.execute("INSERT INTO mhs VALUES(:NIM, :name, :jkRadio, :jurusan, :gabung)",
                {
                    'NIM': NIM.get(),
                    'name': name.get(),
                    'jkRadio': jkRadio.get(),
                    'jurusan': jurusan.get(),
                    'gabung': gabung
                })
        messagebox.showinfo("Pop-up", "Data berhasil dimasukan")

    conn.commit()

    conn.close()
    # kosongkan inputan
    NIM.delete(0, END)
    name.delete(0, END)
    jkRadio.set("Pria")
    jurusan.set("Ilkom")
    check1.deselect()
    check2.deselect()
    check3.deselect()
    check4.deselect()

# fungsi untuk melihat data
def lihat():
    # bikin window baru
    top = Toplevel()
    top.title("Data Mahasiswa")
    # connect db
    conn = sqlite3.connect("mahasiswa.db")

    c = conn.cursor()
    # query select
    c.execute("SELECT *, oid FROM mhs")
    records = c.fetchall()
    index = 0

    # printRecords = ""
    # tampilkan data dengan loop
    for record in records:
        labelQuery = Label(top, text=str(record), padx="10", pady="10")
        labelQuery.grid(row=index, column=0)
        # button delete
        btnDelete = Button(top, text="Delete", command=delete).grid(row=index, column=1)
        index += 1

    conn.commit()

    conn.close()

# ini harusnya buat delete data tapi gk bisa:(
def delete():
    conn = sqlite3.connect("mahasiswa.db")

    c = conn.cursor()

    c.execute("DELETE from mhs WHERE oid")

    conn.commit()

    conn.close()
# ini juga sama gk bisa:D
def clear():
    conn = sqlite3.connect("mahasiswa.db")

    c = conn.cursor()

    c.execute("DELETE * from mhs")

    conn.commit()

    conn.close()

# ini fungsi tentang aplikasi
def about():
    # buat window baru
    top = Toplevel()
    top.title("About")
    # label tentang aplikasi
    labelAbout = Label(top, text="Ini aplikasi Data mahasiswa", padx="10", pady="10").pack()

# Ini input text
NIM = Entry(frameForm)
NIM.grid(row="0", column="1")
name = Entry(frameForm)
name.grid(row="1", column="1")
# input radio
jkRadio = StringVar()
jkRadio.set("Pria")
Radiobutton(frameForm, text="Pria", variable=jkRadio, value="Pria").grid(row="2", column="1")
Radiobutton(frameForm, text="Wanita", variable=jkRadio, value="Wanita").grid(row="3", column="1")
# input dropdown
jurusan = StringVar()
jurusan.set("Ilkom")
dropDown = OptionMenu(frameForm, jurusan, "Ilkom", "Pilkom", "MTK", "Kimia").grid(row="4", column="1")
# input checkbox
hobiButton1 = StringVar()
hobiButton2 = StringVar()
hobiButton3 = StringVar()
hobiButton4 = StringVar()
check1 = Checkbutton(frameForm, text="Gibah", variable=hobiButton1, onvalue="Gibah", offvalue="0")
check1.deselect()
check1.grid(row="5", column="1")
check2 = Checkbutton(frameForm, text="Olahraga", variable=hobiButton2, onvalue="Olahraga", offvalue="0")
check2.deselect()
check2.grid(row="5", column="2")
check3 = Checkbutton(frameForm, text="Desain", variable=hobiButton3, onvalue="Desain", offvalue="0")
check3.deselect()
check3.grid(row="6", column="1")
check4 = Checkbutton(frameForm, text="Bucin", variable=hobiButton4, onvalue="Bucin", offvalue="0")
check4.deselect()
check4.grid(row="6", column="2")

# label disamping inputan
labelFirst = Label(frameForm, text="NIM")
labelFirst.grid(row="0", column="0")
labelLast = Label(frameForm, text="Nama")
labelLast.grid(row="1", column="0")
labelJk = Label(frameForm, text="Jenis kelamin")
labelJk.grid(row="2", column="0")
labelProdi = Label(frameForm, text="Pilih prodi")
labelProdi.grid(row="4", column="0")
labelHobi = Label(frameForm, text="Hobi")
labelHobi.grid(row="5", column="0")
# button untuk submit
btnSubmit = Button(frameForm, text="Submit", command=add).grid(row="7", column="2")

# bikin frame lagi
frameCommand = LabelFrame(root, padx="5", pady="10")
frameCommand.pack(padx="10", pady="10")
# button lihat data, clear data, about
btnSee = Button(frameCommand, text="See All data", command=lihat).grid(row=0, column=0)
btnClear = Button(frameCommand, text="Clear data", command=clear).grid(row=0, column=1)
btnAbout = Button(frameCommand, text="About", command=about).grid(row=0, column=2)
# button exit
b_exit = Button(root, text="Exit", command=root.quit).pack()

conn.commit()
# close db
conn.close()
root.mainloop()