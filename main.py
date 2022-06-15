import time

from DataPrep import DataPrep
from Processing import Processing
import tkinter as tk
import tkinter.messagebox
import math

window = tk.Tk()
window.resizable(False, False)
opt = []

# 0 is for label, subsequent are options...
coreData = [["1. What is your assigned gender at birth?", "0. Female", "1. Male"],
            ["2. Have you been diagnosed with High Blood Pressure?", "1. Yes", "2. No"],
            ["3. Do you have Diabetes?", "1. No", "2. Pre-Diabetes", "3. Yes"],
            ["4. Have you been diagnosed with a Stroke?", "1. Yes", "2. No"],
            ["5. Have you ever smoked or vaped more than 100 times?", "1. Yes", "2. No"],
            ["6. Do you consume more 1 or more servings of fruits per day?", "1. Yes", "2. No"],
            ["7. Do you consume more 1 or more servings of vegetables per day?", "1. Yes", "2. No"],
            ["8. Do you consume more than 10 alcoholic beverages per week?", "1. Yes", "2. No"],
            ["9. On a scale of one to five, what is your general health?", "1", "2", "3", "4", "5"],
            ["10. How many days in the past month has your mental health been down (1 to 30)?"],
            ["11. How many days in the past month has your physical health been down (1 to 30)?"],
            ["12. What is your BMI (1 to 45)?"],
            ["13. How old are you (15 to 100)?"]]

# On button click
def go():
    submit_button['state'] = 'disabled'

    time.sleep(1)

    if finalVal():
        vals = {
            'sex': clean(variable_sex.get()),
            'BP': clean(variable_BP.get()),
            'diabetes': clean(variable_Diabetes.get()),
            'stroke': clean(variable_Stroke.get()),
            'smoke': clean(variable_Smoke.get()),
            'fruit': clean(variable_Fruit.get()),
            'vegetable': clean(variable_Vegetable.get()),
            'alcohol': clean(variable_Alcohol.get()),
            'genhealth': clean(variable_GenHealth.get()),
            'mental': int(variable_Mental.get()),
            'physical': int(variable_Physical.get()),
            'BMI': int(variable_BMI.get()),
            'age': math.floor((int(variable_Age.get()) / 5) - 2)
        }

        data = DataPrep("data.csv")

        for j in range(0, 3):
            Processing(data.NextSet(5000), "#" + str(j) + " - " + str(5000))

        if Processing.Final >= 2:
            tkinter.messagebox.showinfo(message="You have a high chance of heart problems.")
        else:
            tkinter.messagebox.showinfo(message="You have a low chance of heart problems.")
    else:
        tkinter.messagebox.showerror(message="Please check your values, make sure they are numeric, within the range specified.")

    submit_button['state'] = 'active'

def clean(val):
    return int(val[0])

def finalVal():
    if variable_Mental.get().isdigit():
        if 1 > int(variable_Mental.get()) > 30:
            return False
    else:
        return False

    if variable_Physical.get().isdigit():
        if 1 > int(variable_Physical.get()) > 30:
            return False
    else:
        return False

    if variable_BMI.get().isdigit():
        if 1 > int(variable_BMI.get()) > 45:
            return False
    else:
        return False

    if variable_Age.get().isdigit():
        if 15 > int(variable_Age.get()) > 100:
            return False
    else:
        return False

    return True

def validateText(name, max):
    if name == '.!frame10.!entry' or name == '.!frame11.!entry': #text_Mental/Physical
        name = "Mental/Physical not between 1 and 30"
        if max.isdigit():
            if 1 <= int(max) <= 30:
                validText = True
            else:
                validText = False
        else:
            validText = False
    elif name == '.!frame12.!entry': #text_BMI
        name = "BMI is not in between 1 and 45"
        if max.isdigit():
            if 1 <= int(max) <= 45:
                validText = True
            else:
                validText = False
        else:
            validText = False
    elif name == '.!frame13.!entry': #text_Age
        name = "Age is not between 15 and 100"
        if max.isdigit():
            if 15 <= int(max) <= 100:
                validText = True
            else:
                validText = False
        else:
            validText = False
    else:
        validText = False

    if validText:
        submit_button['state'] = 'active'
    elif max == "":
        submit_button['state'] = 'disabled'
    else:
        tkinter.messagebox.showerror(message=name)
        submit_button['state'] = 'disabled'

    #refresh validation
    window.after_idle(lambda: text_Mental.config(validate='focusout'))
    window.after_idle(lambda: text_Age.config(validate='focusout'))
    window.after_idle(lambda: text_BMI.config(validate='focusout'))
    window.after_idle(lambda: text_Physical.config(validate='focusout'))

# Register Validation Function
valid_func = window.register(validateText)

#Title
tk.Label(text="Heart Disease Predictor", font=("Arial", 18)).pack(padx=30, pady=25)

# Sex 0: Female, 1: Male
frame_sex = tk.Frame(window)
tk.Label(frame_sex, text=coreData[0][0]).pack(side='left')
variable_sex = tk.StringVar(frame_sex)
variable_sex.set(coreData[0][1])  # default value
tk.OptionMenu(frame_sex, variable_sex, *coreData[0][1::]).pack(side='left')
frame_sex.pack(fill='x', padx=15, pady=5)

# High BP Yes/No
frame_BP = tk.Frame(window)
tk.Label(frame_BP, text=coreData[1][0]).pack(side='left')
variable_BP = tk.StringVar(frame_BP)
variable_BP.set(coreData[1][1])  # default value
tk.OptionMenu(frame_BP, variable_BP, *coreData[1][1::]).pack(side='left')
frame_BP.pack(fill='x', padx=15, pady=5)

