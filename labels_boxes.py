from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import datetime
import time
from frames_variables import *

sem_list = ('', '2', '4', '6')
branch_list = ('', 'Computer Science', 'Mechanical', 'Electronics', 'Physics', 'Chemistry')
course_list = ('', 'B.Tech', 'B.Sc')


#=====================================Student Details Labels (SCREEN 2)======================================================
# Student ID
lbStudentID = Label(StudentFrame, font=('arial', 12, 'bold'), text="Student ID: ", bd=7, anchor='w', justify=LEFT)
lbStudentID.grid (row=0, column=0, sticky=W, padx=5, pady=5)
txtStudentID = Entry(StudentFrame, font=('arial', 12, 'bold'), bd=5, width=25, justify='left', textvariable=StudentID)        
txtStudentID.grid(row=0, column=1)

# First Name
lbFirstName = Label(StudentFrame, font=('arial', 12, 'bold'), text="First Name: ", bd=7, anchor='w', justify=LEFT)
lbFirstName.grid(row=1, column=0, sticky=W, padx=5, pady=5)
txtFirstName = Entry(StudentFrame, font=('arial', 12, 'bold'), bd=5, width=25, justify='left', textvariable=FirstName)
txtFirstName.grid(row=1, column=1)

# Last Name
lbLastName = Label(StudentFrame, font=('arial', 12, 'bold'), text="Last Name: ", bd=7, anchor='w', justify=LEFT)
lbLastName.grid(row=2, column=0, sticky=W, padx=5, pady=5)
txtLastName = Entry(StudentFrame, font=('arial', 12, 'bold'), bd=5, width=25, justify='left', textvariable=LastName)
txtLastName.grid(row=2, column=1)

# Address
lbAddress = Label(StudentFrame, font=('arial', 12, 'bold'), text="Address: ", bd=7, anchor='w', justify=LEFT)
lbAddress.grid(row=3, column=0, sticky=W, padx=5, pady=5)
txtAddress = Entry(StudentFrame, font=('arial', 12, 'bold'), bd=5, width=25, justify='left', textvariable=Address)
txtAddress.grid(row=3, column=1)

# DOB
lbDOB = Label(StudentFrame, font=('arial', 12, 'bold'), text="DOB: ", bd=7, anchor='w', justify=LEFT)
lbDOB.grid(row=4, column=0, sticky=W, padx=5, pady=5)
txtDOB = Entry(StudentFrame, font=('arial', 12, 'bold'), bd=5, width=25, justify='left', textvariable=DOB)
txtDOB.grid(row=4, column=1)

# Mobile
lbMobile = Label(StudentFrame, font=('arial', 12, 'bold'), text="Mobile: ", bd=7, anchor='w', justify=LEFT)
lbMobile.grid(row=5, column=0, sticky=W, padx=5, pady=5)
txtMobile = Entry(StudentFrame, font=('arial', 12, 'bold'), bd=5, width=25, justify='left', textvariable=Mobile)
txtMobile.grid(row=5, column=1)

# Email
lbEmail = Label(StudentFrame, font=('arial', 12, 'bold'), text="Email: ", bd=7, anchor='w', justify=LEFT)
lbEmail.grid(row=6, column=0, sticky=W, padx=5, pady=5)
txtEmail = Entry(StudentFrame, font=('arial', 12, 'bold'), bd=5, width=25, justify='left', textvariable=Email)
txtEmail.grid(row=6, column=1)

# Semester
lbSemester = Label(StudentFrame, font=('arial', 12, 'bold'), text="Semester:", bd=7, anchor='w', justify=LEFT)
lbSemester.grid(row=7, column=0, sticky=W, padx=5, pady=5)
cbSemester = ttk.Combobox(StudentFrame, textvariable=Semester, width=23)
cbSemester['value'] = sem_list
cbSemester.current(0)
cbSemester.grid(row=7, column=1)

# Course
lbCourse = Label(StudentFrame, font=('arial', 12, 'bold'), text="Course:", bd=7, anchor='w', justify=LEFT)
lbCourse.grid(row=8, column=0, sticky=W, padx=5, pady=5)
cbCourse = ttk.Combobox(StudentFrame, textvariable=Course, width=23)
cbCourse['value'] = course_list
cbCourse.current(0)
cbCourse.grid(row=8, column=1)

