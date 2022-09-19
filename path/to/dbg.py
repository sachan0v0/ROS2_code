import rclpy 
from rclpy.node import Node 
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from circle.msg import msg
import cv2
 
class Img_Sub(Node):
 
  def __init__(self):

    super().__init__('img_sub')
    self.subscription = self.create_subscription(Image, 'traffic_light_image_in', self.listener_callback, 10)
    self.subscription 
      
    self.br = CvBridge()
   
  def listener_callback(self, data):

    self.get_logger().info('Receiving video')
    current_frame = self.br.imgmsg_to_cv2(data)
    #x y radius 出力：認識結果（色（赤・青）：color，座標：x,y，半径：radius）→traffic_light_recognition_resultが飛んでくる
    #create_subscription で img_result.msg.msg<msgファイル名>にしたらあとは変数名で受信できる？
    #curent_frameのところraw_imgが入ればオッケー
    center_x = msg.circle_x
    center_y = msg.circle_y
    cv2.circle(current_frame, center=(center_x, center_y), radius= msg.radius, color= msg.color, thickness= 4, lineType= cv2.LINE_4, shift= 0)
    cv2.imshow("camera", current_frame)
    cv2.waitKey(1)
  
def main(args=None):
  
  rclpy.init(args=args)
  img_sub = Img_Sub()
  rclpy.spin(img_sub)
  img_sub.destroy_node()
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()
