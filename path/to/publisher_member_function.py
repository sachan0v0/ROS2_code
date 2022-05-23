import rclpy #rclpyライブラリをインポート
from rclpy.node import Node #rclpyをインポートしてNodeクラスから継承

from std_msgs.msg import String #msg用のStringをクラスから持ってくる トピックに渡すデータを構造化するため
                                #xmlの依存関係に記述する必要あり


class MinimalPublisher(Node): #Nodeクラスからインスタンスを借りる　ノードから継承してminimal_pubを作成

    def __init__(self):#初期化 https://qiita.com/ishigen/items/2d8b6e6398743f2c8110
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10) #Stringをtopicに流す　10は品質　キューをどれだけ貯めるかどこまで保証するか
        timer_period = 0.5 #タイマーをインスタンス化　設定する　今回は0.5秒
        self.timer = self.create_timer(timer_period, self.timer_callback)# (timer_period_sec, callback, callback_group=None, clock=None)
        #The timer will be started and every timer_period_sec number of seconds the provided callback function will be called.
        #https://docs.ros2.org/latest/api/rclpy/api/node.html#rclpy.node.Node.create_timer
        self.i = 0 #加算で使う（パブリッシュの回数）変数を初期化してる？

    def timer_callback(self):
        msg = String()#String()関数をmsgにインスタンス化　あとで使うため
        msg.data = 'hello worold:%d' % self.i #%dのところにself.iが入る　加算されて回数が表示される　callbackが回るごとに加算
        self.publisher_.publish(msg)#publisherクラスのpublish関数にmsgを入れる
        self.get_logger().info('Publishing: "%s"' % msg.data)#msgのdataを%sに表示　get_logger.infoでlogが出る
        self.i += 1 #コールバックが回りきったら加算　回った回数がわかるように
    
def main(args=None):#デフォルト引数設定　None入らないと何も返さない？
    rclpy.init(args=args)#argsで初期化　init呼び出し準備？

    minimal_publisher = MinimalPublisher()#minimal_publisherにクラスをインスタンス化
    rclpy.spin(minimal_publisher)#それをspinに入れてminimalを走らせる

    minimal_publisher.destroy_node()#ノードの破壊　通信をやめる準備
    rclpy.shutdown()#通信終了

if __name__ == '__main__':#エントリーポイント用のやつ　ないと走らないっぽいい
    main()
    