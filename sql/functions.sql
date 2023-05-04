CREATE OR REPLACE FUNCTION calcTotMarks(p_student_id IN VARCHAR2) RETURN NUMBER IS
  v_marks NUMBER(10);
  v_tot_marks NUMBER(10) := 0;
  
  CURSOR c_marks IS
    SELECT ObtainedMarks FROM Marks WHERE StudentID = p_student_id;
BEGIN
  FOR c IN c_marks LOOP
    v_marks := c.ObtainedMarks;
    v_tot_marks := v_tot_marks + v_marks;
  END LOOP;
  RETURN v_tot_marks;
END;
/

DECLARE
  v_tot_marks NUMBER;
BEGIN
  v_tot_marks := calcTotMarks('ST0095');
  DBMS_OUTPUT.PUT_LINE('Total marks: ' || v_tot_marks);
END;
/

CREATE OR REPLACE FUNCTION calcStatus(p_student_id IN VARCHAR2) RETURN NUMBER IS
  v_marks NUMBER(10);
  v_cutoff NUMBER(10) := 0;
  v_sub_id VARCHAR2(10);
  res NUMBER := 1;
  CURSOR c_marks IS
    SELECT * FROM Marks WHERE StudentID = p_student_id;
BEGIN
  
  FOR c IN c_marks LOOP
    v_marks := c.ObtainedMarks;
    v_sub_id := c.SubjectID;
    SELECT Cutoff INTO v_cutoff FROM Subject WHERE SubjectID = v_sub_id;
    IF v_marks < v_cutoff THEN
        res := 0;
    END IF;
  END LOOP;
  RETURN res;
END;
/

DECLARE
  v_res NUMBER;
BEGIN
  v_res := calcStatus('ST0095');
  DBMS_OUTPUT.PUT_LINE('Status: ' || v_res);
END;
/
