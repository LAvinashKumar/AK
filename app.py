import streamlit as st
import streamlit.components.v1 as components
import base64
import os

st.set_page_config(page_title="For Harinii ❤️", layout="wide")

# Function to convert local image to base64 so Streamlit can see it
def get_image_base64(path):
    try:
        with open(path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return None

# Load your images
images = {}
for i in range(1, 7):
    img_data = get_image_base64(f"{i}.jpeg")
    if img_data:
        images[f"img{i}"] = img_data
    else:
        st.error(f"Missing file: {i}.jpeg. Please upload it to your GitHub repository.")
        st.stop()

# The Surprise Logic
html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{ 
            background: #fff0f5; 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            text-align: center; 
            overflow: hidden; 
            height: 100vh; 
            margin: 0; 
        }}
        
        /* Balloon Styling */
        .balloon {{
            position: absolute; width: 65px; height: 85px; 
            border-radius: 50% 50% 50% 50% / 40% 40% 60% 60%;
            cursor: pointer; 
            box-shadow: inset -10px -10px 20px rgba(0,0,0,0.1), 5px 10px 15px rgba(0,0,0,0.05);
            animation: sway 4s infinite ease-in-out;
            z-index: 10;
        }}
        .balloon::after {{
            content: ''; position: absolute; top: 15%; left: 20%;
            width: 15px; height: 25px; background: rgba(255,255,255,0.4);
            border-radius: 50%; transform: rotate(15deg);
        }}

        /* Pop-up Modal Styling */
        #pop-modal {{
            position: fixed; top: 0; left: 0; width: 100%; height: 100%; 
            background: rgba(0,0,0,0.92);
            display: none; flex-direction: column; 
            justify-content: center; align-items: center; 
            z-index: 1000; color: white;
        }}
        
        /* Image Control */
        #pop-modal img {{ 
            max-width: 85%; 
            max-height: 55vh; 
            object-fit: contain; 
            border: 4px solid white; 
            border-radius: 15px; 
            margin-bottom: 20px;
        }}
        
        /* Text Visibility */
        #m-txt {{ 
            font-size: 1.5rem; 
            font-weight: bold;
            padding: 0 25px;
            color: #ffb3c1;
            text-shadow: 2px 2px 8px rgba(0,0,0,0.8);
            line-height: 1.4;
        }}

        .hidden {{ display: none !important; }}
        @keyframes sway {{ 0%, 100% {{ transform: translateY(0) rotate(0deg); }} 50% {{ transform: translateY(-25px) rotate(5deg); }} }}
        
        .start-btn {{
            padding: 18px 40px; border-radius: 50px; border: none; 
            background: linear-gradient(45deg, #ff416c, #ff4b2b); 
            color: white; cursor: pointer; font-size: 1.1rem;
            font-weight: bold; box-shadow: 0 10px 20px rgba(255, 65, 108, 0.4);
            transition: transform 0.2s;
        }}
        .start-btn:active {{ transform: scale(0.95); }}
    </style>
</head>
<body>
    <div id="intro">
        <h1 style="color: #d81b60; margin-top: 60px; padding: 0 15px;">Happy Women's Day, Harinii❤️✨</h1>
        <div style="position: relative; display: inline-block; margin: 20px 0;">
             <span style="position: absolute; top: -30px; left: 50%; transform: translateX(-50%); font-size: 40px;">👑</span>
             <img src="data:image/jpeg;base64,{images['img6']}" style="width:140px; height:140px; border-radius:50%; border: 5px solid white; object-fit: cover;">
        </div>
        <p style="color: #d81b60; font-size: 1.1rem;">I've prepared 6 special surprises for you.<br>Pop the balloons to find them! 🎈</p>
        <button class="start-btn" onclick="start()">Start the Magic ✨</button>
    </div>

    <div id="game" class="hidden">
        <h2 id="counter" style="color: #d81b60; padding-top: 20px;">6 surprises remaining</h2>
    </div>

    <div id="pop-modal" onclick="this.style.display='none'; checkFinal();">
        <img id="m-img" src="">
        <p id="m-txt"></p>
        <p style="font-size: 0.9rem; color: #bbb; margin-top: 15px;">Tap anywhere to continue</p>
    </div>

    <div id="final" class="hidden" style="display: flex; flex-direction: column; justify-content: center; height: 90vh;">
        <div style="background: white; margin: auto; padding: 40px; border-radius: 30px; width: 80%; max-width: 500px; box-shadow: 0 15px 40px rgba(0,0,0,0.1);">
            <h1 style="color: #d81b60;">You are Incredible, Harinii! 💖</h1>
            <p style="color: #666; font-size: 1.1rem; line-height: 1.6;">Today and every day, keep shining bright and being the amazing force that you are.</p>
            <p style="font-size: 2.5rem; margin-top: 20px;">🌸👑✨💪</p>
        </div>
    </div>

    <audio id="pop-snd" src="https://www.soundjay.com/buttons/sounds/button-10.mp3" preload="auto"></audio>

    <script>
        const data = [
            {{img: "{images['img1']}", txt: "Hii Chittiii! 💪"}},
            {{img: "{images['img2']}", txt: "You are radiant inside and out. ✨"}},
            {{img: "{images['img3']}", txt: "Your perspective is a gift. 🧠"}},
            {{img: "{images['img4']}", txt: "Your heart changes lives, always keep smiling. ❤️"}},
            {{img: "{images['img5']}", txt: "Keep reaching for the stars! 🚀"}},
            {{img: "{images['img6']}", txt: "Never drop your crown, Queen. 👑"}}
        ];
        let popped = 0;
        const colors = ['#ff4d6d', '#ff758f', '#ff8fa3', '#ffb3c1', '#fb6f92', '#ff99ac'];

        function start() {{
            document.getElementById('intro').classList.add('hidden');
            document.getElementById('game').classList.remove('hidden');
            data.forEach((d, i) => {{
                let b = document.createElement('div');
                b.className = 'balloon';
                b.style.left = (Math.random() * 70 + 10) + "%";
                b.style.top = (Math.random() * 60 + 20) + "%";
                b.style.background = `radial-gradient(circle at 30% 30%, ${{colors[i]}}, #900)`;
                
                b.onclick = () => {{
                    try {{ 
                        let s = document.getElementById('pop-snd');
                        s.currentTime = 0;
                        s.play(); 
                    }} catch(e) {{}}
                    
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

components.html(html_code, height=850)
