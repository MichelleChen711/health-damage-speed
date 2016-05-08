"""Health Damage Speed"""
#Michelle Chen & Kevin Carter
import sys
from sdl2 import *
import sdl2.ext
import time
import math
#import sdl2.sdlmixer   //SDL2_mixer import didn't want to work
#import sdl2.sdlttf
from sdl2.ext.compat import byteify
from ctypes import *

# Constant variables
WHITE = sdl2.ext.Color(255, 255, 255)
BLACK = sdl2.ext.Color(0, 0, 0)
RED = sdl2.ext.Color(255, 0, 0)
GREEN = sdl2.ext.Color(0, 255, 0)
BLUE = sdl2.ext.Color(0, 0, 255)

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


class Missile(sdl2.ext.Entity):
    def __init__(self, world, sprite, damage, vx, posx=0, posy=0):
        self.sprite = sprite
        self.sprite.damage = damage
        self.sprite.position = posx, posy
        self.sprite.x = posx
        self.sprite.y = posy
        self.sprite.vx = vx


class WavSound(object):
    def __init__(self, file):
        super(WavSound, self).__init__()
        self._buf = POINTER(Uint8)()
        self._length = Uint32()
        self._bufpos = 0
        self.spec = SDL_AudioSpec(0, 0, 0, 0)
        self._load_file(file)
        self.spec.callback = SDL_AudioCallback(self._play_next)
        self.done = False

    def __del__(self):
        SDL_FreeWAV(self._buf)

    def _load_file(self, file):
        rw = SDL_RWFromFile(byteify(file, "utf-8"), b"rb")
        sp = SDL_LoadWAV_RW(rw, 1, byref(self.spec), byref(self._buf), byref(self._length))
        if sp is None:
            raise RuntimeError("Could not open audio file: {}".format(SDL_GetError()))

    def _play_next(self, notused, stream, len):
        length = self._length.value
        numbytes = min(len, length - self._bufpos)
        for i in range(0, numbytes):
            stream[i] = self._buf[self._bufpos + i]
        self._bufpos += numbytes

        # If not enough bytes in buffer, add silence
        rest = min(0, len - numbytes)
        for i in range(0, rest):
            stream[i] = 0

        # Are we done playing sound?
        if self._bufpos == length:
            self.done = True

def renderHPBar2(x, y, w, h, health, fgColor, bgColor, surface):
    if health > 18:
        health = 18
    elif health < 0:
        health = 0

    rect1 = (x,y,w,h)

    pw = w * (health/18)
    px = x + (w - pw)
    rect2 = (px,y,pw,h)

    sdl2.ext.fill(surface, bgColor, rect1)
    sdl2.ext.fill(surface, fgColor, rect2)


def renderHPBar1(x, y, w, h, health, fgColor, bgColor, surface):
    if health > 18:
        health = 1
    elif health < 0:
        health = 0

    rect1 = (x,y,w,h)

    pw = w * (health/18)
    pw = pw
    #px = x + (w - pw)
    rect2 = (x,y,pw,h)

    sdl2.ext.fill(surface, bgColor, rect1)
    sdl2.ext.fill(surface, fgColor, rect2)

def moveMissile(missile):
    missile.sprite.x += missile.sprite.vx


def check_cooldown(now_time, last_fire_time):
    return float(now_time) - float(last_fire_time)


def isCollision(mx,my,mwidth,cx,cy,cheight):
    # right side of missile is more than left of character
    # top of missile is less than bottom of character and more than top of character

    #print(mx + mwidth, cx)
    if (mx + mwidth >= cx) and (mx + mwidth <= cx + 10) and (my < cy + cheight) and (my > cy):
        return True
    else:
        return False


