#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import PointField
from sensor_msgs.msg import PointCloud2
from sensor_msgs import point_cloud2
from std_msgs.msg import Header
import sensor_msgs.point_cloud2 as pcl2
import numpy as np
import struct
import open3d as o3d

# Clone from https://github.com/eric-wieser/ros_numpy
import ros_numpy


def bin_to_pcd(binFileName):
    size_float = 4
    list_pcd = []
    with open(binFileName, "rb") as f:
        byte = f.read(size_float * 4)
        while byte:
            x, y, z, intensity = struct.unpack("ffff", byte)
            list_pcd.append([x, y, z])
            byte = f.read(size_float * 4)
    np_pcd = np.asarray(list_pcd)
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(np_pcd)
    return pcd
    
def callback(data):
    rospy.loginfo('Received a PointCloud2 message')
    
    pc = ros_numpy.numpify(data)

    print(pc.shape)
    points=np.zeros((pc.shape[0],pc.shape[1],4))
  
    points[:,:,0]=pc['x']
    points[:,:,1]=pc['y']
    points[:,:,2]=pc['z']
    points[:,:,3]=pc['intensity']

    # Add to
    p = np.array(points, dtype=np.float32)

    global pc_number
    pc_number += 1

    # Save files
    bin_file = f'/home/max/Desktop/bin/{pc_number}.bin'       
    pcd_file = f'/home/max/Desktop/pcd/{pc_number}.pcd'
    p.astype('float32').tofile(bin_file)
    pcd = bin_to_pcd(bin_file)

    o3d.io.write_point_cloud(pcd_file, pcd)



def listener():
    global pub
    global pc_number
    
    # Init pc number
    pc_number = 0
    
    rospy.init_node('pointcloud_to_bin_file', anonymous=True)

    # Subscribe to the input PointCloud2 topic
    input_cloud = 'ouster/points' # TODO: Change this to your pc topic
    rospy.Subscriber(input_cloud, PointCloud2, callback)

    # Create a publisher for the output PointCloud2 topic
    pub = rospy.Publisher('/output_cloud', PointCloud2, queue_size=10)

    rospy.spin()

if __name__ == '__main__':
    listener()
