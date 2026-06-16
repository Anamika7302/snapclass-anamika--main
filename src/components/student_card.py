import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    with st.container(border=True):
        c1, c2 = st.columns([4, 1])

        with c1:
            st.markdown(
                f"""
                <h3 style='margin-bottom:0;color:#EB459E;'>{name}</h3>
                <p style='color:gray; margin-top:4px;'>
                Code: <b>{code}</b> | Section: <b>{section}</b>
                </p>
                """,
                unsafe_allow_html=True
            )

        if stats:
            cols = st.columns(len(stats))
            for i, (icon, label, value) in enumerate(stats):
                with cols[i]:
                    st.metric(
                        label=f"{icon} {label}",
                        value=value
                    )

        if footer_callback:
            footer_callback()

        st.divider()