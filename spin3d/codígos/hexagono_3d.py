import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Função para criar a matriz de rotação em torno do eixo X
def rotation_x(angle):
    return np.array([
        [1, 0, 0],
        [0, np.cos(angle), -np.sin(angle)],
        [0, np.sin(angle), np.cos(angle)]
    ])

# Função para criar a matriz de rotação em torno do eixo Y
def rotation_y(angle):
    return np.array([
        [np.cos(angle), 0, np.sin(angle)],
        [0, 1, 0],
        [-np.sin(angle), 0, np.cos(angle)]
    ])

# Função para criar a matriz de rotação em torno do eixo Z
def rotation_z(angle):
    return np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle), np.cos(angle), 0],
        [0, 0, 1]
    ])

# Define as coordenadas dos vértices de um prisma hexagonal
def create_hexa():
    return np.array([
        [1, 0, 0],        # Base inferior
        [0.5, 0.87, 0],
        [-0.5, 0.87, 0],
        [-1, 0, 0],
        [-0.5, -0.87, 0],
        [0.5, -0.87, 0],
        [1, 0, 1],        # Base superior
        [0.5, 0.87, 1],
        [-0.5, 0.87, 1],
        [-1, 0, 1],
        [-0.5, -0.87, 1],
        [0.5, -0.87, 1],
    ])

# Define as arestas que conectam os vértices do prisma hexagonal
def hexa_edges():
    return [
        [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0],  # Base inferior
        [6, 0], [7, 1], [8, 2], [9, 3], [10, 4], [11, 5],  # Conexões verticais
        [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 6]  # Base superior
    ]

# Função de animação que atualiza a rotação do prisma
def animate(i, hexa_vertices, edges, ax):
    angle = np.radians(i)  # Converte o ângulo de graus para radianos
    matrix_rotation = rotation_z(angle)  # Aplica a rotação no eixo Z

    # Calcula as novas posições dos vértices após a rotação
    rotated_vertices = np.dot(hexa_vertices, matrix_rotation.T)

    # Limpa e redefine o gráfico
    ax.clear()
    ax.set_title("HEXÁGONO GIRATÓRIO", color='white')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)
    ax.set_box_aspect([1, 1, 1])  # Define proporções iguais para os eixos
    ax.set_facecolor('black')  # Define a cor de fundo do gráfico como preto
    fig.patch.set_facecolor('black')  # Define a cor de fundo da figura como preto

    # Desenha as arestas do prisma com base nos vértices rotacionados
    for edge in edges:
        ax.plot([rotated_vertices[edge[0], 0], rotated_vertices[edge[1], 0]],
                [rotated_vertices[edge[0], 1], rotated_vertices[edge[1], 1]],
                [rotated_vertices[edge[0], 2], rotated_vertices[edge[1], 2]], color='white')
    
    return ax,

# Inicializa os vértices e arestas do prisma
hexa_vertices = create_hexa()
edges = hexa_edges()

# Cria a figura e o gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Configura a animação para rotacionar o prisma
ani = FuncAnimation(fig, animate, frames=np.arange(0, 360, 2),
                    fargs=(hexa_vertices, edges, ax), interval=50)

# Mostra o gráfico animado
plt.show()

        