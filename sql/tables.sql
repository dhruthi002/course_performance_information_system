DROP TABLE Student;
DROP TABLE Enrolled;
DROP TABLE Instructor;
DROP TABLE TaughtBy;
DROP TABLE TeacherGuardian;
DROP TABLE Marks;
DROP TABLE Subject;

CREATE TABLE Student (
   StudentID VARCHAR2(10) PRIMARY KEY,
   FirstName VARCHAR2(30),
   LastName VARCHAR2(30),
   Address VARCHAR2(100),
   DOB DATE,
   Mobile VARCHAR2(20),
   Email VARCHAR2(50)
);

CREATE TABLE Enrolled (
   StudentID VARCHAR2(10) PRIMARY KEY,
   Semester VARCHAR2(10),
   Course VARCHAR2(20),
   Branch VARCHAR2(30),
   CONSTRAINT fk_enrolled
        FOREIGN KEY (StudentID)
        REFERENCES Student(StudentID)
        ON DELETE CASCADE
);

CREATE TABLE Instructor (
    InstructorID VARCHAR2(10) PRIMARY KEY,
    FullName VARCHAR2(50),
    Course VARCHAR2(20),
    Branch VARCHAR2(30)
);

CREATE TABLE TaughtBy (
    SubjectID VARCHAR2(30),
    InstructorID VARCHAR2(10),
    CONSTRAINT fk_taughtby
        FOREIGN KEY (SubjectID)
        REFERENCES Subject(SubjectID)
        ON DELETE CASCADE,
    CONSTRAINT fkt_taughtby
        FOREIGN KEY (InstructorID)
        REFERENCES Instructor(StudentID)
        ON DELETE CASCADE
); 

CREATE TABLE TeacherGuardian (
    StudentID VARCHAR2(10),
    InstructorID VARCHAR2(10),
    CONSTRAINT fk_teachergrd
        FOREIGN KEY (StudentID)
        REFERENCES Student(StudentID)
        ON DELETE CASCADE,
    CONSTRAINT fkt_teachergrd
        FOREIGN KEY (InstructorID)
        REFERENCES Instructor(InstructorID)
        ON DELETE CASCADE
);


CREATE TABLE Subject (
    SubjectID VARCHAR2(10) PRIMARY KEY,
    SubjectName VARCHAR2(30),
    Course VARCHAR2(20),
    Branch VARCHAR2(30),
    Cutoff NUMBER,
    Semester NUMBER,
    NumOfAssignments NUMBER
);

CREATE TABLE Marks (
    StudentID VARCHAR2(10),
    SubjectID VARCHAR2(10),
    ObtainedMarks NUMBER(10),
    CONSTRAINT fk_marks
        FOREIGN KEY (StudentID)
        REFERENCES Student(StudentID)
        ON DELETE CASCADE
    CONSTRAINT fks_marks
        FOREIGN KEY (SubjectID)
        REFERENCES Subject(SubjectID)
        ON DELETE CASCADE
);

