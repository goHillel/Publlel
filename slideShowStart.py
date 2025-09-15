import pygame
import os
import time

# 1. Folder with downloaded images
folder = "images"
image_files = [os.path.join(folder, f) for f in os.listdir(folder)
               if f.lower().endswith((".png", ".jpg", ".jpeg"))]

if not image_files:
    print("No images found in folder!")
    exit()

# 2. Initialize Pygame
pygame.init()
info = pygame.display.Info()
screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN)
pygame.display.set_caption("Slideshow")

# 3. Show images in a loop
clock = pygame.time.Clock()
index = 0
delay = 5  # seconds per image

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    # Load image and scale to screen
    image = pygame.image.load(image_files[index])
    image = pygame.transform.scale(image, (info.current_w, info.current_h))
    screen.blit(image, (0, 0))
    pygame.display.flip()

    time.sleep(delay)
    index = (index + 1) % len(image_files)
