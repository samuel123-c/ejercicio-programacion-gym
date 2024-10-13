import pygame
import json
import time

# Pygame initialization
pygame.init()

# Colors
BACKGROUND_COLOR = (0, 0, 0)
START_BUTTON_COLOR = (0, 100, 0)
PAUSE_BUTTON_COLOR = (255, 165, 0)
RESUME_BUTTON_COLOR = (30, 144, 255)
TEXT_COLOR = (255, 255, 255)
INPUT_BOX_COLOR = (255, 255, 255)
ERROR_COLOR = (255, 0, 0)

# Screen dimensions
WIDTH = 1000
HEIGHT = 700

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Entrenador Personal - Pygame')

# Load background image
background_image = pygame.image.load('imagenes/fondo de pantalla.jpg')  
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  

# Exercise data by body part
workouts = {
    "Upper Body": {
        "Bíceps": [
            {"name": "Curl con barra", "sets": 3, "reps": 12},
            {"name": "Curl con mancuerna", "sets": 3, "reps": 10},
            {"name": "Curl de concentración", "sets": 3, "reps": 12},
            {"name": "Curl martillo", "sets": 3, "reps": 12},
            {"name": "Curl predicador", "sets": 3, "reps": 10}
        ],
        "Tríceps": [
            {"name": "Fondos", "sets": 3, "reps": 10},
            {"name": "Extensión de tríceps", "sets": 3, "reps": 12},
            {"name": "Press francés", "sets": 3, "reps": 10},
            {"name": "Patadas de tríceps", "sets": 3, "reps": 12},
            {"name": "Jalón de tríceps", "sets": 3, "reps": 10}
        ],
        "Antebrazo": [
            {"name": "Curl de muñeca", "sets": 3, "reps": 12},
            {"name": "Extensiones de muñeca", "sets": 3, "reps": 12},
            {"name": "Curl inverso", "sets": 3, "reps": 12},
            {"name": "Rollos de muñeca", "sets": 3, "reps": 15},
            {"name": "Sostener peso", "sets": 3, "reps": 30}
        ],
        "Pecho": [
            {"name": "Press de banca", "sets": 3, "reps": 10},
            {"name": "Flexiones", "sets": 3, "reps": 15},
            {"name": "Press inclinado", "sets": 3, "reps": 10},
            {"name": "Aperturas", "sets": 3, "reps": 12},
            {"name": "Fondos", "sets": 3, "reps": 10}
        ],
        "Espalda": [
            {"name": "Dominadas", "sets": 3, "reps": 8},
            {"name": "Remo con barra", "sets": 3, "reps": 10},
            {"name": "Jalón al pecho", "sets": 3, "reps": 10},
            {"name": "Remo en máquina", "sets": 3, "reps": 10},
            {"name": "Peso muerto", "sets": 3, "reps": 8}
        ]
    },
    "Lower Body": {
        "Gemelos": [
            {"name": "Elevaciones de talón", "sets": 4, "reps": 15},
            {"name": "Elevaciones de talón en máquina", "sets": 4, "reps": 12},
            {"name": "Elevaciones de talón sentado", "sets": 4, "reps": 15},
            {"name": "Elevaciones de talón a una pierna", "sets": 4, "reps": 10},
            {"name": "Saltos de pantorrilla", "sets": 4, "reps": 20}
        ],
        "Isquiotibiales": [
            {"name": "Curl de pierna", "sets": 3, "reps": 12},
            {"name": "Peso muerto rumano", "sets": 3, "reps": 10},
            {"name": "Puente de glúteos", "sets": 3, "reps": 15},
            {"name": "Zancadas", "sets": 3, "reps": 12},
            {"name": "Hip Thrust", "sets": 3, "reps": 12}
        ],
        "Cuádriceps": [
            {"name": "Sentadillas", "sets": 3, "reps": 10},
            {"name": "Press de piernas", "sets": 3, "reps": 12},
            {"name": "Zancadas hacia adelante", "sets": 3, "reps": 10},
            {"name": "Sentadilla frontal", "sets": 3, "reps": 10},
            {"name": "Sentadilla sumo", "sets": 3, "reps": 12}
        ],
        "Bíceps": [
            {"name": "Curl de pierna", "sets": 3, "reps": 12},
            {"name": "Peso muerto", "sets": 3, "reps": 10},
            {"name": "Press de piernas", "sets": 3, "reps": 12},
            {"name": "Zancadas", "sets": 3, "reps": 10},
            {"name": "Hip Thrust", "sets": 3, "reps": 12}
        ],
        "Glúteos": [
            {"name": "Sentadillas", "sets": 3, "reps": 10},
            {"name": "Puente de glúteos", "sets": 3, "reps": 12},
            {"name": "Zancadas", "sets": 3, "reps": 10},
            {"name": "Hip Thrust", "sets": 3, "reps": 12},
            {"name": "Sentadilla sumo", "sets": 3, "reps": 12}
        ]
    }
}

