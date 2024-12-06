import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Função para criar a matriz de rotação no eixo X
def rotation_matrix_x(angle):
    return np.array([
        [1, 0, 0],
        [0, np.cos(angle), -np.sin(angle)],
        [0, np.sin(angle), np.cos(angle)]
    ])

# Função para criar a matriz de rotação no eixo Y
def rotation_matrix_y(angle):
    return np.array([
        [np.cos(angle), 0, np.sin(angle)],
        [0, 1, 0],
        [-np.sin(angle), 0, np.cos(angle)]
    ])

# Função para criar a matriz de rotação no eixo Z
def rotation_matrix_z(angle):
    return np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle), np.cos(angle), 0],
        [0, 0, 1]
    ])

# Função para definir os vértices de um cubo unitário
def create_cube():
    # Vértices do cubo (8 vértices de um cubo)
    return np.array([
        [-1, -1, -1],
        [1, -1, -1],
        [1, 1, -1],
        [-1, 1, -1],
        [-1, -1, 1],
        [1, -1, 1],
        [1, 1, 1],
        [-1, 1, 1]
    ])

# Definir as conexões entre os vértices para formar as arestas
def cube_edges():
    return [
        [0, 1], [1, 2], [2, 3], [3, 0],  # Faces inferior
        [4, 5], [5, 6], [6, 7], [7, 4],  # Faces superior
        [0, 4], [1, 5], [2, 6], [3, 7]   # Conectando as faces superior e inferior
    ]

# Função para animar o cubo girando
def animate(i, cube_vertices, edges, ax):
    angle = np.radians(i)  # Convertendo o ângulo para radianos
    rotation_matrix = rotation_matrix_z(angle)  # Girando no eixo Z (pode mudar para X ou Y)
    
    rotated_vertices = np.dot(cube_vertices, rotation_matrix.T)  # Aplicando a rotação aos vértices
    
    ax.clear()  # Limpa a tela
    ax.set_title("CUBO GIRATÓRIO", color='white')  # Título com cor branca
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)
    ax.set_box_aspect([1, 1, 1])  # Garante que a proporção seja igual nos 3 eixos

    # Mudando o fundo para preto
    ax.set_facecolor('black')  # Fundo preto para a área de plotagem
    fig.patch.set_facecolor('black')  # Fundo preto para a figura inteira

    # Mudando a cor das linhas para branco
    for edge in edges:
        ax.plot([rotated_vertices[edge[0], 0], rotated_vertices[edge[1], 0]],
                [rotated_vertices[edge[0], 1], rotated_vertices[edge[1], 1]],
                [rotated_vertices[edge[0], 2], rotated_vertices[edge[1], 2]], color='white')

    return ax,

# Criar os vértices e arestas do cubo
cube_vertices = create_cube()
edges = cube_edges()

# Configurar o gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Criar a animação
ani = FuncAnimation(fig, animate, frames=np.arange(0, 360, 2), 
                    fargs=(cube_vertices, edges, ax), interval=50)

# Exibir a animação
plt.show()


      