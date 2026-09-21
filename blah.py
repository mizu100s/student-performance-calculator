#chris gose
#student performance calculator
#pm class

print("================================")
print("STUDENT PERFORMANCE ANALYZER")
print("================================")
name = input("what is the students name: ")
grade = int(input("what is the students grade level: "))
assignmentavg = float(input("what is the students assignment average: "))
quizavg = float(input("what is the students quiz average: "))
testavg = float(input("what is the students test average: "))
attendance = float(input("what is the students attendance percentage: "))
missing = int(input("how many missing assingments does the student have: "))


def calculategrade(assingmentavrg, quizavrg, testavrg):
    assingmentavrg = assignmentavg * .30
    quizavrg = quizavg * .30
    testavrg = testavg * .40 
    overall = assingmentavrg + quizavrg + testavrg
    


def lettergrade(overall):
    if overall >= 90:
        print("A")
    elif overall >= 80:
        print("B")
    elif overall >= 70:
        print("C")
    elif overall >= 60:
        print("D")
    else:
        print("F")

def attendance(attendance):
    if attendance >= 95:
        print("excellent attendance")
    elif attendance >= 90:
        print("good attendance")
    elif attendance >= 80:
        print("attendance warning")
    else:
        print("poor attendance")

def assignmentstatus(missing):
    if missing <= 0:
        print("excellent")
    elif missing >= 1:
        print("good")
    elif missing >= 3:
        print("warning")
    else:
        print("critical")

def checkeligibillity(overall, attendancee,missing):
    if overall >= 70:
        if attendance >= 90:
            if missing <= 2:
                print("academic eligibility: eligible")
                print("student passes all three requirements")
            else:
                print("academic eligibility: not eligible")
                print("reason: too many missing assignments")
        else:
            print("academic eligibility: not eligible")
            print("reason: overall attendance is too low")
    else:
        print("academic eligibillity: not eligible")
        print("reason: overall grade is too low ")

def checkhighhonors(overall, attendance,missing):
    if overall >= 90:
        if attendance >= 95:
            if missing == 0:
                print("high honors: yes ")
                print("requirements met")
            else:
                print("high honors: no")
                print("reason: student has missing assingmnets")
        else:
            print("high honors: no")
            print("reason: attendance requirement not met")
    else:
        print("high honors: no")
        print("reason: grade requirement not met")


def checkgoodstanding(overall, attendance):
    if overall >= 70 and attendance >= 90:
        print("good standing: yes")
    else:
        print("good standing: no")

def checksupport(overall,attendance):
    if overall < 70 or attendance < 80:
        print("additional support: recomended")
    else:
        print("additional support: not needed")

username = input("enter username: ")
pin = int(input("enter pin:"))
if username == "student":
    if pin == "1234":
        print("login successfull")
    else:
        ("login failed: incorrect pin")
else:
    ("login failed: incorrect username")

def gradelevelmssg(grade):
    if grade == 9 :
        print("welcome to freshman year")
    elif grade == 10:
        print("keep building your skills ")
    elif grade == 11:
        print("keep pushing")
    elif grade == 12:
        print("finish strong")
    else:
        print("invalid grade level")

    