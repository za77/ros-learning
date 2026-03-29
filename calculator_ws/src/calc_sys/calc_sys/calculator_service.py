import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class CalculatorService(Node):
    # Node is parent class in that case __init__ will override the Node constructor init to
    # avoid the main class override we use super().init()
    def __init__(self):
        # Calls the parent calls Node and pass the name
        super().__init__('calculator_service')
        self.srv = self.create_service(AddTwoInts,'add_two_ints',self.handle_req)
        
    def handle_req(self, req, res):
        res.sum = req.a + req.b
        self.get_logger().info(f'Request : {req.a} + {req.b} = {res.sum}')
        return res
    
def main(args = None):
    rclpy.init(args=args)
    node = CalculatorService()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
