import streamlit as st
import streamlit.components.v1 as components
import base64
import os

st.set_page_config(page_title="For Harinii ❤️", layout="wide")

# Function to convert local image to base64 so Streamlit can see it
def get_image_base64(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Load your images
try:
    img1 = get_image_base64("1.jpeg")
    img2 = get_image_base64("2.jpeg")
    img3 = get_image_base64("3.jpeg")
    img4 = get_image_base64("4.jpeg")
    img5 = get_image_base64("5.jpeg")
    img6 = get_image_base64("6.jpeg")
except FileNotFoundError:
    st.error("Make sure 1.jpeg through 6.jpeg are in the same folder as this script!")
    st.stop()

# The Surprise Logic
html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ background: #fff0f5; font-family: sans-serif; text-align: center; overflow: hidden; height: 100vh; margin: 0; }}
        .balloon {{
            position: absolute; width: 80px; height: 100px; border-radius: 50% 50% 50% 50% / 40% 40% 60% 60%;
            cursor: pointer; box-shadow: inset -10px -10px 20px rgba(0,0,0,0.1); animation: sway 4s infinite ease-in-out;
        }}
        .balloon::after {{ content: ''; position: absolute; top: 15%; left: 20%; width: 15px; height: 25px; background: rgba(255,255,255,0.4); border-radius: 50%; }}
        @keyframes sway {{ 0%, 100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-20px); }} }}
        
        #pop-modal {{
            position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.9);
            display: none; flex-direction: column; justify-content: center; align-items: center; z-index: 1000; color: white;
        }}
        #pop-modal img {{ max-width: 80%; border: 5px solid white; border-radius: 15px; }}
        .hidden {{ display: none !important; }}
    </style>
</head>
<body>
    <div id="intro">
        <h1 style="color: #d81b60; margin-top: 50px;">Happy Women's Day, Harinii❤️✨</h1>
        <img src="data:image/jpeg;base64,{img6}" style="width:150px; border-radius:50%; border: 4px solid white;">
        <p>Pop the balloons for your surprises! 🎈</p>
        <button onclick="start()" style="padding: 15px 30px; border-radius: 50px; border: none; background: #ff416c; color: white; cursor: pointer;">Start the Magic ✨</button>
    </div>

    <div id="game" class="hidden">
        <h2 id="counter" style="color: #d81b60;">6 surprises remaining</h2>
    </div>

    <div id="pop-modal" onclick="this.style.display='none'; checkFinal();">
        <img id="m-img" src="">
        <p id="m-txt" style="font-size: 1.5rem;"></p>
    </div>

    <div id="final" class="hidden" style="margin-top: 100px;">
        <h1 style="color: #d81b60;">You are Incredible, Harinii! 💖</h1>
        <p>Keep shining bright! 🌸👑✨</p>
    </div>

    <audio id="pop-snd" src="https://www.soundjay.com/buttons/sounds/button-10.mp3"></audio>

    <script>
        const data = [
            {{img: "{img1}", txt: "Hii Chittiii! 💪"}},
            {{img: "{img2}", txt: "You are radiant! ✨"}},
            {{img: "{img3}", txt: "You are a gift! 🧠"}},
            {{img: "{img4}", txt: "Keep smiling! ❤️"}},
            {{img: "{img5}", txt: "Reach for stars! 🚀"}},
            {{img: "{img6}", txt: "Never drop your crown! 👑"}}
        ];
        let popped = 0;

        function start() {{
            document.getElementById('intro').classList.add('hidden');
            document.getElementById('game').classList.remove('hidden');
            data.forEach((d, i) => {{
                let b = document.createElement('div');
                b.className = 'balloon';
                b.style.left = (Math.random() * 70 + 10) + "%";
                b.style.top = (Math.random() * 60 + 20) + "%";
                b.style.background = "radial-gradient(circle at 30% 30%, #ff758f, #900)";
                b.onclick = () => {{
                    document.getElementById('pop-snd').play();
                    document.getElementById('m-img').src = "data:image/jpeg;base64," + d.img;
                    document.getElementById('m-txt').innerText = d.txt;
                    document.getElementById('pop-modal').style.display = 'flex';
                    b.remove();
                    popped++;
                    document.getElementById('counter').innerText = (6 - popped) + " remaining";
                }};
                document.getElementById('game').appendChild(b);
            }});
        }}

        function checkFinal() {{
            if(popped === 6) {{
                document.getElementById('game').classList.add('hidden');
                document.getElementById('final').classList.remove('hidden');
            }}
        }}
    </script>
</body>
</html>
"""

components.html(html_code, height=800)