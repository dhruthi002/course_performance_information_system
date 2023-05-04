from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime
import cx_Oracle
from frames_variables import *
from labels_boxes import *

student_eboxes = [txtStudentID, txtFirstName, txtLastName, txtAddress, txtDOB, txtMobile, txtEmail, txtTeacherGuardian]
student_scores = [txtScore1, txtScore2, txtScore3, txtScore4, txtScore5]
student_cboxes = [cbSemester, cbCourse, cbBranch]

cx_Oracle.init_oracle_client(lib_dir=r"path\to\oracle\21c\binaries")
dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='xe') 
conn = cx_Oracle.connect(user=r'system', password='<redacted>', dsn=dsn_tns)
cursor = conn.cursor()

treeStudents = ttk.Treeview(StudListFrame, show='headings')
treeSubjects = ttk.Treeview(SubListFrame, show='headings')

treeStudents['columns'] = ('id', 'fname', 'lname', 'email')
treeStudents.heading('id', text='ID')
treeStudents.heading('fname', text='First Name')
treeStudents.heading('lname', text='Last Name')
treeStudents.heading('email', text='Email')

treeStudents.column("id", anchor=CENTER, width=50)
treeStudents.column("fname", anchor=CENTER, width=100)
treeStudents.column("lname", anchor=CENTER, width=100)
treeStudents.column("email", anchor=CENTER, width=200)

treeSubjects['columns'] = ('sub_id', 'subname', 'brnch', 'sem')
treeSubjects.heading('sub_id', text='ID')
treeSubjects.heading('subname', text='Subject')
treeSubjects.heading('brnch', text='Branch')
treeSubjects.heading('sem', text='Semester')

treeSubjects.column("sub_id", anchor=CENTER, width=50)
treeSubjects.column("subname", anchor=CENTER, width=200)
treeSubjects.column("brnch", anchor=CENTER, width=140)
treeSubjects.column("sem", anchor=CENTER, width=30)

treeStudents['height']=20
treeSubjects['height']=20

scrollStudent = ttk.Scrollbar(StudListFrame)
scrollStudent.configure(command=treeStudents.yview)
treeStudents.configure(yscrollcommand=scrollStudent.set)
scrollStudent.pack(side= RIGHT, fill= BOTH)

scrollSubject = ttk.Scrollbar(SubListFrame)
scrollSubject.configure(command=treeSubjects.yview)
treeSubjects.configure(yscrollcommand=scrollSubject.set)
scrollSubject.pack(side= RIGHT, fill= BOTH)

cursor.execute('SELECT StudentID, FirstName, LastName, Email FROM Student')
rows = cursor.fetchall()
for row in rows:
    treeStudents.insert('', END, values=row)

cursor.execute('SELECT SubjectID, SubjectName, Branch, Semester FROM Subject')
rows = cursor.fetchall()
for row in rows:
    treeSubjects.insert('', END, values=row)

treeStudents.pack(fill='x')
treeSubjects.pack(fill='x')

def Reset ():
    for ebox in student_eboxes:
        ebox.delete(0, END)
    for ebox in student_scores:
        ebox.delete(0, END)
    for cbox in student_cboxes:
        cbox.current(0)
    txtSubject1.delete(0, END)
    txtSubject2.delete(0, END)
    txtSubject3.delete(0, END)
    txtSubject4.delete(0, END)
    txtSubject5.delete(0, END)

    txtGrade1.delete(0, END)
    txtGrade2.delete(0, END)
    txtGrade3.delete(0, END)
    txtGrade4.delete(0, END)
    txtGrade5.delete(0, END)
    txtTotalMarks.delete(0, END)
    return "break"

