import PySimpleGUI as sg
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def update_figure(data):
    axes = fig.axes
    x = [i[0] for i in data]
    y = [int(i[1]) for i in data]
    axes[0].plot(x, y, 'r-')
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack()

def input_check(indut_data):
    for symb in new_value:
        if not symb in avalaible_symbols:
            return False
        else:
            return True
            
sg.theme('DarkTeal6')
table_content = []
avalaible_symbols = ('x', ' ', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '-', '+', '*',
                     '^', 'exp', '(', ')', 'sqrt')
x = 0
layout = [
    [sg.Table(headings = ['Observation', 'Result'],
              values = table_content,
              expand_x = True,
              hide_vertical_scroll=True,
              key = '-TABLE-')],
    [sg.Input(key = '-INPUT-', expand_x = True), sg.Button('Submit')],
    [sg.Canvas(key = '-CANVAS-')]

]

window = sg.Window('Graph App', layout, finalize=True)

fig = Figure(figsize = (5,4))
fig.add_subplot(111).plot([],[])
figure_canvas_agg = FigureCanvasTkAgg(fig, window['-CANVAS-'].TKCanvas)
figure_canvas_agg.draw()
figure_canvas_agg.get_tk_widget().pack()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Submit':
        new_value = values["-INPUT-"]
        if input_check(new_value):
            for elem in new_value:
                if elem == 'x':
                    pass
                elif elem.isdigit():
                    pass
                elif elem == (' ', '(', ')', '+', '*', '-'):
                    pass
            table_content.append([len(table_content) +1 , float(new_value)])
            window['-TABLE-'].update(table_content)
            window['-INPUT-'].update('')
            update_figure(table_content)

window.close()
