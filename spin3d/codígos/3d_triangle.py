import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Função para criar a matriz de rotação em torno do eixo X
def matrix_rotation_x(angle):
    return np.array([
        [1, 0, 0],
        [0, np.cos(angle), -np.sin(angle)],
        [0, np.sin(angle), np.cos(angle)]
    ])

# Função para criar a matriz de rotação em torno do eixo Y
def matrix_rotation_y(angle):
    return np.array([
        [np.cos(angle), 0, np.sin(angle)],
        [0, 1, 0],
        [-np.sin(angle), 0, np.cos(angle)]
    ])

# Função para criar a matriz de rotação em torno do eixo Z
def matrix_rotation_z(angle):
    return np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle), np.cos(angle), 0],
        [0, 0, 1]
    ])

# Define os vértices de uma pirâmide triangular
def create_triangle():
    return np.array([
        [-1, -1, 0],  # Base inferior esquerda
        [1, -1, 0],   # Base inferior direita
        [1, 1, 0],    # Base superior direita
        [-1, 1, 0],   # Base superior esquerda
        [0, 0, 1]     # Ponto do topo
    ])

# Define as arestas que conectam os vértices da pirâmide
def triangle_edges():
    return [
        [0, 1], [1, 2], [2, 3], [3, 0],  # Arestas da base
        [0, 4], [1, 4], [2, 4], [3, 4]   # Arestas conectando a base ao topo
    ]

# Função de animação para rotacionar a pirâmide
def animate(i, triangle_vertices, edges, ax):
    angle = np.radians(i)  # Converte o ângulo de graus para radianos
    matrix_rotation = matrix_rotation_z(angle)  # Rotação em torno do eixo Z

    # Aplica a rotação aos vértices da pirâmide
    rotated_vertices = np.dot(triangle_vertices, matrix_rotation.T)

    # Limpa e redefine o gráfico
    ax.clear()
    ax.set_title("PIRÂMIDE GIRATÓRIA", color='white')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)
    ax.set_box_aspect([1, 1, 1])  # Define proporções iguais para os eixos
    ax.set_facecolor('black')  # Fundo preto do gráfico
    fig.patch.set_facecolor('black')  # Fundo preto da figura

    # Desenha as arestas da pirâmide
    for edge in edges:
        ax.plot([rotated_vertices[edge[0], 0], rotated_vertices[edge[1], 0]],
                [rotated_vertices[edge[0], 1], rotated_vertices[edge[1], 1]],
                [rotated_vertices[edge[0], 2], rotated_vertices[edge[1], 2]], color='white')
    return ax,

# Inicializa os vértices e arestas da pirâmide
triangle_vertices = create_triangle()
edges = triangle_edges()

# Cria a figura e o gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Configura a animação para rotacionar a pirâmide
ani = FuncAnimation(fig, animate, frames=np.arange(0, 360, 2),
                    fargs=(triangle_vertices, edges, ax), interval=50)

# Mostra o gráfico animado
plt.show()