# Branch
lbBranch = Label(StudentFrame, font=('arial', 12, 'bold'), text="Branch:", bd=7, anchor='w', justify=LEFT)
lbBranch.grid(row=9, column=0, sticky=W, padx=5, pady=5)
cbBranch = ttk.Combobox(StudentFrame, textvariable=Branch, width=23)
cbBranch['value'] = branch_list
cbBranch.current(0)
cbBranch.grid(row=9, column=1)

# Teacher/Guardian
lbTeacherGuardian = Label(StudentFrame, font=('arial', 12, 'bold'), text="Teacher Guardian: ", bd=7, anchor='w', justify=LEFT)
lbTeacherGuardian.grid(row=10, column=0, sticky=W, padx=5, pady=5)
txtTeacherGuardian = Entry(StudentFrame, font=('arial', 12, 'bold'), bd=5, width=25, justify='left', textvariable=TeacherGuardian)
txtTeacherGuardian.grid(row=10, column=1)

# Subject Labels
lbSNo = Label(SubjectFrame, font=('arial', 13, 'bold'), text="Marks Scored ", background="lightblue", justify=CENTER)
lbSNo.grid(row=0, column=0, padx=(10, 30), pady=5, columnspan=3, )

lb1SubNo = Label(SubjectFrame, font=('arial', 12, 'bold'), text="1. ")
lb2SubNo = Label(SubjectFrame, font=('arial', 12, 'bold'), text="2. ")
lb3SubNo = Label(SubjectFrame, font=('arial', 12, 'bold'), text="3. ")
lb4SubNo = Label(SubjectFrame, font=('arial', 12, 'bold'), text="4. ")
lb5SubNo = Label(SubjectFrame, font=('arial', 12, 'bold'), text="5. ")

lb1SubNo.grid(row=1, column=0, padx=10, pady=5)
lb2SubNo.grid(row=2, column=0, padx=10, pady=5)
lb3SubNo.grid(row=3, column=0, padx=10, pady=5)
lb4SubNo.grid(row=4, column=0, padx=10, pady=5)
lb5SubNo.grid(row=5, column=0, padx=10, pady=5)

txtSubject1 = Entry(SubjectFrame, font=('arial', 12, 'bold'), textvariable=Subject1, width=30)
txtSubject2 = Entry(SubjectFrame, font=('arial', 12, 'bold'), textvariable=Subject2, width=30)
txtSubject3 = Entry(SubjectFrame, font=('arial', 12, 'bold'), textvariable=Subject3, width=30)
txtSubject4 = Entry(SubjectFrame, font=('arial', 12, 'bold'), textvariable=Subject4, width=30)
txtSubject5 = Entry(SubjectFrame, font=('arial', 12, 'bold'), textvariable=Subject5, width=30)
lbTotalMarks = Label(StatusFrameStud, font=('arial', 12, 'bold'), text="Total Marks Scored: ", bg="lightgrey")
lbStatus = Label(StatusFrameStud, font=('arial', 12, 'bold'), text="Status: ", bg="lightgrey")

txtSubject1.grid(row=1, column=1, padx=10, pady=5)
txtSubject2.grid(row=2, column=1, padx=10, pady=5)
txtSubject3.grid(row=3, column=1, padx=10, pady=5)
txtSubject4.grid(row=4, column=1, padx=10, pady=5)
txtSubject5.grid(row=5, column=1, padx=10, pady=5)
lbTotalMarks.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
lbStatus.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

txtScore1 = Entry (SubjectFrame, font=('arial', 12, 'bold'), textvariable=Marks1,  width=5, bd=5)
txtScore2 = Entry (SubjectFrame, font=('arial', 12, 'bold'), textvariable=Marks2,  width=5, bd=5)
txtScore3 = Entry (SubjectFrame, font=('arial', 12, 'bold'), textvariable=Marks3,  width=5, bd=5)
txtScore4 = Entry (SubjectFrame, font=('arial', 12, 'bold'), textvariable=Marks4,  width=5, bd=5)
txtScore5 = Entry (SubjectFrame, font=('arial', 12, 'bold'), textvariable=Marks5,  width=5, bd=5)
txtTotalMarks = Entry (StatusFrameStud, font=('arial', 12, 'bold'), textvariable=TotalMarks,  width=10, bd=5)
txtStatus = Entry (StatusFrameStud, font=('arial', 12, 'bold'), textvariable=Status,  width=10, bd=5)

