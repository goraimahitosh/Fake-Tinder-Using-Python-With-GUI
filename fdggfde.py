import mysql.connector

class Tinder:
    def __init__(self):
        #connect to the database
        self.conn=mysql.connector.connect(host="localhost",user="root",password="",database="tinder")

        self.mycursor=self.conn.cursor()
        self.program_menu()

    def program_menu(self):
        program_input=input("""HI! how may i help you
        1. Enter 1 t Register
        2. Enter 2 to Login
        3. Enter anything else to exit""")


        if program_input=="1":
            self.register()
            print("register")
        elif program_input=="2":
            self.login()
            print("login")
        else:
            print("bye")
    def register(self):
        name=input("enter name")
        email=input("enter email")
        password=input("enter password")
        gender=input("enter gender")
        age=input("enter age")
        city=input("enter city")
        hobbies=input("enter hobbies")

        self.mycursor.execute("""INSERT INTO `users`(`user_id`,`name`,`email`,`password`,`gender`,`age`,`city`,`hobbies`) VALUES (NULL,'{}','{}','{}','{}','{}','{}','{}')""".format(name,email,password,gender,age,city,hobbies))
        self.conn.commit()

        print("you have registered successfully")

        self.program_menu()
    def login(self):

        emaillogin=input("enter email")
        passwordlogin=input("enter password")

        self.mycursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(emaillogin,passwordlogin))

        user_info=self.mycursor.fetchall()

        #print(user_info)

        if len(user_info)>0:
            print("welcome user")
            self.current_user_id=user_info[0][0]
            #display next menu
            self.user_menu()

        else:
            print("incorrect email/password")
            self.program_menu()
    def user_menu(self):

        user_input=input("""hi how would you like to proceed?
        1. view all users
        2. view who proposed you
        3. view your proposals
        4. view all matches
        5. logout""")

        if user_input=="1":
            self.view_users()
        elif user_input=="2":
            self.view_proposed()
        elif user_input=="3":
            self.view_proposals()
        elif user_input=="4":
            self.view_matches()
        else:
            self.logout()

    def view_users(self):

        self.mycursor.execute("""SELECT * FROM `users` WHERE `user_id` NOT LIKE '{}'""".format(self.current_user_id))

        all_users=self.mycursor.fetchall()

        for i in all_users:
            print(i[0],"|", i[1],"|", i[4],"|",i[5],"|",i[6],"|",i[7])
            print("----------------------------------------------------------------------")

            input("enter the user id of the user whom you would like to propose")



obj=Tinder()
