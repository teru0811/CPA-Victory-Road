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
        background: rgba(255, 255, 255, 0.85);
        border-radius: 20px;
        border: 4px solid #FFCCFF;
        padding: 15px;
        text-align: center;
        margin-bottom: 10px;
    }}
    .main-title {{ color: #FF66CC; font-size: 24px; font-weight: 900; }}
    .pop-card {{
        background: rgba(255, 255, 255, 0.9);
        border-radius: 20px;
        padding: 15px;
        border: 2px solid #FFCCFF;
        margin-bottom: 10px;
        width: 100%;
        box-sizing: border-box;
    }}
    .stButton > button {{
        width: 100% !important; height: 60px !important; font-size: 18px !important;
        font-weight: bold !important; border-radius: 30px !important; border: 3px solid #FFFFFF !important;
    }}
    .stButton > button[key*="z_"] {{ background: linear-gradient(135deg, #FF66CC 0%, #FF99CC 100%) !important; }}
    .stButton > button[key*="k_"] {{ background: linear-gradient(135deg, #33CCFF 0%, #99EEFF 100%) !important; }}
    [data-testid="stMetricValue"] {{ color: #FF1493 !important; font-size: 28px !important; }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. 記憶の魔法 ---
# 以前のデータと混ざらないようIDを更新
s_z = st_javascript("localStorage.getItem('cpa_v23_z');")
s_k = st_javascript("localStorage.getItem('cpa_v23_k');")

if 'z' not in st.session_state:
    st.session_state.z = int(s_z) if s_z and s_z != "null" else 39
    st.session_state.k = int(s_k) if s_k and s_k != "null" else 15

def save():
    st_javascript(f"localStorage.setItem('cpa_v23_z', '{st.session_state.z}');")
    st_javascript(f"localStorage.setItem('cpa_v23_k', '{st.session_state.k}');")

# --- 5. メイン表示 ---

# 目標日を 2026年5月31日に設定
goal_date = date(2026, 5, 31) 
days_left = (goal_date - date.today()).days

st.markdown(f'''
    <div class="rainbow-header">
        <div class="main-title">✨ クマ勉ログ ✨</div>
        <div style="color:#6666FF; font-weight:bold; font-size:18px; margin-top:5px;">
            🎉 全講義完走まで あと <span style="font-size:28px; color:#FF1493;">{max(0, days_left)}</span> 日！
        </div>
        <div style="font-size:12px; color:#999;">（目標リミット: {goal_date.strftime('%Y年%m月%d日')}）</div>
    </div>
    ''', unsafe_allow_html=True)

# クマさんとツール
top_col1, top_col2 = st.columns([1, 1.5])
with top_col1:
    st.image("bear.png", use_container_width=True)
with top_col2:
    if st.button("💌 クマからの激励", key="msg_btn"):
        st.toast(random.choice(["5月31日には笑ってようね！🌸", "今のポチッが未来を変える！🐾", "講義終わらせて最高の夏にしよう☕"]))
    if st.button("⏲️ 1分タイマー", key="timer_btn"):
        p = st.empty()
        for i in range(60, -1, -1):
            p.write(f"⏳ あと {i} 秒...")
            time.sleep(1)
        st.balloons()
    st.link_button("🌸 CPA講義ページへGO", "https://tlp.edulio.com/cpa/mypage/chapter/")

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