txtScore1.grid(row=1, column=3, padx=10, pady=5)
txtScore2.grid(row=2, column=3, padx=10, pady=5)
txtScore3.grid(row=3, column=3, padx=10, pady=5)
txtScore4.grid(row=4, column=3, padx=10, pady=5)
txtScore5.grid(row=5, column=3, padx=10, pady=5)
txtTotalMarks.grid(row=1, column=3, padx=10, pady=5)
txtStatus.grid(row=2, column=3, padx=10, pady=5)




#=====================================Grade Sheet Labels (SCREEN 1)======================================================
lbGSNo = Label(GradeSheetFrame, font=('arial', 15, 'bold'), text="       GRADE SHEET", justify=LEFT, bg="#e6bbad")
lbGSNo.grid(row=0, column=0, padx=(10, 30), pady=10, columnspan=3, )

lb1GSubNo = Label(GradeSheetFrame, font=('arial', 12, 'bold'), text="1. ", bg="#e6bbad")
lb2GSubNo = Label(GradeSheetFrame, font=('arial', 12, 'bold'), text="2. ", bg="#e6bbad")
lb3GSubNo = Label(GradeSheetFrame, font=('arial', 12, 'bold'), text="3. ", bg="#e6bbad")
lb4GSubNo = Label(GradeSheetFrame, font=('arial', 12, 'bold'), text="4. ", bg="#e6bbad")
lb5GSubNo = Label(GradeSheetFrame, font=('arial', 12, 'bold'), text="5. ", bg="#e6bbad")

lb1GSubNo.grid(row=1, column=0, padx=10, pady=10)
lb2GSubNo.grid(row=2, column=0, padx=10, pady=10)
lb3GSubNo.grid(row=3, column=0, padx=10, pady=10)
lb4GSubNo.grid(row=4, column=0, padx=10, pady=10)
lb5GSubNo.grid(row=5, column=0, padx=10, pady=10)

txtGSubject1 = Entry(GradeSheetFrame, font=('arial', 12, 'bold'), textvariable=Subject1, width=30, bd=5)
txtGSubject2 = Entry(GradeSheetFrame, font=('arial', 12, 'bold'), textvariable=Subject2, width=30, bd=5)
txtGSubject3 = Entry(GradeSheetFrame, font=('arial', 12, 'bold'), textvariable=Subject3, width=30, bd=5)
txtGSubject4 = Entry(GradeSheetFrame, font=('arial', 12, 'bold'), textvariable=Subject4, width=30, bd=5)
txtGSubject5 = Entry(GradeSheetFrame, font=('arial', 12, 'bold'), textvariable=Subject5, width=30, bd=5)

txtGSubject1.grid(row=1, column=1, padx=10, pady=10)
txtGSubject2.grid(row=2, column=1, padx=10, pady=10)
txtGSubject3.grid(row=3, column=1, padx=10, pady=10)
txtGSubject4.grid(row=4, column=1, padx=10, pady=10)
txtGSubject5.grid(row=5, column=1, padx=10, pady=10)

txtGrade1 = Entry (GradeSheetFrame, font=('arial', 12, 'bold'), textvariable=Grade1,  width=5, bd=5)
txtGrade2 = Entry (GradeSheetFrame, font=('arial', 12, 'bold'), textvariable=Grade2,  width=5, bd=5)
txtGrade3 = Entry (GradeSheetFrame, font=('arial', 12, 'bold'), textvariable=Grade3,  width=5, bd=5)
txtGrade4 = Entry (GradeSheetFrame, font=('arial', 12, 'bold'), textvariable=Grade4,  width=5, bd=5)
txtGrade5 = Entry (GradeSheetFrame, font=('arial', 12, 'bold'), textvariable=Grade5,  width=5, bd=5)

txtGrade1.grid(row=1, column=3, padx=10, pady=10)
txtGrade2.grid(row=2, column=3, padx=10, pady=10)
txtGrade3.grid(row=3, column=3, padx=10, pady=10)
txtGrade4.grid(row=4, column=3, padx=10, pady=10)
txtGrade5.grid(row=5, column=3, padx=10, pady=10)


#=====================================Subject Details Labels (SCREEN 3)======================================================
# SubjectID
lbSSubjectID = Label(SubFilterFrame, font=('arial', 12, 'bold'), text="Subject ID: ", bd=7, anchor='w', justify=LEFT)
lbSSubjectID.grid (row=1, column=0, sticky=W, padx=15, pady=5)
txtSSubjectID = Entry(SubFilterFrame, font=('arial', 12, 'bold'), bd=5, width=25, justify='left', textvariable=S_SubjectID)        
txtSSubjectID.grid(row=1, column=1, padx=15, pady=5)

