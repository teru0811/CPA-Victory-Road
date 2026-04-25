import streamlit as st
import time
import random
import base64
from datetime import date
from streamlit_javascript import st_javascript

# --- 1. ページ設定 ---
st.set_page_config(page_title="クマ勉ログ 🎀", page_icon="🎀")

# --- 2. 画像を背景に使うための魔法 ---
def get_image_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

back_b64 = get_image_base64("back.png")

# --- 3. 💖 デザイン設定 (CSS) 💖 ---
st.markdown(f"""
    <style>
    /* 全体の背景画像 */
    .stApp {{
        background-image: url("data:image/png;base64,{back_b64}");
        background-size: cover;
        background-attachment: fixed;
    }}
    
    /* クマさんの画像の「グレーの格子」を隠す魔法 */
    [data-testid="stImage"] {{
        background-color: rgba(255, 255, 255, 0.8); /* 白く光らせて背景になじませる */
        padding: 10px;
        border-radius: 50%; /* 丸く切り抜く */
        box-shadow: 0 0 20px white; /* 周りをぼかす */
    }}

    .header-box {{
        background-color: rgba(255, 255, 255, 0.85);
        padding: 20px; border-radius: 30px; border: 4px solid #FFFFFF;
        text-align: center; margin-bottom: 10px;
    }}
    .header-text {{ color: #FF69B4; font-size: 28px; font-weight: bold; margin: 0; }}
    
    .utility-box {{
        background-color: rgba(255, 255, 255, 0.9);
        padding: 15px; border-radius: 20px; margin: 10px 0;
        border: 2px solid #FFC0CB; text-align: center;
    }}

    .message-box {{
        background-color: #FFFFFF; color: #FF1493; padding: 15px;
        border-radius: 20px; border-left: 10px solid #FFC0CB;
        margin: 10px 0; font-weight: bold;
    }}

    .stButton > button {{
        background: linear-gradient(135deg, #FF9A9E 0%, #FAD0C4 100%) !important;
        color: white !important; height: 70px !important; width: 100% !important;
        border-radius: 35px !important; font-size: 20px !important;
        font-weight: bold !important; border: 4px solid #FFFFFF !important;
    }}
    
    .stTabs {{
        background-color: rgba(255, 255, 255, 0.8);
        padding: 15px; border-radius: 20px;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. 記憶の魔法 ---
s_z_count = st_javascript("localStorage.getItem('cpa_v15_z_count');")
s_k_count = st_javascript("localStorage.getItem('cpa_v15_k_count');")

if 'z_count' not in st.session_state:
    st.session_state.z_count = int(s_z_count) if s_z_count and s_z_count != "null" else 39
    st.session_state.k_count = int(s_k_count) if s_k_count and s_k_count != "null" else 15

def save_all():
    st_javascript(f"localStorage.setItem('cpa_v15_z_count', '{st.session_state.z_count}');")
    st_javascript(f"localStorage.setItem('cpa_v15_k_count', '{st.session_state.k_count}');")

# --- 5. メイン表示 ---
days_left = (date(2026, 5, 31) - date.today()).days
st.markdown(f'<div class="header-box"><p class="header-text">クマ勉ログ 🎀</p><p style="color:#6A5ACD; font-weight:bold; margin:0;">試験まであと <span style="font-size:24px; color:#FF1493;">{max(0, days_left)}</span> 日</p></div>', unsafe_allow_html=True)

# 応援メッセージ
messages = ["頑張ってるね！🧸", "財務の天才！✨", "休憩も大事だよ☕", "合格して楽しもう！🌈", "君ならできる！💪"]
with st.container():
    st.markdown('<div class="utility-box"><b>💌 クマちゃん応援</b>', unsafe_allow_html=True)
    if st.button("メッセージをもらう！"):
        st.markdown(f'<div class="message-box">{random.choice(messages)}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# タイマー
with st.container():
    st.markdown('<div class="utility-box"><b>⏱️ 1分タイマー</b>', unsafe_allow_html=True)
    if st.button("⏲️ スタート！"):
        p = st.empty()
        for i in range(60, -1, -1):
            p.markdown(f"### ⏳ 残り {i} 秒")
            time.sleep(1)
        p.markdown("### 🎉 終了！えらい！")
        st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

st.link_button("🌸 CPA講義ページへ飛ぶ", "https://tlp.edulio.com/cpa/mypage/chapter/")

# クマさん（周りを白くぼかしてなじませる）
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("bear.png", use_container_width=True)

# 進捗
tab1, tab2 = st.tabs(["📘 財務", "📙 管理"])
with tab1:
    st.metric("財務 完了", f"{st.session_state.z_count} / 70")
    st.progress(st.session_state.z_count / 70)
    if st.button("✨ 財務ポチッ！", key="z"):
        st.session_state.z_count += 1; save_all(); st.balloons(); st.rerun()
    if st.button("間違えた（財務-1）", key="uz"):
        st.session_state.z_count -= 1; save_all(); st.rerun()

with tab2:
    st.metric("管理 完了", f"{st.session_state.k_count} / 33")
    st.progress(st.session_state.k_count / 33)
    if st.button("🔥 管理ポチッ！", key="k"):
        st.session_state.k_count += 1; save_all(); st.balloons(); st.rerun()
    if st.button("間違えた（管理-1）", key="uk"):
        st.session_state.k_count -= 1; save_all(); st.rerun()
