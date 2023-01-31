import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from sensor_msgs.msg import Range
import random
#from tf2 import transformations
#import tf2

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Range, 'topic', 10)
        self.publisher_imu = self.create_publisher(Imu, 'topic_imu', 10)
        
        self.ranges = [float('NaN'), 1.0, -float('Inf'), 3.0, float('Inf')]
        self.min_range = 0.01
        self.max_range = 0.5
        
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Range()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.radiation_type = 0
        msg.field_of_view = 0.1
        msg.min_range = self.min_range
        msg.max_range = self.max_range
        msg.range = random.uniform(0.01, 0.15)
        
        # msg.header.frame_id = "/ultrasonic_sensor_link"
        # self.publisher_.publish(msg)
        
        msg.header.frame_id = "/ultrasonic_sensor_test_link"
        
        #self.publisher_.publish(msg)
        #self.get_logger().info('Publishing: "%s"' % msg)
        #self.i += 1
        
        self.torsoIMU = Imu()
        self.torsoIMU.header.frame_id = "/imu_link"
        
        self.torsoIMU.header.stamp = self.get_clock().now().to_msg()
        
        memData = [1.0,2.0,3.0,3.0,2.0,1.0,1.0,2.0,3.1,2.1]
        
        #self.torsoIMU.orientation.x = q[0]
        #self.torsoIMU.orientation.y = q[1]
        #self.torsoIMU.orientation.z = q[2]
        #self.torsoIMU.orientation.w = q[3]
        self.torsoIMU.angular_velocity.x = random.uniform(0.1, 4)
        self.torsoIMU.angular_velocity.y = random.uniform(0.1, 4)
        self.torsoIMU.angular_velocity.z = random.uniform(0.1, 4)
        self.torsoIMU.linear_acceleration.x = random.uniform(0.1, 4)
        self.torsoIMU.linear_acceleration.y = random.uniform(0.1, 4)
        self.torsoIMU.linear_acceleration.z = random.uniform(0.1, 4)
        
        self.publisher_imu.publish(self.torsoIMU)
        self.get_logger().info('Publishing: "%s"' % msg)
     
    def pub_imu(self):
    	
    	pass
	    #self.dataNamesList = ["DCM/Time",
        #                    "Device/SubDeviceList/InertialSensor/AngleX/Sensor/Value","Device/SubDeviceList/InertialSensor/AngleY/Sensor/Value",
        #                    "Device/SubDeviceList/InertialSensor/AngleZ/Sensor/Value",
        #                    "Device/SubDeviceList/InertialSensor/GyroscopeX/Sensor/Value", "Device/SubDeviceList/InertialSensor/GyroscopeY/Sensor/Value",
        #                    "Device/SubDeviceList/InertialSensor/GyroscopeZ/Sensor/Value",
        #                    "Device/SubDeviceList/InertialSensor/AccelerometerX/Sensor/Value", "Device/SubDeviceList/InertialSensor/AccelerometerY/Sensor/Value",
        #                    "Device/SubDeviceList/InertialSensor/AccelerometerZ/Sensor/Value"]
                            
    	#self.torsoIMU = Imu()
		#self.torsoIMU.header.frame_id = "/imu_link"
		
		# IMU data:
        #self.torsoIMU.header.stamp = self.get_clock().now().to_msg()
		
		#memData = [1,2,3,3,2,1,1,2,3]
		#q = transformations.quaternion_from_euler(memData[1], memData[2], memData[3])
		
		#self.torsoIMU.orientation.x = q[0]
		#self.torsoIMU.orientation.y = q[1]
		#self.torsoIMU.orientation.z = q[2]
		#self.torsoIMU.orientation.w = q[3]

		#self.torsoIMU.angular_velocity.x = memData[4]
		#self.torsoIMU.angular_velocity.y = memData[5]
		#self.torsoIMU.angular_velocity.z = memData[6] # currently always 0

		#self.torsoIMU.linear_acceleration.x = memData[7]
		#self.torsoIMU.linear_acceleration.y = memData[8]
		#self.torsoIMU.linear_acceleration.z = memData[9]

		# covariances unknown
		# cf http://www.ros.org/doc/api/sensor_msgs/html/msg/Imu.html
		#self.torsoIMU.orientation_covariance[0] = -1
		#self.torsoIMU.angular_velocity_covariance[0] = -1
		#self.torsoIMU.linear_acceleration_covariance[0] = -1

		#self.torsoIMUPub.publish(self.torsoIMU)

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    minimal_publishemsg.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
