import pygame
import colors

def draw_house(surface, x, y, size):
    house_width = size
    house_height = size // 1.5
    roof_height = size // 2
    door_width = size // 4
    door_height = size // 3
    window_size = size // 4
    chimney_width = size // 8
    chimney_height = size // 3
    
    # Draw the house base
    house_rect = pygame.Rect(x - house_width // 2, y, house_width, house_height)
    pygame.draw.rect(surface, (210, 180, 140), house_rect)  # Light brown house
    
    # Draw the roof
    roof_points = [(x - house_width // 2, y), (x + house_width // 2, y), (x, y - roof_height)]
    pygame.draw.polygon(surface, (165, 42, 42), roof_points)  # Brown roof
    
    # Draw the door
    door_rect = pygame.Rect((x * 1.05) - door_width // 2, y + house_height - door_height, door_width, door_height)
    pygame.draw.rect(surface, (139, 69, 19), door_rect)  # Dark brown door
    
    # Draw the window
    window_rect = pygame.Rect(x - house_width // 3, y + house_height // 4, window_size, window_size)
    pygame.draw.rect(surface, (173, 216, 230), window_rect)  # Light blue window
    pygame.draw.line(surface, (0, 0, 0), (window_rect.left, window_rect.centery), (window_rect.right, window_rect.centery), 2)
    pygame.draw.line(surface, (0, 0, 0), (window_rect.centerx, window_rect.top), (window_rect.centerx, window_rect.bottom), 2)
    
    # Draw the chimney
    chimney_rect = pygame.Rect(x + house_width // 4, y - roof_height + chimney_height // 2, chimney_width, chimney_height)
    pygame.draw.rect(surface, (139, 69, 19), chimney_rect)  # Dark brown chimney

def draw_tree(surface, x, y, size):
    trunk_width = size // 4
    trunk_height = size // 2
    foliage_radius = size // 4
            
    # Draw the trunk
    trunk_rect = pygame.Rect(x - trunk_width // 2, y, trunk_width, trunk_height)
    pygame.draw.rect(surface, (139, 69, 19), trunk_rect)
            
    # Draw the foliage (three overlapping circles)
    pygame.draw.circle(surface, (colors.FOREST_GREEN), (x, y - foliage_radius // 2), foliage_radius)
    pygame.draw.circle(surface, colors.FOREST_GREEN, (x - foliage_radius // 2, y - foliage_radius), foliage_radius)
    pygame.draw.circle(surface, (colors.FRESHLY_MOWED_GRASS), (x + foliage_radius // 2, y - foliage_radius), foliage_radius)

def draw_background(surface):
   
    width, height = surface.get_size()
    ground_level = height * 0.75
    hill_color = colors.WINDOWS_XP_GRASS_GREEN  # Green hills
    sky_color = (135, 206, 250)  # Sky blue
    
    # Fill background with sky color
    surface.fill(sky_color)
    
    # Draw rolling hills
    pygame.draw.ellipse(surface, hill_color, (width * 0.1, ground_level - height * 0.2, width * 0.4, height * 0.3))
    pygame.draw.ellipse(surface, hill_color, (width * 0.4, ground_level - height * 0.25, width * 0.5, height * 0.35))
    pygame.draw.ellipse(surface, hill_color, (-width * 0.2, ground_level - height * 0.15, width * 0.5, height * 0.25))
    
    # Draw the valley floor
    pygame.draw.rect(surface, hill_color, (0, ground_level, width, height * 0.25))

def draw_cloud(surface, x, y, size):
    cloud_color = colors.WHITE
    
    # Draw overlapping circles
    pygame.draw.circle(surface, cloud_color, (x, y), size)
    pygame.draw.circle(surface, cloud_color, (x + size // 2, y - size // 3), size * 0.8)
    pygame.draw.circle(surface, cloud_color, (x - size // 2, y - size // 3), size * 0.8)
    pygame.draw.circle(surface, cloud_color, (x + size // 3, y + size // 4), size * 0.6)
    pygame.draw.circle(surface, cloud_color, (x - size // 3, y + size // 4), size * 0.6)

import pygame

def draw_staircase(surface, x, y, step_size):
    step_color = (125, 196, 235)  # sky color offset
    
    for i in range(8):  # 8 steps
        pygame.draw.rect(surface, step_color, (x + i * step_size, y - i * step_size, step_size, step_size))
