import PySimpleGUI as sg


def ver2():
    layout=[
        [sg.Text('Vértice 1:'), sg.Text("X:"),sg.Input(key='x1',size=(10,1)),sg.Text("Y:"),sg.Input(key='y1',size=(10,1))],
        [sg.Text('Vértice 2:'), sg.Text("X:"),sg.Input(key='x2',size=(10,1)),sg.Text("Y:"),sg.Input(key='y2',size=(10,1))],
        [sg.Text('Ordem de Ligação dos Vértices:'),sg.Input(key='e1',size=(10,1)),sg.Input(key='e2',size=(10,1))],
        [sg.Button('Criar',key='CRIAR')],
    ]
    return sg.Window('2 vértices',layout=layout)

def ver3():
    layout=[
        [sg.Text('Vértice 1:'), sg.Text("X:"),sg.Input(key='x1',size=(10,1)),sg.Text("Y:"),sg.Input(key='y1',size=(10,1))],
        [sg.Text('Vértice 2:'), sg.Text("X:"),sg.Input(key='x2',size=(10,1)),sg.Text("Y:"),sg.Input(key='y2',size=(10,1))],
        [sg.Text('Vértice 3:'), sg.Text("X:"),sg.Input(key='x3',size=(10,1)),sg.Text("Y:"),sg.Input(key='y3',size=(10,1))],
        [sg.Text('Ordem de Ligação dos Vértices:'),sg.Input(key='e1',size=(10,1)),sg.Input(key='e2',size=(10,1)),sg.Input(key='e3',size=(10,1))],
        [sg.Button('Criar',key='CRIAR')],
    ]
    return sg.Window('3 vértices',layout=layout)

def ver4():
    layout=[
       [sg.Text('Vértice 1:'), sg.Text("X:"),sg.Input(key='x1',size=(10,1)),sg.Text("Y:"),sg.Input(key='y1',size=(10,1))],
        [sg.Text('Vértice 2:'), sg.Text("X:"),sg.Input(key='x2',size=(10,1)),sg.Text("Y:"),sg.Input(key='y2',size=(10,1))],
        [sg.Text('Vértice 3:'), sg.Text("X:"),sg.Input(key='x3',size=(10,1)),sg.Text("Y:"),sg.Input(key='y3',size=(10,1))],
        [sg.Text('Vértice 4:'), sg.Text("X:"),sg.Input(key='x4',size=(10,1)),sg.Text("Y:"),sg.Input(key='y4',size=(10,1))],
        [sg.Text('Ordem de Ligação dos Vértices:'),sg.Input(key='e1',size=(10,1)),sg.Input(key='e2',size=(10,1)),sg.Input(key='e3',size=(10,1)),sg.Input(key='e4',size=(10,1))],
        [sg.Button('Criar',key='CRIAR')],
    ]
    return sg.Window('4 vértices',layout=layout)

def ver5():
    layout=[
        [sg.Text('Vértice 1:'), sg.Text("X:"),sg.Input(key='x1',size=(10,1)),sg.Text("Y:"),sg.Input(key='y1',size=(10,1))],
        [sg.Text('Vértice 2:'), sg.Text("X:"),sg.Input(key='x2',size=(10,1)),sg.Text("Y:"),sg.Input(key='y2',size=(10,1))],
        [sg.Text('Vértice 3:'), sg.Text("X:"),sg.Input(key='x3',size=(10,1)),sg.Text("Y:"),sg.Input(key='y3',size=(10,1))],
        [sg.Text('Vértice 4:'), sg.Text("X:"),sg.Input(key='x4',size=(10,1)),sg.Text("Y:"),sg.Input(key='y4',size=(10,1))],
        [sg.Text('Vértice 5:'), sg.Text("X:"),sg.Input(key='x5',size=(10,1)),sg.Text("Y:"),sg.Input(key='y5',size=(10,1))],
        [sg.Text('Ordem de Ligação dos Vértices:'),sg.Input(key='e1',size=(10,1)),sg.Input(key='e2',size=(10,1)),sg.Input(key='e3',size=(10,1)),sg.Input(key='e4',size=(10,1)),sg.Input(key='e5',size=(10,1))],
        [sg.Button('Criar',key='CRIAR')],
    ]
    return sg.Window('5 vértices',layout=layout)

def ver6():
    layout=[
        [sg.Text('Vértice 1:'), sg.Text("X:"),sg.Input(key='x1',size=(10,1)),sg.Text("Y:"),sg.Input(key='y1',size=(10,1))],
        [sg.Text('Vértice 2:'), sg.Text("X:"),sg.Input(key='x2',size=(10,1)),sg.Text("Y:"),sg.Input(key='y2',size=(10,1))],
        [sg.Text('Vértice 3:'), sg.Text("X:"),sg.Input(key='x3',size=(10,1)),sg.Text("Y:"),sg.Input(key='y3',size=(10,1))],
        [sg.Text('Vértice 4:'), sg.Text("X:"),sg.Input(key='x4',size=(10,1)),sg.Text("Y:"),sg.Input(key='y4',size=(10,1))],
        [sg.Text('Vértice 5:'), sg.Text("X:"),sg.Input(key='x5',size=(10,1)),sg.Text("Y:"),sg.Input(key='y5',size=(10,1))],
        [sg.Text('Vértice 6:'), sg.Text("X:"),sg.Input(key='x6',size=(10,1)),sg.Text("Y:"),sg.Input(key='y6',size=(10,1))],
        [sg.Text('Ordem de Ligação dos Vértices:'),sg.Input(key='e1',size=(10,1)),sg.Input(key='e2',size=(10,1)),sg.Input(key='e3',size=(10,1)),sg.Input(key='e4',size=(10,1)),sg.Input(key='e5',size=(10,1)),sg.Input(key='e6',size=(10,1))],
        [sg.Button('Criar',key='CRIAR')],
    ]

    return sg.Window('6 vértices',layout=layout)