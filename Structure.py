import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pywavefront import Wavefront


class Object:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges


def draw_object(canvas, obj, vp_width, vp_height):
    ax = canvas.figure.add_subplot(111)
    ax.clear()

    # Desenhar o objeto no subplot
    for edge in obj.edges:
        x = [obj.vertices[edge[0] - 1][0], obj.vertices[edge[1] - 1][0]]
        y = [obj.vertices[edge[0] - 1][1], obj.vertices[edge[1] - 1][1]]
        ax.plot(x, y, marker='o', linestyle='-', color='b', markersize=8)

    # Adiciona os pontos
    x_points = [vertex[0] for vertex in obj.vertices]
    y_points = [vertex[1] for vertex in obj.vertices]
    ax.plot(x_points + [x_points[0]], y_points + [y_points[0]], marker='o', linestyle='-', color='b', markersize=8)
    ax.set_facecolor('#FCFBEF')
    ax.set_xlim(-vp_width/2, vp_width/2)
    ax.set_ylim(-vp_height/2, vp_height/2)
    canvas.draw()