# Diabetes No/Pre/Yes
frame_Diabetes = tk.Frame(window)
tk.Label(frame_Diabetes, text=coreData[2][0]).pack(side='left')
variable_Diabetes = tk.StringVar(frame_Diabetes)
variable_Diabetes.set(coreData[2][1])  # default value
tk.OptionMenu(frame_Diabetes, variable_Diabetes, *coreData[2][1::]).pack(side='left')
frame_Diabetes.pack(fill='x', padx=15, pady=5)

# Stroke Yes/No
frame_Stroke = tk.Frame(window)
tk.Label(frame_Stroke, text=coreData[3][0]).pack(side='left')
variable_Stroke = tk.StringVar(frame_Stroke)
variable_Stroke.set(coreData[3][1])  # default value
tk.OptionMenu(frame_Stroke, variable_Stroke, *coreData[3][1::]).pack(side='left')
frame_Stroke.pack(fill='x', padx=15, pady=5)

# Smoke/Vape >100 in life time Yes/No
frame_Smoke = tk.Frame(window)
tk.Label(frame_Smoke, text=coreData[4][0]).pack(side='left')
variable_Smoke = tk.StringVar(frame_Smoke)
variable_Smoke.set(coreData[4][1])  # default value
tk.OptionMenu(frame_Smoke, variable_Smoke, *coreData[4][1::]).pack(side='left')
frame_Smoke.pack(fill='x', padx=15, pady=5)

# Fruit consume more than 1 serving per day Yes/No
frame_Fruit = tk.Frame(window)
tk.Label(frame_Fruit, text=coreData[5][0]).pack(side='left')
variable_Fruit = tk.StringVar(frame_Fruit)
variable_Fruit.set(coreData[5][1])  # default value
tk.OptionMenu(frame_Fruit, variable_Fruit, *coreData[5][1::]).pack(side='left')
frame_Fruit.pack(fill='x', padx=15, pady=5)

# Vegetable consume more than 1 serving per day Yes/No
frame_Vegetable = tk.Frame(window)
tk.Label(frame_Vegetable, text=coreData[6][0]).pack(side='left')
variable_Vegetable = tk.StringVar(frame_Vegetable)
variable_Vegetable.set(coreData[6][1])  # default value
#variable_Vegetable.trace('w', check)
tk.OptionMenu(frame_Vegetable, variable_Vegetable, *coreData[6][1::]).pack(side='left')
frame_Vegetable.pack(fill='x', padx=15, pady=5)

# Alcohol consume more than 10 drinks in a week Yes/No
frame_Alcohol = tk.Frame(window)
tk.Label(frame_Alcohol, text=coreData[7][0]).pack(side='left')
variable_Alcohol = tk.StringVar(frame_Alcohol)
variable_Alcohol.set(coreData[7][1])  # default value
tk.OptionMenu(frame_Alcohol, variable_Alcohol, *coreData[7][1::]).pack(side='left')
frame_Alcohol.pack(fill='x', padx=15, pady=5)

# GenHealth 1 to 5
frame_GenHealth = tk.Frame(window)
tk.Label(frame_GenHealth, text=coreData[8][0]).pack(side='left')
variable_GenHealth = tk.StringVar(frame_GenHealth)
variable_GenHealth.set(coreData[8][1])  # default value
tk.OptionMenu(frame_GenHealth, variable_GenHealth, *coreData[8][1::]).pack(side='left')
frame_GenHealth.pack(fill='x', padx=15, pady=5)

# Mental Health 1 to 30
frame_Mental = tk.Frame(window)
tk.Label(frame_Mental, text=coreData[9][0]).pack(side='left')
variable_Mental = tk.StringVar()
text_Mental  = tk.Entry(frame_Mental, validate='focusout', validatecommand=(valid_func, '%W', '%P'), textvariable=variable_Mental)
text_Mental.pack()
frame_Mental.pack(fill='x', padx=15, pady=5)

# Physical Health 1 to 30
frame_Physical = tk.Frame(window)
tk.Label(frame_Physical, text=coreData[10][0]).pack(side='left')
variable_Physical = tk.StringVar()
text_Physical  = tk.Entry(frame_Physical, validate='focusout', validatecommand=(valid_func, '%W', '%P'), textvariable=variable_Physical)
text_Physical.pack()
frame_Physical.pack(fill='x', padx=15, pady=5)

# BMI
frame_BMI = tk.Frame(window)
tk.Label(frame_BMI, text=coreData[11][0]).pack(side='left')
variable_BMI = tk.StringVar()
text_BMI  = tk.Entry(frame_BMI, validate='focusout', validatecommand=(valid_func, '%W', '%P'), textvariable=variable_BMI)
text_BMI.pack()
frame_BMI.pack(fill='x', padx=15, pady=5)

# Age
frame_Age = tk.Frame(window)
tk.Label(frame_Age, text=coreData[12][0]).pack(side='left')
variable_Age = tk.StringVar()
text_Age  = tk.Entry(frame_Age, validate='focusout', validatecommand=(valid_func, '%W', '%P'), textvariable=variable_Age)
text_Age.pack()
frame_Age.pack(fill='x', padx=15, pady=5)

submit_button = tk.Button(text="Submit", command=lambda: go())
submit_button.pack(padx=15, pady=10, side='bottom')

tk.mainloop()



