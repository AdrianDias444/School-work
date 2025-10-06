import turtle
import math

def draw_hexagon(t, size, depth=0.3):
    """Desenha um hexágono com Turtle, simulando profundidade."""
    t.pensize(2)  # Bordas mais grossas como na imagem
    for _ in range(6):
        t.forward(size)
        t.left(60)
    
    # Simula profundidade desenhando um hexágono interno menor
    t.penup()
    t.forward(size * depth)  # Move para dentro
    t.left(30)  # Ajusta para alinhar com o centro
    t.pendown()
    t.pensize(1)  # Bordas internas mais finas
    for _ in range(6):
        t.forward(size * (1 - depth))
        t.left(60)
    t.penup()
    t.goto(t.xcor() - size * depth, t.ycor())  # Volta ao ponto inicial
    t.setheading(t.heading() - 30)  # Corrige orientação

def generate_honeycomb(rows=8, cols=10, hex_size=20):
    """
    Gera uma estrutura de favos de mel hexagonal usando Turtle.
    
    Parâmetros:
    - rows: Número de linhas de hexágonos.
    - cols: Número de colunas de hexágonos.
    - hex_size: Tamanho do lado do hexágono.
    
    Baseado na tesselação {6,3} (Schläfli) e otimizado para parecer com a imagem.
    """
    t = turtle.Turtle()
    t.speed(0)  # Máxima velocidade
    t.hideturtle()  # Esconde o Turtle para melhor visualização
    
    # Configurações de cor baseadas na imagem (tons de mel)
    t.fillcolor("#FFD700")  # Dourado mel
    t.pencolor("#DAA520")  # Bege acastanhado para bordas
    
    # Distâncias para posicionamento hexagonal
    hex_width = math.sqrt(3) * hex_size
    hex_height = 2 * hex_size
    
    for row in range(rows):
        y = row * (3/2 * hex_size)  # Offset vertical
        for col in range(cols):
            # Offset horizontal para linhas pares/ímpar
            x_offset = (col * hex_width) + (row % 2) * (hex_width / 2)
            
            # Move para a posição inicial
            t.penup()
            t.goto(x_offset - (cols * hex_width / 2), -y - (rows * hex_height / 4))  # Centraliza
            t.pendown()
            
            # Desenha e preenche o hexágono
            t.begin_fill()
            draw_hexagon(t, hex_size, depth=0.3)
            t.end_fill()
    
    # Mantém a janela aberta
    turtle.done()

# Exemplo de uso
if __name__ == "__main__":
    generate_honeycomb(rows=8, cols=10, hex_size=20)
