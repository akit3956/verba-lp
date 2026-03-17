import streamlit as st

st.set_page_config(page_title="Terms & Privacy - Verba", page_icon="📜", layout="centered")

st.title("📜 Terms of Service & Privacy Policy")
st.write("利用規約およびプライバシーポリシー (Terms of Service and Privacy Policy)")

st.markdown("---")

# Dummy text container for full screen scrolling reading
text = """
### 1. Introduction (はじめに)
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam in dui mauris. Vivamus hendrerit arcu sed erat molestie vehicula.
(ここに後ほど本番の利用規約やプライバシーポリシーのテキストを挿入してください。)

### 2. User Obligations (ユーザーの義務)
Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. 
(ここに後ほど本番の利用規約やプライバシーポリシーのテキストを挿入してください。)

### 3. Privacy Policy (プライバシーポリシー)
Donec sed odio dui. Nullam quis risus eget urna mollis ornare vel eu leo. 
(ここに後ほど本番の利用規約やプライバシーポリシーのテキストを挿入してください。)

### 4. Limitation of Liability (免責事項)
Cras justo odio, dapibus ac facilisis in, egestas eget quam. 
(ここに後ほど本番の利用規約やプライバシーポリシーのテキストを挿入してください。)

### 5. Changes to Terms (規約の変更)
Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. 
(ここに後ほど本番の利用規約やプライバシーポリシーのテキストを挿入してください。)
"""

st.markdown(f'<div style="height: 400px; overflow-y: scroll; padding: 10px; border: 1px solid #ddd; border-radius: 5px;">{text}</div>', unsafe_allow_html=True)

st.markdown("---")
st.info("Please contact support if you have any questions regarding these terms.")