def PopulateStudent(event):
    try:
        item = treeStudents.selection()[0]
    except:
        return
    stu_id = (treeStudents.item(item)['values'][0])
    cursor.execute(f"SELECT * FROM Student WHERE StudentID = '{stu_id}'")
    row = cursor.fetchone()
    Reset()
    txtStudentID.insert(0, row[0])
    txtFirstName.insert(0, row[1])
    txtLastName.insert(0, row[2])
    txtAddress.insert(0, row[3])
    txtDOB.insert(0, (row[4]).strftime("%d-%m-%Y"))
    txtMobile.insert(0, row[5])
    txtEmail.insert(0, row[6])

    subjects = []
    scores = []
    cursor.execute(f"SELECT * FROM Marks WHERE StudentID = '{stu_id}'")
    rows=cursor.fetchall()

    for i in range (0, 5):
        score = rows[i][2]
        sub_id = rows[i][1]
        cursor.execute(f"SELECT * FROM Subject WHERE SubjectID = '{sub_id}' ORDER BY SubjectID")
        row=cursor.fetchone()
        subject = row[1]
        subjects.append(subject)
        scores.append(score)

    txtScore1.insert(0, scores[0])
    txtScore2.insert(0, scores[1])
    txtScore3.insert(0, scores[2])
    txtScore4.insert(0, scores[3])
    txtScore5.insert(0, scores[4])

    txtSubject1.insert(0, subjects[0])
    txtSubject2.insert(0, subjects[1])
    txtSubject3.insert(0, subjects[2])
    txtSubject4.insert(0, subjects[3])
    txtSubject5.insert(0, subjects[4])

    cursor.execute(f"SELECT FullName FROM Instructor WHERE InstructorID = (SELECT InstructorID FROM TeacherGuardian WHERE StudentID = '{stu_id}')")
    row=cursor.fetchone()
    txtTeacherGuardian.insert(0, row[0])

    cursor.execute(f"SELECT * FROM Enrolled WHERE StudentID = '{stu_id}'")
    row=cursor.fetchone()
    ind = sem_list.index(f'{row[1]}')
    cbSemester.current(ind)
    ind = course_list.index(f'{row[2]}')
    cbCourse.current(ind)
    ind = branch_list.index(f'{row[3]}')
    cbBranch.current(ind)
    PopulateGrades()
    return "break"

def chkFilled ():
    for ebox in student_eboxes:
        val = ebox.get()
        if len(val)==0:
            messagebox.showinfo("Insertion Failed", "Please fill in all fields")
            return -1
    for cbox in student_cboxes:
        if cbox.get() == '':
            messagebox.showinfo("Insertion Failed", "Please fill in all fields")
            return -1

def Insert():
    if chkFilled() == -1:
        return "break"
    stu_id = txtStudentID.get()
    cursor.execute (f"SELECT * FROM Enrolled WHERE StudentID = '{stu_id}'")
    if (len(cursor.fetchall())) != 0:
        messagebox.showinfo("Insertion Failed", "Student ID already exists")
        return "break"
    f_name = txtFirstName.get()
    l_name = txtLastName.get()
    addr = txtAddress.get()
    dob = txtDOB.get()
    mob = txtMobile.get()
    email = txtEmail.get()
    tg = txtTeacherGuardian.get()

    cursor.execute(f"SELECT * FROM Instructor WHERE FullName='{tg}'")
    row = cursor.fetchone()
    if (row==None):
        messagebox.showinfo("Insertion Failed", "Teacher Guardian does not exist")
        return "break"
    inst_id = row[0]
    cursor.execute(f"INSERT INTO TeacherGuardian VALUES ('{stu_id}', '{inst_id}')")

    cursor.execute (f"INSERT INTO  Student VALUES ('{stu_id}', '{f_name}', '{l_name}', '{addr}', TO_DATE('{dob}', 'DD-MM-YYYY'), '{mob}', '{email}')")
    branch = cbBranch.get()
    course = cbCourse.get()
    sem = cbSemester.get()
    cursor.execute (f"INSERT INTO Enrolled VALUES ('{stu_id}', {sem}, '{course}', '{branch}')")
    
    cursor.execute(f"SELECT * FROM Subject WHERE Branch='{branch}' AND Semester={sem} ORDER BY SubjectID")
    rows=cursor.fetchall()
    for i in range (0, 5):
        tb = student_scores[i]
        val = tb.get()
        sub_id = rows[i][0]
        if (len(val)==0):
            continue
        else:
            cursor.execute(f"INSERT INTO Marks VALUES ('{stu_id}', '{sub_id}', {int(val)})")
    
    conn.commit()
    cursor.execute(f"SELECT StudentID, FirstName, LastName, Email FROM Student WHERE StudentID='{stu_id}'")
    row = cursor.fetchone()
    treeStudents.insert('', END, values=row)
    messagebox.showinfo("Insert Student", "Student successfully Inserted")
    return "break"

