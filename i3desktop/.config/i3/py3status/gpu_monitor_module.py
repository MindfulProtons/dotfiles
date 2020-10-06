import pyamdgpuinfo as info
import subprocess
import os

info.detect_gpus()
gpu = info.get_gpu(0)
class Py3status:

    
    def show_gpu_load(self):
        load = str(round(gpu.query_load() * 100)) + "%"
        power_usage = str(round(gpu.query_power())) + "W"
        return {
            'full_text': "GPU: " + load + ", " + power_usage,
            'cached_until': self.py3.time_in(0.5)
        }
    def on_click(self, event):
        subprocess.Popen("python ~/.config/i3/py3status/run_ui.py", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, preexec_fn=os.setpgrp)
