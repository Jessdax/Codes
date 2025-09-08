import webview
from threading import Thread
from app import app  # Import your existing Flask app

def run_flask():
    # Run Flask app without debug and accessible only locally
    app.run(debug=False, port=5000, use_reloader=False)

if __name__ == "__main__":
    # Start Flask in a separate thread
    flask_thread = Thread(target=run_flask)
    flask_thread.start()

    # Open the desktop window pointing to Flask
    webview.create_window("Inventory Counter System", "http://127.0.0.1:5000")
    webview.start()