def Update ():
    attr = ['StudentID', 'FirstName', 'LastName', 'Address', 'DOB', 'Mobile', 'Email']
    scores = []
    old_scores = []
    sub_ids = []
    stu_id = txtStudentID.get()
    tg = txtTeacherGuardian.get()

    #Check if StudentID is valid
    if len(stu_id)==0:
        messagebox.showwarning("Update Error", "Student ID cannot be empty")
        return "break"
    else:
        cursor.execute (f"SELECT * FROM Student WHERE StudentID = '{stu_id}'")
        row = cursor.fetchone()
        if (row==None):
            messagebox.showerror("Update Failed", "Student ID does not exist")
            return "break"
        
    #Get entered student scores
    for sbox in student_scores:
        val = sbox.get()
        if (len(val)!=0):
            scores.append(int(val))
        else:
            scores.append(-1)
    
    #Get existing student scores
    cursor.execute(f"SELECT * FROM Marks WHERE StudentID = '{stu_id}'")
    rows=cursor.fetchall()
    for i in range (0, 5):
        old_scores.append(rows[i][2])

    #Update TeacherGuardian table
    if (len(tg)!=0):
        cursor.execute(f"SELECT * FROM Instructor WHERE FullName='{tg}'")
        row = cursor.fetchone()
        if (row==None):
            messagebox.showinfo("Update Failed", "Teacher Guardian does not exist")
            return "break"
        inst_id = row[0]
        cursor.execute(f"UPDATE TeacherGuardian SET InstructorID='{inst_id}' WHERE StudentID='{stu_id}'")

    #Update Student table values
    for i in range (1, 7):
        ebox = student_eboxes[i]
        val = ebox.get()
        if len(val)!=0:
            if i==4:
                cursor.execute (f"UPDATE Student SET {attr[i]}=TO_DATE('{val}', 'DD-MM-YYYY') WHERE StudentID='{stu_id}'")
            else:
                cursor.execute (f"UPDATE Student SET {attr[i]}='{val}' WHERE StudentID='{stu_id}'")

    #Update Enrolled table values (Except Course)
    flag=0
    val = cbSemester.get()
    if (len(val)!=0):
        s = int(val)
        cursor.execute (f"UPDATE Enrolled SET Semester={int(val)} WHERE StudentID='{stu_id}'")
        flag=1
    val = cbBranch.get()
    if (len(val)!=0):
        b = val
        cursor.execute (f"UPDATE Enrolled SET Branch='{val}' WHERE StudentID='{stu_id}'")
        flag=1
    
    if (flag==0):
        cursor.execute((f"SELECT * FROM Enrolled WHERE StudentID='{stu_id}'"))
        row = cursor.fetchone()
        cursor.execute(f"SELECT * FROM Subject WHERE Branch='{row[3]}' AND Semester={int (row[1])} ORDER BY SubjectID")
        rows=cursor.fetchall()
        #Update new marks entries
        for i in range (0, 5):
            if scores[i]!=-1:
                cursor.execute(f"UPDATE Marks SET ObtainedMarks={scores[i]} WHERE SubjectID='{rows[i][0]}'")

    #If new score has not been entered, use old score
    for i in range (0, 5):
        if (scores[i]==-1):
            scores[i]=old_scores[i]

    #If Enrolled has been changed, accordingly change the subjects and enter marks
    if (flag==1):
        cursor.execute(f"SELECT * FROM Subject WHERE Branch='{b}' AND Semester={s} ORDER BY SubjectID")
        rows=cursor.fetchall()
        #Delete old marks entries
        cursor.execute(f"DELETE FROM Marks WHERE StudentID='{stu_id}'")
        #Insert new marks entries
        for i in range (0, 5):
            cursor.execute(f"INSERT INTO Marks VALUES ('{stu_id}', '{rows[i][0]}', {scores[i]})")

    #Delete the old tree entry
    tree_items = treeStudents.get_children()
    for item in tree_items:
        col_value = treeStudents.item(item)['values'][0]
        if col_value == stu_id:
            treeStudents.delete(item)

    conn.commit()    
    cursor.execute(f"SELECT StudentID, FirstName, LastName, Email FROM Student WHERE StudentID='{stu_id}'")
    row = cursor.fetchone()
    treeStudents.insert('', END, values=row) #Insert new table entry
    PopulateGrades()
    messagebox.showinfo("Update Student", "Student successfully updated")
    return "break"
    

def UpdateSubject ():
    sub_id = txtSSubjectID.get()
    if len(sub_id)==0:
        messagebox.showwarning("Update Error", "Subject ID cannot be empty")
        return "break"
    else:
        cursor.execute (f"SELECT * FROM Subject WHERE SubjectID = '{sub_id}'")
        row = cursor.fetchone()
        if (row==None):
            messagebox.showerror("Update Failed", "Subject ID does not exist")
            return "break"
    cutoff = txtCutoff.get()
    numA = txtNumAssgn.get()
    if (len(cutoff)!=0):
        cursor.execute (f"UPDATE Subject SET Cutoff={int(cutoff)} WHERE SubjectID='{sub_id}'")
    if (len(numA)!=0):
        cursor.execute (f"UPDATE Subject SET NumOfAssignments={int(numA)} WHERE SubjectID='{sub_id}'")
    PopulateGrades()
    messagebox.showinfo ("Subject Update", "Subject information updated successfully")
    return "break"


