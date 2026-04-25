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

# --- 3. 💖 視認性重視デザイン ---
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{back_b64}");
        background-size: cover;
        background-attachment: fixed;
    }}
    .top-message {{
        text-align: center; padding: 15px; font-size: 18px; font-weight: 800;
        color: #0071BC; background: rgba(255, 255, 255, 0.85);
        border-bottom: 3px solid #80D8FF; margin: -10px -10px 20px -10px;
    }}
    .rainbow-header {{
        background: white; border-radius: 20px;
        border: 4px solid #80D8FF; padding: 15px; text-align: center; margin-bottom: 20px;
    }}
    .money-card, .pop-card {{
        background: white !important; border-radius: 20px; padding: 20px; 
        border: 2px solid #B3E5FC; margin-bottom: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }}
    .stButton > button {{
        width: 100% !important; height: 60px !important; font-size: 18px !important;
        font-weight: bold !important; border-radius: 30px !important; 
    }}
    .stButton > button[key*="z_"] {{ background: linear-gradient(135deg, #4FC3F7 0%, #81D4FA 100%) !important; color: white !important; }}
    .stButton > button[key*="k_"] {{ background: linear-gradient(135deg, #26C6DA 0%, #80DEEA 100%) !important; color: white !important; }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. 💎 データの絶対防衛ロジック 💎 ---
# 保存用のキーを完全に新しくして、干渉を防ぎます
K_Z, K_K, K_M = 'CPA_DB_Z_V1', 'CPA_DB_K_V1', 'CPA_DB_M_V1'

# JavaScriptでデータを取得
res_z = st_javascript(f"localStorage.getItem('{K_Z}');")
res_k = st_javascript(f"localStorage.getItem('{K_K}');")
res_m = st_javascript(f"localStorage.getItem('{K_M}');")

# 🔴 重要：データが読み込めるまで初期化を待機する
if res_z is None or res_z == "":
    st.info("データを魔法の袋から取り出しています...🧸（数秒かかります）")
    st.stop() # 読み込みが終わるまで、下の描画を止める！

# 読み込み成功後、session_stateにセット（一度だけ）
if 'z' not in st.session_state:
    st.session_state.z = int(res_z) if res_z != "null" else 39
if 'k' not in st.session_state:
    st.session_state.k = int(res_k) if res_k != "null" else 15
if 'money' not in st.session_state:
    st.session_state.money = int(res_m) if res_m != "null" else 0

def save_all():
    st_javascript(f"localStorage.setItem('{K_Z}', '{st.session_state.z}');")
    st_javascript(f"localStorage.setItem('{K_K}', '{st.session_state.k}');")
    st_javascript(f"localStorage.setItem('{K_M}', '{st.session_state.money}');")

# --- 5. メイン表示 ---
if 'daily_msg' not in st.session_state:
    st.session_state.daily_msg = random.choice([
        "今日の一歩が、合格発表の日の自分を救う。🔥",
        "未来の自分に、最高のプレゼントを贈ろう。💎",
        "君ならできる。クマちゃんは信じてるよ。🐾"
    ])

st.markdown(f'<div class="top-message">🧸 {st.session_state.daily_msg}</div>', unsafe_allow_html=True)

# 完走日数計算
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

col_1, col_2 = st.columns(2)

def click(subj, plus=True):
    if plus:
        if subj == "z": st.session_state.z += 1
        else: st.session_state.k += 1
        st.session_state.money += 100
        save_all()
        st.snow(); st.balloons()
        time.sleep(1) # 保存の余韻
    else:
        if subj == "z": st.session_state.z -= 1
        else: st.session_state.k -= 1
        st.session_state.money -= 100
        save_all()
    st.rerun()

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
