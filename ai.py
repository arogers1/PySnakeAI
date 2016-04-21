import random
import cv2
import numpy as np

class AI(object):
	def __init__(self, sg):
		self.sg = sg
		self.wait_timer = random.randint(2,10)

	def get_input(self):
		self.surface_img = cv2.imread(self.sg.surface_img_path)
		apple = self.detect_apple()
		print "dir: " + str(self.sg.dirs)
		print "Apple: " + str(apple)
		snake = self.detect_snake()
		if len(snake) == 0 or len(apple) == 0:
			return
		max_x = np.max(snake[:,1])
		min_x = np.min(snake[:,1])
		max_y = np.max(snake[:,0])
		min_y = np.min(snake[:,0])
		print "snake: " + str((min_x,min_y,max_x,max_y))
		d = self.sg.dirs

		# UP or DOWN
		if d == 0 or d == 2:
			# Avoid walls
			if (d == 2 and min_y <= 21) or (d == 0 and max_y >= self.surface_img.shape[0] - 21):
				print "Going up/down and close to wall"
				if apple[1] > max_x:
					self.sg.dirs = 1
					print "go right to avoid wall"
				else:
					self.sg.dirs = 3
					print "go left to avoid wall"
			else:
				print "Going up/down and not close to wall"
				y_val = max_y if d == 2 else min_y
				# further away in x than in y
				if (apple[1] > max_x) and (apple[1] - max_x > abs(apple[0] - y_val)):
					self.sg.dirs = 1
					print "go right to approach apple"
				elif (apple[1] < min_x) and (min_x - apple[1] > abs(apple[0] - y_val)):
					self.sg.dirs = 3
					print "go left to approach apple"
		# LEFT OR RIGHT
		else:
			# Avoid walls
			if (d == 3 and min_x <= 21) or (d == 1 and max_x >= self.surface_img.shape[1] - 21):
				print "Going left/right and close to wall"
				if apple[1] > max_y:
					self.sg.dirs = 0
					print "go down to avoid wall"
				else:
					self.sg.dirs = 2
					print "go up to avoid wall"
			else:
				print "Going left/right and not close to wall"
				x_val = max_x if d == 1 else min_x
				# further away in x than in y
				if (apple[0] > max_y) and (apple[0] - max_y > abs(apple[1] - x_val)):
					self.sg.dirs = 0
					print "go down to approach apple"
				elif (apple[0] < min_y) and (min_y - apple[0] > abs(apple[1] - x_val)):
					self.sg.dirs = 2
					print "go up to approach apple"

		## RANDOM MOVEMENT
		# self.wait_timer -= 1
		# if self.wait_timer == 0:
		# 	if self.sg.dirs == 0 or self.sg.dirs == 2:
		# 		dirs = [1,3]
		# 	else:
		# 		dirs = [0,2]
		# 	self.sg.dirs = dirs[random.randint(0, 1)]
		# 	self.wait_timer = random.randint(2,10)

	def detect_snake(self):
		w = np.where((self.surface_img[:,:,2] == 255) & (self.surface_img[:,:,0] != 255))
		snake = np.stack((w[0],w[1]),1)
		return snake

	def detect_apple(self):
		w = np.where((self.surface_img[:,:,1] == 255) & (self.surface_img[:,:,0] != 255))
		return (w[0][0], w[1][0])