def calculateGrade (cutoff, s):
    wt = (100 - cutoff)/6
    if (s>(100-wt)):
        return "A+"
    elif (s>(100-(2*wt))):
       return "A"
    elif (s>(100-(3*wt))):
        return"B"
    elif (s>(100-(4*wt))):
       return"C"
    elif (s>(100-(5*wt))):
        return"D"
    elif (s>cutoff):
        return"E"
    else:
        return"F"


def PopulateGrades():
    try:
        item = treeStudents.selection()[0]
    except:
        return
    stu_id = (treeStudents.item(item)['values'][0])
    cursor.execute(f"SELECT * FROM Marks WHERE StudentID = '{stu_id}'")
    rows=cursor.fetchall()
    cutoff=0
    grades=[]
    for i in range (0, 5):
        score = rows[i][2]
        sub_id = rows[i][1]
        cursor.execute(f"SELECT * FROM Subject WHERE SubjectID = '{sub_id}' ORDER BY SubjectID")
        row=cursor.fetchone()
        cutoff = row[4]
        grades.append(calculateGrade(cutoff, score))

    txtGrade1.delete(0, END)
    txtGrade2.delete(0, END)
    txtGrade3.delete(0, END)
    txtGrade4.delete(0, END)
    txtGrade5.delete(0, END)

    txtGrade1.insert(0, grades[0])
    txtGrade2.insert(0, grades[1])
    txtGrade3.insert(0, grades[2])
    txtGrade4.insert(0, grades[3])
    txtGrade5.insert(0, grades[4])
    total = cursor.callfunc("calcTotMarks", int, [stu_id])
    status = cursor.callfunc("calcStatus", int, [stu_id])
    txtStatus.delete(0, END)
    if (status==0):
        txtStatus.insert(0, "FAIL")
    else:
        txtStatus.insert(0, "PASS")
    txtTotalMarks.insert(0, total)
    return "break"


def Delete ():
    stu_id = txtStudentID.get()
    tree_items = treeStudents.get_children()
    for item in tree_items:
        col_value = treeStudents.item(item)['values'][0]
        if col_value == stu_id:
            treeStudents.delete(item)
    cursor.execute(f"DELETE FROM Student WHERE StudentID='{stu_id}'")
    conn.commit()
    Reset()
    messagebox.showinfo("Delete Student", "Student successfully Deleted")
    return "break"


def Exit ():
    root.destroy()


def PopulateSubject (event):
    try:
        item = treeSubjects.selection()[0]
    except:
        return
    sub_id = (treeSubjects.item(item)['values'][0])
    brnch = (treeSubjects.item(item)['values'][2])
    sem = (treeSubjects.item(item)['values'][3])
    cursor.execute(f"SELECT * FROM Subject WHERE SubjectID = '{sub_id}'")
    row = cursor.fetchone()

    txtSSubjectID.delete(0, END)
    txtSSubjectN.delete(0, END)
    txtNumAssgn.delete(0, END)
    txtCutoff.delete(0, END)
    cbSSem.current(0)
    cbSCrse.current(0)
    cbSBrnch.current(0)

    txtSSubjectID.insert(0, row[0])
    txtSSubjectN.insert(0, row[1])
    ind = sem_list.index(f'{row[5]}')
    cbSSem.current(ind)
    ind = course_list.index(f'{row[2]}')
    cbSCrse.current(ind)
    ind = branch_list.index(f'{row[3]}')
    cbSBrnch.current(ind)
    txtCutoff.insert(0, row[4])
    txtNumAssgn.insert(0, row[6])
    cursor.execute(f"SELECT COUNT(*) FROM Enrolled WHERE Branch = '{brnch}' AND Semester = '{sem}'")
    row = cursor.fetchone()
    txtStuEnrold.config(text=row[0])

    cursor.execute(f"SELECT * FROM Marks WHERE SubjectID = '{sub_id}'")
    rows = cursor.fetchall()
    n=len(rows)
    tot=0
    for i in range (0, n):
        tot = tot+int(rows[i][2])
    av=tot//n
    txtAvgMarks.config(text=av)
    return "break"
    


treeStudents.bind('<<TreeviewSelect>>', PopulateStudent)
treeSubjects.bind('<<TreeviewSelect>>', PopulateSubject)
btnDelete.bind("<Button-1>", lambda event: Delete())
btnReset.bind("<Button-1>", lambda event: Reset())
btnExit.bind("<Button-1>", lambda event: Exit())
btnInsert.bind("<Button-1>", lambda event: Insert())
btnUpdate.bind("<Button-1>", lambda event: Update())
btnUpdateSub.bind("<Button-1>", lambda event: UpdateSubject())
