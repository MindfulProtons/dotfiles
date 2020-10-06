import pyamdgpuinfo as info
from tkinter import *
import time
from threading import Thread

info.detect_gpus()
gpu = info.get_gpu(0)
gpu.start_utilisation_polling()

keepLooping = True

print("Starting polling...")
time.sleep(2)

root = Tk()

variables = {
    "Temperature": [Label(), StringVar(root)],
    "Vram usage": [Label(), StringVar(root)],
    "Power": [Label(), StringVar(root)],
    "Load": [Label(), StringVar(root)],
    "Texture Addresser": [Label(), StringVar(root)],
    "Shader Export": [Label(), StringVar(root)],
    "Shader Interpolator": [Label(), StringVar(root)],
    "Scan Converter": [Label(), StringVar(root)],
    "Primitive Assembly": [Label(), StringVar(root)],
    "Depth Block": [Label(), StringVar(root)],
    "Color Block": [Label(), StringVar(root)],
    "Graphics Pipe": [Label(), StringVar(root)]
}

def build_ui():
    root.geometry("300x450")
    root.title("GPU Info")
    root.bind('<Escape>', close)
    root.configure(background='#506070')

    for key in variables:
        variables[key][0] = Label(root, textvariable = variables[key][1], background='#506070', fg='#FFFFFF', font="Iosevka 14")
        variables[key][1].set(key + " ")
        variables[key][0].pack(anchor="w")

def close(thingy):
    keepLooping = False
    root.destroy()


GPU_NAME = "renderD128"
poll_info = None

try:
    poll_info = gpu.query_utilisation()
except RuntimeError as e:
    print("Daemon not running. Unable to display usage information.")

poll_info_dict = {
'texture_addresser': None,
'shader_interpolator': None,
'shader_export': None,
'sequencer_instruction_cache': None,
'shader_interpolator': None,
'scan_converter': None,
'primitive_assembly': None,
'depth_block': None,
'colour_block': None,
'graphics_pipe': None
}

def update_loop():
    try:
        while True:
            if poll_info:
                poll_info_dict = gpu.query_utilisation()

            temperature = gpu.query_temperature()
            vram = gpu.query_vram_usage()
            power = gpu.query_power()
            load = gpu.query_load()

            variables["Temperature"][1].set("Temperature: " + str(temperature) + "º C")
            variables["Vram usage"][1].set("Vram usage: " + str(round(vram * 0.000000001, 1)) + " GB")
            variables["Power"][1].set("Power: " + str(power) + " W")
            variables["Load"][1].set("Load: " + str(round(load * 100)) + "%")
            if poll_info:
                variables["Texture Addresser"][1].set("Texture Addresser: " + str(round(poll_info_dict["texture_addresser"] * 100)) + "%")
                variables["Shader Export"][1].set("Shader Export: " + str(round(poll_info_dict["shader_export"] * 100)) + "%")
                variables["Shader Interpolator"][1].set("Shader Interpolator: " + str(round(poll_info_dict["shader_interpolator"] * 100)) + "%")
                variables["Scan Converter"][1].set("Scan Converter: " + str(round(poll_info_dict["scan_converter"] * 100)) + "%")
                variables["Primitive Assembly"][1].set("Primitive Assembly: " + str(round(poll_info_dict["primitive_assembly"] * 100)) + "%")
                variables["Depth Block"][1].set("Depth Block: " + str(round(poll_info_dict["depth_block"] * 100)) + "%")
                variables["Color Block"][1].set("Color Block: " + str(round(poll_info_dict["colour_block"] * 100)) + "%")
                variables["Graphics Pipe"][1].set("Graphics Pipe: " + str(round(poll_info_dict["graphics_pipe"] * 100)) + "%")
            time.sleep(0.5)
    except RuntimeError:
        pass

build_ui()
thread = Thread(target=update_loop)
thread.start()
root.mainloop()
