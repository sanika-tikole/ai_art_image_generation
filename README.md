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
# 👨‍💻 Author
Developed by [sanika tikole].
Feel free to fork or modify this project for your own experiments.

