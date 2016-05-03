"""Health Damage Speed"""
import sys
import sdl2
import sdl2.ext
import time
from random import randint

# Constant variables
WHITE = sdl2.ext.Color(255, 255, 255)
BLACK = sdl2.ext.Color(0, 0, 0)
RED = sdl2.ext.Color(255, 0, 0)
GREEN = sdl2.ext.Color(0, 255, 0)
RESOURCES = sdl2.ext.Resources(__file__, "resources")


class SoftwareRenderSystem(sdl2.ext.SoftwareSpriteRenderSystem):
    def __init__(self, window):
        super(SoftwareRenderSystem, self).__init__(window)

    def render(self, components):
        #sdl2.ext.fill(self.surface, WHITE)
        #renderHPBar(10, 10, 450, 40, 1, GREEN, BLACK, self.surface)
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
        self.sprite.x = posx
        self.sprite.y = posy
        self.sprite.playerdata = PlayerData(health, damage, speed)
        self.vx = 0
        self.vy = 0
        self.sprite.missiles = 0



class Missile1(sdl2.ext.Entity):
    def __init__(self, world, sprite, damage, posx=0, posy=0):
        self.sprite = sprite
        self.sprite.damage = damage
        self.sprite.position = posx, posy
        self.sprite.x = posx
        self.sprite.y = posy


def renderHPBar2(x, y, w, h, percent, fgColor, bgColor, surface):
    if percent > 1:
        percent = 1
    elif percent < 0:
        percent = 0

    rect1 = (x,y,w,h)

    pw = w * percent
    px = x + (w - pw)
    rect2 = (px,y,pw,h)

    sdl2.ext.fill(surface, bgColor, rect1)
    sdl2.ext.fill(surface, fgColor, rect2)


def renderHPBar1(x, y, w, h, percent, fgColor, bgColor, surface):
    if percent > 1:
        percent = 1
    elif percent < 0:
        percent = 0

    rect1 = (x,y,w,h)

    pw = w * percent
    pw = pw
    #px = x + (w - pw)
    rect2 = (x,y,pw,h)

    sdl2.ext.fill(surface, bgColor, rect1)
    sdl2.ext.fill(surface, fgColor, rect2)

def check_cooldown(now_time, last_fire_time):
    return float(now_time) - float(last_fire_time)

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
    context = sdl2.ext.Renderer(window)
    world.add_system(spriterenderer)

    windowsurface = window.get_surface()

    player1 = Player(world, sprite1, 10, 5, 5, 0, 250)
    player2 = Player(world, sprite2, 8, 10, 2, 790, 250)

    missileSprite1 = factory.from_color(RED,size=(player1.sprite.playerdata.damage * 2,player1.sprite.playerdata.damage * 2))


    player1missiles = []
    player2missiles = []

    sdl2.ext.fill(windowsurface, WHITE)

    last_fire_time = 0

    running = True
    while running:

        #full health 18 = 1 percentage
        sdl2.ext.fill(windowsurface, WHITE)
        renderHPBar1(30, 10, 400, 40, 1, GREEN, BLACK, windowsurface)
        renderHPBar2(480, 10, 400, 40, 1, GREEN, BLACK, windowsurface)

        now_time = time.time()
        for event in sdl2.ext.get_events():
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_SPACE:
                    # shoot a missile based on character damage
                    player1.sprite.missiles += 1
                    if player1.sprite.missiles <= 3:
                        missile1 = Missile1(world, missileSprite1, player1.sprite.playerdata.damage,
                                            player1.sprite.x + 50, player1.sprite.y + 80)
                        player1missiles.append(missile1)
                    else:
                        player1.sprite.missiles = 0

        keystatus = sdl2.SDL_GetKeyboardState(None)

        # shoot a missile based on character damage
        if keystatus[sdl2.SDL_SCANCODE_SPACE]:
            print(player1missiles)
            print(now_time, float(now_time- last_fire_time))
            if check_cooldown(now_time,last_fire_time) > 2:
                last_fire_time = time.time()
                #player1.sprite.missiles += 1
                missile1 = Missile1(world, missileSprite1, player1.sprite.playerdata.damage, player1.sprite.x + 50, player1.sprite.y + 80)
                player1missiles.append(missile1)
                cd_clock_start = time.time()

        if keystatus[sdl2.SDL_SCANCODE_W]:
            player1.vy = player1.sprite.playerdata.speed
            if player1.sprite.y <= 100:
                player1.sprite.y = player1.sprite.y
            else:
                player1.sprite.y -= player1.sprite.playerdata.speed

        if keystatus[sdl2.SDL_SCANCODE_S]:
            player1.vy = player1.sprite.playerdata.speed
            if player1.sprite.y >= 620:
                player1.sprite.y = player1.sprite.y
            else:
                player1.sprite.y += player1.sprite.playerdata.speed

        if keystatus[sdl2.SDL_SCANCODE_UP]:
            player2.vy = player2.sprite.playerdata.speed
            if player2.sprite.y <= 100:
                player2.sprite.y = player2.sprite.y
            else:
                player2.sprite.y -= player2.sprite.playerdata.speed

        if keystatus[sdl2.SDL_SCANCODE_DOWN]:
            player2.vy = player2.sprite.playerdata.speed
            if player2.sprite.y >= 620:
                player2.sprite.y = player2.sprite.y
            else:
                player2.sprite.y += player2.sprite.playerdata.speed

<<<<<<< HEAD
        for missile in player1missiles:
                missile.sprite.x += 1
=======
        for i in range(len(player1missiles)-1):
            if player1missiles[i].sprite.x < 900: #size of the screen
                player1missiles[i].sprite.x += 3


>>>>>>> 25cc3c73ce1ab92cce44a1402f512e869da9852a

        """
        if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_UP:
                    player2.sprite.y -= player2.playerdata.speed
                    player2.vy = player2.playerdata.speed
                if event.key.keysym.sym == sdl2.SDLK_DOWN:
                    player2.sprite.y += player2.playerdata.speed
                    player2.vy = player2.playerdata.speed

                if event.key.keysym.sym == sdl2.SDLK_w:
                    player2.sprite.y -= player2.playerdata.speed
                    player2.vy = player2.playerdata.speed
                if event.key.keysym.sym == sdl2.SDLK_s:
                    player2.sprite.y += player2.playerdata.speed
                    player2.vy = player2.playerdata.speed
        if event.type == sdl2.SDL_KEYUP:
                if event.key.keysym.sym in (sdl2.SDLK_UP, sdl2.SDLK_DOWN):
                        player2.vy = 0
        """

        sdl2.SDL_Delay(10)
        world.process()

        #processor = sdl2.ext.TestEventProcessor()
        #processor.run(window)
        #spriterenderer.render(sprite)
if __name__ == "__main__":
    sys.exit(run())
