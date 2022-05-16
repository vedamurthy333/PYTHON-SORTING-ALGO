from tkinter import *
from tkinter import ttk
import random
from bubbleSort import bubble_sort
from quickSort import quick_sort
from mergeSort import merge_sort
from insertionSort import  insertionSort
root = Tk()
# masterWindow = Tk()
root.title('Sorting Algorithm Visualisation')
#masterWindow.title('Sorting Algorithm Visualisation')
# screen_width = 1600
# screen_height = 900
root.maxsize(1600,900)
# window_width = 1600 * .01
# window_height = 900 * .04
# window_start_x = (screen_width/2)
# window_start_y = (screen_height/2)
# masterWindow.geometry("%dx%d+%d+%d" % (window_width, window_height, window_start_x, window_start_y))
#masterWindow.geometry("+%d+%d" % (window_start_x, window_start_y))
root.config(bg='black')
#masterWindow.config(bg='black',)
Grid.rowconfigure(root,0,weight=1)
Grid.columnconfigure(root,0,weight=1)
Grid.rowconfigure(root,1,weight=1)
selected_alg = StringVar()
data = []
def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 650
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 290
    spacing = 20
    normalizedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 440
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    root.update_idletasks()


def Generate():
    global data
    
    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))
    
    drawData(data, ['red' for x in range(len(data))])

def StartAlgorithm():
    global data
    if not data: return

    if algMenu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, speedScale.get())
    
    elif algMenu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, speedScale.get())

    elif algMenu.get() == 'Merge Sort':
        merge_sort(data, drawData, speedScale.get())

    elif algMenu.get() == 'Insertion Sort':
        insertionSort(data, drawData, speedScale.get())
    
    drawData(data, ['green' for x in range(len(data))])

UI_frame = Frame(root, width = 1100, height= 650, bg= 'grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width= 1100, height= 650, bg= 'white')
canvas.grid( row=1, column=0,  padx=10, pady=5)


Label(UI_frame, text="Algorithm : ", bg='grey').grid(row=0, column=0, padx=5, pady=5)
algMenu = ttk.Combobox(UI_frame, textvariable= selected_alg, values=['Bubble Sort', 'Merge Sort', 'Insertion Sort', 'Quick Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.1, to=5.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed [s]")
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text="Start", command=StartAlgorithm, bg='red').grid(row=0, column=3, padx=5, pady=5)

#Row[1]
sizeEntry = Scale(UI_frame, from_=4, to=25, resolution=1, orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Min Value")
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value")
maxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, text="Generate", command=Generate, bg='white').grid(row=1, column=3, padx=5, pady=5)

root.mainloop()