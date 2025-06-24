# 🎨 ai_art_image_generation
A simple Flask-based web app that generates AI-powered artwork using **Stable Diffusion**. It allows users to input a text prompt and receive a beautifully rendered image in return. The app uses `ngrok` to expose the local server to the internet and supports GPU acceleration if available.

---
## 🚀 Features

- 🖼️ Text-to-image generation using **Stable Diffusion v1.5**
- 🌐 Web interface with prompt input and image display
- 🔌 Accessible remotely using **ngrok**
- ⚡ Automatically uses GPU if available (CUDA)

---
# Install dependencies
pip install flask flask-ngrok pyngrok diffusers transformers accelerate scipy safetensors

---
# 🔒 Set up ngrok
Sign up at ngrok.com and get your auth token. Then, configure it:

ngrok config add-authtoken YOUR_AUTHTOKEN_HERE

---
# 🧠 How It Works
- The app loads Stable Diffusion v1.5 using the Hugging Face diffusers library.
- User enters a prompt on the web page.
- The prompt is passed to the model which generates an image.
- The image is displayed directly in the browser using base64 encoding.
- The entire app is served on a public URL using ngrok.

---
# Screenshot

![image](https://github.com/user-attachments/assets/e87d409c-460e-4c8b-97a7-7c5d2ffaf37e)

---

![image](https://github.com/user-attachments/assets/c8bf1c18-963c-43b5-9410-00a6c222e343)

---

![image](https://github.com/user-attachments/assets/4caf9b71-e01c-462c-a6af-c01833e2acc2)

----


# 👨‍💻 Author
Developed by [sanika tikole].
Feel free to fork or modify this project for your own experiments.

