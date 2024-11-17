#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String # Quando usar a example_interfaces pela primeira vez, ela deve ser adicionada no arquivo .xml

class Publisher(Node):
    def __init__(self):
        super().__init__("publisher_node") 

        self.publisher_ = self.create_publisher(String, "teste", 10) # Tipo, tópico, QosProfile (tipo um buffer)
        self.timer_ = self.create_timer(0.5, self.publish_teste) # Criando um timer para chamar a função a cada 0.5s
        print("O teste começou!")

    def publish_teste(self): # Criando uma função para publicar o tópico (boa prática)
        msg = String() # A mensagem é um objeto tipo "String" que pegamos da biblioteca String
        msg.data = "Bom dia!"
        self.publisher_.publish(msg) # Publicando a mensagem

def main(args=None):
    rclpy.init(args=args)
    node = Publisher() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()