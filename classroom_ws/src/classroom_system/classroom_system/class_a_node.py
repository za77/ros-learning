# ---------------------------------------------------------------------------
# FILE: class_a_node.py
# ROLE: The "Class A" node — a SUBSCRIBER
#       It listens ONLY to /tamil topic and prints whatever it receives
#
# KEY DIFFERENCE FROM PUBLISHERS:
#   Publishers use → create_publisher() + create_timer()
#   Subscribers use → create_subscription()
#   A subscriber does not push — it just reacts when a message arrives
#   Think of it like an event listener: element.addEventListener('click', handler)
# ---------------------------------------------------------------------------

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class ClassANode(Node):

    def __init__(self):
        # ---------------------------------------------------------------------------
        # Node name is 'class_a'
        # This is what appears when you run: ros2 node list
        # ---------------------------------------------------------------------------
        super().__init__('class_a')

        # ---------------------------------------------------------------------------
        # create_subscription() sets up a channel to RECEIVE messages
        # Arguments:
        #   String                    → message type we expect to receive
        #   '/tamil'                  → the topic we are tuning into
        #   self.receive_tamil_lesson → the function to call when a message arrives
        #   10                        → queue size buffer (same as publisher)
        #
        # This is the key line — Class A is ONLY subscribing to /tamil
        # It has zero knowledge of /english — that topic simply does not exist
        # from Class A's perspective
        # ---------------------------------------------------------------------------
        self.subscription = self.create_subscription(
            String,
            '/tamil',
            self.receive_tamil_lesson,
            10
        )

        self.get_logger().info('Class A node started — listening to /tamil only')

    # ---------------------------------------------------------------------------
    # receive_tamil_lesson() is called automatically by ROS 2
    # every time a new message arrives on /tamil
    #
    # The parameter 'msg' is the message object sent by the publisher
    # msg.data contains the actual text string
    #
    # You never call this function yourself — ROS 2 calls it for you
    # Think of it like a callback in an event listener — it just waits and fires
    # ---------------------------------------------------------------------------
    def receive_tamil_lesson(self, msg):

        self.get_logger().info(
            f'Class A received Tamil lesson → {msg.data}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = ClassANode()

    # ---------------------------------------------------------------------------
    # spin() here keeps Class A alive and waiting
    # It sits quietly doing nothing until a /tamil message arrives
    # Then it fires receive_tamil_lesson() and goes back to waiting
    # This is exactly like an async event loop waiting for incoming requests
    # ---------------------------------------------------------------------------
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()