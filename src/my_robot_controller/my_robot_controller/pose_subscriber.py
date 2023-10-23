#!/usr/bin/env python3

import rclpy
from rclpy.node import Node 
from turtlesim.msg import Pose


class PoseSubscriberNode(Node):
    
    def __init__(self):
        super().__init__("pose_subscriber")
        self.pose_subscriber = self.create_subscription(
            msg_type=Pose,
            topic="/turtle1/pose",
            callback=self.pose_callback,
            qos_profile=10, # queue size
        )

    def pose_callback(self, msg: Pose):
        self.get_logger().info(f"({str(msg.x)}, {str(msg.y)})")



def main(args=None):
    rclpy.init(args=args)
    node = PoseSubscriberNode()
    rclpy.spin(node) # node is running until killed
    rclpy.shutdown()