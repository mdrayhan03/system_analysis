import webview

# URL for the locally running Django application
django_url = "http://127.0.0.1:8000"

# Create and launch the webview window
webview.create_window("My Django Desktop App", django_url)

# Run the webview
webview.start()