from tkinter import *
from tkinter import ttk
import Compare
    
root = Tk()

EVENTS = ['100m', '200m', '400m', '800m', '1600m', '3200m']
YEARS = ['2014', '2015', '2016', '2017', '2018']
GRADES = ['9', '10', '11', '12']

def convert():
    if inputMenVar.get():
        inputGender = 'Men'
    else:
        inputGender = 'Women'
    if outputMenVar.get():
        outputGender = 'Men'
    else:
        outputGender = 'Women'
    
    inputGenderEvent = inputGender + inputEvent.get()
    outputGenderEvent = outputGender + outputEvent.get()
    inputData = []
    outputData = []
    for i in range(YEARS.index(inputYear1.get()), YEARS.index(inputYear2.get()) + 1):
        inputData.append(inputGenderEvent + YEARS[i])
    
    for i in range(YEARS.index(outputYear1.get()), YEARS.index(outputYear2.get()) + 1):
        outputData.append(outputGenderEvent + YEARS[i])
    
    min = inputMinutes.get() or 0;
    sec = inputSeconds.get() or 0.0;
    
    result = Compare.compare(inputData, outputData, 'AthleticData.db', int(min) * 60 + float(sec), int(inputGrade1.get()), int(inputGrade2.get()), int(outputGrade1.get()), int(outputGrade2.get()))
    ResultMinVar.set(str(int(result[0] // 60)))
    outputSeconds = result[0] % 60
    if outputSeconds < 10:
        ResultSecVar.set('0' + str(outputSeconds))
    else:
        ResultSecVar.set(str(round(outputSeconds, 2)))
    percentile.set(str(round(result[1], 6) * 100))

inputEventLabel = Label(root, text="1. Input Event:")
inputEventLabel.grid(sticky=W, padx = 4)
root.title("Not Mercier Score")

#---Men/Women Option---#
input1 = Frame(root)

inputMenVar = BooleanVar()
inputMen = Checkbutton(input1, variable = inputMenVar, text="Men")
inputMen.pack(side=LEFT)
inputWomenVar = BooleanVar()
inputWomen = Checkbutton(input1, variable = inputWomenVar, text="Women")
inputWomen.pack(side=LEFT)
inputMen.config(command = lambda: (inputWomenVar.set(False), inputMenVar.set(True)))
inputWomen.config(command = lambda: (inputMenVar.set(False), inputWomenVar.set(True)))
inputMen.select()

input1.grid(row=0, column=1, sticky=W)

#---Input Time and Input Event---#
input2 = Frame(root)

inputEvent = StringVar()
inputEvent.set("800m")
inputOptions = OptionMenu(input2, inputEvent, *EVENTS)
inputOptions.pack(side=TOP, anchor=W)

inputMinVar = StringVar()
inputSecVar = StringVar()
inputMinutes = Entry(input2, text="m", width = 8, textvariable = inputMinVar)
inputSeconds = Entry(input2, text="s", width = 9, textvariable = inputSecVar)

inputMinutes.pack(side=LEFT, pady = 3, padx=1)
inputColon = Label(input2, text=":", width = 1)
inputColon.pack(side=LEFT, pady = 3)
inputSeconds.pack(side=LEFT, pady = 3)

input2.grid(row=1, column=0, sticky=W, padx = 8)


#---Input Grade Range Frame---#
inputGradeRange = Frame(root)
Label(inputGradeRange, text="Grade Range:").pack(side=TOP, anchor = W, padx = 5)
inputGrade1 = StringVar()
inputGrade1.set("9")
inputGrade2 = StringVar()
inputGrade2.set("12")
gradeOptions1 = OptionMenu(inputGradeRange, inputGrade1, '9', '10', '11', '12')
gradeOptions1.pack(side=LEFT, padx = 4)
Label(inputGradeRange, text="->").pack(side=LEFT)
gradeOptions2 = OptionMenu(inputGradeRange, inputGrade2, '9', '10', '11', '12')
gradeOptions2.pack(side=LEFT, padx = 4)
inputGradeRange.grid(row = 2, column = 0, sticky = W, pady = 5)


#---Input Time Frame (that's a pun)---#
inputYearRange = Frame(root)
Label(inputYearRange, text="Time frame: ").pack(side=TOP, anchor = W, padx = 5)
inputYear1 = StringVar()
inputYear1.set("2018")
inputYear2 = StringVar()
inputYear2.set("2018")
gradeOptions1 = OptionMenu(inputYearRange, inputYear1, '2014', '2015', '2016', '2017', '2018').pack(side=LEFT, padx = 4)
Label(inputYearRange, text="->").pack(side=LEFT)
yearOptions2 = OptionMenu(inputYearRange, inputYear2, '2014', '2015', '2016', '2017', '2018').pack(side=LEFT, padx = 4)
inputYearRange.grid(row = 2, column = 1, sticky = W, pady = 5)

separator = ttk.Separator(root, orient=HORIZONTAL)
separator.grid(row = 3, sticky = EW, columnspan = 2)

#----Output Section----#

Label(root, text="2. Output Event:").grid(row = 4, sticky=W, padx = 4, pady=4)

#---Men/Women Option (Output)---#
output1 = Frame(root)

outputMenVar = BooleanVar()
outputMen = Checkbutton(output1, variable = outputMenVar, text="Men")
outputMen.pack(side=LEFT)
outputWomenVar = BooleanVar()
outputWomen = Checkbutton(output1, variable = outputWomenVar, text="Women")
outputWomen.pack(side=LEFT)
outputMen.config(command = lambda: (outputWomenVar.set(False), outputMenVar.set(True)))
outputWomen.config(command = lambda: (outputMenVar.set(False), outputWomenVar.set(True)))
outputMen.select()

output1.grid(row=4, column=1, sticky=W, pady = 4)

#---Output Event Selection---#
outputEvent = StringVar()
outputEvent.set("1600m")
outputOptions = OptionMenu(root, outputEvent, *EVENTS)
outputOptions.grid(row = 5, sticky = W, padx = 4)

#---Output Grade Range Frame---#
outputGradeRange = Frame(root)
Label(outputGradeRange, text="Grade Range:").pack(side=TOP, anchor = W, padx = 5)
outputGrade1 = StringVar()
outputGrade1.set("9")
outputGrade2 = StringVar()
outputGrade2.set("12")
gradeOptions1 = OptionMenu(outputGradeRange, outputGrade1, '9', '10', '11', '12').pack(side=LEFT, padx = 4)
Label(outputGradeRange, text="->").pack(side=LEFT)
gradeOptions2 = OptionMenu(outputGradeRange, outputGrade2, '9', '10', '11', '12').pack(side=LEFT, padx = 4)
outputGradeRange.grid(row = 6, column = 0, sticky = W, pady = 5)


#---Output Time Frame---#
outputYearRange = Frame(root)
Label(outputYearRange, text="Time frame: ").pack(side=TOP, anchor = W, padx = 5)
outputYear1 = StringVar()
outputYear1.set("2018")
outputYear2 = StringVar()
outputYear2.set("2018")
yearOptions1 = OptionMenu(outputYearRange, outputYear1, '2014', '2015', '2016', '2017', '2018').pack(side=LEFT, padx = 4)
Label(outputYearRange, text="->").pack(side=LEFT)
yearOptions2 = OptionMenu(outputYearRange, outputYear2, '2014', '2015', '2016', '2017', '2018').pack(side=LEFT, padx = 4)
outputYearRange.grid(row = 6, column = 1, sticky = W, pady = 5)

#---Result---#
resultSeparator = ttk.Separator(root, orient=HORIZONTAL)
resultSeparator.grid(row = 7, sticky = EW, columnspan = 2)

convertButton = Button(root, text="Get Result", command = convert, bg='sandy brown')
convertButton.grid(row = 8, padx = 4, sticky=W)
Label(root, text="----------->").grid(row = 8, sticky = E)

resultFrame = Frame(root)

ResultMinVar = StringVar()
ResultSecVar = StringVar()
resultMinutes = Entry(resultFrame, width = 8, textvariable = ResultMinVar)
resultSeconds = Entry(resultFrame, width = 10, textvariable = ResultSecVar)

resultMinutes.pack(side=LEFT, pady = 3, padx=3)
Label(resultFrame, text=":", width = 1).pack(side=LEFT, pady = 6)
resultSeconds.pack(side=LEFT, pady = 3, padx = 3)
resultFrame.grid(row = 8, column = 1, padx = 3, pady = 4, sticky=W)

percentileFrame = Frame(root)

percentile = StringVar()
resultPercentile = Entry(percentileFrame, width = 8, textvariable = percentile)
resultPercentile.pack(side = LEFT)
Label(percentileFrame, text="%").pack(side=LEFT)

percentileFrame.grid(row = 9, column = 1, pady = 3, sticky = W, padx = 5)
Label(root, text="-------------->").grid(row = 9, sticky = W)
Label(root, text="In the top").grid(row = 9, sticky = E)


root.mainloop()
