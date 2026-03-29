# ---------------------------------------------------------------------------
# FILE: tamil_publisher.py
# ROLE: The "Tamil Subject" node — a PUBLISHER
#       It sends a new lesson message every 2 seconds on the /tamil topic
# ---------------------------------------------------------------------------

# rclpy is the main ROS 2 Python library
# Think of it like "express" in Node.js — it gives you all the ROS 2 tools
import rclpy

# Node is the base class for every ROS 2 node
# All your nodes will inherit from this class
from rclpy.node import Node

# String is the message type we are sending
# ROS 2 has many message types (String, Int32, Float64, Image, etc.)
# We use String because our lesson content is plain text
from std_msgs.msg import String


# ---------------------------------------------------------------------------
# Every node is a Python class that inherits from Node
# Think of Node as a base class — like extending a framework's BaseController
# ---------------------------------------------------------------------------
class TamilPublisher(Node):

    def __init__(self):
        # ---------------------------------------------------------------------------
        # super().__init__('tamil_subject')
        # This registers our node with ROS 2 under the name 'tamil_subject'
        # This name appears when you run: ros2 node list
        # ---------------------------------------------------------------------------
        super().__init__('tamil_subject')

        # ---------------------------------------------------------------------------
        # create_publisher() sets up a channel to SEND messages
        # Arguments:
        #   String     → the type of message we will send (plain text)
        #   '/tamil'   → the topic name — like a channel name in Redis pub/sub
        #   10         → queue size — how many messages to buffer if receiver is slow
        # ---------------------------------------------------------------------------
        self.publisher_ = self.create_publisher(String, '/tamil', 10)

        # ---------------------------------------------------------------------------
        # create_timer() calls our function repeatedly on a schedule
        # Arguments:
        #   2.0                      → every 2.0 seconds
        #   self.publish_lesson      → the function to call each time
        # Think of this like setInterval(publishLesson, 2000) in JavaScript
        # ---------------------------------------------------------------------------
        self.timer = self.create_timer(2.0, self.publish_lesson)

        # A counter so each message is unique and we can track order
        self.lesson_number = 1

        # This prints to terminal when the node first starts
        self.get_logger().info('Tamil Subject node started — publishing to /tamil')

    def publish_lesson(self):
        # ---------------------------------------------------------------------------
        # String() creates a new empty message object of type String
        # It has one field called .data where we put our actual content
        # ---------------------------------------------------------------------------
        msg = String()
        msg.data = f'Tamil Lesson {self.lesson_number}: vowels — அ ஆ இ ஈ'

        # ---------------------------------------------------------------------------
        # publish() sends the message onto the /tamil topic
        # Anyone subscribed to /tamil will instantly receive it
        # ---------------------------------------------------------------------------
        self.publisher_.publish(msg)

        # Log to terminal so we can see it working
        self.get_logger().info(f'Published → {msg.data}')

        self.lesson_number += 1


# ---------------------------------------------------------------------------
# main() is the entry point — ROS 2 calls this when you run the node
# ---------------------------------------------------------------------------

def main(args=None):
    # rclpy.init() boots up the ROS 2 communication system
    # Always the first line in main()
    rclpy.init(args=args)

    # Create an instance of our node class
    node = TamilPublisher()

    # ---------------------------------------------------------------------------
    # rclpy.spin() keeps the node alive and listening
    # Without this, the node would start and immediately shut down
    # Think of it like app.listen(3000) in Express — keeps the process running
    # ---------------------------------------------------------------------------
    rclpy.spin(node)

    # Clean up when the node is stopped (Ctrl+C)
    node.destroy_node()
    rclpy.shutdown()
