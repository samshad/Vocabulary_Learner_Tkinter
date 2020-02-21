from tkinter import *
from tkinter import messagebox
import sqlite3
from random import choice
import webbrowser


def update_changes(current_v, mysen, chvar, frame):
    if messagebox.askyesno("Confirmation", "Are You Sure To Update Your Changes?"):
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
                      'word': current_v[0],
                      'meaning': current_v[1],
                      'shortdef': current_v[2],
                      'longdef': current_v[3],
                      'url': current_v[4],
                      'done': chvar,
                      'mysentense': mysen,
                      'oid': current_v[7]
                  })

        conn.commit()
        conn.close()

        raise_frame(frame)
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


def get_my_List_vocab():
    conn = sqlite3.connect('vocab.db')
    c = conn.cursor()
    a = c.execute("SELECT *, oid FROM vocab WHERE done = 1")
    ret = a.fetchall()
    conn.close()
    if len(ret) > 0:
        return ret
    else:
        return []


def my_List_random_btn_handler():
    global current_vocab_my_List_arr
    clear_word_my_List()
    my_List_show(choice(current_vocab_my_List_arr))


def clear_word_random():
    global wlabel
    global dlabel
    global word
    global def_label
    global txt
    global txt2
    global check_frame
    global mylist_check
    global done_check
    global mysentense_label
    global txt3
    global update_btn
    global details_label
    global clickhere_label
    global another_word
    global prev_btn
    global next_btn
    global warning

    wlabel.destroy()
    dlabel.destroy()
    word.destroy()
    def_label.destroy()
    txt.destroy()
    txt2.destroy()
    check_frame.destroy()
    mylist_check.destroy()
    done_check.destroy()
    mysentense_label.destroy()
    txt3.destroy()
    update_btn.destroy()
    details_label.destroy()
    clickhere_label.destroy()
    another_word.destroy()


def clear_word_my_List():
    global wlabel_my_List
    global dlabel_my_List
    global word_my_List
    global def_label_my_List
    global txt_my_List
    global txt2_my_List
    global check_frame_my_List
    global mylist_check_my_List
    global done_check_my_List
    global mysentense_label_my_List
    global txt3_my_List
    global update_btn_my_List
    global details_label_my_List
    global clickhere_label_my_List
    global another_word_my_List
    global prev_btn_my_List
    global next_btn_my_List
    global warning_my_List

    wlabel_my_List.destroy()
    dlabel_my_List.destroy()
    word_my_List.destroy()
    def_label_my_List.destroy()
    txt_my_List.destroy()
    txt2_my_List.destroy()
    check_frame_my_List.destroy()
    mylist_check_my_List.destroy()
    done_check_my_List.destroy()
    mysentense_label_my_List.destroy()
    txt3_my_List.destroy()
    update_btn_my_List.destroy()
    details_label_my_List.destroy()
    clickhere_label_my_List.destroy()
    another_word_my_List.destroy()
    prev_btn_my_List.destroy()
    next_btn_my_List.destroy()
    warning_my_List.destroy()


