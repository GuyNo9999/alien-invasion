import pygame #functions
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
	#Initialize a game and create a screen onject
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	#Make a ship, bullets and aliens
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens= Group()
	trees = Group()
	#Create a fleet
	gf.create_fleet(ai_settings, screen, ship, aliens)
	gf.create_forest(ai_settings, screen, trees)
	#Create an instance to store game statistics and create a scoreboard
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	#Make the Play Button
	play_button = Button(ai_settings, screen, "Play")
	#Start main loop for the game
	while True: 
		#Watch keyboard and mouse events.
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats,  sb, screen, ship, aliens, bullets)
			#Redraw the screem during each pass of the loop
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, trees, play_button)
	
run_game()
