import streamlit as st
import time
import random
import base64
from datetime import date
from streamlit_javascript import st_javascript

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
    [data-testid="stAppViewBlockContainer"] {{ opacity: 1 !important; }}
    
    .praise-action {{
        position: fixed; top: 45%; left: 50%; transform: translate(-50%, -50%);
        font-size: 120px; font-weight: 900;
        z-index: 9999; pointer-events: none;
        text-align: center;
        animation: super-pop 2.5s cubic-bezier(0.17, 0.89, 0.32, 1.49) forwards;
    }}
    .praise-word {{
        background: linear-gradient(to bottom, #FF1493, #FF69B4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(4px 4px 0px white);
    }}
    @keyframes super-pop {{
        0% {{ transform: translate(-50%, -50%) scale(0) rotate(-20deg); opacity: 0; }}
        20% {{ transform: translate(-50%, -50%) scale(1.5) rotate(10deg); opacity: 1; }}
        80% {{ transform: translate(-50%, -50%) scale(1.2) rotate(0deg); opacity: 1; }}
        100% {{ transform: translate(-50%, -50%) scale(3.0) rotate(5deg); opacity: 0; }}
    }}

    .rainbow-header {{
        background: rgba(230, 247, 255, 0.9); border-radius: 20px;
        border: 4px solid #80D8FF; padding: 15px; text-align: center; margin-bottom: 10px;
    }}
    .main-title {{ color: #0091EA; font-size: 24px; font-weight: 900; }}
    .money-card {{
        background: rgba(255, 255, 255, 0.9); border-radius: 25px;
        padding: 15px; border: 3px solid #FFCCFF; text-align: center; margin-bottom: 10px;
    }}
    .pop-card {{
        background: rgba(255, 255, 255, 0.95); border-radius: 25px;
        padding: 20px; border: 3px solid #B3E5FC; margin-bottom: 15px;
    }}
    .stButton > button {{
        width: 100% !important; height: 65px !important; font-size: 20px !important;
        font-weight: bold !important; border-radius: 35px !important; 
        transition: 0.3s; border: 3px solid #FFFFFF !important;
    }}
    .stButton > button[key*="z_"] {{ background: linear-gradient(135deg, #4FC3F7 0%, #81D4FA 100%) !important; color: white !important; box-shadow: 0 6px 0px #039BE5 !important; }}
    .stButton > button[key*="k_"] {{ background: linear-gradient(135deg, #26C6DA 0%, #80DEEA 100%) !important; color: white !important; box-shadow: 0 6px 0px #00ACC1 !important; }}
    /* 修正ボタンは少し控えめに */
    .stButton > button[key*="undo"] {{
        height: 40px !important; font-size: 14px !important; background: #f0f2f6 !important; color: #666 !important; box-shadow: none !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. 記憶の魔法 ---
# データの一貫性を保つためIDを固定
s_z = st_javascript("localStorage.getItem('cpa_v40_z');")
s_k = st_javascript("localStorage.getItem('cpa_v40_k');")
s_m = st_javascript("localStorage.getItem('cpa_v40_money');")

if 'z' not in st.session_state:
    st.session_state.z = int(s_z) if s_z and s_z != "null" else 39
    st.session_state.k = int(s_k) if s_k and s_k != "null" else 15
    st.session_state.money = int(s_m) if s_m and s_m != "null" else 0

def save_data():
    st_javascript(f"localStorage.setItem('cpa_v40_z', '{st.session_state.z}');")
    st_javascript(f"localStorage.setItem('cpa_v40_k', '{st.session_state.k}');")
    st_javascript(f"localStorage.setItem('cpa_v40_money', '{st.session_state.money}');")

# --- 📣 モチベお迎えメッセージ ---
welcome_messages = [
    "「今日」という日は、残りの人生の最初の一歩。さあ、最高のスタートを切ろうぜ！🔥",
    "君が今日流す汗は、合格発表の日の笑顔に変わる。約束するよ。💎",
    "周りが休んでいる今、君が動けば差は開く。今の1コマが未来の君を救うんだ。🐾",
    "夢を語る人は多い。でも実行する人は一握り。君はその一握りなんだ！🌊"
]

if 'first_visit' not in st.session_state:
    st.toast(random.choice(welcome_messages), icon="🧸")
    st.session_state.first_visit = True
    time.sleep(2.0) # お出迎えメッセージをしっかり見せるためのタメ！

# 激褒め長文
long_praises = [
    "信じられないくらい凄い！今の1コマで合格にグッと近づいたよ。君の集中力は本当に異次元だね！🧸✨",
    "見てたよ！今の論点をやり遂げた君は最高にかっこいい！公認会計士への道がハッキリ見えたね！💎",
    "ポチッとお疲れ様！自分に打ち勝った証拠がまた一つ増えたね。未来の君を助ける最強の武器だよ！💰🌈"
]

# --- 5. メイン表示 ---
goal_date = date(2026, 5, 31) 
days_left = (goal_date - date.today()).days

st.markdown(f'<div class="rainbow-header"><div class="main-title">💎 クマ勉ログ 💎</div><div style="color:#0288D1; font-weight:bold;">完走まで あと {max(0, days_left)} 日</div></div>', unsafe_allow_html=True)

top_col1, top_col2 = st.columns([1, 1.5])
with top_col1:
    st.image("bear.png", use_container_width=True)
with top_col2:
    st.markdown('<div class="money-card">', unsafe_allow_html=True)
    st.image("money_bag.png", width=140) 
    st.markdown(f"<p style='margin:0; font-size:32px; font-weight:900; color:#FFB300;'>¥ {st.session_state.money:,}</p>", unsafe_allow_html=True)
    st.link_button("🌸 講義ページを開く", "https://tlp.edulio.com/cpa/mypage/chapter/")
    if st.button("⏲️ 1分集中開始！", key="timer_btn"):
        placeholder = st.empty()
        for i in range(60, -1, -1):
            placeholder.markdown(f"<h3 style='color:#00B0FF; text-align:center;'>⏳ 残り {i} 秒</h3>", unsafe_allow_html=True)
            time.sleep(1)
        st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

st.write("---")
mid_col1, mid_col2 = st.columns(2, gap="small")

# --- アクション用関数 ---
def handle_click(subject, plus=True):
    if plus:
        if subject == "z": st.session_state.z += 1
        else: st.session_state.k += 1
        st.session_state.money += 100
        word = random.choice(["神！！", "天才！！", "最強！！", "優勝！！", "最高！！"])
        st.markdown(f'<div class="praise-action"><span class="praise-word">{word}</span></div>', unsafe_allow_html=True)
        st.snow()
        st.balloons()
        st.toast(random.choice(long_praises), icon="🧸")
        save_data()
        time.sleep(2.5)
    else:
        # 修正（戻る）のとき
        if subject == "z": st.session_state.z -= 1
        else: st.session_state.k -= 1
        st.session_state.money -= 100 # ここで貯金もマイナス100！
        save_data()
    st.rerun()

with mid_col1:
    st.markdown('<div class="pop-card">', unsafe_allow_html=True)
    st.subheader("📘 財務会計")
    st.metric("完了", f"{st.session_state.z} / 70")
    st.progress(st.session_state.z / 70)
    if st.button("💎 財務ポチッ！", key="z_btn"):
        handle_click("z", plus=True)
    if st.button("修正: 財務-1 & 貯金-100", key="z_undo"):
        handle_click("z", plus=False)
    st.markdown('</div>', unsafe_allow_html=True)

with mid_col2:
    st.markdown('<div class="pop-card">', unsafe_allow_html=True)
    st.subheader("📙 管理会計")
    st.metric("完了", f"{st.session_state.k} / 33")
    st.progress(st.session_state.k / 33)
    if st.button("❄️ 管理ポチッ！", key="k_btn"):
        handle_click("k", plus=True)
    if st.button("修正: 管理-1 & 貯金-100", key="k_undo"):
        handle_click("k", plus=False)
    st.markdown('</div>', unsafe_allow_html=True)
