import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
    <div style="background:white;border:2px solid #bfc6d4;border-radius:18px;padding:18px;margin-bottom:4px;box-shadow:0 2px 8px rgba(0,0,0,0.05);">
        <h3 style="margin:0;color:#EB459E;font-size:32px;">{name}</h3>
        <p style="color:#666;margin:8px 0 14px 0;font-size:18px;">
            Code: <b>{code}</b> | Section: <b>{section}</b>
        </p>
    """

    if stats:
        html += '<div style="display:flex;gap:12px;flex-wrap:wrap;">'

        for icon, label, value in stats:
            html += f"""
            <div style="background:#F8FAFC;padding:8px 14px;border-radius:12px;border:1px solid #E2E8F0;font-size:15px;">
                {icon} <b>{value}</b> {label}
            </div>
            """

        html += "</div>"

    html += "</div>"

    st.html(html)   

    if footer_callback:
        footer_callback()