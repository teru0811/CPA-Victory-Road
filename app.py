import streamlit as st
import time
import random
import base64
from datetime import date
from streamlit_javascript import st_javascript

# --- 1. ページ設定（layout="wide" で横長モードに！） ---
st.set_page_config(page_title="クマ勉ログ 🎀", page_icon="🧸", layout="wide")

# --- 2. 画像読み込み ---
def get_image_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

back_b64 = get_image_base64("back.png")

# --- 3. 💖 横長スッキリ・デザイン (CSS) 💖 ---
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{back_b64}");
        background-size: cover;
        background-attachment: fixed;
    }}

    /* ヘッダーを少しコンパクトに */
    .rainbow-header {{
        background: rgba(255, 255, 255, 0.85);
        border-radius: 20px;
        border: 4px solid;
        border-image: linear-gradient(to right, #ff99ff, #99ffff) 1;
        padding: 10px;
        text-align: center;
        margin-bottom: 15px;
    }}
    .main-title {{ color: #FF66CC; font-size: 28px; font-weight: 900; margin: 0; }}

    /* カードを横に並べた時に綺麗に見える設定 */
    .pop-card {{
        background: rgba(255, 255, 255, 0.85);
        border-radius: 20px;
        padding: 15px;
        border: 2px solid #FFCCFF;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        min-height: 250px;
    }}

    /* ボタン（少し高さを抑えて横長に馴染ませる） */
    .stButton > button {{
        height: 60px !important;
        font-size: 20px !important;
        font-weight: bold !important;
        border-radius: 30px !important;
        border: 3px solid #FFFFFF !important;
    }}
    
    .stButton > button[key="z_btn"] {{
        background: linear-gradient(135deg, #FF66CC 0%, #FF99CC 100%) !important;
        box-shadow: 0 5px 0px #CC3399 !important;
    }}
    .stButton > button[key="k_btn"] {{
        background: linear-gradient(135deg, #33CCFF 0%, #99EEFF 100%) !important;
        box-shadow: 0 5px 0px #0099CC !important;
    }}

    [data-testid="stMetricValue"] {{
        color: #FF1493 !important;
        font-size: 35px !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. 記憶の魔法 ---
s_z = st_javascript("localStorage.getItem('cpa_v19_z');")
s_k = st_javascript("localStorage.getItem('cpa_v19_k');")

if 'z' not in st.session_state:
    st.session_state.z = int(s_z) if s_z and s_z != "null" else 39
    st.session_state.k = int(s_k) if s_k and s_k != "null" else 15

def save():
    st_javascript(f"localStorage.setItem('cpa_v19_z', '{st.session_state.z}');")
    st_javascript(f"localStorage.setItem('cpa_v19_k', '{st.session_state.k}');")

# --- 5. メイン表示 ---

# ヘッダー（カウントダウンとタイトルを1行に凝縮）
days_left = (date(2026, 5, 31) - date.today()).days
st.markdown(f"""
    <div class="rainbow-header">
        <span class="main-title">✨ クマ勉ログ ✨</span>
        <span style="color:#6666FF; font-weight:bold; margin-left:20px;">
            試験まであと <b>{max(0, days_left)}</b> 日！
        </span>
    </div>
    """, unsafe_allow_html=True)

# 上段：クマさんとお役立ちツールを横に並べる
top_col1, top_col2, top_col3 = st.columns([1, 1, 1.5])

with top_col1:
    st.image("bear.png", use_container_width=True)

with top_col2:
    st.markdown("##### 🧸 クマ応援＆リンク")
    if st.button("💌 応援もらう！"):
        st.toast(random.choice(["君ならできる！💪", "休憩も大事☕", "天才すぎる！✨"]))
    st.link_button("🌸 CPA講義へGO", "https://tlp.edulio.com/cpa/mypage/chapter/")

with top_col3:
    st.markdown("##### ⏱️ 集中タイマー")
    if st.button("⏲️ 1分スタート！"):
        p = st.empty()
        for i in range(60, -1, -1):
            p.write(f"⏳ あと {i} 秒...")
            time.sleep(1)
        st.balloons()

st.write("---")

# 下段：財務と管理を【左右に並べる】
mid_col1, mid_col2 = st.columns(2)

with mid_col1:
    st.markdown('<div class="pop-card">', unsafe_allow_html=True)
    st.subheader("📘 財務会計")
    st.metric("完了", f"{st.session_state.z} / 70")
    st.progress(st.session_state.z / 70)
    if st.button("✨ 財務完了ポチッ！", key="z_btn"):
        st.session_state.z += 1; save(); st.balloons(); st.rerun()
    if st.button("修正: 財務-1", key="uz"):
        st.session_state.z -= 1; save(); st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

with mid_col2:
    st.markdown('<div class="pop-card">', unsafe_allow_html=True)
    st.subheader("📙 管理会計")
    st.metric("完了", f"{st.session_state.k} / 33")
    st.progress(st.session_state.k / 33)
    if st.button("🔥 管理完了ポチッ！", key="k_btn"):
        st.session_state.k += 1; save(); st.balloons(); st.rerun()
    if st.button("修正: 管理-1", key="uk"):
        st.session_state.k -= 1; save(); st.rerun()
    st.markdown('</div>', unsafe_allow_html=True):
        st.session_state.k -= 1; save(); st.rerun()
