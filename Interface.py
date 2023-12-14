import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pywavefront import Wavefront
import numpy as np
from Operacoes import realize_operations
from Structure import Object,draw_object
from layouts import ver2,ver3,ver4,ver5,ver6

sg.theme('DarkBlue13')

def set_viewport(canvas, width, height):
    ax = canvas.figure.add_subplot(111)
    ax.cla()
    canvas.figure.clear()
    ax = canvas.figure.add_subplot(111)
    ax.set_xlim(-width/2, width/2)
    ax.set_ylim(-height/2, height/2)
    ax.set_xticks(np.arange(-width/2, width/2 + 1, 1))
    ax.set_yticks(np.arange(-height/2, height/2 + 1, 1))
    canvas.draw()


def load_obj_file(filename):
    wavefront = Wavefront(filename)
    vertices = np.array(wavefront.vertices)
    edges = np.array(wavefront.mesh_list[0].faces) + 1  # Ajusta os índices das faces
    return Object(vertices, edges)



layout_Sup= [sg.Text("Insira um polígono com:"),sg.Button("2 vértices",key="2VER"),sg.Button("3 vértices",key="3VER"),sg.Button("4 vértices",key="4VER"),sg.Button("5 vértices",key="5VER"),sg.Button("6 vértices",key="6VER")]
layout_dir=[[sg.Text("Dimensão da ViewPort",size=(22,1),justification='c')],[sg.Input(key="-VP_WIDTH-", size=(10, 1)), sg.Text("x",size=(2,1)), sg.Input(key="-VP_HEIGHT-", size=(10, 1))],[sg.Button("Set Viewport",key="SET-VIEW",size=(22,1))], [sg.Button("Load Object",key='LOAD',size=(22,1))], [sg.Button("Transform Object",key='TRANSFORM',size=(22,1))], [sg.Button("Realize Transformation",key='REALIZE',size=(22,1))],[sg.Button("Reset",key='RESET',size=(22,1))],[sg.Exit(size=(22,1))]]
layout_esq=[[sg.Canvas(key="-CANVAS-", size=(600, 600),background_color="#FCFBEF")]]

def createwindow():
        layout= [
        [layout_Sup],
        [sg.Column(layout_esq),sg.VSeparator(),sg.Push(),sg.Column(layout_dir),sg.Push()],
        ]
        return 



