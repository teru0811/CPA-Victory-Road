import streamlit as st
import time
import random
import base64
from datetime import date
from streamlit_javascript import st_javascript

# --- 1. ページ設定 ---
st.set_page_config(page_title="クマ勉ログ 🎀", page_icon="🧸")

# --- 2. 画像読み込み ---
def get_image_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

back_b64 = get_image_base64("back.png")

# --- 3. 💖 カラフル・ポップ・デザイン (CSS) 💖 ---
st.markdown(f"""
    <style>
    /* 全体の背景 */
    .stApp {{
        background-image: url("data:image/png;base64,{back_b64}");
        background-size: cover;
        background-attachment: fixed;
    }}

    /* タイトルボックス（虹色グラデの枠！） */
    .rainbow-header {{
        background: rgba(255, 255, 255, 0.8);
        border-radius: 30px;
        border: 5px solid;
        border-image: linear-gradient(to right, #ff99ff, #99ffff) 1; /* 虹色のフチ */
        padding: 20px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }}
    .main-title {{
        color: #FF66CC;
        font-size: 32px;
        font-weight: 900;
        text-shadow: 2px 2px 0px #FFFFFF;
        margin-bottom: 5px;
    }}
    .days-text {{
        color: #6666FF;
        font-size: 18px;
        font-weight: bold;
    }}

    /* 応援・タイマーのカード */
    .pop-card {{
        background: rgba(255, 255, 255, 0.8);
        border-radius: 20px;
        padding: 15px;
        margin: 10px 0;
        border: 2px solid #FFCCFF;
    }}

    /* 財務ボタン（キャンディピンク） */
    .stButton > button[key="z_btn"] {{
        background: linear-gradient(135deg, #FF66CC 0%, #FF99CC 100%) !important;
        color: white !important;
        border-radius: 30px !important;
        height: 80px !important;
        font-size: 24px !important;
        font-weight: bold !important;
        border: 4px solid #FFFFFF !important;
        box-shadow: 0 8px 0px #CC3399 !important; /* 飛び出すような立体感 */
    }}
    
    /* 管理ボタン（ソーダブルー） */
    .stButton > button[key="k_btn"] {{
        background: linear-gradient(135deg, #33CCFF 0%, #99EEFF 100%) !important;
        color: white !important;
        border-radius: 30px !important;
        height: 80px !important;
        font-size: 24px !important;
        font-weight: bold !important;
        border: 4px solid #FFFFFF !important;
        box-shadow: 0 8px 0px #0099CC !important;
    }}

    /* タブの色 */
    .stTabs [data-baseweb="tab"] {{
        color: #999 !important;
        font-size: 18px !important;
        font-weight: bold !important;
    }}
    .stTabs [aria-selected="true"] {{
        color: #FF66CC !important;
        border-bottom: 4px solid #FF66CC !important;
    }}
    
    /* 進捗の数字 */
    [data-testid="stMetricValue"] {{
        color: #FF1493 !important;
        font-size: 40px !important;
        font-weight: 900 !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. 記憶の魔法 ---
s_z = st_javascript("localStorage.getItem('cpa_v18_z');")
s_k = st_javascript("localStorage.getItem('cpa_v18_k');")

if 'z' not in st.session_state:
    st.session_state.z = int(s_z) if s_z and s_z != "null" else 39
    st.session_state.k = int(s_k) if s_k and s_k != "null" else 15

def save():
    st_javascript(f"localStorage.setItem('cpa_v18_z', '{st.session_state.z}');")
    st_javascript(f"localStorage.setItem('cpa_v18_k', '{st.session_state.k}');")

# --- 5. メイン表示 ---

# ヘッダー
days_left = (date(2026, 5, 31) - date.today()).days
st.markdown(f"""
    <div class="rainbow-header">
        <p class="main-title">✨ クマ勉ログ ✨</p>
        <p class="days-text">試験まで あと <b>{max(0, days_left)}</b> 日！</p>
    </div>
    """, unsafe_allow_html=True)

# 応援＆リンクを横並びでポップに
c1, c2 = st.columns(2)
with c1:
    if st.button("💌 クマ応援！"):
        msgs = ["君ならできる！💪", "休憩も大事だよ☕", "一歩ずついこう🐾", "天才すぎる！✨", "合格して遊びまくろ！🌈"]
        st.toast(random.choice(msgs))
with c2:
    st.link_button("🌸 CPA講義へGO", "https://tlp.edulio.com/cpa/mypage/chapter/")

# クマさん
col1, col2, col3 = st.columns([1,4,1])
with col2:
    st.image("bear.png", use_container_width=True)

# 進捗エリア
st.markdown('<div class="pop-card">', unsafe_allow_html=True)
tab1, tab2 = st.tabs(["📘 財務会計", "📙 管理会計"])

with tab1:
    st.metric("完了したコマ数", f"{st.session_state.z} / 70")
    st.progress(st.session_state.z / 70)
    if st.button("✨ 財務ポチッ！", key="z_btn"):
        st.session_state.z += 1; save(); st.balloons(); st.rerun()

with tab2:
    st.metric("完了したコマ数", f"{st.session_state.k} / 33")
    st.progress(st.session_state.k / 33)
    if st.button("🔥 管理ポチッ！", key="k_btn"):
        st.session_state.k += 1; save(); st.balloons(); st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# お役立ちツール
with st.expander("🛠️ タイマーとか修正とか"):
    if st.button("⏲️ 1分集中タイマー"):
        p = st.empty()
        for i in range(60, -1, -1):
            p.markdown(f"### ⏳ あと {i} 秒...")
            time.sleep(1)
        st.success("お疲れ様！えらすぎる！🎉")
        st.balloons()
    
    st.write("---")
    st.write("押し間違えた時はここから直してね！")
    ca, cb = st.columns(2)
    if ca.button("財務 -1回"):
        st.session_state.z -= 1; save(); st.rerun()
    if cb.button("管理 -1回"):
        st.session_state.k -= 1; save(); st.rerun()
