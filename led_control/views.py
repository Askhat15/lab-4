from django.shortcuts import render
import serial
def index(request):
    return render(request, 'led_control/index.html')
def control_led(request):
    port = 'COM' # используйте свой COM-порт здесь
    baudrate = 9600
    action = request.POST.get('action')
    if action == 'on':
        send_command(port, baudrate, '1')
    elif action == 'off':
        send_command(port, baudrate, '0')
    return render(request, 'led_control/index.html')
def send_command(port, baudrate, command):
        arduino = serial.Serial(port, baudrate, timeout=1)
        arduino.write(command.encode())
        arduino.close()
def index(request1):
    return render(request1, 'Alphabet/index1.html')