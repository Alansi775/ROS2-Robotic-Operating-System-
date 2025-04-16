#!/usr/bin/env python3
# This code is for status_publisher_node.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class WeatherPublisher(Node):
    def __init__(self):
        super().__init__('status_publisher')  # Initialize the node with the name 'status_publisher'
        self.publisher_ = self.create_publisher(String, 'weather', 10)  # Create a publisher on the this topic
        self.timer = self.create_timer(5.0, self.publish_weather)  # we are setting a timer to call publish_status every 2 seconds
        self.weather_conditions = ['Robot is moving', 'Robot is idle', 'Charging', 'Warning: Obstacle detected', 'System shutdown']  # List of robot status conditions

    def publish_weather(self):
        # Randomly select a robot status condition
        weather = random.choice(self.weather_conditions)
        msg = String()
        msg.data = weather
        self.publisher_.publish(msg)  # Publish the robot status condition
        self.get_logger().info(f'Published: {msg.data}')  # Log the published robot condition


def main(args=None):
    rclpy.init(args=args)  # Initialize the ROS 2 Python client library
    weather_publisher = WeatherPublisher()  # Create an instance of the StatusPublisher node
    rclpy.spin(weather_publisher)  # Keep the node running
    weather_publisher.destroy_node()  # Destroy the node when done
    rclpy.shutdown()  # Shutdown the ROS 2 Python client library


if __name__ == '__main__':
    main()