def run():
    sdl2.ext.init()

    window = sdl2.ext.Window("Health Damage Speed", size=(900, 800))
    window.show()

    factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
    sprite1 = factory.from_image(RESOURCES.get_path("bunny.bmp"))
    sprite2 = factory.from_image(RESOURCES.get_path("monkey.bmp"))

    win1 = factory.from_image(RESOURCES.get_path("winner1.bmp"))
    win2 = factory.from_image(RESOURCES.get_path("winner2.bmp"))

    win1.position = 450 - 140, 400 - 100
    win2.position = 450 - 140, 400 - 100

    world = sdl2.ext.World()

    spriterenderer = SoftwareRenderSystem(window)
    context = sdl2.ext.Renderer(window)
    world.add_system(spriterenderer)

    windowsurface = window.get_surface()

    player1 = Player(world, sprite1, 15, 5, 5, 0, 250)
    player2 = Player(world, sprite2, 8, 10, 2, 790, 250)
    #player1 = Player(world, sprite1, 5, 15, 5, 0, 250)
    #player2 = Player(world, sprite2, 10, 6, 4, 790, 250)

    missileSprite1 = factory.from_color(RED, size=(player1.sprite.playerdata.damage * 5,
                                                   player1.sprite.playerdata.damage * 5))
    missileSprite2 = factory.from_color(BLUE, size=(player2.sprite.playerdata.damage * 5,
                                                    player2.sprite.playerdata.damage * 5))
    missileSprite1_2 = factory.from_color(RED, size=(player1.sprite.playerdata.damage * 5,
                                                   player1.sprite.playerdata.damage * 5))
    missileSprite2_2 = factory.from_color(BLUE, size=(player2.sprite.playerdata.damage * 5,
                                                    player2.sprite.playerdata.damage * 5))
    missileSprite1_3 = factory.from_color(RED, size=(player1.sprite.playerdata.damage * 5,
                                                   player1.sprite.playerdata.damage * 5))
    missileSprite2_3 = factory.from_color(BLUE, size=(player2.sprite.playerdata.damage * 5,
                                                    player2.sprite.playerdata.damage * 5))

    player1missiles = []
    player2missiles = []
    player1missiles2 = []
    player2missiles2 = []
    player1missiles3 = []
    player2missiles3 = []

    last_fire_time1 = 0
    last_fire_time1_1 = 0
    last_fire_time2 = 0
    last_fire_time2_1 = 0


    #sdl2.ext.fill(windowsurface, WHITE)
    #renderHPBar1(30, 10, 400, 40, 1, GREEN, BLACK, windowsurface)
    #renderHPBar2(480, 10, 400, 40, 1, GREEN, BLACK, windowsurface)

    hit2 = False
    hit1 = False
    player1win = False
    player2win = False

    #font = sdl2.ext.BitmapFont(windowsurface, (100, 100))

    #playername = sdl2.sdlttf.TTF_RenderText_Solid(font, "Player 1", (255, 255, 255))

    if SDL_Init(SDL_INIT_AUDIO) != 0:
        raise RuntimeError("Cannot initialize audio system: {}".format(SDL_GetError()))

    sound_file = RESOURCES.get_path("music.wav")
    sound = WavSound(sound_file)
    devid = SDL_OpenAudioDevice(None, 0, sound.spec, None, 0)

    missile_file = RESOURCES.get_path("shoot2.wav")
    missileSound = WavSound(missile_file)
    devid2 = SDL_OpenAudioDevice(None, 0, missileSound.spec, None, 0)


    if devid == 0:
        raise RuntimeError("Unable to open audio device: {}".format(SDL_GetError()))

    shot = False
    #SDL_PauseAudioDevice(devid, 0)

    running = True
    while running:
        #SDL_PauseAudioDevice(devid2, 0)
        sdl2.ext.fill(windowsurface, WHITE)
        renderHPBar1(30, 10, 400, 40, player1.sprite.playerdata.health, GREEN, BLACK, windowsurface)
        renderHPBar2(480, 10, 400, 40, player2.sprite.playerdata.health, GREEN, BLACK, windowsurface)

        #font.render_on(windowsurface, "player 1", (30, 30))
        #font.render("Player1")

        now_time = time.time()

        if len(player1missiles) > 0:
            missile = player1missiles[0]
            moveMissile(player1missiles[0])
            if isCollision(missile.sprite.x, missile.sprite.y, missileSprite1.size[0], player2.sprite.x,
                           player2.sprite.y, 120):
                hit2 = True
            if player1missiles[0].sprite.x >= 900 + missileSprite1.size[0]:
                player1missiles.pop(0)

        if len(player1missiles2) > 0:
            missile = player1missiles2[0]
            moveMissile(player1missiles2[0])
            if isCollision(missile.sprite.x, missile.sprite.y, missileSprite1.size[0], player2.sprite.x,
                           player2.sprite.y, 120):
                hit2 = True
            if player1missiles2[0].sprite.x >= 900 + missileSprite1_2.size[0]:
                player1missiles2.pop(0)

        if len(player1missiles3) > 0:
            missile = player1missiles3[0]
            moveMissile(player1missiles3[0])
            if isCollision(missile.sprite.x, missile.sprite.y, missileSprite1.size[0], player2.sprite.x,
                           player2.sprite.y, 120):
                hit2 = True
            if player1missiles3[0].sprite.x >= 900 + missileSprite1_3.size[0]:
                player1missiles3.pop(0)

        if len(player2missiles) > 0:
            missile = player2missiles[0]
            moveMissile(player2missiles[0])
            if isCollision(missile.sprite.x, missile.sprite.y, missileSprite2.size[0], player1.sprite.x,
                           player1.sprite.y, 120):
                hit1 = True
            if player2missiles[0].sprite.x <= 0 - missileSprite2.size[0]:
                player2missiles.pop(0)

        if len(player2missiles2) > 0:
            missile = player2missiles2[0]
            moveMissile(player2missiles2[0])
            if isCollision(missile.sprite.x, missile.sprite.y, missileSprite2.size[0], player1.sprite.x,
                           player1.sprite.y, 120):
                hit1 = True
            if player2missiles2[0].sprite.x <= 0 - missileSprite2_2.size[0]:
                player2missiles2.pop(0)

        if len(player2missiles3) > 0:
            missile = player2missiles3[0]
            moveMissile(player2missiles3[0])
            if isCollision(missile.sprite.x, missile.sprite.y, missileSprite2.size[0], player1.sprite.x,
                           player1.sprite.y, 120):
                hit1 = True
            if player2missiles3[0].sprite.x <= 0 - missileSprite2_3.size[0]:
                player2missiles3.pop(0)


        for event in sdl2.ext.get_events():
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            #if event.type == sdl2.SDL_KEYDOWN:
                #if event.key.keysym.sym == sdl2.SDLK_SPACE:

        keystatus = sdl2.SDL_GetKeyboardState(None)

        if keystatus[sdl2.SDL_SCANCODE_SPACE]:
            if len(player1missiles) == 0:
                missile1 = Missile(world, missileSprite1, player1.sprite.playerdata.damage, 8,
                                   player1.sprite.x + 50,
                                   player1.sprite.y + 60 - int(missileSprite1.size[0]/2))
                player1missiles.append(missile1)
                last_fire_time1 = time.time()
                last_fire_time1_1 = time.time()
                SDL_CloseAudioDevice(devid2)
                missileSound = WavSound(missile_file)
                devid2 = SDL_OpenAudioDevice(None, 0, missileSound.spec, None, 0)
                SDL_PauseAudioDevice(devid2, 0)
            if check_cooldown(now_time, last_fire_time1) > .2:
                if len(player1missiles2) == 0:
                    missile2 = Missile(world, missileSprite1_2, player1.sprite.playerdata.damage, 8,
                                       player1.sprite.x + 50,
                                       player1.sprite.y + 60 - int(missileSprite1.size[0]/2))
                    player1missiles2.append(missile2)
                    last_fire_time1 = time.time()
                    last_fire_time1_1 = time.time()
                    SDL_CloseAudioDevice(devid2)
                    missileSound = WavSound(missile_file)
                    devid2 = SDL_OpenAudioDevice(None, 0, missileSound.spec, None, 0)
                    SDL_PauseAudioDevice(devid2, 0)
            if check_cooldown(now_time, last_fire_time1_1) > .2:
                if len(player1missiles3) == 0:
                    missile3 = Missile(world, missileSprite1_3, player1.sprite.playerdata.damage, 8,
                                       player1.sprite.x + 50,
                                       player1.sprite.y + 60 - int(missileSprite1.size[0]/2))
                    player1missiles3.append(missile3)
                    last_fire_time1_1 = time.time()
                    last_fire_time1 = time.time()
                    SDL_CloseAudioDevice(devid2)
                    missileSound = WavSound(missile_file)
                    devid2 = SDL_OpenAudioDevice(None, 0, missileSound.spec, None, 0)
                    SDL_PauseAudioDevice(devid2, 0)
        # shoot a missile based on character damage
        if keystatus[sdl2.SDL_SCANCODE_RETURN]:
            if len(player2missiles) == 0:
                missile1 = Missile(world, missileSprite2, player2.sprite.playerdata.damage, -8,
                                    player2.sprite.x + 50,
                                    player2.sprite.y + 60 - int(missileSprite2.size[0]/2))
                player2missiles.append(missile1)
                last_fire_time2 = time.time()
                last_fire_time2_1 = time.time()
                SDL_CloseAudioDevice(devid2)
                missileSound = WavSound(missile_file)
                devid2 = SDL_OpenAudioDevice(None, 0, missileSound.spec, None, 0)
                SDL_PauseAudioDevice(devid2, 0)
            if check_cooldown(now_time, last_fire_time2) > .2:
                if len(player2missiles2) == 0:
                    missile2 = Missile(world, missileSprite2_2, player2.sprite.playerdata.damage, -8,
                                    player2.sprite.x + 50,
                                    player2.sprite.y + 60 - int(missileSprite2.size[0]/2))
                    player2missiles2.append(missile2)
                    last_fire_time2 = time.time()
                    last_fire_time2_1 = time.time()
                    SDL_CloseAudioDevice(devid2)
                    missileSound = WavSound(missile_file)
                    devid2 = SDL_OpenAudioDevice(None, 0, missileSound.spec, None, 0)
                    SDL_PauseAudioDevice(devid2, 0)

            if check_cooldown(now_time, last_fire_time2_1) > .2:
                if len(player2missiles3) == 0:
                    missile3 = Missile(world, missileSprite2_3, player2.sprite.playerdata.damage, -8,
                                    player2.sprite.x + 50,
                                    player2.sprite.y + 60 - int(missileSprite2.size[0]/2))
                    player2missiles3.append(missile3)
                    last_fire_time2_1 = time.time()
                    last_fire_time2 = time.time()
                    SDL_CloseAudioDevice(devid2)
                    missileSound = WavSound(missile_file)
                    devid2 = SDL_OpenAudioDevice(None, 0, missileSound.spec, None, 0)
                    SDL_PauseAudioDevice(devid2, 0)
        if keystatus[sdl2.SDL_SCANCODE_W]:
            player1.vy = player1.sprite.playerdata.speed
            if player1.sprite.y <= 100:
                player1.sprite.y = player1.sprite.y
            else:
                player1.sprite.y -= 4 + (player1.sprite.playerdata.speed)

        if keystatus[sdl2.SDL_SCANCODE_S]:
            player1.vy = player1.sprite.playerdata.speed
            if player1.sprite.y >= 620:
                player1.sprite.y = player1.sprite.y
            else:
                player1.sprite.y += 4 + (player1.sprite.playerdata.speed)

        if keystatus[sdl2.SDL_SCANCODE_UP]:
            player2.vy = player2.sprite.playerdata.speed
            if player2.sprite.y <= 100:
                player2.sprite.y = player2.sprite.y
            else:
                player2.sprite.y -= 4 + (player2.sprite.playerdata.speed)

        if keystatus[sdl2.SDL_SCANCODE_DOWN]:
            player2.vy = player2.sprite.playerdata.speed
            if player2.sprite.y >= 620:
                player2.sprite.y = player2.sprite.y
            else:
                player2.sprite.y += 4 + (player2.sprite.playerdata.speed)

        if hit2:
            print("called")
            player2.sprite.playerdata.health -= math.ceil(player1.sprite.playerdata.damage/2)
            hit2 = False

        if hit1:
            print("called")
            player1.sprite.playerdata.health -= math.ceil(player2.sprite.playerdata.damage/2)
            hit1 = False

        if player1.sprite.playerdata.health <= 0:
            #spriterenderer.render(win2)
            player2win = True
            #running = False
        elif player2.sprite.playerdata.health <= 0:
            #spriterenderer.render(win1)
            player1win = True
            #running = False

        if player1win:
            spriterenderer.render(win1)
            player1.sprite.x = 1100
            player2.sprite.x = -200
            SDL_PauseAudioDevice(devid, 0)
        elif player2win:
            spriterenderer.render(win2)
            player1.sprite.x = 1100
            player2.sprite.x = -200
            SDL_PauseAudioDevice(devid, 0)

        if sound.done:
            SDL_CloseAudioDevice(devid)

        sdl2.SDL_Delay(10)

        world.process()

        #processor = sdl2.ext.TestEventProcessor()
        #processor.run(window)
        #sdl2.ext.quit()
        #return 0

if __name__ == "__main__":
    sys.exit(run())
