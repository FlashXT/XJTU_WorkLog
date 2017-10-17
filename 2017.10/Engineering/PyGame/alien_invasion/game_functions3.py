#coding=utf-8
#2017.10.3,Flash,game_functions module

import sys
import pygame
from bullet import Bullet

def check_keydown_events(event,ai_settings, screen, ship, bullets):
	"""��Ӧ����"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
def check_keyup_events(event, ship):
	"""��Ӧ�ɿ�"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
def check_events(ai_settings, screen, ship, bullets):
	"""��Ӧ����������¼�"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)
			
def update_screen(ai_settings,screen,ship,bullets):
	"""������Ļ�ϵ�ͼ�񣬲��л�������Ļ"""
	screen.fill(ai_settings.bg_color)
	
	#�ڷɴ��������˺����ػ������ӵ�
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	
	#��������Ƶ���Ļ�ɼ�
	pygame.display.flip()
def update_bullets(bullets):
	"""�����ӵ���λ�ã���ɾ������ʧ���ӵ�"""
	# �����ӵ���λ��
	bullets.update()
	
    # ɾ������ʧ���ӵ�
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	
	
def fire_bullet(ai_settings, screen, ship, bullets):
	"""���δ�ﵽ���ƣ��ͷ���һ���ӵ�"""
	if len(bullets) < ai_settings.bullets_allowed:
			new_bullet = Bullet(ai_settings, screen, ship)
			bullets.add(new_bullet)	