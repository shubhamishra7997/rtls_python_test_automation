# rtls_python_test_automation
This repo contains RTLS for sensors with data transmission via Protobuf and socket programming.

## Steps to Execute

1. **Create a virtual environment (if preferred)**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Install the required packages**:
    ```sh
    pip3 install protobuf pyzmq numpy
    ```

3. **Execute the proto file to generate the Python file (`position_pb2.py`)**:
    ```sh
    protoc --python_out=. position.proto
    ```

4. **Run the server**:
    Open a terminal and execute:
    ```sh
    python3 server.py
    ```

5. **Run the client**:
    Open another terminal and execute:
    ```sh
    python3 client.py
    ```

### Note
- Make sure the server is running before starting the client.
- If you encounter any issues, ensure that all dependencies are correctly installed and the protobuf file is properly generated.


### FREEDOM
- Z is limited from 0m to 10m, assuming average height of small warehouse.
- Distance is scaled down when the randomly generated value for position goes beyond the given constraint (7m/s).

### USE OF AI 
- AI was used to create comments in the code and for the functions.
