import streamlit as st
import time
import random
import base64
from datetime import date
from streamlit_javascript import st_javascript

# --- 1. ページ設定 ---
st.set_page_config(page_title="CPA Log 🧸", page_icon="🧸", layout="centered")

# --- 2. 画像読み込み ---
def get_image_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

back_b64 = get_image_base64("back.png")

# --- 3. 💖 プレミアム・デザイン (CSS) 💖 ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700&display=swap');

    /* 全体のフォントと背景 */
    .stApp {{
        font-family: 'Noto Sans JP', sans-serif;
        background-image: url("data:image/png;base64,{back_b64}");
        background-size: cover;
        background-attachment: fixed;
    }}

    /* ガラス風ヘッダー */
    .glass-header {{
        background: rgba(255, 255, 255, 0.4);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 30px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        padding: 25px;
        text-align: center;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        margin-bottom: 20px;
    }}
    .title-text {{
        color: #5d5d5d;
        font-size: 22px;
        letter-spacing: 2px;
        font-weight: 700;
        margin: 0;
    }}
    .days-badge {{
        display: inline-block;
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
        color: white;
        padding: 5px 15px;
        border-radius: 50px;
        font-size: 14px;
        margin-top: 10px;
        font-weight: bold;
    }}

    /* ユーティリティ・カード */
    .utility-card {{
        background: rgba(255, 255, 255, 0.6);
        border-radius: 20px;
        padding: 15px;
        margin: 10px 0;
        border: 1px solid rgba(255, 255, 255, 0.5);
    }}

    /* プレミアム・ボタン */
    .stButton > button {{
        background: linear-gradient(to right, #6a11cb 0%, #2575fc 100%) !important; /* シックな青紫系グラデ */
        background: linear-gradient(135deg, #FF9A9E 0%, #FAD0C4 100%) !important; /* やっぱりピンク系 */
        color: white !important;
        border: none !important;
        padding: 15px 20px !important;
        border-radius: 18px !important;
        font-weight: bold !important;
        font-size: 18px !important;
        transition: 0.3s !important;
        box-shadow: 0 4px 15px rgba(255, 154, 158, 0.4) !important;
    }}
    .stButton > button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 154, 158, 0.6) !important;
    }}

    /* 進捗タブのカスタマイズ */
    .stTabs [data-baseweb="tab-list"] {{
        background-color: transparent;
    }}
    .stTabs [data-baseweb="tab"] {{
        background-color: rgba(255, 255, 255, 0.4);
        border-radius: 12px;
        margin-right: 5px;
        color: #888 !important;
    }}
    .stTabs [data-baseweb="tab"][aria-selected="true"] {{
        background-color: white;
        color: #FF69B4 !important;
        border: 1px solid #FFC0CB;
    }}
    
    /* 指標表示 */
    [data-testid="stMetric"] {{
        background: rgba(255, 255, 255, 0.5);
        padding: 10px;
        border-radius: 15px;
        text-align: center;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. 記憶の魔法 ---
s_z = st_javascript("localStorage.getItem('cpa_v17_z');")
s_k = st_javascript("localStorage.getItem('cpa_v17_k');")

if 'z' not in st.session_state:
    st.session_state.z = int(s_z) if s_z and s_z != "null" else 39
    st.session_state.k = int(s_k) if s_k and s_k != "null" else 15

def save():
    st_javascript(f"localStorage.setItem('cpa_v17_z', '{st.session_state.z}');")
    st_javascript(f"localStorage.setItem('cpa_v17_k', '{st.session_state.k}');")

# --- 5. メイン表示 ---

# ヘッダー
days_left = (date(2026, 5, 31) - date.today()).days
st.markdown(f"""
    <div class="glass-header">
        <p class="title-text">CPA STUDY LOG</p>
        <div class="days-badge">試験まで あと {max(0, days_left)} 日</div>
    </div>
    """, unsafe_allow_html=True)

# クマさん (スマホでの主役感)
col1, col2, col3 = st.columns([1,3,1])
with col2:
    st.image("bear.png", use_container_width=True)

# 応援 & リンク (横並びでスッキリ)
c1, c2 = st.columns(2)
with c1:
    if st.button("💌 Message"):
        msgs = ["君ならできる！💪", "休憩も大事☕", "一歩ずついこう🐾", "天才すぎる！✨"]
        st.toast(random.choice(msgs)) # 画面端にふわっと出す
with c2:
    st.link_button("🌸 CPA Link", "https://tlp.edulio.com/cpa/mypage/chapter/")

# 進捗セクション
st.markdown('<div class="utility-card">', unsafe_allow_html=True)
t1, t2 = st.tabs(["Financial", "Managerial"])
with t1:
    st.metric("Progress", f"{st.session_state.z} / 70")
    st.progress(st.session_state.z / 70)
    if st.button("DONE", key="z_btn"):
        st.session_state.z += 1; save(); st.balloons(); st.rerun()
with t2:
    st.metric("Progress", f"{st.session_state.k} / 33")
    st.progress(st.session_state.k / 33)
    if st.button("DONE", key="k_btn"):
        st.session_state.k += 1; save(); st.balloons(); st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# タイマー & 修正 (目立たなく配置)
with st.expander("Tools & Adjust"):
    if st.button("⏲️ 1min Timer"):
        p = st.empty()
        for i in range(60, -1, -1):
            p.write(f"Remaining: {i}s")
            time.sleep(1)
        st.success("Finish!")
    
    col_a, col_b = st.columns(2)
    if col_a.button("財務 -1"):
        st.session_state.z -= 1; save(); st.rerun()
    if col_b.button("管理 -1"):
        st.session_state.k -= 1; save(); st.rerun()
