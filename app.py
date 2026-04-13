from flask import Flask, jsonify
import psutil
import time
import logging
from datetime import datetime

app = Flask(__name__)
start_time = time.time()


@app.route('/')
def home():
    return jsonify({
        "message": "System Monitoring API is Running",
        "status": "healthy"
    })


@app.route('/health')
def health():
    try:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        return jsonify({
            "cpu_usage_percent": cpu,
            "memory": {
                "total": memory.total,
                "available": memory.available,
                "used_percent": memory.percent
            },
            "disk": {
                "total": disk.total,
                "used": disk.used,
                "free": disk.free,
                "used_percent": disk.percent
            },
            "timestamp": datetime.utcnow().isoformat()
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@app.route('/system')
def system_info():
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - start_time

    return jsonify({
        "cpu_cores_physical": psutil.cpu_count(logical=False),
        "cpu_cores_logical": psutil.cpu_count(logical=True),
        "boot_time": datetime.fromtimestamp(boot_time).isoformat(),
        "uptime_seconds": uptime_seconds,
        "system_load": psutil.getloadavg() if hasattr(psutil, "getloadavg") else "N/A"
    })


@app.route('/network')
def network():
    net = psutil.net_io_counters()

    return jsonify({
        "bytes_sent": net.bytes_sent,
        "bytes_received": net.bytes_recv,
        "packets_sent": net.packets_sent,
        "packets_received": net.packets_recv
    })

@app.get("/health")
def health():
        return {"status":"ok"}

logging.basicConfig(level=logging.INFO)

@app.get("/")
def home():
    logging.info("Home endpoint hit")
    return {"message":"Hello World"}

@app.ger("/crash")
def crash():
    1/0

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)