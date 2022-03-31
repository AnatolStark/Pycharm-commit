#  from Point import Point

#  point_1 = Point(1, 33)
#  point_2 = Point(4, -9)


#  print(point_1.x)

import point as pt

point_1 = pt.Point(1, 33, 'meters')
point_2 = pt.Point(4, -9, 'millimeters')

# print(point_1.x, point_1.y)  #  1 33
# print(point_2.x, point_2.y)  #  4 -9

# print(point_1.distance_to(point_2))  #   42.1070065428546
# print(point_2.distance_to(point_1))  #   42.1070065428546

# print(point_1.distance_to(point_1))   #  0.0

# print(point_1)   #  Point(1.00000, 33.000000)  pri def __str__(self):
# print(type(point_1))   # <class 'Point.Point'> pri def __str__(self):

point3D_1 = pt.Point3D(2, 4, 9, 'meters')
point3D_2 = pt.Point3D(5, 14, -29, 'millimeters')


print(point3D_1.distance_to(point3D_2))  # 39.408120990476064
print(point3D_1)  #  Point(2.00000, 4.000000, 9.00000)
print(point3D_1.hello())  #  Hello! My coords are:2.00000, 4.000000, 9.00000 - naslednik
print(point_1.hello())  #  Hello! My coords are:1.00000, 33.000000  -roditel
print(point_1.y)  #  33

print(point_1.get_units())  #  meters

point_1.set_units('centimeters')    #  set - ustanovit
print(point_1.get_units())  #  centimeters  #  get - poluchit