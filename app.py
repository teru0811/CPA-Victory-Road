import streamlit as st
import time
import random
from datetime import date
from streamlit_javascript import st_javascript

# --- 1. ページ設定 ---
st.set_page_config(page_title="クマ勉ログ 🎀", page_icon="🎀")

# --- 2. 💖 デザイン設定 (CSS) 💖 ---
st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(135deg, #FFDEE9 0%, #B5FFFC 100%);
    }}
    
    .header-box {{
        background-color: rgba(255, 255, 255, 0.7);
        padding: 20px;
        border-radius: 30px;
        border: 4px solid #FFFFFF;
        text-align: center;
        margin-bottom: 10px;
    }}
    .header-text {{ color: #FF69B4; font-size: 28px; font-weight: bold; margin: 0; }}
    
    .utility-box {{
        background-color: rgba(255, 255, 255, 0.5);
        padding: 15px;
        border-radius: 20px;
        margin: 10px 0;
        border: 2px solid #FFFFFF;
        text-align: center;
    }}

    /* 応援メッセージの吹き出し風デザイン */
    .message-box {{
        background-color: #FFFFFF;
        color: #FF1493;
        padding: 15px;
        border-radius: 20px;
        border-left: 10px solid #FFC0CB;
        margin: 10px 0;
        font-weight: bold;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }}

    .stLinkButton > a {{
        background: linear-gradient(to right, #ffffff, #fff0f5) !important;
        color: #FF69B4 !important;
        border-radius: 25px !important;
        border: 3px solid #FFC0CB !important;
        font-weight: bold !important;
    }}

    .stButton > button {{
        background: linear-gradient(135deg, #FF9A9E 0%, #FAD0C4 100%) !important;
        color: white !important;
        height: 70px !important;
        width: 100% !important;
        border-radius: 35px !important;
        font-size: 20px !important;
        font-weight: bold !important;
        border: 4px solid #FFFFFF !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. 🧠 記憶の魔法 ---
s_z_count = st_javascript("localStorage.getItem('cpa_v13_z_count');")
s_k_count = st_javascript("localStorage.getItem('cpa_v13_k_count');")

if 'z_count' not in st.session_state:
    st.session_state.z_count = int(s_z_count) if s_z_count and s_z_count != "null" else 39
    st.session_state.k_count = int(s_k_count) if s_k_count and s_k_count != "null" else 15

def save_all():
    st_javascript(f"localStorage.setItem('cpa_v13_z_count', '{st.session_state.z_count}');")
    st_javascript(f"localStorage.setItem('cpa_v13_k_count', '{st.session_state.k_count}');")

# --- 4. メイン表示 ---

# ヘッダー & カウントダウン
days_left = (date(2026, 5, 31) - date.today()).days
st.markdown(f"""
    <div class="header-box">
        <p class="header-text">クマ勉ログ 🎀</p>
        <p style="color:#6A5ACD; font-weight:bold; margin:0;">試験まであと <span style="font-size:24px; color:#FF1493;">{max(0, days_left)}</span> 日</p>
    </div>
    """, unsafe_allow_html=True)

# 応援メッセージ機能
messages = [
    "毎日コツコツ頑張ってるの、クマちゃんは知ってるよ！🧸",
    "財務の計算、昨日より早くなってるね！天才！✨",
    "疲れたら1分だけ目を閉じよう。休憩も勉強のうちだよ☕",
    "計算が合わなくても大丈夫。本番で合えばいいんだから！💪",
    "CPA合格して、やりたいこと全部やろうね！🌈",
    "今日の1コマが、未来の自分を助けるよ！🌸",
    "難しい論点も、クマちゃんと一緒なら乗り越えられる！🐾",
    "無理しすぎないでね。君のペースで大丈夫だよ。🌻"
]

with st.container():
    st.markdown('<div class="utility-box"><b>🧸 クマちゃんからの応援</b>', unsafe_allow_html=True)
    if st.button("💌 メッセージをもらう！"):
        msg = random.choice(messages)
        st.markdown(f'<div class="message-box">{msg}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 1分タイマー
with st.container():
    st.markdown('<div class="utility-box"><b>⏱️ 1分集中タイマー</b>', unsafe_allow_html=True)
    if st.button("⏲️ タイマースタート！"):
        placeholder = st.empty()
        for i in range(60, -1, -1):
            placeholder.markdown(f"### ⏳ 残り {i} 秒")
            time.sleep(1)
        placeholder.markdown("### 🎉 1分経過！えらすぎる！")
        st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

# 講義リンク
st.link_button("🌸 CPA講義ページへ飛ぶ 🌸", "https://tlp.edulio.com/cpa/mypage/chapter/")

# クマさん表示
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("bear.png", use_container_width=True)

# 進捗タブ
tab1, tab2 = st.tabs(["📘 財務会計", "📙 管理会計"])

with tab1:
    st.metric("財務 完了", f"{st.session_state.z_count} / 70")
    st.progress(st.session_state.z_count / 70)
    if st.button("✨ 財務ポチッ！", key="z_btn"):
        st.session_state.z_count += 1; save_all(); st.balloons(); st.rerun()
    if st.button("間違えて押した（財務-1）", key="uz"):
        st.session_state.z_count -= 1; save_all(); st.rerun()

with tab2:
    st.metric("管理 完了", f"{st.session_state.k_count} / 33")
    st.progress(st.session_state.k_count / 33)
    if st.button("🔥 管理ポチッ！", key="k_btn"):
        st.session_state.k_count += 1; save_all(); st.balloons(); st.rerun()
    if st.button("間違えて押した（管理-1）", key="uk"):
        st.session_state.k_count -= 1; save_all(); st.rerun()
