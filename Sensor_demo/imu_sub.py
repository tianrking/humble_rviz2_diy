import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
import random

class IMUSubscriber(Node):

    def __init__(self):
        super().__init__('imuSubscriber')
        self.subscription = self.create_subscription(
            Imu,
            'imu',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('nanosec: %d' %(msg.header.stamp.nanosec))


def main(args=None):
    rclpy.init(args=args)

    imuSubscriber = IMUSubscriber()

    rclpy.spin(imuSubscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    imuSubscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
