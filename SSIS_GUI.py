from tkinter import*
import tkinter.ttk as ttk
import csv

SSIS = Tk()
SSIS.geometry("1250x640")
SSIS.title("MSU-IIT SSIS")

#global variables
ssis_csv = "SSIS.csv"
field_names = ["ID Number", "Name", "Course", "Year Level", "Gender"]
idnumber_entry = ""
name_entry = ""
course_entry = ""
yearlevel_entry = ""
gender_entry = ""
TreeView = ""
greetings1 = ""
Search_Student_id = ""

#functions
def my_treeview():
    global ssiv_csv
    global fieldnames
    global TreeView


    #Style
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", background = "goldenrod", foreground = "goldenrod", fieldbackground = "goldenrod")
    style.map("Treeview", background=[("selected", "maroon")])

    #Treeview
    TreeView = ttk.Treeview(SSIS)

    #Columns
    TreeView["columns"] = field_names

    #Columns Format
    TreeView.column("#0", stretch = NO, width=0)
    TreeView.column("ID Number", anchor = W, width = 150)
    TreeView.column("Name", anchor = W, width = 150)
    TreeView.column("Course", anchor = W, width = 150)
    TreeView.column("Year Level", anchor = W, width = 150)
    TreeView.column("Gender", anchor = W, width = 150)

    #Headings
    TreeView.heading("#0", anchor = W)
    TreeView.heading("ID Number", text = "ID Number", anchor = W)
    TreeView.heading("Name", text = "Name", anchor = W)
    TreeView.heading("Course", text = "Course", anchor = W)
    TreeView.heading("Year Level", text = "Year Level", anchor = W)
    TreeView.heading("Gender", text = "Gender", anchor = W)


    TreeView.place(x = 430, y = 210)

def display_data():
    global greetings1
    my_treeview()
    
    with open(ssis_csv, 'r') as display:
        display1 = csv.reader(display)

        next(display1)
        delete_all()

        for line in display1:
            TreeView.insert(parent='', index='end', iid = line[0], text='',
                           values=(line[0], line[1],line[2],line[3],line[4]))

    Update_Student = Button(SSIS, text = "Update",
                            font = ("Arial Rounded MT Bold", 12),
                            fg = "white",
                            bg = "maroon",
                            bd = 4
                            )
    Delete_Student = Button(SSIS, text = "Delete",
                            font = ("Arial Rounded MT Bold", 12),
                            fg = "white",
                            bg = "maroon",
                            bd = 4,
                            command = remove_one
                            )
    Update_Student.place(x=1000, y=445)
    Delete_Student.place(x=1100, y=445)
    greetings1.destroy()
    studentList = Label(SSIS, text = "MSU-IIT STUDENTS LIST",
                font = ("Arial Rounded MT Bold", 20),
                fg = "black",
                width = 20,
                height = 1
                )
    studentList.place(x = 640, y = 170)

def delete_all():
    my_treeview()
    for record in TreeView.get_children():
        TreeView.delete(record)

