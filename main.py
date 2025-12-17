import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Starforged", layout="wide")

html_content = """
<style>
:root{--bg1:#070617;--bg2:#07102a;--accent1:#7f9cff;--accent2:#c77dff;--warm:#ffb703}
body{margin:0;padding:0;font-family:Inter, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;background: radial-gradient(circle at 10% 10%, var(--bg2), #000 70%);color:#e6e6ff;overflow-x:hidden;}
.container{max-width:1000px;margin:0 auto;padding:40px 20px;}
.header{display:flex;flex-direction:column;align-items:center;gap:10px;margin-bottom:20px;}
.title{font-size:4rem;font-weight:900;background:linear-gradient(90deg,var(--accent1),var(--accent2),var(--warm));-webkit-background-clip:text;-webkit-text-fill-color:transparent;text-align:center;}
.lead{font-size:1.25rem;opacity:0.95;text-align:center;max-width:900px;line-height:1.6;}
.card{background:rgba(255,255,255,0.02);border-radius:25px;padding:30px;backdrop-filter:blur(8px);box-shadow:0 10px 50px rgba(0,0,0,0.6);margin-bottom:25px;transition: transform 0.3s ease, box-shadow 0.3s ease;}
.card:hover{transform: translateY(-5px);box-shadow:0 15px 60px rgba(0,0,0,0.75);}
.p{font-size:1.05rem;line-height:1.7;color:rgba(230,230,255,0.95);margin-bottom:14px;}
details{background:rgba(255,255,255,0.01);border-radius:12px;padding:14px;margin-bottom:12px;}
details summary{font-weight:700;font-size:1.15rem;cursor:pointer;outline:none;}
details[open] summary::after{content: " \25B2";}
details summary::after{content: " \25BC";float:right;}
.stars{position:fixed;left:0;right:0;top:0;bottom:0;z-index:-2;background-image:radial-gradient(rgba(255,255,255,0.8) 1px, transparent 1px);background-size: 3px 3px;opacity:0.08;}
.footer{padding:24px;text-align:center;opacity:0.9;}
</style>

<div class='stars'></div>
<div class='container'>
  <div class='header'>
    <div class='title'>STARFORGED — The Journey of a Hydrogen Atom</div>
    <div class='lead'>Follow the story of a hydrogen atom from the Big Bang to consciousness. Ambient music will start automatically when you scroll.</div>
  </div>

  <audio id='ambient' loop>
    <source src='https://cdn.pixabay.com/audio/2022/03/15/audio_7f7429d5c7.mp3' type='audio/mpeg'>
  </audio>

  <div class='card'>
    <details open>
      <summary>1) Overview</summary>
      <div class='p'>I am a hydrogen atom. My journey spans the birth of the universe, the formation of stars and planets, and eventually life itself. I am a witness, a traveler, and now, a participant in consciousness.</div>
    </details>
  </div>

  <div class='card'>
    <details>
      <summary>2) The Big Bang</summary>
      <div class='p'>13.8 billion years ago, the universe erupted from an infinitesimal point of immense energy. I emerged as a proton in a blazing sea of particles and radiation. The universe expanded, cooled, and I began to interact with electrons, forming the first hydrogen atoms. Light spread across the cosmos, carrying the first memories of creation.</div>
    </details>
  </div>

  <div class='card'>
    <details>
      <summary>3) Laws of Being</summary>
      <div class='p'>Gravity pulled me into clouds of gas, forging stars where I fused into helium and heavier elements. Supernovae hurled me across space, scattering the building blocks of life. On planets, I became part of water, minerals, and eventually complex molecules. I experienced order, chemistry, and the rules that shape existence itself.</div>
    </details>
  </div>

  <div class='card'>
    <details>
      <summary>4) Now</summary>
      <div class='p'>Today, I reside within a human neuron. I move with ions, help transmit electrical impulses, and contribute to thought and consciousness. From chaos to cognition, my journey is complete — yet ongoing. Through me, the universe observes itself, reflecting on its own wonder.</div>
    </details>
  </div>

  <div class='footer'>Made with Streamlit — Project: Starforged — Run: <code>streamlit run starforged.py</code></div>
</div>

<script>
let audioStarted = false;
window.addEventListener('scroll', function() {
    if (!audioStarted) {
        document.getElementById('ambient').play();
        audioStarted = true;
    }
});
</script>
"""

html(html_content, height=2800)