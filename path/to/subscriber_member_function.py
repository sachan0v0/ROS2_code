import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')#topic名は一致してないと受信できない
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)#msg_type, topic, callback, qos_profile, *, callback_group=None, event_callbacks=None, raw=False
               #If True, then received messages will be stored in raw binary representation.
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):#ddsはudpなので基本的にlisnercallbackは一生回ってる
        self.get_logger().info('I heard: "%s"' % msg.data)#コールバックはメッセージ受診時にすぐ呼び出される


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()