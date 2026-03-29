import rclpy
from rclpy.node import Node
from smart_school_interfaces.srv import AttendanceRequest


class AttendanceClient(Node):
    def __init__(self):
        super().__init__('attendance_client')

        self.client = self.create_client(
            AttendanceRequest,
            'mark_attendance'
        )

        # Always wait — never assume server is up
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn('Waiting for attendance server...')

    def send_request(self, student_name: str, present: bool):
        request = AttendanceRequest.Request()
        request.student_name = student_name
        request.present = present

        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        return future.result()


def main(args=None):
    rclpy.init(args=args)
    node = AttendanceClient()

    # Test with a few students
    students = [
        ('Alice', True),
        ('Bob', True),
        ('Charlie', False),
        ('Diana', True),
    ]

    for name, present in students:
        result = node.send_request(name, present)
        node.get_logger().info(
            f'Response → {result.message} | '
            f'Total present: {result.total_present}'
        )

    rclpy.shutdown()


if __name__ == '__main__':
    main()