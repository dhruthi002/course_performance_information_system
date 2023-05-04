CREATE TABLE LogStudentChange (
   ChangeTime DATE,
   StudentID VARCHAR2(10),
   FirstName VARCHAR2(30),
   LastName VARCHAR2(30),
   Address VARCHAR2(100),
   DOB DATE,
   Mobile VARCHAR2(20),
   Email VARCHAR2(50)
);

CREATE OR REPLACE TRIGGER logStudent
BEFORE INSERT OR UPDATE OR DELETE ON Student
FOR EACH ROW
BEGIN
CASE
WHEN INSERTING THEN
    INSERT INTO LogStudentChange 
    VALUES(SYSDATE,:NEW.StudentID, :NEW.FirstName, :NEW.LastName, :NEW.Address, :NEW.DOB, :NEW.Mobile, :NEW.Email);
WHEN UPDATING OR DELETING THEN
    INSERT INTO LogStudentChange 
    VALUES(SYSDATE,:OLD.StudentID, :OLD.FirstName, :OLD.LastName, :OLD.Address, :OLD.DOB, :OLD.Mobile, :OLD.Email);
END CASE;
END;
/

CREATE TABLE LogSubjectChange (
    ChangeTime DATE,
    SubjectID VARCHAR2(10),
    Cutoff NUMBER,
    NumOfAssignments NUMBER
);

CREATE OR REPLACE TRIGGER logSubject
BEFORE UPDATE OF Cutoff, NumOfAssignments ON Subject
FOR EACH ROW
BEGIN
    INSERT INTO LogSubjectChange 
    VALUES(SYSDATE,:OLD.SubjectID, :OLD.Cutoff, :OLD.NumOfAssignments);
END;
/
