class student():
    
    my_list = ["dev","bhavya","indrajeet","harshil","bhargav"]
    sr = [101,102,103,104,105]
    
    def create_new(self):
        name = input("Enter A New Student Name:- ")
        sr = input("Enter New SR Number :-")
        
        if name.isalpha():
            name = str(name)
            if name in self.my_list:
                print("Student Name Already Exists")
            else:
                self.my_list.append(name)
                print("Student Name Added Successfully")
                print(self.my_list)
                if sr.isdigit():
                    sr = int(sr)
                    if sr in self.sr:
                        print("SR Number Already Exists")
                    else:
                        self.sr.append(sr)
                        print("SR Number Added Successfully")
                        print(self.sr)
                else:
                    print("sr number should be a number")
        else:
            print("name should contain only letters")
       

            
    def display_student(self):
        print(self.my_list)
            
a=student()
a.create_new()
a.display_student()

