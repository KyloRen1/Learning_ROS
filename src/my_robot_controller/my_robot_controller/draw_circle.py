#!/usr/bin/env python3

import rclpy 
from rclpy.node import Node 
from geometry_msgs.msg import Twist


class DrawCircleNode(Node):

    def __init__(self):
        super().__init__("draw_circle")
        # creating publisher 
        self.cmd_vel_pub = self.create_publisher(
            msg_type=Twist,
            topic="/turtle1/cmd_vel", 
            qos_profile=10, # queue size
        )
        self.timer = self.create_timer(0.5, self.send_velocity_command)
        self.get_logger().info("Draw circle node started")

    def send_velocity_command(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        self.cmd_vel_pub.publish(msg)    



def main(args=None):
    rclpy.init(args=args)
    node = DrawCircleNode()
    rclpy.spin(node) # node is running until killed
    rclpy.shutdown()