def interface(vet_op):
    layout = [
    [layout_Sup],
    [sg.Column(layout_esq),sg.VSeparator(),sg.Push(),sg.Column(layout_dir),sg.Push()],
    ]
    window =  sg.Window("Graphic System", layout = layout, finalize= True, size=(900, 550))
    canvas_elem = window["-CANVAS-"]
    canvas = FigureCanvasTkAgg(plt.figure(), master=canvas_elem.Widget)
    canvas.draw()
    canvas.get_tk_widget().pack(side="top", fill="both", expand=1)
    object_to_display = None
    matrix = np.identity(3)  # Inicializa a matriz de transformação como matriz identidade


    while True:
        event, values = window.read()

        match(event):

            case 'TRANSFORM':
                select = sg.popup_get_text("Escolha a transformação:\n"
                                    "1 - Translação\n"
                                    "2 - Escala\n"
                                    "3 - Cisalhamento\n"
                                    "4 - Reflexão\n"
                                    "5 - Rotação")

                if not select:
                    continue

                match(select):
                    # Entrada dos parâmetros específicos para cada transformação
                    case '1':  # Translação
                        fator1 = float(sg.popup_get_text("Deslocamento em X: "))
                        fator2 = float(sg.popup_get_text("Deslocamento em Y: "))
                    case '2':  # Escala
                        fator1 = float(sg.popup_get_text("Fator de escala em X: "))
                        fator2 = float(sg.popup_get_text("Fator de escala em Y: "))
                    case '3':  # Cisalhamento
                        eixo = sg.popup_get_text("Qual o eixo do cisalhamento(x/y): ")
                        fator1 = float(sg.popup_get_text("Fator de cisalhamento: "))
                        fator2 = 'x' if eixo== 'x' else 'y'
                    case '4':  # Reflexão
                        eixo = sg.popup_get_text("Eixo da reflexão(x/y): ")
                        if eixo == 'x':
                            fator1 = 'x'
                            fator2 = None
                        elif eixo == 'y':
                            fator1 = 'y'
                            fator2 = None
                        else:
                            sg.popup_error("Eixo inválido. Use 'x' ou 'y'.")
                            continue
                    case '5':  # Rotação
                        fator1 = float(sg.popup_get_text("Ângulo da rotação(Em Graus): "))
                        fator2 = None

                vet_op.append([int(select), fator1, fator2])
            case 'SET-VIEW':
                vp_width = float(values["-VP_WIDTH-"])
                vp_height = float(values["-VP_HEIGHT-"])
                set_viewport(canvas, vp_width, vp_height)
                if object_to_display:
                    draw_object(canvas, object_to_display, vp_width, vp_height)

            case 'LOAD':
                obj_file = sg.popup_get_file("Select an OBJ file", file_types=(("OBJ Files", "*.obj"),))
                if obj_file:
                    object_to_display = load_obj_file(obj_file)
                    if values["-VP_WIDTH-"] and values["-VP_HEIGHT-"]:
                        vp_width = float(values["-VP_WIDTH-"])
                        vp_height = float(values["-VP_HEIGHT-"])
                        set_viewport(canvas, vp_width, vp_height)
                        draw_object(canvas, object_to_display, vp_width, vp_height)
                    else:
                        draw_object(canvas, object_to_display, 1, 1)

            case 'RESET':
                canvas.figure.clf()
                canvas.get_tk_widget().pack_forget()
                canvas = FigureCanvasTkAgg(plt.figure(), master=canvas_elem.Widget)
                canvas.draw()
                canvas.get_tk_widget().pack(side="top", fill="both", expand=1)
                object_to_display = None

            case 'REALIZE':
                object_to_display.vertices,vet_op, =realize_operations(vet_op,matrix,object_to_display)
                vp_width = float(values["-VP_WIDTH-"])
                vp_height = float(values["-VP_HEIGHT-"])
                draw_object(canvas, object_to_display, vp_width, vp_height)

            case '2VER'|'3VER'|'4VER'|'5VER'|'6VER':
                match(event):
                    case '2VER':
                        window = ver2()
                    case '3VER':
                        window = ver3()
                    case '4VER':
                        window = ver4()
                    case '5VER':
                        window = ver5()
                    case '6VER':
                        window = ver6()
            case 'CRIAR':
                match(window.Title):
                    case '2 vértices':
                        object_to_display.vertices=[[int(values['x1']),int(values['y1']),1],[int(values['x2']),int(values['y2']),1]]
                        object_to_display.edges= []
                        draw_object(canvas, object_to_display, vp_width, vp_height)     #TENTEI IMPLEMENTAR

                    case '3 vértices':
                        object_to_display.vertices=[[int(values['x1']),int(values['y1']),1],[int(values['x2']),int(values['y2']),1],[int(values['x3']),int(values['y3']),1]]
                        object_to_display.edges= []
                        draw_object(canvas, object_to_display, vp_width, vp_height)     #TENTEI IMPLEMENTAR

                    case '4 vértices':
                        object_to_display.vertices=[[int(values['x1']),int(values['y1']),1],[int(values['x2']),int(values['y2']),1],[int(values['x3']),int(values['y3']),1],[int(values['x4']),int(values['y4']),1]]
                        object_to_display.edges= []
                        draw_object(canvas, object_to_display, vp_width, vp_height)     #TENTEI IMPLEMENTAR

                    case '5 vértices':
                        object_to_display.vertices=[[int(values['x1']),int(values['y1']),1],[int(values['x2']),int(values['y2']),1],[int(values['x3']),int(values['y3']),1],[int(values['x4']),int(values['y4']),1],[int(values['x5']),int(values['y5']),1]]
                        object_to_display.edges= []
                        draw_object(canvas, object_to_display, vp_width, vp_height)     #TENTEI IMPLEMENTAR

                    case '6 vértices':
                        object_to_display.vertices=[[int(values['x1']),int(values['y1']),1],[int(values['x2']),int(values['y2']),1],[int(values['x3']),int(values['y3']),1],[int(values['x4']),int(values['y4']),1],[int(values['x5']),int(values['y5']),1],[int(values['x6']),int(values['y6']),1]]
                        object_to_display.edges= []
                        draw_object(canvas, object_to_display, vp_width, vp_height)     #TENTEI IMPLEMENTAR


            case None:
                break

            case 'Exit':
                break
