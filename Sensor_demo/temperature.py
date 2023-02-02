import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Temperature
import random

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Temperature, 'topic', 10)
        
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Temperature()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.temperature = 1.0 
        msg.variance = 1.0 
        
        msg.header.frame_id = "/temperature_test_link"
        self.publisher_.publish(msg)
        
        self.get_logger().info('Publishing: "%s"' % msg)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    minimal_publishemsg.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
