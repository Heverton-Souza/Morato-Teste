import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/heverton/Morato-Teste/ros2_ws/install/pacote_teste'
