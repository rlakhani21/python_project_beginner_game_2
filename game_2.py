# no of guesses 9
import random 
from random import * 
import tkinter
from tkinter import *
from tkinter import messagebox

n = randint(1,100) #take random number between 1 to 100 
total_attempts = 10
while (total_attempts):
    inp = int(input("Guess the number between 1 to 100 : "))
    if inp > n:
        print("Number is greater than Original Number")
        total_attempts = total_attempts - 1
        continue
    if inp < n:
        print("Number is less than Original Number")
        total_attempts = total_attempts - 1
        continue
    if inp == n: 
        total_attempts = total_attempts -1 
        score = 9 - total_attempts
        messagebox.showinfo("Congratulations ","You successfully guessed the number in  "+ str(score) + " attempts" )
        break
    
if total_attempts == 0 :
        messagebox.showinfo('Error','Gameover')
        print('Game Over')

