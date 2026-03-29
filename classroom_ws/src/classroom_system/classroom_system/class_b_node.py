# ---------------------------------------------------------------------------
# FILE: class_b_node.py
# ROLE: The "Class B" node — a SUBSCRIBER
#       It listens to BOTH /tamil and /english topics
#
# KEY DIFFERENCE FROM CLASS A:
#   Class A has one create_subscription() call
#   Class B has two create_subscription() calls — one for each topic
#   Each topic gets its own separate callback function
#
#   A node can have as many subscriptions as you need
#   There is no limit — a real robot node might subscribe to 10+ topics
# ---------------------------------------------------------------------------

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class ClassBNode(Node):

    def __init__(self):
        # ---------------------------------------------------------------------------
        # Node name is 'class_b'
        # ---------------------------------------------------------------------------
        super().__init__('class_b')

        # ---------------------------------------------------------------------------
        # FIRST subscription — tuning into /tamil
        # When a /tamil message arrives → fires receive_tamil_lesson()
        # ---------------------------------------------------------------------------
        self.tamil_subscription = self.create_subscription(
            String,
            '/tamil',
            self.receive_tamil_lesson,
            10
        )

        # ---------------------------------------------------------------------------
        # SECOND subscription — tuning into /english
        # When an /english message arrives → fires receive_english_lesson()
        #
        # Notice: this is a completely separate subscription object
        # Both subscriptions run independently inside the same node
        # They do not interfere with each other
        # ---------------------------------------------------------------------------
        self.english_subscription = self.create_subscription(
            String,
            '/english',
            self.receive_english_lesson,
            10
        )

        self.get_logger().info(
            'Class B node started — listening to /tamil AND /english'
        )

    # ---------------------------------------------------------------------------
    # Called automatically when a /tamil message arrives
    # ---------------------------------------------------------------------------
    def receive_tamil_lesson(self, msg):

        self.get_logger().info(
            f'Class B received Tamil lesson   → {msg.data}'
        )

    # ---------------------------------------------------------------------------
    # Called automatically when an /english message arrives
    #
    # Notice this is a completely separate function from receive_tamil_lesson()
    # Each topic gets its own dedicated callback
    # This keeps your logic clean and separated — each callback has one job
    # ---------------------------------------------------------------------------
    def receive_english_lesson(self, msg):

        self.get_logger().info(
            f'Class B received English lesson → {msg.data}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = ClassBNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()