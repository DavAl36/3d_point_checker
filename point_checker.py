import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import ConvexHull
from scipy.spatial import Delaunay

# Check if a point i inside or outside respect to a point cloud
def point_in(test_point, cloud_points):
  ax.plot(test_point[0],test_point[1],test_point[2],'go') if Delaunay(cloud_points).find_simplex(test_point) >= 0 else ax.plot(test_point[0],test_point[1],test_point[2],'ro')

# Generate n 3D random points
def point_3d_generator(n):
    points = np.empty((n, 3))
    for i in range(n):
        x = random.uniform(x_min, x_max)
        y = random.uniform(y_min, y_max)
        z = random.uniform(z_min, z_max)
        points[i] = [x, y, z]
    return points

################################# 3D environment dimension #################################
x_min = -10
x_max = 16
y_min = -1
y_max = 5
z_min = -5
z_max = 5
################################## point clouds of 3 figure ################################
cloud_points_1 = np.array([
            [-4,0,0],
            [4,0,0],
            [4,4,0],
            [-4,4,0],
            [4,0,4],
            [4,4,4]])

cloud_points_2 = np.array([
            [8,0,0],
            [4,0,0],
            [4,4,0],
            [8,4,0],
            [8,0,4],
            [4,0,4],
            [4,4,4],
            [8,4,4]])

cloud_points_3 = np.array([
            [8,0,0],
            [14,0,0],
            [14,4,0],
            [8,4,0],
            [8,0,4],
            [14,0,4],
            [14,4,4],
            [8,4,4]])



if __name__ == "__main__":

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	# Concat used for check
	concat = np.concatenate((cloud_points_1, cloud_points_2, cloud_points_3))
	# fig_list used for plot
	fig_list = [cloud_points_1, cloud_points_2, cloud_points_3]
	
	for fig in fig_list:
	  hull=ConvexHull(fig)
	  edges= list(zip(*fig))
	  color = 'k'
	  for i in hull.simplices[2:]:
	      plt.plot(fig[i,0], fig[i,1], fig[i,2], color + '-')
	  ax.plot(edges[0],edges[1],edges[2],color + 'o')


	ax.set_xlabel('x')
	ax.set_ylabel('y')
	ax.set_zlabel('z')
	ax.set_xlim3d(x_min,x_max)
	ax.set_ylim3d(y_min,y_max)
	ax.set_zlim3d(z_min,z_max)

	# Check if the point lies within poly
	test_points = point_3d_generator(40)
	for point in test_points:
	    point_in(point, concat)

	plt.show()


