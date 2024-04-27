#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty
from turtlesim.msg import Color
from turtlesim.srv import SetPen
#merge
def move_turtle():
    # Inicializa el nodo de ROS llamado "move_turtle"
    rospy.init_node('move_turtle', anonymous=True)

    # Crea un objeto para publicar mensajes de Twist (velocidad lineal y angular)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)


    # Crea un objeto de tipo Twist
    twist = Twist()
    
    # Configura las velocidades
    twist.linear.x = 1.5  # Velocidad lineal hacia adelante
    twist.angular.z = 1.5  # Velocidad angular (giro)

    rospy.wait_for_service('/turtle1/set_pen')
    set_pen = rospy.ServiceProxy('/turtle1/set_pen', SetPen)

    # Establece el color y el ancho del lápiz de la tortuga
    rospy.wait_for_service('/turtle1/set_pen')
    set_pen = rospy.ServiceProxy('/turtle1/set_pen', SetPen)

    # Establece el color y el ancho del lápiz de la tortuga
    pen_color = Color()
    pen_color.r = 255
    pen_color.g = 0
    pen_color.b = 0
    pen_width = 2
    off = 0

    set_pen(pen_color.r, pen_color.g, pen_color.b, pen_width, off)




    rospy.wait_for_service('/clear')
    reset_turtle = rospy.ServiceProxy('/clear', Empty)
    reset_turtle()
    # Establece la frecuencia de publicación en 10 Hz (cada 0.1 segundos)
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        # Publica el mensaje de Twist en el topic "/turtle1/cmd_vel"
        pub.publish(twist)
        
        # Espera hasta el próximo ciclo de publicación
        rate.sleep()

if __name__ == '__main__':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass