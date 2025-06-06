"""
Сделал кроссплатформенно, под Linux/MacOS - uptime, под Windows - psutil
pip install psutil
"""
import platform
import subprocess
import time
from flask import Flask

try:
    import psutil
except ImportError:
    psutil = None

app = Flask(__name__)


def get_uptime():
    system = platform.system()

    if system in ('Linux', 'Darwin'):  # Darwin = macOS
        try:
            # 'uptime' : 14:52:55 up 10 min,  1 user,  load average: 1,56, 1,65, 0,98
            # 'uptime -p': up 14 minutes
            result = subprocess.run(['uptime', '-p'], stdout=subprocess.PIPE, text=True)
            output = result.stdout.strip()
            up_part = output.split("up ")
            return up_part[1]
        except Exception as e:
            return f"Could not get uptime: {e}"

    if psutil:
        boot_time = psutil.boot_time()
        uptime_seconds = time.time() - boot_time

        days = int(uptime_seconds // (24 * 3600))
        hours = int((uptime_seconds % (24 * 3600)) // 3600)
        minutes = int((uptime_seconds % 3600) // 60)
        if days:
            return f"{days} days, {hours}:{minutes:02d}"
        else:
            return f"{hours}:{minutes:02d}"

    return "Method not implemented"


@app.route("/uptime", methods=["GET"])
def uptime():
    return f"{get_uptime()}"


if __name__ == '__main__':
    app.run()
