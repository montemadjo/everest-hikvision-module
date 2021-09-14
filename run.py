from queue import Queue
from threading import Thread
from hikvision_camera import Camera
import configparser
import time
from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse

# load configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# read the configuration
URL = config['Remote']['URL']
username = config['Basic']['Username']
password = config['Basic']['Password']
connection_string = config['Iot']['ConnectionString']

def create_client(connection_string):
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    # Define a method request handler
    def method_request_handler(method_request):
        if method_request.name == "SetTelemetryInterval":
            try:
                global INTERVAL
                print("idemo levo")
                INTERVAL = int(method_request.payload)
            except ValueError:
                response_payload = {"Response": "Invalid parameter"}
                response_status = 400
            else:
                response_payload = {"Response": "Executed direct method {}".format(method_request.name)}
                response_status = 200
        else:
            response_payload = {"Response": "Direct method {} not defined".format(method_request.name)}
            response_status = 404

        method_response = MethodResponse.create_from_method_request(method_request, response_status, response_payload)
        client.send_method_response(method_response)

    try:
        # Attach the method request handler
        client.on_method_request_received = method_request_handler
    except:
        # Clean up in the event of failure
        client.shutdown()
        raise

    return client

def run_telemetry_sample(client):
    # This sample will send temperature telemetry every second
    print("IoT Hub device sending periodic messages")

    client.connect()

    while True:
        # Build the message with simulated telemetry values.
        temperature = TEMPERATURE + (random.random() * 15)
        humidity = HUMIDITY + (random.random() * 20)
        msg_txt_formatted = MSG_TXT.format(temperature=temperature, humidity=humidity)
        message = Message(msg_txt_formatted)

        # Add a custom application property to the message.
        # An IoT hub can filter on these properties without access to the message body.
        if temperature > 30:
            message.custom_properties["temperatureAlert"] = "true"
        else:
            message.custom_properties["temperatureAlert"] = "false"

        # Send the message.
        print("Sending message: {}".format(message))
        client.send_message(message)
        print("Message sent")
        time.sleep(INTERVAL)

def main(connection_string):
    print ("IoT Hub Quickstart #2 - Simulated device")
    print ("Press Ctrl-C to exit")

    # Instantiate the client. Use the same instance of the client for the duration of
    # your application
    client = create_client(connection_string)

    # Send telemetry
    try:
        run_telemetry_sample(client)
    except KeyboardInterrupt:
        print("IoTHubClient sample stopped by user")
    finally:
        print("Shutting down IoTHubClient")
        client.shutdown()

if __name__ == '__main__':
    camera = Camera(URL, username, password)
    main(connection_string)
    camera.postOutputRequest(1)
    time.sleep(1)
    camera.postOutputRequest(0)