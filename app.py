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

# --- 3. 💖 水色ポップ・デザイン (CSS) 💖 ---
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
    
    /* 貯金袋カード：イラストに合わせて可愛く */
    .money-card {{
        background: rgba(255, 255, 255, 0.9);
        border-radius: 25px;
        padding: 15px;
        border: 3px solid #FFCCFF; /* 貯金袋に合わせてピンクのフチに */
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
        width: 100% !important; height: 65px !important; font-size: 19px !important;
        font-weight: bold !important; border-radius: 35px !important; 
        transition: 0.3s; border: 3px solid #FFFFFF !important;
    }}
    .stButton > button[key*="z_"] {{ background: linear-gradient(135deg, #4FC3F7 0%, #81D4FA 100%) !important; color: white !important; box-shadow: 0 5px 0px #039BE5 !important; }}
    .stButton > button[key*="k_"] {{ background: linear-gradient(135deg, #26C6DA 0%, #80DEEA 100%) !important; color: white !important; box-shadow: 0 5px 0px #00ACC1 !important; }}
    
    [data-testid="stMetricValue"] {{ color: #0288D1 !important; font-size: 32px !important; font-weight: bold; }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. 記憶の魔法 ---
# データIDを貯金袋版(v28)に更新
s_z = st_javascript("localStorage.getItem('cpa_v28_z');")
s_k = st_javascript("localStorage.getItem('cpa_v28_k');")
s_m = st_javascript("localStorage.getItem('cpa_v28_money');")

if 'z' not in st.session_state:
    st.session_state.z = int(s_z) if s_z and s_z != "null" else 39
    st.session_state.k = int(s_k) if s_k and s_k != "null" else 15
    st.session_state.money = int(s_m) if s_m and s_m != "null" else 0

def save():
    st_javascript(f"localStorage.setItem('cpa_v28_z', '{st.session_state.z}');")
    st_javascript(f"localStorage.setItem('cpa_v28_k', '{st.session_state.k}');")
    st_javascript(f"localStorage.setItem('cpa_v28_money', '{st.session_state.money}');")

# --- 5. メイン表示 ---

goal_date = date(2026, 5, 31) 
days_left = (goal_date - date.today()).days

st.markdown(f'''
    <div class="rainbow-header">
        <div class="main-title">💎 クマ勉ログ 💎</div>
        <div style="color:#0288D1; font-weight:bold; font-size:18px;">
            完走目標まで あと <b>{max(0, days_left)}</b> 日
        </div>
    </div>
    ''', unsafe_allow_html=True)

# --- 上段：レイアウト ---
# クマさん(左) と 貯金袋(右) を並べる
top_col1, top_col2 = st.columns([1, 1.5])

with top_col1:
    # 応援クマちゃん
    st.image("bear.png", use_container_width=True)

with top_col2:
    st.markdown('<div class="money-card">', unsafe_allow_html=True)
    
    # 【ここを書き換え！】貯金袋の画像(money_bag.png)を表示
    # イラストなので、勉強部屋背景にバッチリ馴染みます！
    st.image("money_bag.png", width=160) 
    
    st.markdown(f"<p style='margin:0; font-size:36px; font-weight:900; color:#FFB300;'>¥ {st.session_state.money:,}</p>", unsafe_allow_html=True)
    ca, cb = st.columns([2,1])
    with ca:
        st.link_button("🌸 講義を開く", "https://tlp.edulio.com/cpa/mypage/chapter/")
    with cb:
        if st.button("リセット", key="reset_m"):
            st.session_state.money = 0; save(); st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

st.write("---")

# 財務と管理
mid_col1, mid_col2 = st.columns(2, gap="small")

with mid_col1:
    st.markdown('<div class="pop-card">', unsafe_allow_html=True)
    st.subheader("📘 財務会計")
    st.metric("完了", f"{st.session_state.z} / 70")
    st.progress(st.session_state.z / 70)
    if st.button("💎 財務完了！（+100円）", key="z_btn"):
        st.session_state.z += 1
        st.session_state.money += 100
        save(); st.balloons(); st.rerun()
    if st.button("修正: 財務-1", key="z_undo"):
        st.session_state.z -= 1; save(); st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

with mid_col2:
    st.markdown('<div class="pop-card">', unsafe_allow_html=True)
    st.subheader("📙 管理会計")
    st.metric("完了", f"{st.session_state.k} / 33")
    st.progress(st.session_state.k / 33)
    if st.button("❄️ 管理完了！（+100円）", key="k_btn"):
        st.session_state.k += 1
        st.session_state.money += 100
        save(); st.balloons(); st.rerun()
    if st.button("修正: 管理-1", key="k_undo"):
        st.session_state.k -= 1; save(); st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
