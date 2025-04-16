#!/usr/bin/env python3
# This code is for status_subscriber_node.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import String




class WeatherSubscriber(Node):
    def __init__(self):
        super().__init__('robot_subscriber')  # Initialize the node with the name 'status_subscriber'
        self.subscription = self.create_subscription(
            String,
            'weather',
            self.weather_callback,
            10)  # Subscribe to the topic
        self.subscription  # Prevent unused variable warning

    def weather_callback(self, msg):
        # Print the received robot status conditions and a suggestion
        weather = msg.data
        if weather == 'Robot is moving':
            suggestion = 'Moving'
        elif weather == 'Charging':
            suggestion = 'Charging Mode'
        elif weather == 'Robot is idle':
            suggestion = 'Waitting For Activating'
        elif weather == 'Warning: Obstacle detected':
            suggestion = 'The Robot Started To Avoid Them'
        elif weather == 'System shutdown':
            suggestion = 'Shutting down node...'
        else:
            suggestion = 'No Suggestion Available'

        # Print the robot condition and suggestion with an arrow
        self.get_logger().info(f'--> Received: {weather} --> {suggestion}')


def main(args=None):
    rclpy.init(args=args)  # Initialize the ROS 2 Python client library
    weather_subscriber = WeatherSubscriber()  # Create an instance of the StatusSubscriber node
    rclpy.spin(weather_subscriber)  # Keep the node running
    weather_subscriber.destroy_node()  # Destroy the node when done
    rclpy.shutdown()  # Shutdown the ROS 2 Python client library


if __name__ == '__main__':
    main()