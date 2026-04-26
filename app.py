import streamlit as st
import time
import random
import base64
from datetime import date

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
    .top-message {{
        text-align: center; padding: 15px; font-size: 18px; font-weight: 800;
        color: #0071BC; background: rgba(255, 255, 255, 0.95);
        border-bottom: 3px solid #80D8FF; margin: -10px -10px 20px -10px;
    }}
    .rainbow-header {{
        background: white; border-radius: 20px;
        border: 4px solid #80D8FF; padding: 15px; text-align: center; margin-bottom: 20px;
    }}
    .money-card, .pop-card {{
        background: white !important; border-radius: 20px; padding: 20px; 
        border: 2px solid #B3E5FC; margin-bottom: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }}
    .stButton > button {{
        width: 100% !important; height: 75px !important; font-size: 22px !important;
        font-weight: bold !important; border-radius: 35px !important;
        transition: 0.3s;
    }}
    .stButton > button:hover {{ transform: scale(1.02); box-shadow: 0 5px 15px rgba(0,0,0,0.2); }}
    /* 財務ボタン：深みのある青 */
    .stButton > button[key*="z_btn"] {{ background: linear-gradient(135deg, #4FC3F7 0%, #0288D1 100%) !important; color: white !important; }}
    /* 管理ボタン：鮮やかな水色 */
    .stButton > button[key*="k_btn"] {{ background: linear-gradient(135deg, #26C6DA 0%, #0097A7 100%) !important; color: white !important; }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. 🔗 URLパラメータ同期システム 🔗 ---
query_params = st.query_params

# 初期値設定（進捗は維持、貯金は0から）
if 'z' not in st.session_state:
    st.session_state.z = int(query_params.get("z", 39))
if 'k' not in st.session_state:
    st.session_state.k = int(query_params.get("k", 15))
if 'money' not in st.session_state:
    st.session_state.money = int(query_params.get("m", 0))

# --- 📣 褒め言葉リスト ---
praises = {
    "z": ["💎 財務会計の神！仕訳のスピードが光の速さ！", "💎 資産価値爆上がり！君の努力は複利で増えるよ！", "💎 連結修正も怖くない！無敵の集中力！"],
    "k": ["❄️ 管理会計の天才！意思決定が神がかってる！", "❄️ コスト管理の達人！最短ルートを爆走中！", "❄️ 限界利益も君のやる気もMAXだね！"]
}

# --- 5. メイン表示 ---
st.markdown(f'<div class="top-message">🧸 今日も君の努力が未来を創るよ！</div>', unsafe_allow_html=True)

col_a, col_b = st.columns([1, 1.5])
with col_a:
    st.image("bear.png", use_container_width=True)
with col_b:
    st.markdown('<div class="money-card">', unsafe_allow_html=True)
    st.image("money_bag.png", width=100) 
    st.markdown(f"<h1 style='color:#FFB300; margin:0;'>¥ {st.session_state.money:,}</h1>", unsafe_allow_html=True)
    st.link_button("🌸 講義ページを開く", "https://tlp.edulio.com/cpa/mypage/chapter/")
    st.markdown('</div>', unsafe_allow_html=True)

# 🚀 クリック処理（演出をじっくり見せる2秒のタメを追加！）
def handle_click(subj, plus=True):
    if plus:
        if subj == "z":
            st.session_state.z += 1
            st.balloons() # 財務は風船！
        else:
            st.session_state.k += 1
            st.snow()     # 管理は雪！
        
        st.session_state.money += 100
        st.toast(random.choice(praises[subj]), icon="🧸")
        
        # ここで2秒間停止して演出を見せる！
        time.sleep(2.0)
    else:
        if subj == "z": st.session_state.z -= 1
        else: st.session_state.k -= 1
        st.session_state.money -= 100
    
    # URLを更新して保存
    st.query_params.update(
        z=st.session_state.z,
        k=st.session_state.k,
        m=st.session_state.money
    )
    st.rerun()

# --- 操作パネル ---
st.write("---")
col_1, col_2 = st.columns(2)

with col_1:
    st.markdown('<div class="pop-card">', unsafe_allow_html=True)
    st.subheader("📘 財務会計")
    st.metric("完了", f"{st.session_state.z} / 70")
    if st.button("💎 財務ポチッ！", key="z_btn"): handle_click("z", True)
    if st.button("修正（-1）", key="z_undo"): handle_click("z", False)
    st.markdown('</div>', unsafe_allow_html=True)

with col_2:
    st.markdown('<div class="pop-card">', unsafe_allow_html=True)
    st.subheader("📙 管理会計")
    st.metric("完了", f"{st.session_state.k} / 33")
    if st.button("❄️ 管理ポチッ！", key="k_btn"): handle_click("k", True)
    if st.button("修正（-1）", key="k_undo"): handle_click("k", False)
    st.markdown('</div>', unsafe_allow_html=True)

st.info("💡 使い方：ポチッとした後、風船やメッセージが出る2秒間は『お祝いタイム』です！その後自動で保存されます。")
