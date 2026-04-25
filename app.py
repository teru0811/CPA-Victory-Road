import streamlit as st
import random
from datetime import date
from streamlit_javascript import st_javascript
import base64

# --- ページ設定 ---
st.set_page_config(page_title="CPA合格への道🧸", page_icon="🧸")

# --- 画像を読み込むための関数 ---
def get_image_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

# 画像の読み込み
sun_b64 = get_image_base64("sun.png")
money_b64 = get_image_base64("money.png")
back_b64 = get_image_base64("back.png") # 新しい背景
bear_path = "bear.png"

# --- 1. デザイン（背景をback.pngに固定！） ---
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{back_b64}");
        background-size: cover;
        background-attachment: fixed;
    }}
    .header-box {{
        background-color: rgba(255, 249, 224, 0.9);
        padding: 20px; border-radius: 25px; border: 3px solid #FFDAB9;
        text-align: center; margin-bottom: 10px;
    }}
    .progress-card {{
        background: rgba(255, 255, 255, 0.9);
        padding: 20px; border-radius: 20px;
        border: 3px solid #B2EBF2; text-align: center; margin-bottom: 10px;
    }}
    .stButton > button {{
        background: linear-gradient(135deg, #FFDAB9, #FFB6C1) !important;
        color: #8B4513 !important; height: 70px !important; width: 100%;
        border-radius: 35px !important; font-size: 22px !important; border: 4px solid #FFF !important;
    }}
    .money-box {{
        background-color: rgba(255, 253, 231, 0.9);
        padding: 15px; border-radius: 20px; border: 2px solid #FFD100; text-align: center;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 2. 記憶の読み込み ---
s_money = st_javascript("localStorage.getItem('v7_money');")
s_z_count = st_javascript("localStorage.getItem('v7_z_count');")
s_k_count = st_javascript("localStorage.getItem('v7_k_count');")

if 'money' not in st.session_state:
    st.session_state.money = int(s_money) if s_money and s_money != "null" else 0
    st.session_state.z_count = int(s_z_count) if s_z_count and s_z_count != "null" else 39
    st.session_state.k_count = int(s_k_count) if s_k_count and s_k_count != "null" else 15

def save():
    st_javascript(f"localStorage.setItem('v7_money', '{st.session_state.money}');")
    st_javascript(f"localStorage.setItem('v7_z_count', '{st.session_state.z_count}');")
    st_javascript(f"localStorage.setItem('v7_k_count', '{st.session_state.k_count}');")

# --- 3. 表示 ---
# ヘッダー
days = (date(2026, 5, 31) - date.today()).days
st.markdown(f'<div class="header-box"><img src="data:image/png;base64,{sun_b64}" width="50"><br><b style="font-size:24px; color:#8B4513;">CPA合格への道🏆</b><br><b style="color:#D2691E;">5月31日まで あと {days} 日</b></div>', unsafe_allow_html=True)

# 中央のクマさん
st.image(bear_path, width=250)

# 進捗タブ
t1, t2 = st.tabs(["📘 財務会計", "📙 管理会計"])
with t1:
    st.markdown(f'<div class="progress-card"><h1 style="color:#00897B; margin:0;">{st.session_state.z_count} / 70</h1><p style="margin:0;">完了！</p></div>', unsafe_allow_html=True)
    if st.button("✨ 講義完了！ポチッ", key="z"):
        st.session_state.z_count += 1; st.session_state.money += 500; save(); st.rerun()

with t2:
    st.markdown(f'<div class="progress-card"><h1 style="color:#00897B; margin:0;">{st.session_state.k_count} / 33</h1><p style="margin:0;">完了！</p></div>', unsafe_allow_html=True)
    if st.button("🔥 講義完了！ポチッ", key="k"):
        st.session_state.k_count += 1; st.session_state.money += 500; save(); st.rerun()

# 貯金箱
st.markdown(f'<div class="money-box"><img src="data:image/png;base64,{money_b64}" width="40"><br><b style="font-size:22px; color:#D4AF37;">ご褒美貯金：¥{st.session_state.money:,}</b></div>', unsafe_allow_html=True)

# 修正ボタン
with st.expander("押し間違えを直す"):
    if st.button("財務を1コマ戻す"):
        st.session_state.z_count -= 1; st.session_state.money -= 500; save(); st.rerun()
    if st.button("管理を1コマ戻す"):
        st.session_state.k_count -= 1; st.session_state.money -= 500; save(); st.rerun()
