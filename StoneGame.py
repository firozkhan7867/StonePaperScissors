from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk, messagebox
import random
import time



class Game():
    def __init__(self, root):
        self.root = root
        self.root.geometry("730x500")
        self.root.title("GAME")

        def hi(event):
            self.new()
        
        
        wel_img = ImageTk.PhotoImage(Image.open("Welcome.png"))
        f1 = Frame(self.root)

        
        


        f1.place(relx=0, rely=0, relwidth=1, relheight=1)

        Welcome = Label(f1,image=wel_img)
        Welcome.place(relx=0,rely=0.04,relwidth=1,relheight=1)
        l1 = Label(f1, text="Stone,Paper and Scissors Game!1",
                   bg="dark blue", fg="white", font=("bold", 20))
        l1.place(relx=0,rely=0,relheight=0.12,relwidth=1)
        b1 = Label(f1, text="Welcome", bg="black", fg="red",
                   font=("Helvetica", 20, "bold italic"))
        b1.place(relx=0.438, rely=0.357)

        end = Label(self.root,text="Press any key......",font=("bold"))
        end.place(relx=0.8,rely=0.95)
        con = True
        
        if con == True:

            self.root.bind('<Key>', hi)
        con = False




        self.root.mainloop()

        
    

    def new(self):
        
        self.root.geometry("830x500")
        self.root.title("GAME")
        stone_img = ImageTk.PhotoImage(Image.open("stone2.png"))
        scissor_img = ImageTk.PhotoImage(Image.open("scissors2.png"))
        paper_img = ImageTk.PhotoImage(Image.open("paper4.png"))

        self.user_choice = None
        self.computer_choice = None

        

        self.USER_SCORE = 0
        self.COMP_SCORE = 0


        def user_choice_option(num):
            sps = {0:"Stone",1:"Paper",2:"Scissors"}
            
            self.user_choice = sps[num]

            # global USER_SCORE
            # global COMP_SCORE
            



            

            n = random.randint(0,2)
            self.computer_choice = sps[n]

            if self.computer_choice != None:
                # stone_2 = Button(self.root, image=stone_img, width=110, height=80,state=DISABLED)
                # stone_2.place(x=600, y=80)

                # scissor_2 = Button(self.root, image=scissor_img,
                #                 width=110, height=80,state=DISABLED)
                # scissor_2.place(x=600, y=200)
        
                # paper_2 = Button(self.root, image=paper_img, width=110, height=80,state=DISABLED)
                # paper_2.place(x=600, y=300)

                if self.computer_choice == sps[0]:
                    stone_2 = Button(self.root, image=stone_img,
                                     width=130, height=100,bg="red")
                    stone_2.place(x=600, y=80)
                    scissor_2 = Button(self.root, image=scissor_img,
                                       width=130, height=100, state=DISABLED)
                    scissor_2.place(x=600, y=240)

                    paper_2 = Button(self.root, image=paper_img,
                                    width=130, height=100, state=DISABLED)
                    paper_2.place(x=600, y=380)



                elif self.computer_choice == sps[1]:
                    paper_2 = Button(self.root, image=paper_img,
                                     width=130, height=100,bg="red")
                    paper_2.place(x=600, y=380)

                    stone_2 = Button(self.root, image=stone_img,
                                     width=130, height=100, state=DISABLED)
                    stone_2.place(x=600, y=80)
                    scissor_2 = Button(self.root, image=scissor_img,
                                       width=130, height=100, state=DISABLED)
                    scissor_2.place(x=600, y=240)


                elif self.computer_choice == sps[2]:
                    scissor_2 = Button(self.root, image=scissor_img,
                                       width=130, height=100,bg="red")
                    scissor_2.place(x=600, y=240)

                    stone_2 = Button(self.root, image=stone_img,
                                     width=130, height=100, state=DISABLED)
                    stone_2.place(x=600, y=80)
                    paper_2 = Button(self.root, image=paper_img,
                                     width=130, height=100, state=DISABLED)
                    paper_2.place(x=600, y=380)


            def l():

                if self.user_choice == sps[0]:
                    stone = Button(self.root, image=stone_img,
                                        width=130, height=100,bg="red",command=lambda: user_choice_option(0))
                    stone.place(x=40, y=80)
                    scissor = Button(self.root, image=scissor_img,
                                     width=130, height=100, command=lambda: user_choice_option(2))
                    scissor.place(x=40, y=240)

                    paper = Button(self.root, image=paper_img,
                                   width=130, height=100, command=lambda: user_choice_option(1))
                    paper.place(x=40, y=380)



                elif self.user_choice == sps[1]:
                    paper = Button(self.root, image=paper_img,
                                        width=130, height=100,bg="red",command=lambda: user_choice_option(1))
                    paper.place(x=40, y=380)

                    stone = Button(self.root, image=stone_img,
                                        width=130, height=100,command=lambda: user_choice_option(0))
                    stone.place(x=40, y=80)
                    scissor = Button(self.root, image=scissor_img,
                                     width=130, height=100, command=lambda: user_choice_option(2))
                    scissor.place(x=40, y=240)


                elif self.user_choice == sps[2]:
                    scissor = Button(self.root, image=scissor_img,
                                     width=130, height=100, bg="red", command=lambda: user_choice_option(2))
                    scissor.place(x=40, y=240)

                    stone = Button(self.root, image=stone_img,
                                   width=130, height=100, command=lambda: user_choice_option(0))
                    stone.place(x=40, y=80)
                    paper = Button(self.root, image=paper_img,
                                   width=130, height=100, command=lambda: user_choice_option(1))
                    paper.place(x=40, y=380)
            
            l()

                

            time.sleep(0.5)


            if self.user_choice == sps[0]:
                if self.computer_choice == sps[2]:
                    print(f'player ! won 1 point')
                    self.USER_SCORE += 1
                elif self.computer_choice == sps[1]:
                    print('computer  won 1 point')
                    print('sorry you lose!!! ')
                    self.COMP_SCORE += 1
                elif self.computer_choice == sps[0]:
                    print('Oppss!! its a tie.')

            if self.user_choice == sps[1]:
                if self.computer_choice == sps[2]:
                    print('computer  won 1 point')
                    print('sorry you lose!!! ')
                    self.COMP_SCORE += 1
                elif self.computer_choice == sps[0]:
                    print(f'player 1 won 1 point')
                    self.USER_SCORE += 1
                elif self.computer_choice == sps[1]:
                    print('Oppss!! its a tie.')

            if self.user_choice == sps[2]:
                if self.computer_choice == sps[0]:
                    print('computer  won 1 point')
                    print('sorry you lose!!! ')
                    self.COMP_SCORE += 1
                elif self.computer_choice == sps[1]:
                    print(f'player 1 won 1 point')
                    self.USER_SCORE += 1
                elif self.computer_choice == sps[2]:
                    print('Oppss!! its a tie.')



            text_area = Text(f1, height=12, width=30, bg="#FFF999")
            text_area.place(x=250, y=100)
            answer = "Player 1 Choice: {uc} \nComputer's Choice : {cc} \n Player1 Score : {u} \n Computer Score : {c} ".format(
                uc=self.user_choice, cc=self.computer_choice, u=self.USER_SCORE, c=self.COMP_SCORE)
            text_area.insert(END, answer)

            if self.USER_SCORE >= 5:
                response = messagebox.askyesno(
                    "Congratulations!! ", "Player 1 has won the game \n Would you like to play again")
                if response == 1:
                    self.new()
                else:
                    self.root.destroy()
            elif self.COMP_SCORE >= 5:
                response = messagebox.askyesno(
                    "Opps  !!   sorry.. ", "Computer  has won the game  \n Would you like to play again")
                if response == 1:
                    self.new()
                else:
                    self.root.destroy()



            

            


            
            




        f1 = Frame(self.root, bg="#F0FF99")
        f1.place(relx=0, rely=0, relwidth=1, relheight=1)

        stone = Button(self.root, image=stone_img, width=130,
                       height=100, command=lambda: user_choice_option(0))
        stone.place(x=40,y=80)

        scissor = Button(self.root, image=scissor_img, width=130,
                         height=100, command=lambda: user_choice_option(2))
        scissor.place(x=40, y=240)

        paper = Button(self.root, image=paper_img, width=130,
                       height=100, command=lambda: user_choice_option(1))
        paper.place(x=40, y=380)
        player1_label = Label(f1, text="Player 1", fg="Blue",
                              bg="#F0FF99", font=("Helvetica", 20, "bold"))
        player1_label.place(x=60,y=20)

        stone_2 = Button(self.root, image=stone_img, width=110, height=80)
        stone_2.place(x=600, y=80)

        scissor_2 = Button(self.root, image=scissor_img,
                           width=110, height=80)
        scissor_2.place(x=600, y=240)
 
        paper_2 = Button(self.root, image=paper_img, width=110, height=80)
        paper_2.place(x=600, y=380)

        player1_label = Label(f1, text="Computer", fg="Blue",
                              bg="#F0FF99", font=("Helvetica", 20, "bold"))
        player1_label.place(x=620, y=20)

        text_area = Text(f1, height=12, width=30, bg="#FFF999")
        text_area.place(x=250, y=100)
        answer = "Player 1 Choice: {uc} \nComputer's Choice : {cc} \n Player1 Score : {u} \n Computer Score : {c} ".format(
            uc=self.user_choice, cc=self.computer_choice, u=self.USER_SCORE, c=self.COMP_SCORE)
        text_area.insert(END, answer)
        
            
        

            

        self.root.mainloop()

root = Tk()
s = Game(root)
root.mainloop()
