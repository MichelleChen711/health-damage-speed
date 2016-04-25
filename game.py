"""Health Damage Speed"""
import sys
import sdl2
import sdl2.ext

# Constant variables
WHITE = sdl2.ext.Color(255, 255, 255)
BLACK = sdl2.ext.Color(0, 0, 0)
RESOURCES = sdl2.ext.Resources(__file__, "resources")


class SoftwareRenderSystem(sdl2.ext.SoftwareSpriteRenderSystem):
    def __init__(self, window):
        super(SoftwareRenderSystem, self).__init__(window)

    def render(self, components):
        sdl2.ext.fill(self.surface, BLACK)
        super(SoftwareRenderSystem, self).render(components)


class PlayerData(object):
    def __init__(self, health, damage, speed):
        self.score = 0
        self.health = health
        self.damage = damage
        self.speed = speed


class Player(sdl2.ext.Entity):
    def __init__(self, world, sprite, health, damage, speed, posx=0, posy=0, ai=False):
        self.sprite = sprite
        self.sprite.position = posx, posy
        self.playerdata = PlayerData(health, damage, speed)
        self.vx = 0
        self.vy = 0


def run():
    sdl2.ext.init()
    window = sdl2.ext.Window("Health Damage Speed", size=(900, 800))
    window.show()

    factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
    sprite1 = factory.from_image(RESOURCES.get_path("bunny.bmp"))
    sprite2 = factory.from_image(RESOURCES.get_path("monkey.bmp"))

    world = sdl2.ext.World()

    #spriterenderer = factory.create_sprite_render_system(window)
    spriterenderer = SoftwareRenderSystem(window)

    world.add_system(spriterenderer)


    player1 = Player(world, sprite1, 10, 5, 5, 0, 250)
    player2 = Player(world, sprite2, 8, 10, 2, 780, 250)

    running = True
    while running:
        for event in sdl2.ext.get_events():
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
        if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_UP:
                    player1.vy = -player1.playerdata.speed
                elif event.key.keysym.sym == sdl2.SDLK_DOWN:
                    player1.vy = player1.playerdata.speed
        elif event.type == sdl2.SDL_KEYUP:
                if event.key.keysym.sym in (sdl2.SDLK_UP, sdl2.SDLK_DOWN):
                        player1.vy = 0
        sdl2.SDL_Delay(10)
        world.process()

        #processor = sdl2.ext.TestEventProcessor()
        #processor.run(window)
        #spriterenderer.render(sprite)
if __name__ == "__main__":
    sys.exit(run())
