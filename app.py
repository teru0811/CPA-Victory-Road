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
    st.markdown('</div>', unsafe_allow_html=True) # ← ここ！最後を ) だけにする

with mid_col2:
    st.markdown('<div class="pop-card">', unsafe_allow_html=True)
    st.subheader("📙 管理会計")
    st.metric("完了", f"{st.session_state.k} / 33")
    st.progress(st.session_state.k / 33)
    if st.button("🔥 管理完了ポチッ！", key="k_btn"):
        st.session_state.k += 1; save(); st.balloons(); st.rerun()
    if st.button("修正: 管理-1", key="uk"):
        st.session_state.k -= 1; save(); st.rerun()
    st.markdown('</div>', unsafe_allow_html=True) # ← ここも！run()
