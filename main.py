import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state,log_event
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot
def main():
    print(f"Starting Asteroids")
    print(f"Screen width: {1280} \nScreen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids,updatable,drawable)
    Player.containers = (updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable,drawable)

    asteroid_field = AsteroidField()
    player = Player(x,y)
    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
        

        pygame.display.flip()

        for obj in asteroids:
            if player.collides_with(obj):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()

        for obj in asteroids:
            for bullet in shots:
                if obj.collides_with(bullet):
                    log_event("asteroid_shot")
                    obj.split()
                    bullet.kill()

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
