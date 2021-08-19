import operator
#{a:1000,b:900,c:800,d:700,e:600}
def readStudentDetails():
    print("Enter the number of students:")
    numberOfStudents=int(input())
    studentRecord={}
    for students in range(0,numberOfStudents):
        print("Enter the name of the student:")
        name=input()
        print("Enter the marks scored by the student:")
        marks=int(input())
        studentRecord[name]=marks
    return studentRecord


def rankStudents(studentRecord):
    sortedStudentRecords=sorted(studentRecord.items(),key=operator.itemgetter(1),reverse=True)
    #print(sortedStudentRecords)
    print("{} has scored FIRST rank, scoring {} marks.".format(sortedStudentRecords[0][0],format(sortedStudentRecords[0][1])))
    print("{} has scored SECOND rank, scoring {} marks.".format(sortedStudentRecords[1][0],format(sortedStudentRecords[1][1])))
    print("{} has scored THIRD rank, scoring {} marks.".format(sortedStudentRecords[2][0],format(sortedStudentRecords[2][1])))
    return sortedStudentRecords

def rewardStudents(sortedStudentRecords):
    




studentRecord=readStudentDetails()
rankStudents(studentRecord)
reward=(500,300,100)
