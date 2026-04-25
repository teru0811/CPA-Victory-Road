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

# --- 3. 💖 デザイン (視認性MAX) ---
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

# --- 4. 💎 データの絶対防衛 💎 ---
K_Z, K_K, K_M = 'CPA_ULTRA_Z', 'CPA_ULTRA_K', 'CPA_ULTRA_M'

res_z = st_javascript(f"localStorage.getItem('{K_Z}');")
res_k = st_javascript(f"localStorage.getItem('{K_K}');")
res_m = st_javascript(f"localStorage.getItem('{K_M}');")

if res_z is None:
    st.markdown("<h2 style='text-align:center; color:white; margin-top:100px;'>🧸 クマが全集中でデータを読み込み中...</h2>", unsafe_allow_html=True)
    st.stop()

if 'z' not in st.session_state:
    st.session_state.z = int(res_z) if res_z and res_z != "null" else 39
if 'k' not in st.session_state:
    st.session_state.k = int(res_k) if res_k and res_k != "null" else 15
if 'money' not in st.session_state:
    st.session_state.money = int(res_m) if res_m and res_m != "null" else 0

def save_all():
    st_javascript(f"localStorage.setItem('{K_Z}', '{st.session_state.z}');")
    st_javascript(f"localStorage.setItem('{K_K}', '{st.session_state.k}');")
    st_javascript(f"localStorage.setItem('{K_M}', '{st.session_state.money}');")

# --- 📣 メッセージリスト ---
# 財務会計用
praises_z = [
    "財務会計、お疲れ様！複雑な仕訳を乗り越える君の集中力、本当に尊敬しちゃうよ。合格への資産がまた積み上がったね！💎",
    "借方・貸方の迷宮を突破したね！今の1コマで、君の「会計士の脳」がさらに進化したよ。最高にかっこいい！🧸✨",
    "ポチッとお疲れ！計算の正確さとスピード、どんどん上がってるんじゃない？君の努力は数字に裏切られないよ！📈",
    "難しい論点だったよね。でも投げ出さなかった君は本当にえらい！今日の君は、昨日の君より100倍輝いてるよ！🌊"
]

# 管理会計用
praises_k = [
    "管理会計完了！コストの海を泳ぎきったね。君の分析眼はもうプロの域だよ。本当に誇らしい！❄️",
    "意思決定の天才！今の1コマで、未来を創る力がまた一段と強くなったね。貯金100円と一緒に自信もチャージ完了！💰",
    "お疲れ様！管理の理論は奥が深いけど、着実に自分のものにしてるね。君の粘り強さは、どんな難問も解き明かすよ！🐾",
    "この1コマの重み、クマちゃんは分かってるよ。コツコツ積み上げる君が、最後には一番遠いところまで行くんだね！🌻"
]

if 'daily_msg' not in st.session_state:
    st.session_state.daily_msg = random.choice([
        "今日の一歩が、合格発表の日の自分を救う。🔥",
        "未来の自分に、最高のプレゼントを贈ろう。💎",
        "夢を語る人は多い。でも実行する君は特別なんだ。🌊"
    ])

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

def click(subj, plus=True):
    if plus:
        if subj == "z":
            st.session_state.z += 1
            msg = random.choice(praises_z)
        else:
            st.session_state.k += 1
            msg = random.choice(praises_k)
        st.session_state.money += 100
        save_all()
        st.snow(); st.balloons()
        st.toast(msg, icon="🧸") # ここで長文褒め！
        time.sleep(2)
    else:
        if subj == "z": st.session_state.z -= 1
        else: st.session_state.k -= 1
        st.session_state.money -= 100
        save_all()
    st.rerun()

col_1, col_2 = st.columns(2)
with col_1:
    st.markdown('<div class="pop-card">', unsafe_allow_html=True)
    st.subheader("📘 財務会計")
    st.metric("完了", f"{st.session_state.z} / 70")
    st.progress(min(st.session_state.z / 70, 1.0))
    if st.button("💎 財務ポチッ！", key="z_btn"): click("z", True)
    if st.button("修正: 財-1 & ¥-100", key="z_undo"): click("z", False)
    st.markdown('</div>', unsafe_allow_html=True)

with col_2:
    st.markdown('<div class="pop-card">', unsafe_allow_html=True)
    st.subheader("📙 管理会計")
    st.metric("完了", f"{st.session_state.k} / 33")
    st.progress(min(st.session_state.k / 33, 1.0))
    if st.button("❄️ 管理ポチッ！", key="k_btn"): click("k", True)
    if st.button("修正: 管-1 & ¥-100", key="k_undo"): click("k", False)
    st.markdown('</div>', unsafe_allow_html=True)
