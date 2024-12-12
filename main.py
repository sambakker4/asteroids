import pygame, sys
from constants import *
from circleshape import *
from player import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    dt = 0
    something = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        for thing in updatable:
            thing.update(dt)

        for asteroid in asteroids:
            if player.collision(asteroid):
                something = True
                break
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()
        if something: break

        screen.fill("black")

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
    print("Game over!")
    sys.exit()

if __name__ == "__main__":
    main()