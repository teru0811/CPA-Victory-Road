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
    .rainbow-header {{
        background: rgba(230, 247, 255, 0.9);
        border-radius: 20px;
        border: 4px solid #80D8FF;
        padding: 15px;
        text-align: center;
        margin-bottom: 10px;
    }}
    .main-title {{ color: #0091EA; font-size: 24px; font-weight: 900; }}
    .money-card {{
        background: rgba(255, 255, 255, 0.9);
        border-radius: 25px;
        padding: 15px;
        border: 3px solid #FFCCFF;
        text-align: center;
        margin-bottom: 10px;
    }}
    .pop-card {{
        background: rgba(255, 255, 255, 0.95);
        border-radius: 25px;
        padding: 20px;
        border: 3px solid #B3E5FC;
        margin-bottom: 15px;
    }}
    .stButton > button {{
        width: 100% !important; height: 60px !important; font-size: 18px !important;
        font-weight: bold !important; border-radius: 30px !important; 
        transition: 0.3s; border: 3px solid #FFFFFF !important;
    }}
    /* タイマーボタン専用（ソーダ色） */
    .stButton > button[key="timer_btn"] {{
        background: linear-gradient(135deg, #00B0FF 0%, #00E5FF 100%) !important;
        color: white !important;
        box-shadow: 0 5px 0px #0091EA !important;
    }}
    .stButton > button[key*="z_"] {{ background: linear-gradient(135deg, #4FC3F7 0%, #81D4FA 100%) !important; color: white !important; box-shadow: 0 5px 0px #039BE5 !important; }}
    .stButton > button[key*="k_"] {{ background: linear-gradient(135deg, #26C6DA 0%, #80DEEA 100%) !important; color: white !important; box-shadow: 0 5px 0px #00ACC1 !important; }}
    [data-testid="stMetricValue"] {{ color: #0288D1 !important; font-size: 32px !important; font-weight: bold; }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. 記憶の魔法 (IDを固定して確実に保存) ---
s_z = st_javascript("localStorage.getItem('cpa_v30_z');")
s_k = st_javascript("localStorage.getItem('cpa_v30_k');")
s_m = st_javascript("localStorage.getItem('cpa_v30_money');")

if 'z' not in st.session_state:
    st.session_state.z = int(s_z) if s_z and s_z != "null" else 39
    st.session_state.k = int(s_k) if s_k and s_k != "null" else 15
    st.session_state.money = int(s_m) if s_m and s_m != "null" else 0

def save_data():
    st_javascript(f"localStorage.setItem('cpa_v30_z', '{st.session_state.z}');")
    st_javascript(f"localStorage.setItem('cpa_v30_k', '{st.session_state.k}');")
    st_javascript(f"localStorage.setItem('cpa_v30_money', '{st.session_state.money}');")

# --- 5. メイン表示 ---
goal_date = date(2026, 5, 31) 
days_left = (goal_date - date.today()).days

st.markdown(f'''
    <div class="rainbow-header">
        <div class="main-title">💎 クマ勉ログ 💎</div>
        <div style="color:#0288D1; font-weight:bold; font-size:18px;">
            完走まで あと <b>{max(0, days_left)}</b> 日
        </div>
    </div>
    ''', unsafe_allow_html=True)

top_col1, top_col2 = st.columns([1, 1.5])

with top_col1:
    st.image("bear.png", use_container_width=True)

with top_col2:
    st.markdown('<div class="money-card">', unsafe_allow_html=True)
    st.image("money_bag.png", width=140) 
    st.markdown(f"<p style='margin:0; font-size:32px; font-weight:900; color:#FFB300;'>¥ {st.session_state.money:,}</p>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1.5, 1.5, 1])
    with c1:
        st.link_button("🌸 講義ページ", "https://tlp.edulio.com/cpa/mypage/chapter/")
    with c2:
        if st.button("⏲️ 1分集中", key="timer_btn"):
            placeholder = st.empty()
            for i in range(60, -1, -1):
                placeholder.markdown(f"### ⏳ 残り {i} 秒")
                time.sleep(1)
            st.balloons()
    with c3:
        if st.button("空に!", key="reset_m"):
            st.session_state.money = 0; save_data(); st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

st.write("---")

mid_col1, mid_col2 = st.columns(2, gap="small")

with mid_col1:
    st.markdown('<div class="pop-card">', unsafe_allow_html=True)
    st.subheader("📘 財務会計")
    st.metric("完了", f"{st.session_state.z} / 70")
    st.progress(st.session_state.z / 70)
    if st.button("💎 財務完了！(+100円)", key="z_btn"):
        st.session_state.z += 1
        st.session_state.money += 100
        save_data()
        st.balloons()
        st.rerun()
    if st.button("修正: 財務-1", key="z_undo"):
        st.session_state.z -= 1; save_data(); st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

with mid_col2:
    st.markdown('<div class="pop-card">', unsafe_allow_html=True)
    st.subheader("📙 管理会計")
    st.metric("完了", f"{st.session_state.k} / 33")
    st.progress(st.session_state.k / 33)
    if st.button("❄️ 管理完了！(+100円)", key="k_btn"):
        st.session_state.k += 1
        st.session_state.money += 100
        save_data()
        st.balloons()
        st.rerun()
    if st.button("修正: 管理-1", key="k_undo"):
        st.session_state.k -= 1; save_data(); st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
