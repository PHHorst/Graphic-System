from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pywavefront import Wavefront
import numpy as np
import math

def calcCG(vertices):
    X=[]
    Y=[]
    for i in range(len(vertices)):
        X.append(vertices[i][0])        
        Y.append(vertices[i][1])
    cgX = float (np.mean(X))
    cgY = float (np.mean(Y))
    return cgX,cgY


def apply_translation(matrix, tx, ty):
    translation_matrix = np.array([[1, 0, tx],
                                   [0, 1, ty],
                                   [0, 0, 1]])
    matrix = np.dot( matrix,translation_matrix)
    return matrix

  #Aplica Escala
def apply_scale(matrix, sx, sy):
    scale_matrix = np.array([[sx, 0, 0],
                             [0, sy, 0],
                             [0, 0, 1]])
    result_matrix = np.dot(matrix,scale_matrix)
    return result_matrix

    #Aplica Reflexão
def apply_reflection(matrix, axis):
    if axis == 'x':
        reflection_matrix = np.array([[-1, 0, 0],
                                      [0, 1, 0],
                                      [0, 0, 1]])
    elif axis == 'y':
        reflection_matrix = np.array([[1, 0, 0],
                                      [0, -1, 0],
                                      [0, 0, 1]])
    else:
        print("Eixo inválido. Use 'x' ou 'y'.")

    if axis in ['x', 'y']:
        result_matrix = np.dot(matrix,reflection_matrix)
        return result_matrix

    #Aplica Cisalhamento
def apply_shear(matrix, factor,axis):
    if axis == 'x':
        shear_matrix = np.array([[1, factor, 0],
                                 [0, 1, 0],
                                 [0, 0, 1]])
    elif axis == 'y':
        shear_matrix = np.array([[1, 0, 0],
                                 [factor, 1, 0],
                                 [0, 0, 1]])
    else:
        print("Eixo inválido. Use 'x' ou 'y'.")

    if axis in ['x', 'y']:
        result_matrix = np.dot( matrix,shear_matrix)

    return result_matrix

    #Aplica Rotação
def apply_rotation(matrix, angle):
    # Converter o ângulo para radianos
    radian_angle = math.radians(angle)

    # Calcular coseno e seno do ângulo
    cos_theta = math.cos(radian_angle)
    sin_theta = math.sin(radian_angle)

    # Criar a matriz de rotação
    rotation_matrix = np.array([[cos_theta, -sin_theta, 0],
                                [sin_theta, cos_theta, 0],
                                [0, 0, 1]])

    result_matrix = np.dot(matrix,rotation_matrix)
    return result_matrix

  #Identifica a transformação no vetor e aplica na matriz base
def apply_transform(matrix,vet):
  if (vet[0])==1:
    matrix = apply_translation(matrix,vet[1],vet[2])
  if (vet[0])==2:
    matrix = apply_scale(matrix,vet[1],vet[2])
  if (vet[0])==3:
    matrix = apply_shear(matrix,vet[1],vet[2])
  if (vet[0])==4:
    matrix = apply_reflection(matrix,vet[1])
  if (vet[0])==5:
    matrix = apply_rotation(matrix,vet[1])

  return matrix


def realize_operations(vet_op,matrix,object_to_display):
    vet_op.reverse()
    X,Y=calcCG(object_to_display.vertices)
    vet_op.append([1,-X,-Y])
    matrix=apply_translation(matrix,X,Y)
    for i in range(len(vet_op)):
        matrix = apply_transform(matrix,vet_op[i])

    #print(object_to_display.vertices,"------ Antes\n")
    for i in range(len(object_to_display.vertices)):
       vet_aux=object_to_display.vertices[i]
       vet_aux[2]=1
       vet_aux=np.reshape(vet_aux,(3,1))
       vet_aux= np.dot(matrix,vet_aux)
       vet_aux=np.reshape(vet_aux,(1,3))
       object_to_display.vertices[i]=vet_aux
       
    vet_op=[]
    return object_to_display.vertices,vet_op




 