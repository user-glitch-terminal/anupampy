# By Anupam Ghimire

A Python first-person shooter game inspired by DOOM, built using Pygame and raycasting techniques.

## Controls
| W | Move forward |
| S | Move backward |
| A | Strafe left |
| D | Strafe right |
| Mouse | Look around |
| Left Click | Shoot |
| ESC | Quit game |

## Project Structure


| `main.py` | Entry point. Initializes Pygame, creates the game window, and runs the main game loop (events → update → draw). |
| `settings.py` | Contains all game constants: resolution, player speed, FOV, texture size, raycasting parameters, etc. 

| `player.py` | Handles player movement, mouse look, wall collision, health system, and shooting mechanics. |
| `map.py` | Defines the game world as a 2D grid. Walls are represented by numbers (1-5) corresponding to different textures. |
| `raycasting.py` | The heart of the 3D rendering. Casts rays from player's position to detect walls and calculates wall heights for pseudo-3D effect. |
| `object_renderer.py` | Renders the game visuals: sky, floor, walls (using textures), health display, and game over/win screens. |

| `sprite_object.py` | Base classes for all sprites. `SpriteObject` handles static sprites, `AnimatedSprite` adds animation support. |
| `npc.py` | Enemy AI classes (SoldierNPC, CacoDemonNPC, CyberDemonNPC). Handles pathfinding, attacking, pain/death animations, and player detection via raycasting. |
| `object_handler.py` | Manages all sprites and NPCs. Spawns enemies randomly, updates all entities, and checks win condition. |
| `weapon.py` | Player's weapon (shotgun). Handles shooting animation and damage values. |

| File | Description |
|------|-------------|
| `pathfinding.py` | A* or BFS pathfinding for NPC navigation through the maze. |
| `sound.py` | Audio management for sound effects and music. |

@ Ray casting
1. For each vertical screen column, cast a ray from the player
2. Check intersections with horizontal and vertical grid lines
3. Find the nearest wall hit
4. Calculate wall height based on distance (closer = taller)
5. Apply fish-eye correction using cosine
6. Sample the correct texture column based on hit position

### Game Loop

# NPC Behavior

1. **Idle**: Stand still, play idle animation
2. **Detection**: Raycast to check if player is visible
3. **Chase**: Use pathfinding to navigate toward player
4. **Attack**: When in range, play attack animation and deal damage
5. **Pain**: React to being shot
6. **Death**: Play death animation when health reaches 0


