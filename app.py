import streamlit as st
import time
import random
import base64
from datetime import date
import streamlit.components.v1 as components

# --- 1. ページ設定 ---
st.set_page_config(page_title="クマ勉ログ 🎀", page_icon="🧸", layout="wide")

# --- 2. 画像読み込み ---
def get_image_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

back_b64 = get_image_base64("back.png")

# --- 3. 💖 デザイン設定 ---
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{back_b64}");
        background-size: cover;
        background-attachment: fixed;
    }}
    /* 【修正箇所】メッセージを白背景・青文字に */
    .top-message {{
        text-align: center; padding: 15px; font-size: 20px; font-weight: 800;
        color: #0288D1; background: rgba(255, 255, 255, 0.95);
        border: 3px solid #80D8FF; border-radius: 15px;
        margin: -10px 0px 20px 0px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }}
    .money-card, .pop-card {{
        background: white !important; border-radius: 20px; padding: 20px; 
        border: 2px solid #B3E5FC; margin-bottom: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }}
    .stButton > button {{
        width: 100% !important; height: 80px !important; font-size: 24px !important;
        font-weight: bold !important; border-radius: 40px !important;
        transition: 0.3s; border: none !important;
    }}
    .stButton > button:hover {{ transform: scale(1.05); box-shadow: 0 8px 20px rgba(0,0,0,0.3); }}
    
    .stButton > button[key*="z_btn"] {{ background: linear-gradient(135deg, #FFD700 0%, #FFA000 100%) !important; color: white !important; text-shadow: 1px 1px 3px rgba(0,0,0,0.4); }}
    .stButton > button[key*="k_btn"] {{ background: linear-gradient(135deg, #CFD8DC 0%, #78909C 100%) !important; color: white !important; text-shadow: 1px 1px 3px rgba(0,0,0,0.4); }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. 🎉 画面全体に降り注ぐ紙吹雪 ---
def play_conffeti():
    confetti_js = """
    <canvas id="confetti-canvas" style="position:fixed;top:0;left:0;width:100vw;height:100vh;pointer-events:none;z-index:999999;"></canvas>
    <script src="https://cdn.jsdelivr.net/npm/confetti-js@0.0.18/dist/index.min.js"></script>
    <script>
        var confettiSettings = { 
            target: 'confetti-canvas',
            respawn: false, 
            size: 2,
            start_from_edge: true,
            clock: 40, 
            props: ['circle', 'rect', 'triangle'],
            colors: [[255,215,0],[255,255,255],[0,199,235],[230,61,135]],
            count: 200
        };
        var confetti = new ConfettiGenerator(confettiSettings);
        confetti.render();
        setTimeout(() => {
            confetti.clear();
            document.getElementById('confetti-canvas').remove();
        }, 5000);
    </script>
    """
    components.html(confetti_js, height=0)

# --- 5. 🔗 URLパラメータ同期システム 🔗 ---
query_params = st.query_params
if 'z' not in st.session_state: st.session_state.z = int(query_params.get("z", 39))
if 'k' not in st.session_state: st.session_state.k = int(query_params.get("k", 15))
if 'money' not in st.session_state: st.session_state.money = int(query_params.get("m", 0))

# --- 🔥 モチベ爆上げメッセージ設定 ---
if 'daily_msg' not in st.session_state:
    st.session_state.daily_msg = random.choice([
        "🔥 君が今日ポチッたその1回が、合格発表の日の涙を笑顔に変える！",
        "💎 公認会計士という未来を、今、自分の手で引き寄せてるぞ！",
        "🐾 疲れてても1コマやった。その『意地』が君を最強の会計士にする！",
        "👑 誰も見ていない場所での努力。それが君の最大の武器だ！",
        "🚀 限界なんて、昨日までの君が決めた勝手な境界線にすぎない！",
        "💰 貯まった100円は、未来の自分への『先行投資』だ。積み上げろ！",
        "✨ 迷ったら進め！君の『やりたい』という気持ちが、何よりの正解だ！"
    ])

praises = ["🎉 天才！", "㊗️ おめでとう！", "✨ 神対応！", "🏆 優勝！", "💖 最高！"]

# --- 6. メイン表示 ---
st.markdown(f'<div class="top-message">🧸 {st.session_state.daily_msg}</div>', unsafe_allow_html=True)

col_a, col_b = st.columns([1, 1.5])
with col_a:
    st.image("bear.png", use_container_width=True)
with col_b:
    st.markdown('<div class="money-card">', unsafe_allow_html=True)
    st.image("money_bag.png", width=100) 
    st.markdown(f"<h1 style='color:#FFB300; margin:0;'>¥ {st.session_state.money:,}</h1>", unsafe_allow_html=True)
    st.link_button("🌸 講義ページを開く", "https://tlp.edulio.com/cpa/mypage/chapter/")
    st.markdown('</div>', unsafe_allow_html=True)

# 🚀 クリック処理
if 'playing_effect' not in st.session_state:
    st.session_state.playing_effect = False

def handle_click(subj, plus=True):
    if plus:
        if subj == "z": st.session_state.z += 1
        else: st.session_state.k += 1
        st.session_state.money += 100
        st.toast(random.choice(praises) + " 努力は裏切らない！", icon="🧸")
        st.session_state.playing_effect = True
    else:
        if subj == "z": st.session_state.z -= 1
        else: st.session_state.k -= 1
        st.session_state.money -= 100
    
    st.query_params.update(z=st.session_state.z, k=st.session_state.k, m=st.session_state.money)
    
    if st.session_state.playing_effect:
        time.sleep(4.0)
        st.session_state.playing_effect = False
        st.rerun()
    else:
        st.rerun()

if st.session_state.playing_effect:
    play_conffeti()

# --- 操作パネル ---
st.write("---")
col_1, col_2 = st.columns(2)

with col_1:
    st.markdown('<div class="pop-card">', unsafe_allow_html=True)
    st.subheader("📘 財務会計")
    st.metric("完了", f"{st.session_state.z} / 70")
    if st.button("🏆 財務完了！ポチッ！", key="z_btn"): handle_click("z", True)
    if st.button("修正（-1）", key="z_undo"): handle_click("z", False)
    st.markdown('</div>', unsafe_allow_html=True)

with col_2:
    st.markdown('<div class="pop-card">', unsafe_allow_html=True)
    st.subheader("📙 管理会計")
    st.metric("完了", f"{st.session_state.k} / 33")
    if st.button("🥈 管理完了！ポチッ！", key="k_btn"): handle_click("k", True)
    if st.button("修正（-1）", key="k_undo"): handle_click("k", False)
    st.markdown('</div>', unsafe_allow_html=True)
