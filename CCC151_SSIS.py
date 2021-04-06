#still unfinshed
#undergoing hoping to finished this day

from tkinter import*
import tkinter.ttk as ttk
import csv

SSIS = Tk()
SSIS.geometry("1250x500")
SSIS.title("MSU-IIT SSIS")

#global variables
ssis_csv = "SSIS.csv"
field_names = ["ID Number", "Name", "Course", "Year Level", "Gender"]

def add_student():
    global ssis_csv
    global field_names
    
    with open(ssis_csv, "a") as student_data:
        writer = csv.DictWriter(student_data, fieldnames = field_names)

    writer.writerow({
        "ID Number" : IDnumberVariable.get(),
        "Name" : NameVariable.get(),
        "Course" : CourseVariable.get(),
        "Year Level" : YearlevelVariable.get(),
        "Gender" : GenderVariable.get()
        })
    
#Labels
yellow_bg = Label(SSIS, text = "",
               bg = "yellow3",
               width = 185,
               height = 2
               )
red_bg = Label(SSIS, text = "",
               bg = "maroon",
               width = 185,
               height = 4
               )
black_bg = Label(SSIS, text = "",
               bg = "black",
               width = 185,
               height = 3
               )
school = Label(SSIS, text = "Mindanao State University \n ILIGAN INSTITUTE OF TECHNOLOGY",
                font = ("Times New Roman", 15),
                fg = "white",
                bg = "maroon",
                width = 32,
                height = 2
                )
program = Label(SSIS, text = "Simple Student Information System (SSIS)",
                font = ("Arial Rounded MT Bold", 13),
                fg = "white",
                bg = "black",
                width = 32,
                height = 2
                )
#Buttons
Search = Button(SSIS, text = "Search",
                     font = ("Arial Rounded MT Bold", 12),
                     fg = "black",
                     bg = "goldenrod",
                     )
Display_List = Button(SSIS, text = "Display Students List",
                      font = ("Arial Rounded MT Bold", 12),
                      fg = "black",
                      bg = "goldenrod",
                      #command = display_students
                      )
Add_Student = Button(SSIS, text = "Add Student",
                     font = ("Arial Rounded MT Bold", 12),
                     fg = "black",
                     bg = "goldenrod",
                     command = add_student
                     )
Update_Student = Button(SSIS, text = "Update Student",
                        font = ("Arial Rounded MT Bold", 12),
                        fg = "white",
                        bg = "black"
                        )
Delete_Student = Button(SSIS, text = "Delete",
                        font = ("Arial Rounded MT Bold", 12),
                        fg = "white",
                        bg = "black"
                        )
#Entry
Search_Student_id = Entry(SSIS,
                          text = "Student ID Number",
                          bg = "ghost white",
                          fg = "black",
                          bd = 4,
                          width = 23,
                          font = ("Times New Roman", 10)
                          )
Search_Student_id.insert(0, "ID Number i.e.yyyy-nnnn")

#Positions
yellow_bg.grid(row = 0, column = 0)
red_bg.grid(row = 1, column = 0)
black_bg.grid(row = 2, column = 0)
school.grid(row = 1, column = 0)
program.grid(row = 2, column = 0)
Search_Student_id.place(x=100, y=200)
Search.place(x=250, y=194)
Display_List.place(x=560, y=194)
Add_Student.place(x=980, y=194)
Update_Student.place(x=600, y=350)
Delete_Student.place(x=600, y=400)


SSIS.mainloop()
