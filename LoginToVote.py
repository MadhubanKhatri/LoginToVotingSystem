from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("400x500")
root.title("Login To Voting System")

lst = ["Madhuban","Mahank","Mohit","Sonu"]
voted = []
def login():
    entry_value = entry.get()
    if entry_value in lst:
        tmsg.showinfo("Logged In",f"{entry_value} is logged in")
        lbl["text"] = f"{entry_value} is logged in."
        vote_A["stat"] = "normal"
        vote_B["stat"] = "normal"

        if entry_value in voted:
            lbl["text"] =f"{entry_value} is logged in."
            tmsg.showinfo("ERROR", f"{entry_value} already voted")
            vote_A["stat"] = "disabled"
            vote_B["stat"] = "disabled"
        else:
            voted.append(entry_value)



scoreA = 0
scoreB = 0
def voteA():
    global scoreA
    scoreA+=1
    score_lbl_A["text"] = f"Vote A is: {scoreA}"
    vote_A["stat"] = "disabled"
    vote_B["stat"] = "disabled"
def voteB():
    global scoreB
    scoreB+=1
    score_lbl_B["text"] = f"Vote B is: {scoreB}"
    vote_A["stat"] = "disabled"
    vote_B["stat"] = "disabled"



f1 = Frame(root,borderwidth=7,bg="orange")
f1.pack(fill=X)
entry = Entry(f1,font=("Helvetica", 20,"bold"))
entry.pack()
login_btn = Button(root, text="Login",bg="blue",fg="white",font=("arial",15,"bold"),command=login)
login_btn.pack()

lbl = Label(root, text="",fg="lime",font=("arial",15,"bold"))
lbl.pack()

vote_A = Button(root, text="Vote-A",stat="disabled",
                relief=RIDGE,font=("Helvetica",15,"bold"),command=voteA)
vote_A.pack(fill=X, pady=10)
vote_B = Button(root, text="Vote-B",stat="disabled",
                relief=RIDGE,font=("Helvetica",15,"bold"),command=voteB)
vote_B.pack(fill=X,pady=10)

score_lbl_A = Label(root, text="",font=("arail",20))
score_lbl_A.pack()
score_lbl_B = Label(root, text="",font=("arail",20))
score_lbl_B.pack()

root.mainloop()