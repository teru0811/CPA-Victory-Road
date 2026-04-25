import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
import time
import random
import base64
from datetime import date

# --- 1. ページ設定 ---
st.set_page_config(page_title="クマ勉システム 🧸", page_icon="🧸", layout="wide")

# --- 2. データベース接続 (Google SheetsをDBとして使用) ---
# ※Secretsに spreadsheet URL が入っている前提です
conn = st.connection("gsheets", type=GSheetsConnection)

def get_db_data():
    # キャッシュを無視して、今現在の「真実のデータ」をスプレッドシートから直接取ってくる
    df = conn.read(ttl="0s")
    data = df.set_index('item')['value'].to_dict()
    return int(data.get('z', 0)), int(data.get('k', 0)), int(data.get('money', 0))

def update_db_data(z, k, m):
    # スプレッドシートを「確定」データで上書きする
    df = pd.DataFrame({"item": ["z", "k", "money"], "value": [z, k, m]})
    conn.update(data=df)

# --- 3. システム起動 ---
# 起動した瞬間に、ブラウザの記憶ではなく、サーバー（シート）の値を正とする
current_z, current_k, current_m = get_db_data()

# --- 4. デザイン設定 ---
def get_image_base64(path):
    try:
        with open(path, "rb") as f: return base64.b64encode(f.read()).decode()
    except: return ""

back_b64 = get_image_base64("back.png")
st.markdown(f"""
    <style>
    .stApp {{ background-image: url("data:image/png;base64,{back_b64}"); background-size: cover; background-attachment: fixed; }}
    .status-card {{ background: white; border-radius: 15px; padding: 20px; border: 3px solid #80D8FF; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }}
    .stButton > button {{ width: 100%; height: 70px; font-size: 20px !important; font-weight: bold; border-radius: 35px; }}
    </style>
    """, unsafe_allow_html=True)

# --- 5. メイン画面 ---
st.markdown(f'<h2 style="text-align:center; color:#0071BC; background:rgba(255,255,255,0.8); border-radius:10px;">🧸 クマ勉・進捗同期システム 💎</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="status-card">', unsafe_allow_html=True)
    st.metric("📘 財務会計", f"{current_z} / 70")
    if st.button("💎 財務完了！", key="z_btn"):
        new_z = current_z + 1
        new_m = current_m + 100
        update_db_data(new_z, current_k, new_m)
        st.balloons()
        st.success("サーバーと同期しました！")
        time.sleep(1)
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="status-card">', unsafe_allow_html=True)
    st.metric("📙 管理会計", f"{current_k} / 33")
    if st.button("❄️ 管理完了！", key="k_btn"):
        new_k = current_k + 1
        new_m = current_m + 100
        update_db_data(current_z, new_k, new_m)
        st.snow()
        st.success("サーバーと同期しました！")
        time.sleep(1)
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="status-card">', unsafe_allow_html=True)
    st.image("money_bag.png", width=80)
    st.metric("💰 貯金箱", f"¥ {current_m:,}")
    st.markdown("合格への投資が積み上がってるよ！")
    st.markdown('</div>', unsafe_allow_html=True)

st.info("※このシステムはポチった瞬間にGoogleスプレッドシートを直接書き換えます。リロードしても、別端末から開いてもデータは常に最新です。")
