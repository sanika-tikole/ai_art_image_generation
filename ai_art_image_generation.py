# -*- coding: utf-8 -*-
"""ai art image generation
"""

# Step 1: Install dependencies
!pip install flask flask-ngrok pyngrok diffusers transformers accelerate scipy safetensors --quiet

# Step 2: Import libraries
from flask import Flask, request, render_template_string
from pyngrok import ngrok
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
import io, base64

# Step 3: Load Stable Diffusion model
device = "cuda" if torch.cuda.is_available() else "cpu"

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16 if device == "cuda" else torch.float32
).to(device)

print("✅ Model loaded on", device)



# Step 4: Create Flask app
app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head><title>AI Art Generator</title></head>
<body>
    <h2>🎨 AI Art Generator</h2>
    <form method="POST">
        <input name="prompt" placeholder="Enter prompt" style="width:300px;" required>
        <button type="submit">Generate</button>
    </form>
    {% if img_data %}
        <h3>Prompt: {{ prompt }}</h3>
        <img src="data:image/png;base64,{{ img_data }}" width="512"/>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    img_data = None
    prompt = None
    if request.method == "POST":
        prompt = request.form["prompt"]
        prompt = f"{prompt}, highly detailed, trending on artstation"

        with torch.autocast("cuda" if device == "cuda" else "cpu"):
            image = pipe(prompt).images[0]

        # Convert to base64 for display
        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        img_data = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return render_template_string(HTML, img_data=img_data, prompt=prompt)

!ngrok config add-authtoken add_your_authtoken

# Step 5: Start server with pyngrok
public_url = ngrok.connect(5000)
print("🚀 Public URL:", public_url)

app.run(port=5000)