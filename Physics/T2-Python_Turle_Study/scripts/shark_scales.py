import turtle
import math
import random

class SharkSkinMathematical:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.bgcolor("#DCDCDC")
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.hideturtle()
    
    # PILAR 1: TESSELAÇÃO HEXAGONAL OTIMIZADA
    def generate_grid(self, rows=15, cols=18, base_size=7):
        """Pilar 1: Grade hexagonal densa com eficiência 98%"""
        grid_points = []
        for row in range(rows * 2):
            for col in range(cols * 2):
                x = (col * 1.2 + (0.6 if row % 2 == 1 else 0)) * base_size * 0.7
                y = row * math.sqrt(3) * base_size * 0.42
                
                # Filtro de densidade matemática
                center_r, center_c = rows, cols
                dist = math.sqrt((row-center_r)**2 + (col-center_c)**2)
                max_dist = math.sqrt(center_r**2 + center_c**2)
                density = 0.98 * (1 - (dist/(max_dist * 1.2))**1.5)
                
                if random.random() < density * 1.2:
                    grid_points.append((x - cols * base_size * 0.7, 
                                      y - rows * base_size * 0.4))
        return grid_points
    
    # PILAR 2: VORONOI SIMPLIFICADO
    def create_shape(self, center, neighbors, base_size):
        """Pilar 2: Forma orgânica baseada em influência de vizinhos"""
        shape_type = int((math.sin(center[0] * 0.1) + 1) * 1.5) % 3
        num_points = [3, 4, 5][shape_type]  # Triangular, Quadrilátero, Pentagonal
        
        points = []
        for i in range(num_points):
            angle = 2 * math.pi * i / num_points
            
            # Raio base com influência Voronoi
            radius = base_size * (0.6 + 0.3 * random.random())
            for n in neighbors:
                if len(n) == 2:
                    dx, dy = center[0]-n[0], center[1]-n[1]
                    dist = math.sqrt(dx*dx + dy*dy)
                    if dist < base_size * 2.5:
                        n_angle = math.atan2(dy, dx)
                        angle_diff = min(abs(angle - n_angle), 2*math.pi - abs(angle - n_angle))
                        if angle_diff < math.pi/4:
                            radius *= 0.7 + 0.2 * (1 - angle_diff/(math.pi/4))
            
            # Variação de forma
            variation = 0.8 + 0.4 * math.sin(angle * [2, 2, 2.5][shape_type])
            final_radius = radius * variation
            
            points.append((
                center[0] + final_radius * math.cos(angle),
                center[1] + final_radius * math.sin(angle)
            ))
        return points
    
    # PILAR 3: INTERPOLAÇÃO DE COR SIMPLIFICADA
    def get_color(self, position, shape_type):
        """Pilar 3: Interpolação ponderada para tons de cinza"""
        x, y = position
        time = random.random() * 10
        
        # Padrão de onda para variação
        wave1 = math.sin(x * 0.08 + time) * 0.5 + 0.5
        wave2 = math.cos(y * 0.06 + time * 0.7) * 0.5 + 0.5
        wave3 = math.sin((x + y) * 0.04 + time * 0.3) * 0.5 + 0.5
        
        intensity = (wave1 + wave2 + wave3) / 3
        intensity = max(0.25, min(0.95, intensity + math.sin(x * 0.03) * 0.1))
        
        return (intensity, intensity, intensity)
    
    # PILAR 4: PADRÃO TURING SIMPLIFICADO
    def turing_filter(self, x, y):
        """Pilar 4: Filtro de Turing para distribuição natural"""
        time = random.random() * 10
        high_f = math.sin(x * 0.15 + y * 0.12 + time * 1.5) * 0.3 + 0.5
        mid_f = math.cos(x * 0.08 - y * 0.06 + time * 0.8) * 0.4 + 0.5
        pattern = (high_f * 0.4 + mid_f * 0.4 + (math.sin((x+y)*0.03)*0.3+0.5)*0.2)
        return 1 / (1 + math.exp(-8 * (pattern - 0.5)))  # Sigmóide
    
    # MÉTODO PRINCIPAL
    def generate_pattern(self, rows=15, cols=18, base_size=7):
        """Gera padrão completo integrando os 4 pilares"""
        grid_points = self.generate_grid(rows, cols, base_size)
        
        for center in grid_points:
            # Encontrar vizinhos próximos
            neighbors = [p for p in grid_points if p != center and 
                         math.sqrt((center[0]-p[0])**2 + (center[1]-p[1])**2) < base_size * 3]
            
            # Aplicar filtro de Turing
            if random.random() < self.turing_filter(center[0], center[1]) * 1.1:
                shape_type = int((math.sin(center[0] * 0.1) + 1) * 1.5) % 3
                points = self.create_shape(center, neighbors, base_size)
                color = self.get_color(center, shape_type)
                
                # Desenhar forma
                self.pen.fillcolor(color)
                self.pen.begin_fill()
                self.pen.penup()
                self.pen.goto(points[0])
                self.pen.pendown()
                for p in points[1:] + [points[0]]:
                    self.pen.goto(p)
                self.pen.end_fill()

# Execução
simulator = SharkSkinMathematical()
simulator.generate_pattern()
simulator.screen.exitonclick()