def add_student():
    global ssis_csv
    
    flag = 0
    with open(ssis_csv, 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            if idnumber_entry.get() == row[0]:
                flag += 1
    if flag<1 and idnumber_entry.get()!="":
        with open(ssis_csv, 'a', newline='') as file:
                reader = csv.DictWriter(file,
                                        fieldnames=("ID Number", "Name", "Course", "Year Level", "Gender"),
                                        lineterminator='\n'
                                        )
                reader.writerow({
                    'ID Number': idnumber_entry.get(),
                    'Name': name_entry.get(),
                    'Year Level': yearlevel_entry.get(),
                    'Course': course_entry.get(),
                    'Gender': gender_entry.get()
                    })
    display_data()
        
def remove_one():
    global ssis_csv
    trees = list()
    branch = TreeView.focus()
    with open(ssis_csv, 'r') as read_file:
        reader = csv.reader(read_file)
        for row in reader:
            trees.append(row)
            if row[0] == branch:
                trees.remove(row)
    with open(ssis_csv, 'w', newline='') as write_file:
        writer = csv.writer(write_file)
        writer.writerows(trees)
    display_data()

def search():
    global ssis_csv
    global TreeView
    global Search_Student_id
    global greetings1

    my_treeview()
    
    TreeView.delete(*TreeView.get_children())
    word = Search_Student_id.get().title()
    with open(ssis_csv, 'r') as display:
        display2 = csv.reader(display)
        if Search_Student_id.get():
            for i in display2:
                if word in i:
                    TreeView.insert('', 'end', values = i)
        else:
            for i in display2:
                TreeView.insert('', 'end', values = i)
            error = Label(SSIS, text = "Sorry",
                          font = ("Arial Rounded MT Bold", 20),
                          fg = "black",
                          width = 20,
                          height = 1
                          )
            error.place(x = 640, y = 500)
                
        Search_Student_id.delete(0, 'end')
    greetings1.destroy()   
    
def add_student_widget():
    global idnumber_entry, name_entry, course_entry, yearlevel_entry, gender_entry
    global greetings1
    
    #labels
    addStudent = Label(SSIS, text = "Add Student",
                font = ("Arial Rounded MT Bold", 20),
                fg = "black",
                width = 15,
                height = 1
                )
    id_number = Label(SSIS, text = "ID Number:",
                font = ("Arial Rounded MT Bold", 13),
                fg = "white",
                bg = "black",
                width = 13,
                height = 1
                )
    name = Label(SSIS, text = "Full Name:",
                font = ("Arial Rounded MT Bold", 13),
                fg = "white",
                bg = "black",
                width = 13,
                height = 1
                )
    course = Label(SSIS, text = "Course:",
                font = ("Arial Rounded MT Bold", 13),
                fg = "white",
                bg = "black",
                width = 13,
                height = 1
                )
    year_level = Label(SSIS, text = "Year Level:",
                font = ("Arial Rounded MT Bold", 13),
                fg = "white",
                bg = "black",
                width = 13,
                height = 1
                )
    gender = Label(SSIS, text = "Gender:",
                font = ("Arial Rounded MT Bold", 13),
                fg = "white",
                bg = "black",
                width = 14,
                height = 1
                )

    #entry
    idnumber_entry = Entry(SSIS,
                           bg = "ghost white",
                           fg = "black",
                           bd = 4,
                           width = 25,
                           font = ("Times New Roman", 10)
                           )
    idnumber_entry.insert(0, "ID Number i.e.yyyy-nnnn")
    name_entry = Entry(SSIS,
                           bg = "ghost white",
                           fg = "black",
                           bd = 4,
                           width = 25,
                           font = ("Times New Roman", 10)
                           )
    course_entry = Entry(SSIS,
                           bg = "ghost white",
                           fg = "black",
                           bd = 4,
                           width = 25,
                           font = ("Times New Roman", 10)
                           )
    yearlevel_entry = Entry(SSIS,
                           bg = "ghost white",
                           fg = "black",
                           bd = 4,
                           width = 25,
                           font = ("Times New Roman", 10)
                           )
    gender_entry = Entry(SSIS,
                           bg = "ghost white",
                           fg = "black",
                           bd = 4,
                           width = 25,
                           font = ("Times New Roman", 10)
                           )

    #buttons
    Confirm = Button(SSIS, text = "Confirm",
                     font = ("Arial Rounded MT Bold", 12),
                     fg = "white",
                     bg = "maroon",
                     bd = 4,
                     command = add_student
                     )
    
    #positions
    addStudent.place(x = 875, y = 575)
    id_number.place(x = 429, y = 512)
    name.place(x = 579, y = 512)
    course.place(x = 729, y = 512)
    year_level.place(x = 879, y = 512)
    gender.place(x = 1029, y = 512)
    idnumber_entry.place(x = 428, y = 540)
    name_entry.place(x = 578, y = 540)
    course_entry.place(x = 728, y = 540)
    yearlevel_entry.place(x = 878, y = 540)
    gender_entry.place(x = 1028, y = 540)
    Confirm.place(x = 1095, y = 575)

    greetings1.destroy()

    
#Labels
yellow_bg = Label(SSIS, text = "",
               bg = "yellow3",
               width = 185,
               height = 2
               )
maroon_bg = Label(SSIS, text = "",
               bg = "maroon",
               width = 185,
               height = 4
               )
black_bg = Label(SSIS, text = "",
               bg = "black",
               width = 185,
               height = 3
               )
black2_bg = Label(SSIS, text = "",
               bg = "black",
               width = 50,
               height = 50
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
greetings2 = Label(SSIS, text = "Hello! \n What can I do for you?",
                font = ("Arial Rounded MT Bold", 13),
                fg = "white",
                bg = "black",
                width = 20,
                height = 2
                )
greetings1 = Label(SSIS, text = "WELCOME!",
                font = ("Arial Rounded MT Bold", 80),
                fg = "yellow3",
                bg = "maroon",
                width = 10,
                height = 2
                )

#Buttons
Search = Button(SSIS, text = "Search",
                     font = ("Arial Rounded MT Bold", 12),
                     fg = "black",
                     bg = "goldenrod",
                     bd = 4,
                     command = search
                     )
Display_List = Button(SSIS, text = "Display Students List",
                      font = ("Arial Rounded MT Bold", 12),
                      fg = "black",
                      bg = "goldenrod",
                      bd = 4,
                      command = display_data
                      )
Add_Student = Button(SSIS, text = "Add Student",
                     font = ("Arial Rounded MT Bold", 12),
                     fg = "black",
                     bg = "goldenrod",
                     bd = 4,
                     command = add_student_widget
                     )

#Entry
Search_Student_id = Entry(SSIS,
                          bg = "ghost white",
                          fg = "black",
                          bd = 4,
                          width = 25,
                          font = ("Times New Roman", 10)
                          )
Search_Student_id.insert(0, "ID Number i.e.yyyy-nnnn")

#Positions
yellow_bg.grid(row = 0, column = 0)
maroon_bg.grid(row = 1, column = 0)
black_bg.grid(row = 2, column = 0)
black2_bg.place(x=0, y=155)
school.grid(row = 1, column = 0)
program.grid(row = 2, column = 0)
greetings2.place(x = 63, y = 200)
greetings1.place(x = 480, y = 255)
Search_Student_id.place(x = 95, y = 270)
Search.place(x = 138, y = 300)
Display_List.place(x = 85, y = 360)
Add_Student.place(x = 120, y = 420)


SSIS.mainloop()
