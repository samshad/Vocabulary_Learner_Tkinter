from tkinter import *
from tkinter import messagebox
import sqlite3
from random import choice
import webbrowser


def update_changes():
    global var_check
    global current_vocab
    global txt3

    if messagebox.askyesno("Confirmation", "Are You Sure To Update Your Changes?"):
        mysen = str(txt3.get("1.0", 'end-1c')).strip()

        conn = sqlite3.connect('vocab.db')
        c = conn.cursor()

        c.execute("""UPDATE vocab SET
                    word = :word,
                    meaning = :meaning,
                    shortdef = :shortdef,
                    longdef = :longdef,
                    url = :url,
                    done = :done,
                    mysentense = :mysentense
                    
                    WHERE oid = :oid""",
                  {
                      'word': current_vocab[0],
                      'meaning': current_vocab[1],
                      'shortdef': current_vocab[2],
                      'longdef': current_vocab[3],
                      'url': current_vocab[4],
                      'done': var_check.get(),
                      'mysentense': mysen,
                      'oid': current_vocab[7]
                  })

        conn.commit()
        conn.close()
    else:
        return


def open_url(url):
    webbrowser.open_new(url)


def get_current_mylist_count():
    conn = sqlite3.connect('vocab.db')
    c = conn.cursor()
    a = c.execute("SELECT COUNT(done) FROM vocab WHERE done = 1")
    ret = a.fetchone()[0]
    conn.close()
    return ret


def init_current_mylist_count():
    global current_mylist_count
    global mylist
    current_mylist_count = get_current_mylist_count()
    mylist.grid_forget()
    mylist = Label(home, text='Words in MyList: ' + str(current_mylist_count), font='calibri 18 bold')
    mylist.grid(row=3, column=1, columnspan=3, padx=200, pady=30)


def init_current_done():
    global current_done
    global doneword
    current_done = get_done_word()
    doneword.grid_forget()
    doneword = Label(home, text='Learned Words: ' + str(current_done), font='calibri 18 bold')
    doneword.grid(row=2, column=1, columnspan=3, padx=200, pady=10)


def init_word():
    global word
    global def_label
    global txt3
    global check_frame
    global current_vocab
    global mylist_check
    global done_check
    global var_check
    short = str(current_vocab[2])
    long = str(current_vocab[3])

    current_vocab = get_random_vocab()
    word.destroy()
    word = Label(random, text=current_vocab[0], font='calibri 25 bold')
    #word.grid(row=1, column=1, columnspan=2, padx=5, pady=10)
    word.place(x=200, y=40)

    def_label.destroy()
    def_label = Label(random, text=current_vocab[1], font='calibri 15')
    #def_label.grid(row=2, column=0, columnspan=3, padx=5, pady=10)
    def_label.place(x=150, y=100)

    txt = Text(random, height=13, width=30, font='calibri 15', wrap=WORD)
    txt.place(x=20, y=185)
    #txt.grid(row=3, column=0, padx=10)
    txt.insert(INSERT, short)
    txt.config(state="disabled")

    txt2 = Text(random, height=13, width=42, font='calibri 15', wrap=WORD)
    txt2.place(x=350, y=185)
    #txt2.grid(row=3, column=2, columnspan=2, padx=15)
    txt2.insert(INSERT, long)
    txt2.config(state="disabled")

    check_frame.destroy()
    check_frame = LabelFrame(random)
    check_frame.place(x=230, y=520)

    var_check = IntVar()

    mylist_check.destroy()
    mylist_check = Checkbutton(check_frame, text='Add To My List.', variable=var_check, onvalue=1, offvalue=0,
                               font='calibri 12')
    mylist_check.deselect()
    if current_vocab[5] == 1:
        mylist_check.select()
    mylist_check.pack(side=LEFT)

    done_check.destroy()
    done_check = Checkbutton(check_frame, text='Done With This Word.', variable=var_check, onvalue=2, offvalue=0,
                             font='calibri 12')
    done_check.deselect()
    if current_vocab[5] == 2:
        done_check.select()
    done_check.pack(side=LEFT, padx=10)

    mysentense_label = Label(random, text='My Sentense:', font='calibri 20')
    mysentense_label.place(x=20, y=590)

    txt3.destroy()
    txt3 = Text(random, height=4, width=45, font='calibri 13', wrap=WORD)
    txt3.insert(INSERT, str(current_vocab[6]))
    txt3.place(x=180, y=570)

    update_btn = Button(random, text='Update', command=update_changes, height=1, width=13,
                          font='calibri 15')
    update_btn.place(x=620, y=590)


