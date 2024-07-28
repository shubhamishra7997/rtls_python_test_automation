import zmq
from position_pb2 import Position

def main():
    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    socket.connect("tcp://127.0.0.1:5555")
    print("Connecting socket to tcp://127.0.0.1:5555")

    while True:
        message = socket.recv()
        gen_pos = Position()
        gen_pos.ParseFromString(message)

        print(f"\nSensor {gen_pos.sensorID}:")
        print(f"Timestamp: {gen_pos.timestampUsec}")
        print(f"X-Value: {gen_pos.position.x:.2f} | Y-Value: {gen_pos.position.y:.2f} | Z-Value: {gen_pos.position.z:.2f}")

if __name__ == "__main__":
    main()