import pygame
from pygame.locals import *
import sys
from random import randint
from pygame import surface
import time
import os

animation_directory = r'C:\\Users\\ctcar\\Documents\\CompSci\\GameDev\\selfgame\\Graphics\\Player_Graphics'

class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()

    self.jump = False
    self.facing_left = False
    self.facing_right = False

    sprite_lst = []
    self.animation_frames = []

    for filename in sorted(os.listdir(animation_directory), key = len):
      if filename.endswith('.png'):
        sprite_lst.append('Graphics/Player_Graphics/' + filename)

    for sprite in sprite_lst:
      alpha_sprite = pygame.image.load(sprite).convert_alpha()
      self.animation_frames.append(alpha_sprite)  

    self.sprite_idx = 0
    self.player_idle = self.animation_frames
    self.image = self.player_idle[self.sprite_idx]
    self.rect = self.image.get_rect(midbottom = (200,750))
    self.gravity = 0
    self.direction = pygame.math.Vector2(100,750)
    self.speed = 3



  

  def animation(self):
    if True:
      self.sprite_idx += 0.1
      if self.sprite_idx >= len(self.player_idle):
        self.sprite_idx = 0
      self.image = self.player_idle[int(self.sprite_idx)]

  def apply_player_gravity(self):
    self.gravity +=1
    self.rect.bottom += self.gravity
    if self.rect.bottom >= 750:
      self.rect.bottom = 750

  def player_input(self):
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
      self.direction.x = 1
      self.facing_right = True
      self.facing_left = False

    elif keys[pygame.K_a]:
      self.direction.x = -1
      self.facing_left = True
      self.facing_right = False
   
    else:
      self.direction.x = 0

    on_ground = False
    if self.rect.bottom == 750:
      on_ground = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and on_ground:
      self.gravity = -20

    
  def direction_facing(self):
    if self.facing_left:
       self.image = pygame.transform.flip(self.image, True, False)

    else:
      self.image = pygame.transform.flip(self.image, False, False)



    for tile in world.tile_list:
      if tile[1].colliderect(self.rect):
        print('collide')


  def update(self):
    
    self.animation()
    self.apply_player_gravity()
    self.player_input()
    self.rect.x += self.direction.x * self.speed
    self.direction_facing()

    pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)



   

class obstacle(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()

    Obstacle_directory = r'C:\\Users\\ctcar\\Documents\\CompSci\\GameDev\\selfgame\\Graphics\\Obstacles'

    obstacle_lst = []
    self.obstacle_frames = []

    for filename in sorted(os.listdir(Obstacle_directory), key = len):
      if filename.endswith('.png'):
        obstacle_lst.append('Graphics/Obstacles/' + filename)
      
    for sprite in obstacle_lst:
      alpha_sprite = pygame.image.load(sprite).convert_alpha()
      self.obstacle_frames.append(alpha_sprite)  


    y_pos = -20
    self.obstacle_idx = 0
    self.frames = self.obstacle_frames
    self.image = self.frames[self.obstacle_idx]
    self.rect = self.image.get_rect(midbottom = (randint(20, 800), y_pos))
 

  def obstacle_animation(self):
    self.obstacle_idx += 0.1
    if self.obstacle_idx >= len(self.frames):
      self.obstacle_idx = 0
    self.image = self.frames[int(self.obstacle_idx)]


  def destroy(self):
    if self.rect.y >=900: 
      self.kill()

  def update(self):
    self.obstacle_animation()
    self.rect.y += 4
    self.destroy()
    pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)

pygame.init()

screen_width = 1000
screen_height = 900

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('First Game')
clock = pygame.time.Clock()
game_active = False


tile_size = 50

class World():
    def __init__(self, data):
      
        self.tile_list = []

        # Load images
        Top_tile = pygame.image.load('Graphics/Tile-Images/Top-Tile.png')
        mid_tile = pygame.image.load('Graphics/Tile-Images/Mid-Tile.png')
        bot_tile = pygame.image.load('Graphics/Tile-Images/Bot-Tile.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                  img = pygame.transform.scale(Top_tile, (tile_size, tile_size))
                  img_rect = img.get_rect()
                  img_rect.x = col_count * tile_size
                  img_rect.y = row_count * tile_size
                  tile = (img, img_rect)
                  self.tile_list.append(tile)
               

                if tile == 2:
                  img = pygame.transform.scale(mid_tile, (tile_size, tile_size))
                  img_rect = img.get_rect()
                  img_rect.x = col_count * tile_size
                  img_rect.y = row_count * tile_size
                  tile = (img, img_rect)
                  self.tile_list.append(tile)


                
                if tile == 3:
                  img = pygame.transform.scale(bot_tile, (tile_size, tile_size))
                  img_rect = img.get_rect()
                  img_rect.x = col_count * tile_size
                  img_rect.y = row_count * tile_size
                  tile = (img, img_rect)
                  self.tile_list.append(tile)
                 
      
                col_count += 1
            row_count += 1

            
       
     
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            pygame.draw.rect(screen, (255, 255, 255), tile[1], 1)




 
      

world_data = [


[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
[0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0], 
[0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0],  

]


# def draw_grid():
#     for line in range(0, 20):
#         pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
#         pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))


player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()


sky_surface = pygame.image.load('Graphics/Tile-Images/Background.png').convert_alpha()


obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, randint(1200, 2500))

world = World(world_data)

game_active = True
while True: 
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    
    if game_active:
      if event.type == obstacle_timer:
        obstacle_group.add(obstacle())

  if game_active:

    screen.blit(sky_surface,(0,0))

    world.draw()
    # draw_grid()
  
    player.draw(screen)
    player.update()

    obstacle_group.draw(screen) 
    obstacle_group.update()


  pygame.display.update()
  clock.tick(60)



