#chris gose
#student performance calculator
#pm class



#asks for student info
print("================================")
print("STUDENT PERFORMANCE ANALYZER")
print("================================")
name = input("what is the students name: ")
gradelevel = int(input("what is the students grade level: "))
assignmentavg = float(input("what is the students assignment average: "))
quizavg = float(input("what is the students quiz average: "))
testavg = float(input("what is the students test average: "))
attendance = float(input("what is the students attendance percentage: "))
missing = int(input("how many missing assingments does the student have: "))

#calculate overgrade
def calculategrade(assingmentavg, quizavg, testavg,):
    overallgrade = (assingmentavg * .30) + (quizavg * .30) + (testavg * .40)
    print("overall grade: " + str(overallgrade))
    return overallgrade

 

# calculate lettergrade
def lettergrade(overall):
    if overall >= 90:
        print("letter grade: A")
        return "A"
    elif overall >= 80:
        print("letter grade: B")
        return "B"
    elif overall >= 70:
        print("letter grade: C")
        return "C"
    elif overall >= 60:
        print("letter grade: D")
        return "D"
    else:
        print("letter grade: F")
        return "F"
    
# calculate attendance
def attendancee(attendancepct):
    if attendancepct >= 95:
        print("excellent attendance")
    elif attendancepct >= 90:
        print("good attendance")
    elif attendancepct >= 80:
        print("attendance warning")
    else:
        print("poor attendance")

#calculate missing assingment
def assignmentstatus(missing):
    if missing == 0:
        print("excellent")
    elif missing <= 2:
        print("good")
    elif missing <= 4:
        print("warning")
    else:
        print("critical")


#check eligibilty
def checkeligibillity(overall, attendancepct, missing):
    if overall >= 70:
        if attendancepct >= 90:
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


# checks if high honors
def checkhighhonors(overall, attendancepct, missing):
    if overall >= 90:
        if attendancepct >= 95:
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

# checks if good standing
def checkgoodstanding(overall, attendancepct):
    if overall >= 70 and attendancepct >= 90:
        print("good standing: yes")
    else:
        print("good standing: no")

#checks if support is needed
def checksupport(overall, attendancepct):
    if overall < 70 or attendancepct < 80:
        print("additional support: recomended")
    else:
        print("additional support: not needed")


#checks login
username = input("enter username: ")
pin = int(input("enter pin:"))
if username == "student":
    if pin == 1234:
        print("login successfull")
    else:
        print("login failed: incorrect pin")
else:
    print("login failed: incorrect username")

#checks what grade level and sends a message
def gradelevelmssg(gradelevel):
    if gradelevel == 9 :
        print("welcome to freshman year")
    elif gradelevel == 10:
        print("keep building your skills ")
    elif gradelevel == 11:
        print("keep pushing")
    elif gradelevel == 12:
        print("finish strong")
    else:
        print("invalid grade level")
# finds out what strongest catagory is 
def strongestcatagory(assignmentavrg, quizavrg,testavrg):
        if assignmentavrg > quizavrg and assignmentavrg > testavrg:
            print("strongest catagory: assignments")
        elif quizavrg > assignmentavrg and quizavrg > testavrg:
            print("strongest catagory: quiz")
        else:
            print("strongest catagory: tests")


# student summary
print("==========================")
print("student summary")
print("==========================")

print("student: " + name )
print("grade level: " + str(gradelevel))
gradelevelmssg(gradelevel)


overallgrade = calculategrade(assignmentavg,quizavg,testavg)

lettergraderesult = lettergrade(overallgrade)

attendanceoverall = attendancee(attendance)
assignmentstatus(missing)
checkeligibillity(overallgrade, attendance, missing)
checkhighhonors(overallgrade, attendance, missing)
checkgoodstanding(overallgrade, attendance)
checksupport(overallgrade, attendance)
strongestcatagory(assignmentavg, quizavg, testavg)

print("==========================")