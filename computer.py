import time
import psutil
import serial

ser = serial.Serial('COM3', 115200)
time.sleep(2)

while True:
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    
    cpu_t = 0.0
    gpu_u = 0.0
    gpu_t = 0.0

    try:
        from PyLibreHardwareMonitor import Computer
        comp = Computer()
        comp.Open()
        comp.Update()
        gpu_u = comp.gpu.load
        gpu_t = comp.gpu.temperature
    except:
        pass

    data = str(cpu) + "," + str(cpu_t) + "," + str(gpu_u) + "," + str(gpu_t) + "," + str(ram) + "\n"
    ser.write(data.encode())
    time.sleep(0.5)