def my_List_show(current_vocab_my_List):
    global wlabel_my_List
    global dlabel_my_List
    global word_my_List
    global def_label_my_List
    global txt_my_List
    global txt2_my_List
    global check_frame_my_List
    global mylist_check_my_List
    global done_check_my_List
    global mysentense_label_my_List
    global txt3_my_List
    global update_btn_my_List
    global details_label_my_List
    global clickhere_label_my_List
    global another_word_my_List
    global prev_btn_my_List
    global next_btn_my_List

    wlabel_my_List = Label(my_List, text='Word: ', font='calibri 20')
    wlabel_my_List.place(x=20, y=45)

    dlabel_my_List = Label(my_List, text='Definitions: ', font='calibri 20')
    dlabel_my_List.place(x=20, y=140)

    word_my_List = Label(my_List, text=current_vocab_my_List[0], font='calibri 25 bold')
    word_my_List.place(x=200, y=40)

    def_label_my_List = Label(my_List, text=current_vocab_my_List[1], font='calibri 15')
    def_label_my_List.place(x=150, y=100)

    txt_my_List = Text(my_List, height=13, width=30, font='calibri 15', wrap=WORD, padx=10, pady=5)
    txt_my_List.place(x=20, y=185)
    txt_my_List.insert(INSERT, str(current_vocab_my_List[2]))
    txt_my_List.config(state="disabled")

    txt2_my_List = Text(my_List, height=13, width=42, font='calibri 15', wrap=WORD, padx=10, pady=5)
    txt2_my_List.place(x=350, y=185)
    txt2_my_List.insert(INSERT, str(current_vocab_my_List[3]))
    txt2_my_List.config(state="disabled")

    check_frame_my_List = LabelFrame(my_List)
    check_frame_my_List.place(x=230, y=520)

    var_check_my_List = IntVar()

    mylist_check_my_List = Checkbutton(check_frame_my_List, text='Add To My List.', variable=var_check_my_List,
                                       onvalue=1, offvalue=0, font='calibri 12')
    if current_vocab_my_List[5] == 1:
        mylist_check_my_List.select()
    mylist_check_my_List.pack(side=LEFT)

    done_check_my_List = Checkbutton(check_frame_my_List, text='Done With This Word.', variable=var_check_my_List,
                                     onvalue=2, offvalue=0, font='calibri 12')
    if current_vocab_my_List[5] == 2:
        done_check_my_List.select()
    done_check_my_List.pack(side=LEFT, padx=10)

    mysentense_label_my_List = Label(my_List, text='My Sentense:', font='calibri 20')
    mysentense_label_my_List.place(x=20, y=590)

    txt3_my_List = Text(my_List, height=4, width=45, font='calibri 13', wrap=WORD, padx=10, pady=5)
    txt3_my_List.insert(INSERT, str(current_vocab_my_List[6]))
    txt3_my_List.place(x=180, y=570)

    update_btn_my_List = Button(my_List, text='Update',
                                command=lambda: update_changes(current_vocab_my_List,
                                                               str(txt3_my_List.get("1.0", 'end-1c')).strip(),
                                                               var_check_my_List.get(), my_List), height=1, width=13,
                                font='calibri 15')
    update_btn_my_List.place(x=620, y=590)

    details_label_my_List = Label(my_List, text='For More Details:', font='calibri 15')
    details_label_my_List.place(x=20, y=690)

    clickhere_label_my_List = Label(my_List, text='Click Here', font='calibri 15', fg="blue", cursor="hand2")
    clickhere_label_my_List.place(x=180, y=690)
    clickhere_label_my_List.bind("<Button-1>", lambda e: open_url(str(current_vocab_my_List[4])))

    another_word_my_List = Button(my_List, text='Random Word', command=my_List_random_btn_handler, height=1,
                                  width=13, font='calibri 15')
    another_word_my_List.place(x=310, y=735)

    prev_btn_my_List = Button(my_List, text='<<', command="", height=1, width=13, font='calibri 15 bold')
    prev_btn_my_List.place(x=150, y=735)

    next_btn_my_List = Button(my_List, text='>>', command="", height=1, width=13, font='calibri 15 bold')
    next_btn_my_List.place(x=470, y=735)


def init_word_my_List():
    global current_vocab_my_List_arr
    global warning_my_List

    current_vocab_my_List_arr = get_my_List_vocab()
    
    if len(current_vocab_my_List_arr) > 0:
        warning_my_List.destroy()
        my_List_show(choice(current_vocab_my_List_arr))
    else:
        warning_my_List = Label(my_List, text="Add Words First !!!", font='calibri 15 bold')
        warning_my_List.place(x=25, y=250)


def random_random_btn_handler():
    global random_vocab_arr
    clear_word_random()
    random_show(choice(random_vocab_arr))


