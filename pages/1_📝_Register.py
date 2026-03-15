import streamlit as st
import sys
import os

# Add parent directory to path to import db module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import db

st.set_page_config(page_title="Register - Verba", page_icon="📝", layout="centered")

# Initialize database
db.init_db()

st.title("📝 アカウント登録 (Register)")

st.success("""
🎉 **Payment Successful! Welcome to the Verba Founders!**  
🎉 **決済完了！Verbaファウンダーへのご参加ありがとうございます！**
""")

st.markdown("""
Thank you for your support, Aki and the team are thrilled to have you! Please follow the 3 steps below to claim your Founder's Pack rewards:  
サポートありがとうございます！以下の3つのステップで、ファウンダー特典を受け取ってください。

---

### 1️⃣ Join the Exclusive Discord Community (限定コミュニティに参加)
Join our Discord server to get early access to the Beta app and chat with the team!  
まずは以下のリンクから、ファウンダー限定のDiscordサーバーに参加してください！ベータ版のテストやフィードバックはここで行います。  
👉 [💡 **Discordコミュニティに参加する (Join Discord)**](#) *(URLを後でここに入力してください)*

### 2️⃣ Download Aki's Original PDFs (オリジナルPDF教材をダウンロード)
Download your practical JLPT mock exams and materials here.  
Akiオリジナルの実践的なJLPT教材（PDF）はこちらからダウンロードできます。  
👉 [💡 **PDF教材をダウンロードする (Download PDFs)**](#) *(URLを後でここに入力してください)*

### 3️⃣ Claim Your 10,000 VRB Tokens (トークンの受け取りについて)
To receive your 10,000 VRB tokens, please join the Discord server and send a Direct Message (DM) to "Aki" with your MetaMask wallet address.  
10,000 VRBトークンを受け取るために、Discordに参加後、ファウンダーの「Aki」宛にあなたのMetaMaskウォレットアドレスをDM（ダイレクトメッセージ）で送信してください。

---

🌟 **Your Lifetime Premium Access is now active. Let's revolutionize Japanese learning together!**  
🌟 **あなたの一生涯プレミアムアクセス権は有効化されました。一緒に日本語学習の未来を作りましょう！**
""")

st.write("---")
st.subheader("ユーザー登録 (User Registration)")
st.write("アプリを利用するために、以下からアカウントを作成してください。(Please create an account below to use the app.)")

with st.form("register_form"):
    username = st.text_input("ユーザー名 (Username)*")
    email = st.text_input("メールアドレス (Email)*")
    password = st.text_input("パスワード (Password)*", type="password")
    
    # Detailed list of nationalities (in Japanese and English)
    nationalities = [
        "", # Default empty
        "日本 (Japan)",
        "アメリカ (United States)",
        "中国 (China)",
        "韓国 (South Korea)",
        "台湾 (Taiwan)",
        "ベトナム (Vietnam)",
        "フィリピン (Philippines)",
        "インドネシア (Indonesia)",
        "タイ (Thailand)",
        "インド (India)",
        "ブラジル (Brazil)",
        "イギリス (United Kingdom)",
        "フランス (France)",
        "ドイツ (Germany)",
        "その他 (Other)"
    ]
    
    nationality = st.selectbox("国籍 (Nationality)*", nationalities)
    
    submit_button = st.form_submit_button("登録 (Register)", use_container_width=True)
    
    if submit_button:
        if not username:
            st.warning("⚠️ ユーザー名を入力してください。(Please enter your username.)")
        elif not nationality:
            st.warning("⚠️ 国籍を選択してください。(Please select your nationality.)")
        elif email and password:
            success, message = db.create_user(email, username, password, nationality)
            if success:
                st.success(f"✅ {message} (Registration successful!)")
                st.balloons()
            else:
                st.error(f"⚠️ {message}")
        else:
            st.warning("⚠️ メールアドレスとパスワードを入力してください。(Please enter your email and password.)")

st.divider()
st.caption("※ご登録いただいた情報は、本サービスの提供以外の目的には使用いたしません。")
