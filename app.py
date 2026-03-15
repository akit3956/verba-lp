import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Verba - The Next Gen Language App",
    page_icon="🇯🇵",
    layout="wide"
)

# Title Area
st.title("🇯🇵 Japanese Teacher x Web3 x AI")
st.header("Next Gen Language App: 'Learn to Earn'")

# Notification Box
st.info("💡 We are currently accepting pre-orders for the Founder's Pack to raise development funds.")

# Introduction
st.subheader("👋 Hi, I'm Aki. I'm a former Japanese teacher.")
st.write("""
I have seen many students give up on their dream of learning Japanese because they 'didn't have money' or 'lost motivation'.

So, I decided to build a solution using the latest AI and blockchain technology.
**An app where the more you study, the more rewards (tokens) you earn.**

**Project Name: 'Verba (VRB)'**

Learning words (Verba) helps your life. Let's build this world together.
""")

st.divider()

# Problem
st.subheader("😤 Why do people fail at learning Japanese?")
st.markdown("##### 'No Money', 'No Motivation', 'Boring Textbooks'")
st.write("Traditional learning methods are expensive and quickly become boring. But Verba is different.")

# Solution: Verba (Learn-to-Earn)
st.subheader("💡 Solution: Verba (Learn-to-Earn)")
st.info("The more you study, the more cryptocurrency ($VRB) you earn.")
st.write("Verba uses blockchain technology to record your learning history. Turn your efforts into assets.")

# Tokenomics
st.subheader("💎 Tokenomics (Verba Token)")
st.metric(label="Token Name", value="$VRB")

st.markdown("""
- **Earn**: Answer quizzes correctly, login daily, refer friends.
- **Burn**: Special AI characters, premium materials, JLPT mock exams.
""")

st.divider()

# Roadmap Section
st.subheader("🗺️ Roadmap: The Future We Build")
st.write("Your support ($30) will be the driving force of this journey.")

# Roadmap Columns
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("### 🚩 Q1 2026")
    st.caption("Current Stage")
    st.success("✅ Project Start")
    st.success("✅ Founder Sale")

with col2:
    st.markdown("### 🛠️ Q2 2026")
    st.caption("Development")
    st.info("📱 Beta App Release")
    st.write("Release prototype app for founders only")

with col3:
    st.markdown("### 🌑 Q3 2026")
    st.caption("Token")
    st.info("💰 VRB Airdrop")
    st.write("Distribute 10,000 VRB tokens to early supporters")

with col4:
    st.markdown("### 🚀 Q4 2026")
    st.caption("Global")
    st.warning("🌏 Official Release")
    st.write("Public listing on DEX (Decentralized Exchange).")

st.divider()

# Founder's Pack (CTA)
st.header("⚡ Join Now: Founder's Pack")
st.warning("⚠️ This offer is limited to the first 100 people. The value could triple or more upon listing.")

col_cta_left, col_cta_right = st.columns([1, 1])

with col_cta_left:
    # Spacer to move image down
    st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)
    
    # Nested columns to move image right
    _, img_col = st.columns([0.15, 0.85]) 
    with img_col:
        st.image("vrb_coin.png", width=330)

with col_cta_right:
    st.subheader("🚀 Founder's Pack (Early Access)")
    st.write("We need your support to continue development. Early supporters will receive the biggest rewards.")

    st.markdown("##### 【Pack Contents】")
    st.markdown("""
    - ✅ **Lifetime Premium Access** (No monthly fees forever)
    - ✅ **10,000 VRB Tokens** (Airdropped in future)
    - ✅ **Original PDF Textbooks by Aki** (Practical Japanese materials)
    - ✅ **Access to Dev Community** (Discord, etc.)
    - ❤️ **Deepest Gratitude from Aki**
    """)
    
    # Official PayPal Live HTML Form Button
    st.markdown("""
    <div style="text-align: center; margin-top: 20px; margin-bottom: 10px;">
      <style>.pp-B6NDGVHL4H7B2{text-align:center;border:none;border-radius:0.25rem;min-width:11.625rem;padding:0 2rem;height:2.625rem;font-weight:bold;background-color:#FFD140;color:#000000;font-family:"Helvetica Neue",Arial,sans-serif;font-size:1rem;line-height:1.25rem;cursor:pointer;}</style>
      <form action="https://www.paypal.com/ncp/payment/B6NDGVHL4H7B2" method="post" target="_blank" style="display:inline-grid;justify-items:center;align-content:start;gap:0.5rem;">
        <input class="pp-B6NDGVHL4H7B2" type="submit" value="👉 Get Founder's Pack" />
        <input type="hidden" name="return" value="http://localhost:8503/Register" />
        <img src=https://www.paypalobjects.com/images/Debit_Credit_APM.svg alt="cards" />
        <section style="font-size: 0.75rem;"> Powered by <img src="https://www.paypalobjects.com/paypal-ui/logos/svg/paypal-wordmark-color.svg" alt="paypal" style="height:0.875rem;vertical-align:middle;"/></section>
      </form>
    </div>
    """, unsafe_allow_html=True)
        
    st.caption("*決済完了後に「販売サイトへ戻る」を押すと会員登録画面に移動します")
    st.caption("*Recipient: Akis Create (@akis3956)")

st.divider()

# FAQ
st.subheader("❓ FAQ")
with st.expander("Q: Can I really earn?"):
    st.write("A: Yes. You can earn tokens while learning. The earned tokens are planned to be tradable on exchanges in the future.")

with st.expander("Q: Who is Japanese Teacher Aki?"):
    st.write("A: I am a professional Japanese teacher. I started this project after seeing many students give up learning for financial reasons.")
