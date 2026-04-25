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

# 新しい「勉強部屋」の背景画像を back.png として保存しておいてくださいね！
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
        background: rgba(255, 255, 255, 0.9);
        border-radius: 20px;
        border: 4px solid #FFCCFF;
        padding: 15px;
        text-align: center;
        margin-bottom: 10px;
    }}
    .main-title {{ color: #FF66CC; font-size: 24px; font-weight: 900; }}
    
    /* 勉強部屋背景に合わせて、カードの透明度を調整して文字を見やすく */
    .pop-card {{
        background: rgba(255, 255, 255, 0.92);
        border-radius: 20px;
        padding: 15px;
        border: 2px solid #FFCCFF;
        margin-bottom: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }}
    
    .stButton > button {{
        width: 100% !important; height: 60px !important; font-size: 18px !important;
        font-weight: bold !important; border-radius: 30px !important; border: 3px solid #FFFFFF !important;
    }}
    /* 特別の講義スタートボタン（キラキラ） */
    .stButton > button[key="start_study"] {{
        background: linear-gradient(135deg, #66BB6A 0%, #43A047 100%) !important;
        box-shadow: 0 5px 0px #2E7D32 !important;
    }}
    
    .stButton > button[key*="z_"] {{ background: linear-gradient(135deg, #FF66CC 0%, #FF99CC 100%) !important; }}
    .stButton > button[key*="k_"] {{ background: linear-gradient(135deg, #33CCFF 0%, #99EEFF 100%) !important; }}
    [data-testid="stMetricValue"] {{ color: #FF1493 !important; font-size: 28px !important; }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. 記憶の魔法 ---
s_z = st_javascript("localStorage.getItem('cpa_v24_z');")
s_k = st_javascript("localStorage.getItem('cpa_v24_k');")

if 'z' not in st.session_state:
    st.session_state.z = int(s_z) if s_z and s_z != "null" else 39
    st.session_state.k = int(s_k) if s_k and s_k != "null" else 15

def save():
    st_javascript(f"localStorage.setItem('cpa_v24_z', '{st.session_state.z}');")
    st_javascript(f"localStorage.setItem('cpa_v24_k', '{st.session_state.k}');")

# --- 5. メイン表示 ---

goal_date = date(2026, 5, 31) 
days_left = (goal_date - date.today()).days

st.markdown(f'''
    <div class="rainbow-header">
        <div class="main-title">✨ クマ勉ログ ✨</div>
        <div style="color:#6666FF; font-weight:bold; font-size:18px; margin-top:5px;">
            🎉 全講義完走まで あと <span style="font-size:28px; color:#FF1493;">{max(0, days_left)}</span> 日！
        </div>
    </div>
    ''', unsafe_allow_html=True)

# --- 上段：ここが新しい「同時スタート」エリア ---
top_col1, top_col2 = st.columns([1, 1.5])

with top_col1:
    st.image("bear.png", use_container_width=True)

with top_col2:
    st.markdown('<div class="pop-card">', unsafe_allow_html=True)
    st.write("📖 **講義をはじめる**")
    
    # 講義ページを開きつつタイマーを動かすボタン
    if st.button("🚀 講義を開いて集中スタート！", key="start_study"):
        # 別タブで講義ページを開くJavaScript
        js = "window.open('https://tlp.edulio.com/cpa/mypage/chapter/')"
        st_javascript(js)
        
        # そのままタイマー開始
        st.write("---")
        p = st.empty()
        for i in range(60, -1, -1):
            p.markdown(f"### ⏳ 最初の1分集中！あと {i} 秒")
            time.sleep(1)
        st.success("最初の1分クリア！その調子！")
        st.balloons()
    
    if st.button("💌 クマからの激励", key="msg_btn"):
        st.toast(random.choice(["勉強部屋、いい感じ！🌸", "この1分が大きな一歩！🐾", "講義の海へいってらっしゃい！☕"]))
    st.markdown('</div>', unsafe_allow_html=True)

st.write("---")

# 財務と管理
mid_col1, mid_col2 = st.columns(2, gap="small")

with mid_col1:
    st.markdown('<div class="pop-card">', unsafe_allow_html=True)
    st.subheader("📘 財務会計")
    st.metric("完了", f"{st.session_state.z} / 70")
    st.progress(st.session_state.z / 70)
    if st.button("✨ 財務ポチッ！", key="z_btn"):
        st.session_state.z += 1; save(); st.balloons(); st.rerun()
    if st.button("修正: 財務-1", key="z_undo"):
        st.session_state.z -= 1; save(); st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

with mid_col2:
    st.markdown('<div class="pop-card">', unsafe_allow_html=True)
    st.subheader("📙 管理会計")
    st.metric("完了", f"{st.session_state.k} / 33")
    st.progress(st.session_state.k / 33)
    if st.button("🔥 管理ポチッ！", key="k_btn"):
        st.session_state.k += 1; save(); st.balloons(); st.rerun()
    if st.button("修正: 管理-1", key="k_undo"):
        st.session_state.k -= 1; save(); st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