# Semester
lbSSem = Label(SubFilterFrame, font=('arial', 12, 'bold'), text="Semester:", bd=7, anchor='w', justify=LEFT)
lbSSem.grid(row=3, column=0, sticky=W, padx=15, pady=5)
cbSSem = ttk.Combobox(SubFilterFrame, textvariable=S_Semester, width=23)
cbSSem['value'] = sem_list
cbSSem.current(0)
cbSSem.grid(row=3, column=1, padx=15, pady=5)

# Course
lbSCrse = Label(SubFilterFrame, font=('arial', 12, 'bold'), text="Course:", bd=7, anchor='w', justify=LEFT)
lbSCrse.grid(row=4, column=0, sticky=W, padx=15, pady=5)
cbSCrse = ttk.Combobox(SubFilterFrame, textvariable=S_Course, width=23)
cbSCrse['value'] = course_list
cbSCrse.current(0)
cbSCrse.grid(row=4, column=1, padx=15, pady=5)

# Branch
lbSBrnch = Label(SubFilterFrame, font=('arial', 12, 'bold'), text="Branch:", bd=7, anchor='w', justify=LEFT)
lbSBrnch.grid(row=5, column=0, sticky=W, padx=15, pady=5)
cbSBrnch = ttk.Combobox(SubFilterFrame, textvariable=S_Branch, width=23)
cbSBrnch['value'] = branch_list
cbSBrnch.current(0)
cbSBrnch.grid(row=5, column=1, padx=15, pady=5)

# Subject
lbSSubjectN = Label(SubFilterFrame, font=('arial', 12, 'bold'), text="Subject Name: ", bd=7, anchor='w', justify=LEFT)
lbSSubjectN.grid (row=2, column=0, sticky=W, padx=15, pady=5)
txtSSubjectN = Entry(SubFilterFrame, font=('arial', 12, 'bold'), bd=5, width=25, justify='left', textvariable=S_SubjName)        
txtSSubjectN.grid(row=2, column=1, padx=15, pady=5)

# No. of assignments
lbNumAssgn = Label(SubViewFrame, font=('arial', 12, 'bold'), text="No. of assignments: ", bd=7, anchor='w', justify=LEFT, background="lightblue")
lbNumAssgn.grid (row=2, column=0, sticky=W, padx=15, pady=5)
txtNumAssgn = Entry(SubViewFrame, font=('arial', 12, 'bold'), bd=5, width=15, justify='left', textvariable=S_NumOfAssignments)        
txtNumAssgn.grid(row=2, column=1, padx=15, pady=5)

# Cutoff
lbCutoff = Label(SubViewFrame, font=('arial', 12, 'bold'), text="Cutoff: ", bd=7, anchor='w', justify=LEFT, background="lightblue")
lbCutoff.grid (row=1, column=0, sticky=W, padx=15, pady=5)
txtCutoff = Entry(SubViewFrame, font=('arial', 12, 'bold'), bd=5, width=15, justify='left', textvariable=S_Cutoff)        
txtCutoff.grid(row=1, column=1, padx=15, pady=5)

# Students Enrolled
lbStuEnrold = Label(SubFilterFrame, font=('arial', 12, 'bold'), text="Students Enrolled: ", bd=7, anchor='w', justify=LEFT)
lbStuEnrold.grid (row=7, column=0, sticky=W, padx=15, pady=5)
txtStuEnrold = Label(SubFilterFrame, font=('arial', 12, 'bold'), text=" ", bd=7, anchor='w', justify=LEFT)       
txtStuEnrold.grid(row=7, column=1, padx=15, pady=5)

#Avg Marks
lbAvgMarks = Label(MaxScoreFrame, font=('arial', 11, 'bold'), text="Subject Avg. Marks: ", bd=7, anchor='w', justify=LEFT, bg="lightgrey")
lbAvgMarks.grid (row=1, column=0, sticky=W, padx=15, pady=5)
txtAvgMarks = Label(MaxScoreFrame, font=('arial', 11, 'bold'), text=" ", bd=5, anchor='w', justify=LEFT, bg="lightgrey")       
txtAvgMarks.grid(row=1, column=1, padx=15, pady=5)