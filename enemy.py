import Vector
import game
import bullet

def BuckTarget(game, enemy, target, count, spread, speed, spriteName):
	t = target
	t.RotateAround(enemy.position, spread * (count - 1)/ 2
	for n in range(count):
		b = LinearBullet(enemy.position, t, speed, game, spriteName)
		t.RotateAround(enemy.position, -spread)

def BuckDown(game, enemy, count, spread, speed, spriteName):
	BuckTarget(game, enemy, Vector(10000, enemy.y) ,count, spread, speed, spriteName

def Tracers(game, enemy, player, count, frameOffset, speed, spriteName, frame = 0):
	if frame%frameOffset == 0:
		LinearBullet(enemy.position, player.position, speed, game, spriteName)
	frame+=1
	game.ticker.Queue("Tracers", game, enemy, player, count, frameOffset, speed, spriteName, frame)