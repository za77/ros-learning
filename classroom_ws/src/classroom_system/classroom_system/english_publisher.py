# ---------------------------------------------------------------------------
# FILE: english_publisher.py
# ROLE: The "English Subject" node — a PUBLISHER
#       It sends a new lesson message every 3 seconds on the /english topic
#
# NOTICE: This file is almost identical to tamil_publisher.py
#         Only 3 things change:
#           1. The class name         → EnglishPublisher
#           2. The ROS 2 node name    → 'english_subject'
#           3. The topic name         → '/english'
#         That's the pattern. Learn it once, use it forever.
# ---------------------------------------------------------------------------

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class EnglishPublisher(Node):

    def __init__(self):
        # ---------------------------------------------------------------------------
        # Node name is 'english_subject'
        # This is different from tamil_subject — each node must have a unique name
        # If two nodes have the same name, ROS 2 will shut down the older one
        # ---------------------------------------------------------------------------
        super().__init__('english_subject')

        # ---------------------------------------------------------------------------
        # Topic is '/english' — completely separate channel from '/tamil'
        # Class A will never see these messages because it won't subscribe here
        # ---------------------------------------------------------------------------
        self.publisher_ = self.create_publisher(String, '/english', 10)

        # ---------------------------------------------------------------------------
        # We publish every 3 seconds — slightly different from Tamil's 2 seconds
        # This is intentional so you can see two publishers running at different
        # speeds in the terminal at the same time
        # ---------------------------------------------------------------------------
        self.timer = self.create_timer(3.0, self.publish_lesson)

        self.lesson_number = 1

        self.get_logger().info('English Subject node started — publishing to /english')

    def publish_lesson(self):
        msg = String()
        msg.data = f'English Lesson {self.lesson_number}: Alphabet — A B C D E'

        self.publisher_.publish(msg)

        self.get_logger().info(f'Published → {msg.data}')

        self.lesson_number += 1


def main(args=None):
    rclpy.init(args=args)
    node = EnglishPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()