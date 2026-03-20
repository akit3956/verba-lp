import streamlit.components.v1 as components

import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Verba - The Next Gen Language App",
    page_icon="🇯🇵",
    layout="wide"
)

# ------------------------------

# Main Title Area
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

# Problem Section
st.subheader("😤 Why do people fail at learning Japanese?")
st.markdown("##### 'No Money', 'No Motivation', 'Boring Textbooks'")
st.write("Traditional learning methods are expensive and quickly become boring. But Verba is different.")

# Solution Section
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
    st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)
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
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.info("💡 Please review the Terms of Service and Privacy Policy before proceeding.")
    st.page_link("pages/2_📜_Terms_&_Privacy.py", label="Read the full Terms of Service and Privacy Policy", icon="📜")
    st.markdown("<br>", unsafe_allow_html=True)
    
    agree = st.checkbox("I agree to the Terms of Service and Privacy Policy")
    
    if not agree:
        st.warning("⚠️ 決済を進めるには、上記の利用規約とプライバシーポリシーに同意してください。 (Agreement is required to proceed.)")

    # Get PayPal Client ID from Secrets (defaults to 'test' for Sandbox testing)
    paypal_client_id = st.secrets.get("PAYPAL_CLIENT_ID", "test")
    
    # Inject JavaScript boolean based on the Streamlit checkbox
    js_agreed = "true" if agree else "false"
    
    # PayPal Smart Buttons JS SDK Component
    # We display the component regardless of the 'agree' state, 
    # but use PayPal's onClick function to enforce the agreement.
    components.html(
        f"""
        <div style="text-align: center; margin-top: 20px;">
            <!-- Load PayPal JS SDK with Client ID -->
            <script src="https://www.paypal.com/sdk/js?client-id={paypal_client_id}&currency=USD"></script>
            <div id="paypal-button-container"></div>
            <script>
              paypal.Buttons({{
                onClick: function(data, actions) {{
                  // Show an alert and prevent payment popup if they try to click without agreeing
                  if (!{js_agreed}) {{
                    alert("⚠️ 決済に進むには、「利用規約とプライバシーポリシーに同意します」のチェックボックスにチェックを入れてください。\\n\\nPlease check 'I agree to the Terms of Service and Privacy Policy' above first.");
                    return actions.reject();
                  }}
                  return actions.resolve();
                }},
                createOrder: function(data, actions) {{
                  return actions.order.create({{
                    purchase_units: [{{
                      amount: {{
                        value: '30.00'
                      }}
                    }}]
                  }});
                }},
                onApprove: function(data, actions) {{
                  return actions.order.capture().then(function(details) {{
                    console.log("Payment successful:", details);
                    
                    // Hide the PayPal buttons
                    document.getElementById('paypal-button-container').style.display = 'none';
                    
                    // Show success message and a manual redirect button (target="_blank" escapes iframe reliably)
                    const successDiv = document.createElement('div');
                    successDiv.innerHTML = `
                      <h3 style="color: #2e7d32; font-family: sans-serif; margin-bottom: 20px;">
                        ✅ 決済が完了しました！<br><span style="font-size: 0.8em; color: #555;">以下のボタンを押して特典を受け取ってください</span>
                      </h3>
                      <a href="Register?payment=success" target="_blank" 
                         style="display: inline-block; background-color: #FFD140; color: #000; 
                                padding: 15px 30px; text-decoration: none; font-weight: bold; 
                                border-radius: 8px; font-family: sans-serif; font-size: 16px;
                                box-shadow: 0 4px 6px rgba(0,0,0,0.1); transition: background-color 0.3s;">
                        次へ進む（登録画面へ） 👉<br><span style="font-size: 0.75em; font-weight: normal;">(新しいタブで開きます)</span>
                      </a>
                    `;
                    document.body.appendChild(successDiv);
                  }});
                }}
              }}).render('#paypal-button-container');
            </script>
        </div>
        """,
        height=250,
        scrolling=False
    )

    st.caption("*Recipient: Akis Create (@akis3956)")

st.divider()

# FAQ Section
st.subheader("❓ FAQ")
with st.expander("Q: Can I really earn?"):
    st.write("A: Yes. You can earn tokens while learning. The earned tokens are planned to be tradable on exchanges in the future.")

with st.expander("Q: Who is Japanese Teacher Aki?"):
    st.write("A: I am a professional Japanese teacher. I started this project after seeing many students give up learning for financial reasons.")
