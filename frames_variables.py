from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import datetime


root=Tk()
root.title("Student Grading System")
root.geometry("1350x800+0+0")
notebook = ttk.Notebook(root)
TabControl1 = ttk.Frame(notebook)
TabControl2 = ttk.Frame(notebook)
TabControl3 = ttk.Frame(notebook)
notebook.add(TabControl2, text='Grade Sheet')
notebook.add(TabControl1, text="Student Details")
notebook.add(TabControl3, text='Subject Details')
notebook.grid()

# =======================Variables=============================
StudentID = StringVar()
FirstName = StringVar()
LastName = StringVar()
Address = StringVar()
DOB = StringVar()
Mobile = StringVar()
Email = StringVar()
Semester = StringVar()
Course = StringVar()
Branch = StringVar()
TeacherGuardian = StringVar()

InstructorID = StringVar()
SubjectID = StringVar()

S_SubjectID = StringVar()
S_Semester = StringVar()
S_Course = StringVar()
S_Branch = StringVar()
S_SubjName = StringVar()

S_Cutoff = StringVar()
S_NumOfAssignments = StringVar()

Subject1 = StringVar()
Subject2 = StringVar()
Subject3 = StringVar()
Subject4 = StringVar()
Subject5 = StringVar()

Marks1 = StringVar()
Marks2 = StringVar()
Marks3 = StringVar()
Marks4 = StringVar()
Marks5 = StringVar()

Grade1 = StringVar()
Grade2 = StringVar()
Grade3 = StringVar()
Grade4 = StringVar()
Grade5 = StringVar()

TotalMarks = StringVar()
MaxScorer = StringVar()
AvgScore = StringVar()
Status = StringVar()

# ==========================Frames=========================================
MainFrameUS = Frame(TabControl1, bd=10, width=1350, height=600, relief=GROOVE, background="#a9ccbe")
MainFrameUS.pack(expand=True ,fill=None ,side=TOP)

MainFrameStud = Frame(TabControl2, bd=10, width=1350, height=600, relief=GROOVE, background="#a9ccbe")
MainFrameStud.pack(expand=True ,fill=None ,side=TOP)

MainFrameSub = Frame(TabControl3, bd=10, width=1350, height=600, relief=GROOVE, background="#a9ccbe")
MainFrameSub.pack(expand=True ,fill=None ,side=TOP)

# ==========================Student Details Frames (SCREEN-2)=========================================
# Create three child frames inside MainFrameUS
LeftFrameUS = Frame(MainFrameUS, bd=5, width=700, height=650, relief=GROOVE)
RightFrameUS = Frame(MainFrameUS, bd=5, width=450, height=650, relief=GROOVE)
Button_Frame = Frame(MainFrameUS, bd=0 ,width=430, height=25, relief=GROOVE)

Button_Frame.pack(side=BOTTOM, pady=5)
LeftFrameUS.pack(expand=True ,fill=None ,side=LEFT,  padx=10, pady=5)
RightFrameUS.pack(expand=True ,fill=None,side=LEFT, padx=10, pady=5)

# Create StudentFrame in Left and SubjectFrame in Right
StudentFrame = Frame(LeftFrameUS,bd=0, width=700, height=650, relief=GROOVE)
SubjectFrame = Frame(RightFrameUS,bd=0, width=700, height=650, relief=GROOVE)

StudentFrame.pack(side=LEFT, padx=10, pady=5)
SubjectFrame.pack(side=LEFT, padx=10, pady=5)

# Add buttons to Button_Frame
btnInsert = Button(Button_Frame, pady=1, padx=10, bd=4, font=('arial', 16, 'bold'), text="Insert", bg="light blue")
btnInsert.grid(row=0, column=0, padx=1)
btnUpdate = Button(Button_Frame, pady=1, padx=10, bd=4, font=('arial', 16, 'bold'), text="Update", bg="light blue")
btnUpdate.grid(row=0, column=1, padx=1)
btnDelete = Button(Button_Frame, pady=1, padx=10, bd=4, font=('arial', 16, 'bold'), text="Delete", bg="light blue")
btnDelete.grid(row=0, column=2, padx=1)
btnReset = Button(Button_Frame, pady=1, padx=10, bd=4, font=('arial', 16, 'bold'), text="Reset", bg="light blue")
btnReset.grid(row=0, column=3, padx=1)
btnExit = Button(Button_Frame, pady=1, padx=10, bd=4, font=('arial', 16, 'bold'), text="Exit", bg="light blue")
btnExit.grid(row=0, column=4, padx=1)

# ==========================Grade Sheet Frames (SCREEN-1 )=========================================
# Create two child frames inside MainFrameStud
LeftFrameStud = Frame(MainFrameStud, bd=5, width=450, height=650, relief=GROOVE)
RightFrameStud = Frame(MainFrameStud, bd=5, width=450, height=650, relief=GROOVE)

LeftFrameStud.pack(side=LEFT, padx=10, pady=15)
RightFrameStud.pack(side=LEFT, padx=10, pady=15)

#Create GradeSheetFrame in left and StudListFrame in the right
GradeSheetFrame = Frame(LeftFrameStud,bd=0, width=430, height=650, relief=GROOVE, bg="#e6bbad")
StudListFrame = Frame(RightFrameStud,bd=5, width=430, height=850, relief=GROOVE)
StatusFrameStud = Frame(LeftFrameStud, bd=0 ,width=430, height=25, relief=GROOVE, bg="lightgrey")

StatusFrameStud.pack(side=BOTTOM, padx=15, pady=15)
GradeSheetFrame.pack(side=BOTTOM, padx=15, pady=15)
StudListFrame.pack(side=LEFT, padx=15, pady=15)

# ==========================Subject Details Frames (SCREEN-3)=========================================
# Create two child frames inside MainFrameSub
LeftFrameSub = Frame(MainFrameSub, bd=5, width=450, height=650, relief=GROOVE)
RightFrameSub = Frame(MainFrameSub, bd=5, width=450, height=650, relief=GROOVE)

LeftFrameSub.pack(side=LEFT, padx=10, pady=5)
RightFrameSub.pack(side=LEFT, padx=10, pady=5)

ViewButtonFrame = Frame(LeftFrameSub,bd=5, width=430, height=300, relief=GROOVE, bg="lightblue")
SubFilterFrame = Frame(LeftFrameSub,bd=15, width=430, height=300, relief=FLAT) #, highlightbackground="black", highlightcolor="black", highlightthickness=5
SubViewFrame = Frame(ViewButtonFrame,bd=0, width=430, height=300, relief=RAISED, bg="lightblue")
SubListFrame = Frame(RightFrameSub,bd=0, width=430, height=650, relief=GROOVE)
MaxScoreFrame = Frame(RightFrameSub,bd=0, width=430, height=50, relief=GROOVE, bg="lightgrey")
UButtonFrameSub = Frame(ViewButtonFrame, bd=0 ,width=430, height=25, relief=GROOVE)

ViewButtonFrame.pack(side=BOTTOM, padx=10, pady=5)
UButtonFrameSub.pack(side=BOTTOM, padx=10, pady=5)
SubViewFrame.pack(side=BOTTOM, padx=10, pady=5)
SubFilterFrame.pack(side=BOTTOM, padx=10, pady=5)
MaxScoreFrame.pack(side=BOTTOM,padx=10, pady=5)
SubListFrame.pack(side=BOTTOM, padx=10, pady=5)

btnUpdateSub = Button(UButtonFrameSub, pady=1, padx=10, bd=4, font=('arial', 14, 'bold'), text="Update")
btnUpdateSub.grid (row=0, column=1, padx=1)