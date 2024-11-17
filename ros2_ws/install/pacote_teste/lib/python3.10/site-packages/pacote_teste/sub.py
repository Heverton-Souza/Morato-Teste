#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class Subscriber(Node):
    def __init__(self):
        super().__init__("subscriber_node") 

        self.subscriber_ = self.create_subscription(String, "teste", self.callback_teste, 10) # Tipo, tópico, callback, QosProfile
        print("my_node_3 começou!")

    def callback_teste(self, msg): # Função de callback (toda vez que o publisher mandar uma mensagem o callback será chamado e a mensagem será tratada dentro desta função)
        print(msg.data)
        
def main(args=None):
    rclpy.init(args=args)
    node = Subscriber() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()