def random_show(current_vocab):
    global wlabel
    global dlabel
    global word
    global def_label
    global txt
    global txt2
    global check_frame
    global mylist_check
    global done_check
    global mysentense_label
    global txt3
    global update_btn
    global details_label
    global clickhere_label
    global another_word

    wlabel = Label(random, text='Word: ', font='calibri 20')
    wlabel.place(x=20, y=45)

    word.destroy()
    word = Label(random, text=current_vocab[0], font='calibri 25 bold')
    word.place(x=200, y=40)

    dlabel = Label(random, text='Definitions: ', font='calibri 20')
    dlabel.place(x=20, y=140)

    def_label.destroy()
    def_label = Label(random, text=current_vocab[1], font='calibri 15')
    def_label.place(x=150, y=100)

    txt = Text(random, height=13, width=30, font='calibri 15', wrap=WORD, padx=10, pady=5)
    txt.place(x=20, y=185)
    txt.insert(INSERT, str(current_vocab[2]))
    txt.config(state="disabled")

    txt2 = Text(random, height=13, width=42, font='calibri 15', wrap=WORD, padx=10, pady=5)
    txt2.place(x=350, y=185)
    txt2.insert(INSERT, str(current_vocab[3]))
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
    txt3 = Text(random, height=4, width=45, font='calibri 13', wrap=WORD, padx=10, pady=5)
    txt3.insert(INSERT, str(current_vocab[6]))
    txt3.place(x=180, y=570)

    update_btn = Button(random, text='Update',
                        command=lambda: update_changes(current_vocab, str(txt3.get("1.0", 'end-1c')).strip(),
                                                       var_check.get(), random), height=1, width=13, font='calibri 15')
    update_btn.place(x=620, y=590)

    details_label = Label(random, text='For More Details:', font='calibri 15')
    details_label.place(x=20, y=690)

    clickhere_label = Label(random, text='Click Here', font='calibri 15', fg="blue", cursor="hand2")
    clickhere_label.place(x=180, y=690)
    clickhere_label.bind("<Button-1>", lambda e: open_url(str(current_vocab[4])))

    another_word = Button(random, text='Another Word', command=random_random_btn_handler, height=1, width=13,
                          font='calibri 15')
    another_word.place(x=310, y=735)


def init_word():
    global random_vocab_arr

    random_vocab_arr = get_random_vocab()
    random_show(choice(random_vocab_arr))


def get_done_word():
    conn = sqlite3.connect('vocab.db')
    c = conn.cursor()
    a = c.execute("SELECT COUNT(done) FROM vocab WHERE done = 2")
    ret = a.fetchone()[0]
    conn.close()
    return ret


def get_random_vocab():
    conn = sqlite3.connect('vocab.db')
    c = conn.cursor()
    a = c.execute("SELECT *, oid FROM vocab WHERE done = 0")
    ret = a.fetchall()
    conn.close()
    return ret


def raise_frame(frame):
    init_current_mylist_count()
    init_current_done()
    clear_word_random()
    init_word()
    clear_word_my_List()
    init_word_my_List()

    frame.tkraise()


root = Tk()
root.resizable(width=False, height=False)
root.title('Vocabulary Learner')
root.iconbitmap('Data/sru.ico')
root.geometry('800x800+300+50')
random_vocab_arr = get_random_vocab()
current_vocab_my_List_arr = get_my_List_vocab()
current_done = get_done_word()
current_mylist_count = get_current_mylist_count()

home = Frame(root)
random = Frame(root)
my_List = Frame(root)

for frame in (home, random, my_List):
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

mylist_btn = Button(home, text='My List', command=lambda: raise_frame(my_List), height=2, width=15,
                    font='calibri 20')
mylist_btn.grid(row=5, column=1, columnspan=3, padx=150, pady=20)

revise_btn = Button(home, text='Revise Words', command="", height=2, width=15,
                    font='calibri 20')
revise_btn.grid(row=6, column=1, columnspan=3, padx=150, pady=20)

################################# Random Learning_Frame #################################

home_btn = Button(random, text='Home', command=lambda: raise_frame(home), height=1, width=10,
                    font='calibri 10')
home_btn.place(x=5, y=5)

wlabel = Label()
word = Label()
def_label = Label()
dlabel = Label()
txt = Text()
txt2 = Text()
check_frame = LabelFrame()
mylist_check = Checkbutton()
done_check = Checkbutton()
mysentense_label = Label()
txt3 = Text()
update_btn = Button()
details_label = Label()
clickhere_label = Label()
another_word = Button()

################################# my_List_Frame #################################

home_btn_ml = Button(my_List, text='Home', command=lambda: raise_frame(home), height=1, width=10,
                        font='calibri 10')
home_btn_ml.place(x=5, y=5)

wlabel_my_List = Label()
dlabel_my_List = Label()
word_my_List = Label()
def_label_my_List = Label()
txt_my_List = Text()
txt2_my_List = Text()
check_frame_my_List = LabelFrame()
mylist_check_my_List = Checkbutton()
done_check_my_List = Checkbutton()
mysentense_label_my_List = Label()
txt3_my_List = Text()
update_btn_my_List = Button()
details_label_my_List = Label()
clickhere_label_my_List = Label()
another_word_my_List = Button()
prev_btn_my_List = Button()
next_btn_my_List = Button()
warning_my_List = Label()


raise_frame(home)
root.mainloop()