def get_done_word():
    conn = sqlite3.connect('vocab.db')
    c = conn.cursor()
    a = c.execute("SELECT COUNT(done) FROM vocab WHERE done = 2")
    ret = a.fetchone()[0]
    conn.close()
    return ret


def get_vocabs():
    conn = sqlite3.connect('vocab.db')
    c = conn.cursor()
    a = c.execute("SELECT *, oid FROM vocab WHERE done = 0")
    ret = a.fetchall()
    conn.close()
    return ret


def get_random_vocab():
    global vocabs
    return choice(vocabs)


def raise_frame(frame):
    init_current_mylist_count()
    get_vocabs()
    init_word()
    init_current_done()
    frame.tkraise()


root = Tk()
root.resizable(width=False, height=False)
root.title('Vocabulary Learner')
root.iconbitmap('Data/sru.ico')
root.geometry('800x800+300+50')
vocabs = get_vocabs()
current_vocab = get_random_vocab()
current_done = get_done_word()
current_mylist_count = get_current_mylist_count()

home = Frame(root)
random = Frame(root)

for frame in (home, random):
    frame.grid(row=0, column=0, sticky='news')

title = Label(home, text='Vocabulary Learner', font='calibri 35 bold')
title.grid(row=0, column=1, columnspan=3, padx=200, pady=50)

totalword = Label(home, text='Total Words: 1000', font='calibri 20 bold')
totalword.grid(row=1, column=1, columnspan=3, padx=200, pady=25)

doneword = Label(home, text='Learned Words: ' + str(current_done), font='calibri 18 bold')
doneword.grid(row=2, column=1, columnspan=3, padx=200, pady=10)

mylist = Label(home, text='Words in MyList: ' + str(current_mylist_count), font='calibri 18 bold')
mylist.grid(row=3, column=1, columnspan=3, padx=200, pady=30)

random_btn = Button(home, text='Learn Randomly', command=lambda: raise_frame(random), height=2, width=15,
                    font='calibri 20')
random_btn.grid(row=4, column=1, columnspan=3, padx=150, pady=20)

mylist_btn = Button(home, text='My List', command="", height=2, width=15,
                    font='calibri 20')
mylist_btn.grid(row=5, column=1, columnspan=3, padx=150, pady=20)

revise_btn = Button(home, text='Revise Words', command="", height=2, width=15,
                    font='calibri 20')
revise_btn.grid(row=6, column=1, columnspan=3, padx=150, pady=20)

home_btn = Button(random, text='Home', command=lambda: raise_frame(home), height=1, width=10,
                    font='calibri 10')
#home_btn.grid(row=0, column=0)
home_btn.place(x=5, y=5)

wlabel = Label(random, text='Word: ', font='calibri 20')
#wlabel.grid(row=1, column=0, columnspan=1)
wlabel.place(x=20, y=45)

word = Label(random, text=current_vocab[0], font='calibri 25 bold')
#word.grid(row=1, column=1, columnspan=2, padx=5, pady=10)
word.place(x=200, y=40)

def_label = Label(random, text=current_vocab[1], font='calibri 15')
#def_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
def_label.place(x=150, y=100)

dlabel = Label(random, text='Definitions: ', font='calibri 20')
#wlabel.grid(row=1, column=0, columnspan=1)
dlabel.place(x=20, y=140)

check_frame = LabelFrame(random)
check_frame.place(x=230, y=520)

var_check = IntVar()

mylist_check = Checkbutton(check_frame, text='Add To My List.', variable=var_check, onvalue=1, offvalue=0,
                           font='calibri 12')
mylist_check.deselect()
if current_vocab[5] == 1:
    mylist_check.select()
mylist_check.pack(side=LEFT)

done_check = Checkbutton(check_frame, text='Done With This Word.', variable=var_check, onvalue=2, offvalue=0,
                         font='calibri 12')
done_check.deselect()
if current_vocab[5] == 2:
    done_check.select()
done_check.pack(side=LEFT, padx=10)

txt3 = Text(random, height=4, width=45, font='calibri 13', wrap=WORD)
txt3.insert(INSERT, str(current_vocab[6]))
txt3.place(x=180, y=570)

details_label = Label(random, text='For More Details:', font='calibri 15')
details_label.place(x=20, y=690)

clickhere_label = Label(random, text='Click Here', font='calibri 15', fg="blue", cursor="hand2")
clickhere_label.place(x=180, y=690)
clickhere_label.bind("<Button-1>", lambda e: open_url(str(current_vocab[4])))

another_word = Button(random, text='Another Word', command=lambda: raise_frame(random), height=1, width=13,
                    font='calibri 15')
#another_word.grid(row=4, column=1, columnspan=3, padx=20, pady=15)
another_word.place(x=310, y=735)


raise_frame(home)
root.mainloop()


