#Dice roller made by michael green for my ttrpg, functions in basic python
#works  by taking in user input as a txt file and closing, upon relaunch
#users may select that their stats have been initalized. Once done the
#window will open a fully functional dice roller that can display rolls
#and allows users to track their teamwork dice pool as well.
from tkinter import *
import random

root = Tk()

root.title("Persona Stat Tracker and Roller")
root.geometry('1366x768')

result = []


def hide_button(widget): 
    widget.pack_forget()

def save_file():
    with open("persona_save.txt", 'w') as file:
        for i in result:
            file.write(i)
            file.write('\n')
    file.close()
    root.destroy()

def final_check():
    res = result
    lbl.configure(text = res)
    button2 = Button(root,text = "Click here if the info you've provided is correct", fg = 'purple',command = save_file)
    button2.grid(column=1, row = 10)    

def clicked_weapons():
    weapons = txt.get()
    weapons = weapons.split(',')
    for i in weapons:
        result.append(i)
    print(result)
    final_check()


def clicked_points():
    res = "Please enter your weapon names and accuracy, no spaces, seperated by commas"
    lbl.configure(text = res)
    points = txt.get()
    result.append(points)
    button2 = Button(root,text = "click here when done", fg = 'purple',command = clicked_weapons)
    button2.grid(column=1, row = 9)

def clicked_name():
    res = "Please enter your max teamwork points"
    lbl.configure(text = res)
    player = txt.get()
    name = player
    result.append(name)
    button2 = Button(root,text = "click here when done", fg = 'purple',command = clicked_points)
    button2.grid(column=1, row = 8)

def clicked_stats():
    res = "Please enter your name"
    lbl.configure(text = res)
    insert = txt.get()
    insert.split(',')
    for i in insert:
        if(i != ',') :
            result.append(i)
    button2 = Button(root, text= "click here when done", fg ="green", command = clicked_name)
    button2.grid(column = 1, row = 7)  

def clicked_start():
    res = "Please enter stats in order Strength, Agility, Endurance, Luck, Magic, Charm with no spaces and seperated by commas"
    lbl.configure(text = res)
    button2 = Button(root, text= "click here when done", fg ="blue", command = clicked_stats)
    button2.grid(column = 1, row = 6)  

btn =Button(root, text = "Intialize Stats", fg= "red", command= clicked_start)
btn.grid(column=1, row=5)



