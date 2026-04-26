import streamlit as st
import time
import random
import base64
from datetime import date
import streamlit.components.v1 as components

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
    /* 財務ボタン：金メダルカラー */
    .stButton > button[key*="z_btn"] {{ background: linear-gradient(135deg, #FFD700 0%, #FFA000 100%) !important; color: white !important; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); }}
    /* 管理ボタン：銀メダルカラー */
    .stButton > button[key*="k_btn"] {{ background: linear-gradient(135deg, #E0E0E0 0%, #9E9E9E 100%) !important; color: white !important; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. 🎉 超ド派手・おめでとう紙吹雪システム (JavaScript) ---
def play_conffeti():
    # 画面全体に広がるCanvasを作成し、紙吹雪を降らせるJSコード
    # 5秒間かけて下まで落ちて消える設定
    confetti_js = """
    <canvas id="confetti-canvas" style="position:fixed;top:0;left:0;width:100vw;height:100vh;pointer-events:none;z-index:999999;"></canvas>
    <script src="https://cdn.jsdelivr.net/npm/confetti-js@0.0.18/dist/index.min.js"></script>
    <script>
        var confettiSettings = { 
            target: 'confetti-canvas',
            respawn: false, // 一回きり
            size: 1.5,
            start_from_edge: true, // 上から降らす
            clock: 35, // 落ちる速度（少しゆっくり）
            props: ['circle', 'rect', 'triangle', 'line'],
            colors: [[165,104,246],[230,61,135],[0,199,235],[253,182,0]], # カラフル
            count: 150 # たくさん降らす
        };
        var confetti = new ConfettiGenerator(confettiSettings);
        confetti.render();
        // 5秒後にCanvasを削除して画面を綺麗にする
        setTimeout(() => {
            confetti.clear();
            document.getElementById('confetti-canvas').remove();
        }, 5000);
    </script>
    """
    components.html(confetti_js, height=0)

# --- 5. 🔗 URLパラメータ同期システム 🔗 ---
query_params = st.query_params
if 'z' not in st.session_state: st.session_state.z = int(query_params.get("z", 39))
if 'k' not in st.session_state: st.session_state.k = int(query_params.get("k", 15))
if 'money' not in st.session_state: st.session_state.money = int(query_params.get("m", 0))

# --- 📣 お祝いメッセージリスト ---
praises = [
    "🎉 天才！合格間違いなし！",
    "㊗️ おめでとう！努力の結晶だね！",
    "✨ 神対応！次もこの調子で！",
    "🏆 優勝！自分史上最高の集中力！",
    "💖 最高！クマちゃんも鼻が高いよ！"
]

# --- 6. メイン表示 ---
st.markdown(f'<div class="top-message">🧸 画面がキラキラする時は、君が輝いてる時！</div>', unsafe_allow_html=True)

col_a, col_b = st.columns([1, 1.5])
with col_a:
    st.image("bear.png", use_container_width=True)
with col_b:
    st.markdown('<div class="money-card">', unsafe_allow_html=True)
    st.image("money_bag.png", width=100) 
    st.markdown(f"<h1 style='color:#FFB300; margin:0;'>¥ {st.session_state.money:,}</h1>", unsafe_allow_html=True)
    st.link_button("🌸 講義ページを開く", "https://tlp.edulio.com/cpa/mypage/chapter/")
    st.markdown('</div>', unsafe_allow_html=True)

# 🚀 クリック処理（ド派手演出バージョン）
# セッション状態を保持するためのダミーコンポーネント
if 'playing_effect' not in st.session_state:
    st.session_state.playing_effect = False

def handle_click(subj, plus=True):
    if plus:
        if subj == "z": st.session_state.z += 1
        else: st.session_state.k += 1
        st.session_state.money += 100
        
        # クマの褒め言葉（Toast）を表示
        st.toast(random.choice(praises), icon="🧸")
        
        # 🔥 JavaScriptの紙吹雪を実行！
        st.session_state.playing_effect = True
        
    else:
        if subj == "z": st.session_state.z -= 1
        else: st.session_state.k -= 1
        st.session_state.money -= 100
    
    # URLを更新して保存
    st.query_params.update(z=st.session_state.z, k=st.session_state.k, m=st.session_state.money)
    
    # 演出中なら少し待ってからリラン
    if st.session_state.playing_effect:
        time.sleep(4.0) # 紙吹雪が下まで落ちるのを待つ
        st.session_state.playing_effect = False
        st.rerun()
    else:
        st.rerun()

# 演出を実行する場所
if st.session_state.playing_effect:
    play_conffeti()

# --- 操作パネル ---
st.write("---")
col_1, col_2 = st.columns(2)

with col_1:
    st.markdown('<div class="pop-card">', unsafe_allow_html=True)
    st.subheader("📘 財務会計")
    st.metric("完了", f"{st.session_state.z} / 70")
    # ボタン自体も金メダルカラーに！
    if st.button("🏆 財務完了！ポチッ！", key="z_btn"): handle_click("z", True)
    if st.button("修正（-1）", key="z_undo"): handle_click("z", False)
    st.markdown('</div>', unsafe_allow_html=True)

with col_2:
    st.markdown('<div class="pop-card">', unsafe_allow_html=True)
    st.subheader("📙 管理会計")
    st.metric("完了", f"{st.session_state.k} / 33")
    # ボタン自体も銀メダルカラーに！
    if st.button("🥈 管理完了！ポチッ！", key="k_btn"): handle_click("k", True)
    if st.button("修正（-1）", key="k_undo"): handle_click("k", False)
    st.markdown('</div>', unsafe_allow_html=True)

st.info("💡 使い方：ポチッとした後、4秒間はキラキラお祝いタイム！紙吹雪が下まで落ちるのを眺めてね。")
