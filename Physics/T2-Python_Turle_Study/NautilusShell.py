import math
import turtle

# Configuração inicial
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(1000, 800)
screen.title("Concha Cônica em Espiral Logarítmica")

concha = turtle.Turtle()
concha.speed(0)
concha.hideturtle()


def desenhar_concha_conica():
    """Desenha uma concha cônica alongada baseada na matemática fornecida"""

    # Parâmetros para forma cônica alongada
    a = 3.0  # Tamanho inicial pequeno
    b = 0.12  # Taxa de crescimento mais suave para forma alongada
    c = 0.08  # Fator de conicidade

    # Mais voltas para criar o efeito alongado
    theta_inicial = 0
    theta_final = 10 * math.pi  # 5 voltas completas
    num_pontos = 600

    # Desenhar a espiral principal - lado externo
    concha.color("black")
    concha.pensize(2)
    concha.penup()

    pontos_externos = []

    for i in range(num_pontos + 1):
        theta = theta_inicial + (theta_final - theta_inicial) * (i / num_pontos)
        # Adicionar conicidade: raio cresce mais rápido devido ao termo c*theta
        r = a * math.exp(b * theta) + c * theta

        x = r * math.cos(theta)
        y = r * math.sin(theta)
        pontos_externos.append((x, y, theta))

        if i == 0:
            concha.goto(x, y)
            concha.pendown()
        else:
            concha.goto(x, y)

    # Voltar desenhando o lado interno (SEM abertura expandida)
    concha.penup()

    # Espiral interna (mais estreita)
    for i in range(num_pontos, -1, -1):
        theta = pontos_externos[i][2]
        # Espiral interna mais próxima do centro
        r_interno = a * 0.7 * math.exp(b * theta) + c * theta * 0.8

        x = r_interno * math.cos(theta)
        y = r_interno * math.sin(theta)

        if i == num_pontos:
            concha.goto(x, y)
            concha.pendown()
        else:
            concha.goto(x, y)

    # Fechar no ponto inicial
    concha.goto(pontos_externos[0][0], pontos_externos[0][1])


def desenhar_estrias_conicas():
    """Desenha linhas de crescimento na direção correta para forma cônica"""
    concha.color("#666666")
    concha.pensize(1)

    a = 3.0
    b = 0.12
    c = 0.08

    # Estrias em ângulos estratégicos
    angulos_estrias = [30, 90, 150, 210, 270, 330]

    for angulo in angulos_estrias:
        theta_rad = math.radians(angulo)

        # Ponto interno
        r_interno = a * 0.7 * math.exp(b * theta_rad * 2) + c * theta_rad * 2 * 0.8
        x_interno = r_interno * math.cos(theta_rad * 2)
        y_interno = r_interno * math.sin(theta_rad * 2)

        # Ponto externo
        r_externo = a * math.exp(b * theta_rad * 2) + c * theta_rad * 2
        x_externo = r_externo * math.cos(theta_rad * 2)
        y_externo = r_externo * math.sin(theta_rad * 2)

        concha.penup()
        concha.goto(x_interno, y_interno)
        concha.pendown()
        concha.goto(x_externo, y_externo)


def desenhar_camaras_internas():
    """Desenha as divisórias internas da concha"""
    concha.color("black")
    concha.pensize(1.2)

    a = 3.0
    b = 0.12
    c = 0.08

    # Posições das câmaras (a cada ~1.5π)
    camaras_theta = [
        1.5 * math.pi,
        3.0 * math.pi,
        4.5 * math.pi,
        6.0 * math.pi,
        7.5 * math.pi,
        9.0 * math.pi,
    ]

    for theta_camara in camaras_theta:
        # Ponto interno da câmara
        r_interno = a * 0.7 * math.exp(b * theta_camara) + c * theta_camara * 0.8
        x_interno = r_interno * math.cos(theta_camara)
        y_interno = r_interno * math.sin(theta_camara)

        # Ponto externo da câmara
        r_externo = a * math.exp(b * theta_camara) + c * theta_camara
        x_externo = r_externo * math.cos(theta_camara)
        y_externo = r_externo * math.sin(theta_camara)

        # Desenhar linha divisória curva
        concha.penup()
        concha.goto(x_interno, y_interno)
        concha.pendown()

        # Curva suave para a divisória
        for offset in [-0.2, -0.1, 0, 0.1, 0.2]:
            theta_offset = theta_camara + offset
            r_meio = a * 0.85 * math.exp(b * theta_offset) + c * theta_offset * 0.9
            x_meio = r_meio * math.cos(theta_offset)
            y_meio = r_meio * math.sin(theta_offset)
            concha.goto(x_meio, y_meio)

        concha.goto(x_externo, y_externo)


def desenhar_textura_superficie():
    """Adiciona textura à superfície da concha"""
    concha.color("#888888")
    concha.pensize(0.5)

    a = 3.0
    b = 0.12
    c = 0.08

    # Pequenas linhas de textura seguindo a espiral
    for i in range(15):
        theta_base = i * 0.4 * math.pi

        concha.penup()
        r1 = a * 0.8 * math.exp(b * theta_base) + c * theta_base * 0.85
        x1 = r1 * math.cos(theta_base)
        y1 = r1 * math.sin(theta_base)
        concha.goto(x1, y1)

        concha.pendown()
        r2 = a * 0.9 * math.exp(b * (theta_base + 0.3)) + c * (theta_base + 0.3) * 0.9
        x2 = r2 * math.cos(theta_base + 0.3)
        y2 = r2 * math.sin(theta_base + 0.3)
        concha.goto(x2, y2)


# Executar desenho
print("Criando concha cônica alongada...")
desenhar_concha_conica()
desenhar_estrias_conicas()
desenhar_camaras_internas()
desenhar_textura_superficie()

# Informações matemáticas
info = turtle.Turtle()
info.speed(0)
info.hideturtle()
info.color("black")
info.penup()
info.goto(0, -400)
info.write(
    "Concha Cônica em Espiral Logarítmica", align="center", font=("Arial", 14, "bold")
)

info.goto(0, -430)
info.write(
    "r(θ) = a·e^(bθ) + c·θ com a=3.0, b=0.12, c=0.08",
    align="center",
    font=("Arial", 10, "normal"),
)

info.goto(0, -460)
info.write(
    "Forma alongada com 5 voltas completas - Sem abertura expandida",
    align="center",
    font=("Arial", 9, "normal"),
)

print("Concha cônica concluída!")
print("Pressione 'q' para fechar")


def fechar():
    screen.bye()


screen.onkey(fechar, "q")
screen.listen()
screen.mainloop()