def stats_show():
    root.destroy()
    new_window = Toplevel()
    new_window.title("Persona Stat Tracker and Roller")
    new_window.geometry('1366x768')
    results_roll = Label(new_window,text ="", font=('Times', 20))
    results_roll.grid(column = 9, row = 5)

    teamwork_points_left = Label(new_window,text ="", font=('Times', 20))
    teamwork_points_left.grid(column = 9, row = 8)

    def dice_roll_d20(stat):
        roll = random.randint(1,20) + stat
        roll_results = 'Roll result is:'+ str(roll)
        results_roll.config(text=roll_results)

    def dice_roll_d100():
        roll = random.randint(1,100)
        roll_results = 'Roll result is:'+ str(roll)
        results_roll.config(text=roll_results)

    stats = []
    stre = 'Strength: '
    agl = 'Agility: '
    end = 'Endurance: '
    lck = 'Luck: '
    mgc = 'Magic: '
    chm = 'Charm: '
    tp = 'Teamwork points: '
    ac1 = 'Accuracy weapon 1: '
    ac2 = 'Accuracy weapon 2: ' 
    with open("persona_save.txt", 'r') as file:
        for line in file:
            line = line.replace('\n','')
            stats.append(line)
    strength = int(stats[0])
    agility = int(stats[1])
    endurance = int(stats[2])
    luck = int(stats[3])
    magic = int(stats[4])
    charm = int(stats[5])
    teamwork_points = int(stats[7])
    accuracy_1 = int(stats[9])
    accuracy_2 = int(stats[11])

    global temp_teamwork
    temp_teamwork = teamwork_points
    teamwork_points_left.config(text=str(teamwork_points))

    def teamwork_points_adjust(teamwork_points):
        if teamwork_points == 0:
            return
        teamwork_points = teamwork_points-1
        teamwork = str(teamwork_points)
        teamwork_points_left.config(text=teamwork)
        global temp_teamwork
        temp_teamwork = temp_teamwork -1

    def teamwork_points_reset():
        global temp_teamwork
        temp_teamwork = teamwork_points
        teamwork_points_full = temp_teamwork
        teamwork = str(teamwork_points_full)
        teamwork_points_left.config(text=teamwork)   


    stats = Label(new_window, text = "Stats:", font=('Times', 15))
    stats.grid(column = 0, row = 0)

    stre = stre + str(strength)
    stat1 = Label(new_window,text = stre, font=('Times', 20))
    stat1.grid(column = 5, row = 2)
    strength_roll =Button(new_window, text = "Strength Check", fg= "black", command= lambda: dice_roll_d20(strength))
    strength_roll.grid(column=8, row=2)     

    agl = agl + str(agility)
    stat2 = Label(new_window,text = agl, font=('Times', 20))
    stat2.grid(column = 5, row = 3)
    agility_roll =Button(new_window, text = "Agility Check", fg= "purple", command= lambda: dice_roll_d20(agility))
    agility_roll.grid(column=8, row=3) 

    end = end + str(endurance)
    stat3 = Label(new_window,text = end, font=('Times', 20))
    stat3.grid(column = 5, row = 4)
    Endurance_roll =Button(new_window, text = "Endurance Check", fg= "green", command= lambda: dice_roll_d20(endurance))
    Endurance_roll.grid(column=8, row=4)

    lck = lck + str(luck)
    stat4 = Label(new_window,text = lck, font=('Times', 20))
    stat4.grid(column = 5, row = 5)
    luck_roll =Button(new_window, text = "Luck Check", fg= "orange", command= lambda: dice_roll_d20(luck))
    luck_roll.grid(column=8, row=5)    

    mgc = mgc + str(magic)
    stat5 = Label(new_window,text = mgc, font=('Times', 20))
    stat5.grid(column = 5, row = 6)
    magic_roll =Button(new_window, text = "Magic Check", fg= "blue", command= lambda: dice_roll_d20(magic))
    magic_roll.grid(column=8, row=6)  

    chm = chm + str(charm)
    stat6 = Label(new_window,text = chm, font=('Times', 20))
    stat6.grid(column = 5, row = 7)
    charm_roll =Button(new_window, text = "Charm Check", fg= "red", command= lambda: dice_roll_d20(charm))
    charm_roll.grid(column=8, row=7)      

    tp = tp + str(teamwork_points)
    stat7 = Label(new_window,text = tp, font=('Times', 20))
    stat7.grid(column = 5, row = 8)
    spend_teamwork =Button(new_window, text = "Spend", fg= "black", command= lambda: teamwork_points_adjust(temp_teamwork))
    spend_teamwork.grid(column=8, row=8)
    reset_teamwork =Button(new_window, text = "Reset", fg= "black", command= lambda: teamwork_points_reset())
    reset_teamwork.grid(column=7, row=8)       

    ac1 = ac1 + str(accuracy_1)
    stat8 = Label(new_window,text = ac1, font=('Times', 20))
    stat8.grid(column = 5, row = 9)
    weapon_roll =Button(new_window, text = "Weapon attack", fg= "black", command= lambda: dice_roll_d100())
    weapon_roll.grid(column=8, row=9)       

    ac2 = ac2 + str(accuracy_2)
    stat9 = Label(new_window,text = ac2, font=('Times', 20))
    stat9.grid(column = 5, row = 10)
    gun_roll =Button(new_window, text = "Gun attack", fg= "black", command= lambda: dice_roll_d100())
    gun_roll.grid(column=8, row=10)     





button_main =Button(root, text = "click here if stats are already initialized", fg= "black", command= stats_show)
button_main.grid(column=3, row=5)




lbl = Label(root,text ="Is this working?",font=('Times', 24),wraplength=600)
lbl.grid(column=10, row=10)

txt = Entry(root, width=15)
txt.grid(column =0, row =10)

root.mainloop()