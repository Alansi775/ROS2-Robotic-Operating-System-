# Robot Info ROS2 Package
# student name: Mohammed Saleh B2280.060137
This ROS2 package simulates Robot status publishing and reacting with suitable comments.

## Nodes

### status_publisher_node.py
Publishes a random robot status condition ("Robot is moving", "Robot is idle", "Charging", "Warning: Obstacle detected", "System shutdown") every 5 seconds on a topic.

### status_subscriber_node.py
Subscribes to the robot topic and prints actions based on the received robot status condition.

## Usage

Run the publisher:

python3 status_publisher_node.py

Run the subscriber:

python3 status_subscriber_node.py
