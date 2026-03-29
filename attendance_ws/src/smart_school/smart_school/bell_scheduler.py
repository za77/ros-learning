import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class BellScheduler(Node):
    
    def __init__(self):
        super().__init__('bell_scheduler')
        self.publisher = self.create_publisher(String,'/school/bell_status',10)
        self.bell_count = 1
        self.declare_parameter('school_name', 'Default School')
        self.declare_parameter('max_students', 30)
        self.declare_parameter('bell_interval_seconds', 10)
        timer  = self.get_parameter('bell_interval_seconds').value
        school = self.get_parameter('school_name').value
        self.get_logger().info(f'BELL RANG {school}')
        self.timer = self.create_timer(timer, self.publish_bell)
        
    def publish_bell(self):
        msg = String()
        msg.data = f'BELL RANG — {self.bell_count}'
        self.publisher.publish(msg)
        self.bell_count += 1

    
def main(args=None):
    rclpy.init(args=args)
    node = BellScheduler()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()