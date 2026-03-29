import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MonitorNode(Node):
    
    def __init__(self):
        super().__init__('monitor_node')
        self.subscription = self.create_subscription(String,'/school/bell_status',self.receive_bell,10)
        self.get_logger().info('MONITOR MODE')
        
    def receive_bell(self, msg):
        self.get_logger().info(f'INFO : → {msg.data}')
    
def main(args=None):
    rclpy.init(args=args)
    node = MonitorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()