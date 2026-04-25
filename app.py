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

# --- 3. 💖 デザイン ---
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

# --- 4. 💎 データの絶対防衛（新・金庫システム） 💎 ---
# キーを完全にリフレッシュします
DB_KEYS = {'z': 'CPA_MASTER_Z', 'k': 'CPA_MASTER_K', 'm': 'CPA_MASTER_M'}

# データの読み込み
val_z = st_javascript(f"localStorage.getItem('{DB_KEYS['z']}');")
val_k = st_javascript(f"localStorage.getItem('{DB_KEYS['k']}');")
val_m = st_javascript(f"localStorage.getItem('{DB_KEYS['m']}');")

# 🔴 読み込み待ち：データが「未確定」の間は、絶対に初期値を代入させない
if val_z is None:
    st.markdown("<h2 style='text-align:center; color:white; margin-top:100px;'>🧸 クマが金庫を確認中...</h2>", unsafe_allow_html=True)
    st.stop()

# 読み込みが完了してからセッションに格納
if 'init_done' not in st.session_state:
    st.session_state.z = int(val_z) if val_z and val_z != "null" else 39
    st.session_state.k = int(val_k) if val_k and val_k != "null" else 15
    st.session_state.money = int(val_m) if val_m and val_m != "null" else 0
    st.session_state.init_done = True

def sync_db():
    st_javascript(f"localStorage.setItem('{DB_KEYS['z']}', '{st.session_state.z}');")
    st_javascript(f"localStorage.setItem('{DB_KEYS['k']}', '{st.session_state.k}');")
    st_javascript(f"localStorage.setItem('{DB_KEYS['m']}', '{st.session_state.money}');")

# --- 📣 メッセージ設定 ---
if 'daily_msg' not in st.session_state:
    st.session_state.daily_msg = random.choice([
        "未来の自分に、最高のプレゼントを贈ろう。💎",
        "君が今日流す汗は、合格発表の日の笑顔に変わる。約束するよ。🔥",
        "小さな一歩が、一番遠い場所へ連れて行ってくれる。🐾"
    ])

# 褒め言葉（熱烈）
praises = {
    "z": ["財務会計の神！複雑な仕訳をさらっとこなす君、かっこよすぎる！💎", "仕訳の積み重ねは合格への資産！資産価値が爆上がりだね！📈"],
    "k": ["管理会計の天才！コストと時間を支配する君はもうプロの会計士！❄️", "意思決定のスピード、最高だね！今日の君は無敵だよ！💰"]
}

# --- 5. メイン表示 ---
st.markdown(f'<div class="top-message">🧸 {st.session_state.daily_msg}</div>', unsafe_allow_html=True)

# 完走日数
goal_date = date(2026, 5, 31) 
days_left = (goal_date - date.today()).days
st.markdown(f'''
    <div class="rainbow-header">
        <h2 style="margin:0; color:#0091EA;">💎 クマ勉ログ 💎</h2>
        <p style="margin:0; font-weight:bold; color:#666;">完走まで あと {max(0, days_left)} 日</p>
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
        st.snow(); st.balloons()
        st.toast(random.choice(praises[subj]), icon="🧸")
    else:
        if subj == "z": st.session_state.z -= 1
        else: st.session_state.k -= 1
        st.session_state.money -= 100
    sync_db()
    time.sleep(0.5)
    st.rerun()

col_1, col_2 = st.columns(2)
with col_1:
    st.markdown('<div class="pop-card">', unsafe_allow_html=True)
    st.subheader("📘 財務会計")
    st.metric("完了", f"{st.session_state.z} / 70")
    st.progress(min(st.session_state.z / 70, 1.0))
    if st.button("💎 財務ポチッ！", key="z_btn"): handle_click("z", True)
    if st.button("修正: 財-1 & ¥-100", key="z_undo"): handle_click("z", False)
    st.markdown('</div>', unsafe_allow_html=True)

with col_2:
    st.markdown('<div class="pop-card">', unsafe_allow_html=True)
    st.subheader("📙 管理会計")
    st.metric("完了", f"{st.session_state.k} / 33")
    st.progress(min(st.session_state.k / 33, 1.0))
    if st.button("❄️ 管理ポチッ！", key="k_btn"): handle_click("k", True)
    if st.button("修正: 管-1 & ¥-100", key="k_undo"): handle_click("k", False)
    st.markdown('</div>', unsafe_allow_html=True)
