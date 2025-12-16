import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    asteroid_field = AsteroidField()

    Shot.containers = (updatable, drawable, shots)    

    while True:        
        dt = clock.tick(60)
        dt /= 1000 

        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("black")     
        
        updatable.update(dt)
        for object in drawable:
            object.draw(screen)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()

        pygame.display.flip()




if __name__ == "__main__":
    main()
