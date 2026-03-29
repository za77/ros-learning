import rclpy
from rclpy.node import Node
from smart_school_interfaces.srv import AttendanceRequest # type: ignore


class AttendanceServer(Node):
    # Node is parent class in that case __init__ will override the Node constructor init to
    # avoid the main class override we use super().init()
    def __init__(self):
        # Calls the parent calls Node and pass the name
        super().__init__('calculator_service')
        self.register = {}
        self.declare_parameter('school_name', 'Default School')
        self.srv = self.create_service(AttendanceRequest,'mark_attendance',self.handle_req)
        
    def handle_req(self, req, res):
        self.get_logger().info(f'Request : {req.student_name } + {req.present} ')
        if not req.student_name:
            res.success = False
            res.message = 'Invalid Request'
            return res
        self.register[req.student_name] = req.present
        # Count only present students
        total = sum(1 for v in self.register.values() if v)
        res.success = True
        res.message = f'Stuendet {req.student_name }  Attendance is marked'
        res.total_present = total
        return res

    
def main(args = None):
    rclpy.init(args=args)
    node = AttendanceServer()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
