#coding=utf-8
#2017.10.3,FLash, Project 1 main module

import pygame

from setting import Settings
from ship import Ship
import game_functions3 as gf
from pygame.sprite import Group
def run_game():
	ai_settings=Settings()
	
	#��ʼ����Ϸ������һ����Ļ����
	pygame.init()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	
	#����һ�ҷɴ�
	ship=Ship(ai_settings,screen)
	
	#����һ�����ڴ洢�ӵ��ı���
	bullets = Group()
	
	#��ʼ��Ϸ��ѭ��
	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()	
		gf.update_bullets(bullets)	
		gf.update_screen(ai_settings, screen, ship, bullets)
		
run_game()
