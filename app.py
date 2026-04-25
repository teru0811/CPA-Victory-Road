import streamlit as st
from datetime import date
from streamlit_javascript import st_javascript
import base64

# --- ページ設定 ---
st.set_page_config(page_title="CPA合格クマちゃん貯金箱🧸", page_icon="🧸")

# --- 画像をBase64に変換する魔法（背景用） ---
def get_image_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

# 各画像の読み込み
sun_b64 = get_image_base64("sun.png")
money_b64 = get_image_base64("money.png")
back_b64 = get_image_base64("back.png")

# --- デザイン設定 ---
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{back_b64}");
        background-size: cover;
        background-attachment: fixed;
    }}
    .header-box {{
        background-color: rgba(255, 255, 255, 0.8);
        padding: 15px; border-radius: 20px; text-align: center; border: 2px solid #FFDAB9;
    }}
    .stButton > button {{
        background: linear-gradient(135deg, #FFDAB9, #FFB6C1) !important;
        color: #8B4513 !important; border-radius: 30px !important; height: 60px !important;
        font-weight: bold !important; width: 100%; border: none !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- localStorageでのデータ保存 ---
s_money = st_javascript("localStorage.getItem('cpa_v8_money');")
s_z = st_javascript("localStorage.getItem('cpa_v8_z');")
s_k = st_javascript("localStorage.getItem('cpa_v8_k');")

if 'money' not in st.session_state:
    st.session_state.money = int(s_money) if s_money and s_money != "null" else 0
    st.session_state.z = int(s_z) if s_z and s_z != "null" else 39
    st.session_state.k = int(s_k) if s_k and s_k != "null" else 15

def save():
    st_javascript(f"localStorage.setItem('cpa_v8_money', '{st.session_state.money}');")
    st_javascript(f"localStorage.setItem('cpa_v8_z', '{st.session_state.z}');")
    st_javascript(f"localStorage.setItem('cpa_v8_k', '{st.session_state.k}');")

# --- メイン画面 ---
days = (date(2026, 5, 31) - date.today()).days

st.markdown(f'<div class="header-box">', unsafe_allow_html=True)
if sun_b64:
    st.markdown(f'<img src="data:image/png;base64,{sun_b64}" width="50">', unsafe_allow_html=True)
st.markdown(f'<h2 style="color:#8B4513; margin:0;">CPA合格クマちゃん貯金箱</h2><p>試験まで あと {days} 日</p></div>', unsafe_allow_html=True)

# クマさん
st.image("bear.png", width=200)

t1, t2 = st.tabs(["📘 財務", "📙 管理"])
with t1:
    st.metric("財務進捗", f"{st.session_state.z} / 70")
    if st.button("財務 完了！ポチッ"):
        st.session_state.z += 1; st.session_state.money += 500; save(); st.rerun()
with t2:
    st.metric("管理進捗", f"{st.session_state.k} / 33")
    if st.button("管理 完了！ポチッ"):
        st.session_state.k += 1; st.session_state.money += 500; save(); st.rerun()

# 貯金箱
st.markdown('<div style="background:rgba(255,255,255,0.8); padding:10px; border-radius:15px; text-align:center;">', unsafe_allow_html=True)
if money_b64:
    st.markdown(f'<img src="data:image/png;base64,{money_b64}" width="40">', unsafe_allow_html=True)
st.write(f"### ご褒美貯金：¥{st.session_state.money:,}")
st.markdown('</div>', unsafe_allow_html=True)
