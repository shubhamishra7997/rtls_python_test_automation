import zmq
import time
from position_pb2 import Position, Data3d
from main import init_position, update_position, check_range, add_noise, NUM_SENSORS
from datetime import datetime


"""
Sends a position message to the socket.
Args:
    socket (zmq.Socket): The ZeroMQ socket to send the message.
    sensor_id (int): The ID of the sensor.
    position (Data3d): The position data to be sent.
"""
def send_position(socket, sensor_id, position):
    # Get the current timestamp 
    timestamp_usec = int(datetime.utcnow().timestamp() * 1e6)
    
    # Create a Data3d and Position protobuf message
    data3d_proto = Data3d(x=position.x, y=position.y, z=position.z)
    position_message = Position(sensorID=sensor_id, timestampUsec=timestamp_usec, position=data3d_proto)

    # Serialize and send the message over the socket.
    serialized_msg = position_message.SerializeToString()
    socket.send(serialized_msg)


"""
Main function to initialize positions, update them, and send them via ZeroMQ.
"""
def main():
    # Serialize the message to a string
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.bind("tcp://127.0.0.1:5555")
    print("Binding socket to tcp://127.0.0.1:5555")

    # Initialize positions for all sensors
    positions = [init_position() for _ in range(NUM_SENSORS)]

    # Continuous loop to update and send positions
    while True:
        for sensor_id in range(NUM_SENSORS):
            # Update position, check (range and velocity) and finally add noise.
            updated_position = update_position(positions[sensor_id])
            checked_position = check_range(positions[sensor_id], updated_position)
            final_position = add_noise(checked_position)

            # Send the final position over ZeroMQ
            send_position(socket, sensor_id, final_position)

            # Update the stored position
            positions[sensor_id] = final_position

        time.sleep(1)  # Implement frequency of 1 Hz

if __name__ == "__main__":
    main()