class Point:
	def __init__(self, a=0, b=0):
		self.x = a;
		self.y = b;

def maxPoints(points):
	result = [];
	temp = [];
	count = 0

	if len(points) == 1:
		return 1;
	elif len(points) == 0:
		return 0;

	#print points
	for po1 in points:
		for po2 in points:
			if po1 not in temp:
				temp.append(po1);
			if po2 in temp:
				continue
			flag = False;
			for ps in result:
				if po1 in ps and po2 in ps:
					flag = True;
					break;
			if flag:
				continue;
			temp.append(po2);
			for po3 in points:
				count = count + 1;
				if po3 in temp:
					continue;
				det = po1.x*(po2.y - po3.y) + po2.x*(po3.y - po1.y) + po3.x*(po1.y - po2.y)
				print det;
				if det == 0:
					temp.append(po3);

			result.append(temp);
			temp = [];

	print result
	current = 0;
	for ps in result:
		if len(ps) > current:
			current = len(ps);

	return current;


a = []
a.append(Point(1,2))
a.append(Point(1,3))
a.append(Point(1,4))
a.append(Point(8,5))
a.append(Point(4,6))

a1= []
a1.append(Point(0,0))
a1.append(Point(0,0))

print maxPoints(a1);
