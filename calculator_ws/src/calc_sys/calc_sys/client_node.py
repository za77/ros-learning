import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class CalculatorClient(Node):
    def __init__(self):
        super().__init__('calculator_client')
        self.client = self.create_client(AddTwoInts, 'add_two_ints')
        
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn('Waiting for calculator Server...')
            
    def send_request(self,a,b):
        request = AddTwoInts.Request()
        request.a = a
        request.b = b
        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self,future)
        return future.result()
    
def main(args= None):
    rclpy.init(args= args)
    node = CalculatorClient()
    result = node.send_request(17,15)
    node.get_logger().info(f'Result " {result.sum}')
    rclpy.shutdown()

if __name__ == 'main':
    main()
