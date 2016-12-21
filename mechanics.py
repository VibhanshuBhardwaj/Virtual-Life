import pygame
import random
import math

from addVectors import addVectors

background_colour = (144,238,144)
(width, height) = (400, 400)
gravity = (math.pi/2, 0.002)

elasticity = 0.9
drag = 0.999

class Particle():
    def __init__(self, (x, y), radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = (255, 255, 255)
        self.thickness = 0
        self.speed = 0
        self.angle = 0 #the angle being measured in clockwise direction from +X. (remember +Y is downwards)

    def display(self):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.radius, self.thickness)

    def move(self):
        (self.angle, self.speed) = addVectors((self.angle, self.speed), gravity)
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        self.speed *= drag

    def bounce(self):
        #we'll just change the angle using simple geometry
        if (self.x + self.radius) > width:
            self.x = 2*(width - self.radius) - self.x
            self.angle = math.pi - self.angle
            self.speed *= elasticity
        elif (self.y + self.radius) > height:
            self.y = 2*(height - self.radius) - self.y
            self.angle*=-1
            self.speed *= elasticity
        elif self.x < self.radius:
            self.x = 2*self.radius - self.x
            self.angle = math.pi - self.angle
            self.speed *= elasticity
        elif self.y < self.radius:
            self.y = 2*self.radius - self.y
            self.angle *=-1
            self.speed *= elasticity

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Physics Simulation')

number_of_particles = 2
my_particles = []

for n in range(number_of_particles):
    radius = random.randint(10, 20)
    x = random.randint(radius, width-radius)
    y = random.randint(radius, height-radius)
    particle = Particle((x, y), radius)
    particle.speed = random.random()
    particle.angle = random.uniform(0, 2 * math.pi)
    my_particles.append(particle)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

    screen.fill(background_colour)

    for particle in my_particles:
        particle.move()
        particle.bounce()
        particle.display()

    pygame.display.flip()
