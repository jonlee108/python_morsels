import math

class Circle(object):

	def __init__(self, radius: int = 1):
		self.radius = radius
		self._update_properties()

	def _update_properties(self):
		# print("update called, radius={}, _radius={}".format(self.radius, self._radius))
		self._diameter = self._radius * 2
		self._area = (math.pi) * ((self._radius) ** 2)

	@property
	def radius(self):
		return self._radius
	
	@radius.setter
	def radius(self, val):
		if val >= 0:
			self._radius = val
			self._update_properties()
		else:
			raise ValueError("Radius cannot be negative")
	@property
	def diameter(self):
		return self._diameter
	
	@diameter.setter
	def diameter(self, val):
		if val >= 0:
			self._radius = val/2
			self._update_properties()
		else:
			raise ValueError("Diameter cannot be negative")

	@property
	def area(self):
		return self._area

	@area.setter
	def area(self, val):
		raise AttributeError
	
	def __repr__(self):
		# message = f"radius: {self.radius}\n" \
		# 		f"diameter: {self.diameter}\n" \
		# 		f"area: {self.area}"
		message = f"Circle({self.radius})"
		return message

	def toString(self):
		print("radius: {}".format(self.radius))
		print("diameter: {}".format(self.diameter))
		print("area: {}".format(self.area))
		
if __name__ == "__main__":
	print("\nc1")
	c = Circle(5)
	print(c)

	print("\nc2")
	c2 = Circle(2)
	print(c2)
	print("changing radius to 3")
	c2.radius = 3
	print(c2)
	c2.toString()

	print("\nc3")
	c3 = Circle(10)
	print(c3)
	print("changing diameter to 100")
	c3.diameter = 100
	print(c3)

	# print("\nc4")
	# c4 = Circle(10)
	# print(c4)
	# print("changing area to 10")
	# c4.area= 10
	# print(c4)

	print("\nc5")
	c4 = Circle(-5)
	print(c4)
	