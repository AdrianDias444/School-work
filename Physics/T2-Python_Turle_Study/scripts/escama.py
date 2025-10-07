import turtle
import random
import math

# Parâmetros do autômato celular
GRID_SIZE = 12  # Grade pequena para rapidez
ITERATIONS = 15  # Menos iterações
W = 0.6  # Inibidor ajustado para mais manchas
INNER_RADIUS = 3
OUTER_RADIUS = 6
INITIAL_DENSITY = 0.5  # Densidade maior para mais pontos

# Inicializa grade
random.seed(42)
grid = [[1 if random.random() < INITIAL_DENSITY else 0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def count_neighbors(x, y, radius):
    count = 0
    r2 = radius ** 2
    for i in range(max(0, x - radius), min(GRID_SIZE, x + radius + 1)):
        for j in range(max(0, y - radius), min(GRID_SIZE, y + radius + 1)):
            dist2 = (i - x)**2 + (j - y)**2
            if dist2 <= r2:
                count += grid[i][j]
    return count

# Simulação
for _ in range(ITERATIONS):
    new_grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            AD = count_neighbors(x, y, INNER_RADIUS)
            ID = count_neighbors(x, y, OUTER_RADIUS) - count_neighbors(x, y, INNER_RADIUS)
            new_grid[x][y] = 1 if AD - W * ID > 0 else 0
    grid = new_grid

# Configura Turtle
try:
    screen = turtle.Screen()
    screen.title("Manchas de Leopardo - Padrão de Turing")
    screen.bgcolor("#D4A017")  # Fundo amarelo-mostarda
    screen.setup(600, 600)

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    BASE_CELL_SIZE = 35  # Tamanho base das manchas
    SPOT_COLOR = "#4A2C2A"  # Marrom escuro para manchas

    # Desenha manchas
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if grid[x][y] == 1:
                random.seed(42 + x*GRID_SIZE + y)
                cell_size = BASE_CELL_SIZE * random.uniform(0.8, 1.2)  # Variação 80%-120%
                px = (x - GRID_SIZE/2) * BASE_CELL_SIZE
                py = (y - GRID_SIZE/2) * BASE_CELL_SIZE * -1

                # Mancha arredondada com irregularidade
                t.penup()
                t.goto(px, py)
                t.pendown()
                t.color("black", SPOT_COLOR)
                t.begin_fill()
                sides = random.randint(6, 10)  # Mais lados para simular rosetas
                for i in range(sides):
                    angle = i * (360/sides) + random.uniform(-15, 15)
                    r = cell_size * 0.4 * (1 + random.uniform(-0.3, 0.3))
                    dx = r * math.cos(math.radians(angle))
                    dy = r * math.sin(math.radians(angle))
                    t.goto(px + dx, py + dy)
                t.goto(px + cell_size * 0.4 * math.cos(math.radians(random.uniform(-15, 15))), 
                       py + cell_size * 0.4 * math.sin(math.radians(random.uniform(-15, 15))))
                t.end_fill()

    screen.exitonclick()

except Exception as e:
    print(f"Erro: {e}")
    print("Use um ambiente gráfico (ex.: IDLE, VSCode). Teste 'import turtle; turtle.Turtle()'.")
