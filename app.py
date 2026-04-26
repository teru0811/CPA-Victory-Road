import streamlit as st
import time
import random
import base64
from datetime import date

# --- 1. ページ設定 ---
st.set_page_config(page_title="クマ勉ログ 🎀", page_icon="🧸", layout="wide")

# --- 2. 画像読み込み関数 ---
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
    .top-message {{
        text-align: center; padding: 15px; font-size: 18px; font-weight: 800;
        color: #0071BC; background: rgba(255, 255, 255, 0.95);
        border-bottom: 3px solid #80D8FF; margin: -10px -10px 20px -10px;
    }}
    .rainbow-header {{
        background: white; border-radius: 20px;
        border: 4px solid #80D8FF; padding: 15px; text-align: center; margin-bottom: 20px;
    }}
    .money-card, .pop-card {{
        background: white !important; border-radius: 20px; padding: 20px; 
        border: 2px solid #B3E5FC; margin-bottom: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }}
    .stButton > button {{
        width: 100% !important; height: 60px !important; font-size: 18px !important;
        font-weight: bold !important; border-radius: 30px !important; 
    }}
    .stButton > button[key*="z_"] {{ background: linear-gradient(135deg, #4FC3F7 0%, #81D4FA 100%) !important; color: white !important; }}
    .stButton > button[key*="k_"] {{ background: linear-gradient(135deg, #26C6DA 0%, #80DEEA 100%) !important; color: white !important; }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. 🔗 URLパラメータ同期システム（貯金リセット仕様） 🔗 ---
query_params = st.query_params

# 進捗はこれまでの数字をセット
if 'z' not in st.session_state:
    st.session_state.z = int(query_params.get("z", 39))
if 'k' not in st.session_state:
    st.session_state.k = int(query_params.get("k", 15))
# 貯金は 0 からスタート
if 'money' not in st.session_state:
    st.session_state.money = int(query_params.get("m", 0))

# --- 📣 メッセージ設定 ---
if 'daily_msg' not in st.session_state:
    st.session_state.daily_msg = random.choice([
        "過去の努力は君の力。今日からの貯金は君の楽しみ！💎",
        "心機一転、貯金箱をパンパンにしよう！🔥",
        "未来の自分へのプレゼント、積み立て開始！🐾"
    ])

praises = {
    "z": ["財務会計の神！複雑な仕訳をさらっとこなす君、かっこよすぎる！💎", "仕訳の積み重ねは合格への資産！資産価値が爆上がりだね！📈"],
    "k": ["管理会計の天才！コストと時間を支配する君はもうプロの会計士！❄️", "意思決定のスピード、最高だね！今日の君は無敵だよ！💰"]
}

# --- 5. メイン表示 ---
st.markdown(f'<div class="top-message">🧸 {st.session_state.daily_msg}</div>', unsafe_allow_html=True)

goal_date = date(2026, 5, 31) 
days_left = (goal_date - date.today()).days
st.markdown(f'''
    <div class="rainbow-header">
        <h2 style="margin:0; color:#0091EA;">💎 クマ勉ログ 💎</h2>
        <p style="margin:0; font-weight:bold; color:#666;">目標完走まで あと {max(0, days_left)} 日</p>
    </div>
    ''', unsafe_allow_html=True)

col_a, col_b = st.columns([1, 1.5])
with col_a:
    st.image("bear.png", use_container_width=True)
with col_b:
    st.markdown('<div class="money-card">', unsafe_allow_html=True)
    st.image("money_bag.png", width=120) 
    st.markdown(f"<h1 style='color:#FFB300; margin:0;'>¥ {st.session_state.money:,}</h1>", unsafe_allow_html=True)
    st.link_button("🌸 講義ページを開く", "https://tlp.edulio.com/cpa/mypage/chapter/")
    if st.button("⏲️ 1分集中開始", key="timer_btn"):
        p = st.empty()
        for i in range(60, -1, -1):
            p.markdown(f"<h3 style='color:#00B0FF; text-align:center;'>⏳ 残り {i} 秒</h3>", unsafe_allow_html=True)
            time.sleep(1)
        st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

st.write("---")

def handle_click(subj, plus=True):
    if plus:
        if subj == "z": st.session_state.z += 1
        else: st.session_state.k += 1
        st.session_state.money += 100
        st.toast(random.choice(praises[subj]), icon="🧸")
        st.snow()
    else:
        if subj == "z": st.session_state.z -= 1
        else: st.session_state.k -= 1
        st.session_state.money -= 100
    
    st.query_params.update(
        z=st.session_state.z,
        k=st.session_state.k,
        m=st.session_state.money
    )
    time.sleep(0.2)
    st.rerun()

col_1, col_2 = st.columns(2)
with col_1:
    st.markdown('<div class="pop-card">', unsafe_allow_html=True)
    st.subheader("📘 財務会計")
    st.metric("完了", f"{st.session_state.z} / 70")
    st.progress(min(st.session_state.z / 70, 1.0) if st.session_state.z > 0 else 0.0)
    if st.button("💎 財務ポチッ！", key="z_btn"): handle_click("z", True)
    if st.button("修正: 財-1 & ¥-100", key="z_undo"): handle_click("z", False)
    st.markdown('</div>', unsafe_allow_html=True)

with col_2:
    st.markdown('<div class="pop-card">', unsafe_allow_html=True)
    st.subheader("📙 管理会計")
    st.metric("完了", f"{st.session_state.k} / 33")
    st.progress(min(st.session_state.k / 33, 1.0) if st.session_state.k > 0 else 0.0)
    if st.button("❄️ 管理ポチッ！", key="k_btn"): handle_click("k", True)
    if st.button("修正: 管-1 & ¥-100", key="k_undo"): handle_click("k", False)
    st.markdown('</div>', unsafe_allow_html=True)
