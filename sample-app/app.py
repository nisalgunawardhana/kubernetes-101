from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <html>
    <head><title>K8s-101 Sample App</title></head>
    <body style="font-family:sans-serif;text-align:center;margin-top:60px;background:#0f172a;color:#e2e8f0">
      <h1 style="color:#38bdf8">🚀 Kubernetes 101 Sample App</h1>
      <p>Running on pod: <strong style="color:#34d399">{socket.gethostname()}</strong></p>
      <p>Version: <strong style="color:#f59e0b">{os.environ.get('APP_VERSION', '1.0.0')}</strong></p>
      <p>Environment: <strong style="color:#a78bfa">{os.environ.get('APP_ENV', 'development')}</strong></p>
      <hr style="border-color:#334155">
      <p style="color:#64748b">Kubernetes-101 Learning Project</p>
    </body>
    </html>
    """

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "pod": socket.gethostname()})

@app.route('/info')
def info():
    return jsonify({
        "app": "kubernetes-101-sample",
        "version": os.environ.get('APP_VERSION', '1.0.0'),
        "pod": socket.gethostname(),
        "env": os.environ.get('APP_ENV', 'development')
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