# Load user data from JSON
def cargar_usuarios_json():
    try:
        with open('usuarios.json', 'r') as archivo:
            return json.load(archivo)['usuarios']
    except FileNotFoundError:
        print("Archivo JSON no encontrado.")
        return []

# Function to verify credentials
def verificar_credenciales(nombre, clave):
    usuarios = cargar_usuarios_json()
    for usuario in usuarios:
        if usuario['nombre'] == nombre and usuario['clave'] == clave:
            return True
    return False

# Input box class
class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = INPUT_BOX_COLOR
        self.text = text
        self.txt_surface = font.render(text, True, TEXT_COLOR)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    return self.text
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = font.render(self.text, True, TEXT_COLOR)
        return None

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))

# Function for the login screen
def login_screen():
    nombre_input = InputBox(400, 250, 200, 50)
    clave_input = InputBox(400, 350, 200, 50)
    login_button = pygame.Rect(400, 450, 200, 50)
    login_success = False
    error_message = ""

    while not login_success:
        screen.fill(BACKGROUND_COLOR)
        show_text("Inicio de Sesión", 400, 150)
        show_text("Usuario:", 200, 250)
        show_text("Clave:", 200, 350)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Handle input events
            nombre_input.handle_event(event)
            clave_input.handle_event(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if login_button.collidepoint(event.pos):
                    nombre = nombre_input.text
                    clave = clave_input.text
                    if verificar_credenciales(nombre, clave):
                        login_success = True
                    else:
                        error_message = "Credenciales incorrectas"

        nombre_input.draw(screen)
        clave_input.draw(screen)
        pygame.draw.rect(screen, START_BUTTON_COLOR, login_button)
        show_text("Iniciar Sesión", 420, 460)

        if error_message:
            show_text(error_message, 400, 520, ERROR_COLOR)

        pygame.display.flip()

# Execution state
current_exercise = None
remaining_sets = 0
remaining_reps = 0
time_counter = 0
paused = False
last_second_time = 0
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont(None, 36)

# Functions to draw buttons and text
def draw_button(text, x, y, color):
    pygame.draw.rect(screen, color, (x, y, 200, 50))
    text_width, text_height = font.size(text)
    pos_x = x + (200 - text_width) // 2
    pos_y = y + (50 - text_height) // 2
    screen.blit(font.render(text, True, TEXT_COLOR), (pos_x, pos_y))

def show_text(text, x, y, color=TEXT_COLOR):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Function to select and show exercises
def start_exercise(exercise_name):
    global current_exercise, remaining_sets, remaining_reps, time_counter, paused, last_second_time
    paused = False
    current_exercise = exercise_name
    remaining_sets = exercise_name['sets']
    remaining_reps = exercise_name['reps']
    time_counter = 0
    last_second_time = time.time()

# Function to update exercise counter every real second
def update_exercise():
    global remaining_sets, remaining_reps, time_counter, last_second_time
    if time.time() - last_second_time >= 1:
        if remaining_sets > 0:
            if remaining_reps > 0:
                remaining_reps -= 1
                time_counter += 1
            else:
                remaining_sets -= 1
                remaining_reps = current_exercise['reps']
                time_counter += 1
        last_second_time = time.time()

# Function to stop the exercise
def stop_exercise():
    global current_exercise, remaining_sets, remaining_reps, paused
    current_exercise = None
    remaining_sets = 0
    remaining_reps = 0
    paused = False

# Function to pause the exercise
def pause_exercise():
    global paused
    paused = True

# Function to resume the exercise
def resume_exercise():
    global paused
    paused = False

# Put the images
exercise_images = {
    "Curl con barra": pygame.image.load('imagenes/Curl con barra.jpg'),
    "Curl con mancuerna": pygame.image.load('imagenes/Curl con mancuerna.jpg'),
    "Curl de concentración": pygame.image.load('imagenes/Curl de concentración.jpg'),
    "Curl martillo": pygame.image.load('imagenes/Curl martillo.jpg'),
    "Curl predicador": pygame.image.load('imagenes/Curl predicador.jpg'),
    "Fondos": pygame.image.load('imagenes/Fondos.jpg'),
    "Extensión de tríceps": pygame.image.load('imagenes/Extensión de tríceps.jpg'),
    "Press francés": pygame.image.load('imagenes/Press francés.jpg'),
    "Patadas de tríceps": pygame.image.load('imagenes/Patadas de tríceps.jpg'),
    "Jalón de tríceps": pygame.image.load('imagenes/Jalón de tríceps.jpg'),
    "Curl de muñeca": pygame.image.load('imagenes/Curl de muñeca.jpg'),
    "Extensiones de muñeca": pygame.image.load('imagenes/Extensiones de muñeca.jpg'),
    "Curl inverso": pygame.image.load('imagenes/Curl inverso.jpg'),
    "Rollos de muñeca": pygame.image.load('imagenes/Rollos de muñeca.jpg'),
    "Sostener peso": pygame.image.load('imagenes/Sostener peso.jpg'),
    "Press de banca": pygame.image.load('imagenes/Press de banca.jpg'),
    "Flexiones": pygame.image.load('imagenes/Flexiones.jpg'),
    "Press inclinado": pygame.image.load('imagenes/Press inclinado.jpg'),
    "Aperturas": pygame.image.load('imagenes/Aperturas.jpg'),
    "Dominadas": pygame.image.load('imagenes/Dominadas.jpg'),
    "Remo con barra": pygame.image.load('imagenes/Remo con barra.jpg'),
    "Jalón al pecho": pygame.image.load('imagenes/Jalón al pecho.jpg'),
    "Remo en máquina": pygame.image.load('imagenes/Remo en máquina.jpg'),
    "Peso muerto": pygame.image.load('imagenes/Peso muerto.jpg'),

    "Elevaciones de talón": pygame.image.load('imagenes/Elevaciones de talón.jpg'),
    "Elevaciones de talón en máquina": pygame.image.load('imagenes/Elevaciones de talón en máquina.jpg'),
    "Elevaciones de talón sentado": pygame.image.load('imagenes/Elevaciones de talón sentado.jpg'),
    "Elevaciones de talón a una pierna": pygame.image.load('imagenes/Elevaciones de talón a una pierna.jpg'),
    "Saltos de pantorrilla": pygame.image.load('imagenes/Saltos de pantorrilla.jpg'),
    "Curl de pierna": pygame.image.load('imagenes/Curl de pierna.jpg'),
    "Peso muerto rumano": pygame.image.load('imagenes/Peso muerto rumano.jpg'),
    "Puente de glúteos": pygame.image.load('imagenes/Puente de glúteos.jpg'),
    "Zancadas": pygame.image.load('imagenes/Zancadas.jpg'),
    "Hip Thrust": pygame.image.load('imagenes/Hip Thrust.jpg'),
    "Sentadillas": pygame.image.load('imagenes/Sentadillas.jpg'),
    "Press de piernas": pygame.image.load('imagenes/Press de piernas.jpg'),
    "Zancadas hacia adelante": pygame.image.load('imagenes/Zancadas hacia adelante.jpg'),
    "Sentadilla frontal": pygame.image.load('imagenes/Sentadilla frontal.jpg'),
    "Sentadilla sumo": pygame.image.load('imagenes/Sentadilla sumo.jpg'),
}

# Login before entering the main loop
login_screen()

# Main loop
running = True
current_part = None
selected_exercise = None
exercise_options = []

while running:
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle clicks on buttons
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if 100 <= mouse_x <= 300 and 100 <= mouse_y <= 150:
                current_part = "Upper Body"
                selected_exercise = None
                exercise_options = []
            if 100 <= mouse_x <= 300 and 170 <= mouse_y <= 220:
                current_part = "Lower Body"
                selected_exercise = None
                exercise_options = []

            # Select exercises for Upper Body
            if current_part == "Upper Body":
                if 100 <= mouse_x <= 300 and 240 <= mouse_y <= 290:
                    exercise_options = workouts["Upper Body"]["Bíceps"]
                if 100 <= mouse_x <= 300 and 310 <= mouse_y <= 360:
                    exercise_options = workouts["Upper Body"]["Tríceps"]
                if 100 <= mouse_x <= 300 and 380 <= mouse_y <= 430:
                    exercise_options = workouts["Upper Body"]["Antebrazo"]
                if 100 <= mouse_x <= 300 and 450 <= mouse_y <= 500:
                    exercise_options = workouts["Upper Body"]["Pecho"]
                if 100 <= mouse_x <= 300 and 520 <= mouse_y <= 570:
                    exercise_options = workouts["Upper Body"]["Espalda"]

            # Select exercises for Lower Body
            if current_part == "Lower Body":
                if 100 <= mouse_x <= 300 and 240 <= mouse_y <= 290:
                    exercise_options = workouts["Lower Body"]["Gemelos"]
                if 100 <= mouse_x <= 300 and 310 <= mouse_y <= 360:
                    exercise_options = workouts["Lower Body"]["Isquiotibiales"]
                if 100 <= mouse_x <= 300 and 380 <= mouse_y <= 430:
                    exercise_options = workouts["Lower Body"]["Cuádriceps"]
                if 100 <= mouse_x <= 300 and 450 <= mouse_y <= 500:
                    exercise_options = workouts["Lower Body"]["Bíceps"]
                if 100 <= mouse_x <= 300 and 520 <= mouse_y <= 570:
                    exercise_options = workouts["Lower Body"]["Glúteos"]

            # Select specific exercises
            if exercise_options:
                for i, exercise in enumerate(exercise_options):
                    if 350 <= mouse_x <= 550 and 240 + i * 60 <= mouse_y <= 290 + i * 60:
                        start_exercise(exercise)

            # Pause and resume
            if 100 <= mouse_x <= 300 and 600 <= mouse_y <= 650:
                pause_exercise()
            if 310 <= mouse_x <= 510 and 600 <= mouse_y <= 650:
                resume_exercise()

    # Draw the body part selection buttons
    draw_button("Tren Superior", 100, 100, START_BUTTON_COLOR)
    draw_button("Tren Inferior", 100, 170, START_BUTTON_COLOR)

    # Draw exercise buttons according to the selected part
    if current_part == "Upper Body":
        for i, exercise in enumerate(workouts["Upper Body"]):
            draw_button(exercise, 100, 240 + i * 70, START_BUTTON_COLOR)

    elif current_part == "Lower Body":
        for i, exercise in enumerate(workouts["Lower Body"]):
            draw_button(exercise, 100, 240 + i * 70, START_BUTTON_COLOR)

    # Show specific exercises
    if exercise_options:
        for i, exercise in enumerate(exercise_options):
            draw_button(exercise["name"], 350, 240 + i * 60, START_BUTTON_COLOR)

    # Show current exercise status
    if current_exercise:
        show_text(f'Ejercicio: {current_exercise["name"]}', 580, 60)
        show_text(f'Series restantes: {remaining_sets}', 580, 110)
        show_text(f'Repeticiones restantes: {remaining_reps}', 580, 160)
        show_text(f'Tiempo: {time_counter} s', 580, 210)

        # Show image
        exercise_image = exercise_images.get(current_exercise["name"])
        if exercise_image:
            exercise_image = pygame.transform.scale(exercise_image, (300, 400))
            screen.blit(exercise_image, (580, 240))

        if not paused:
            update_exercise()

    # Draw pause and resume buttons
    draw_button("Pausar", 100, 600, PAUSE_BUTTON_COLOR)
    draw_button("Reanudar", 310, 600, RESUME_BUTTON_COLOR)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
