import streamlit as st

# ページ設定
st.set_page_config(
    page_title="Verba - 次世代の語学アプリ",
    page_icon="🇯🇵",
    layout="wide"
)

# タイトルエリア
st.title("🇯🇵 日本語教師 × Web3 × AI")
st.header("次世代の語学アプリ：「学んで稼ぐ」")

# お知らせボックス
st.info("💡 現在、開発資金を集めるためにファウンダーズパックの事前予約を受け付けています。")

# 自己紹介とプロジェクト概要
st.subheader("👋 こんにちは、アキです。元日本語教師です。")
st.write("""
「お金がない」や「やる気がなくなった」という理由で、日本語を学ぶ夢をあきらめてしまう学生を数多く見てきました。

そこで、最新のAIとブロックチェーン技術を活用したソリューションを構築することにしました。
**勉強すればするほど報酬（トークン）がもらえるアプリです。**

**プロジェクト名：「Verba（VRB）」**

言葉（Verba）を学ぶことはあなたの人生に役立ちます。一緒にこの世界を築きましょう。
""")

st.divider()

# 問題提起
st.subheader("😤 なぜ日本語学習で挫折するのか？")
st.markdown("##### 「お金がない」「やる気が出ない」「教科書がつまらない」")
st.write("従来の学習方法は高額で、すぐに退屈になってしまいます。しかしVerbaは違います。")

# 解決策：Verba (Learn-to-Earn)
st.subheader("💡 解決策：Verba (Learn-to-Earn)")
st.info("勉強すればするほど、仮想通貨（$VRB）が貯まる。")
st.write("Verbaはブロックチェーン技術を活用し、学習履歴を記録。あなたの努力を資産に変えます。")

# トークノミクス
st.subheader("💎 トークノミクス (Verba Token)")
st.metric(label="トークン名", value="$VRB")

st.markdown("""
- **稼ぐ (Earn)**: クイズに正解する、毎日ログインする、友達を紹介する。
- **使う (Burn)**: 特別なAIキャラクター、プレミアム教材、JLPT模擬試験。
""")

st.divider()

# ロードマップセクション
st.subheader("🗺️ ロードマップ: 私たちが築く未来")
st.write("あなたのサポート（30ドル）がこの旅の原動力になります。")

# 4つのカラムでロードマップを表示
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("### 🚩 2026年第1四半期")
    st.caption("現在の段階")
    st.success("✅ プロジェクト開始")
    st.success("✅ 創業者セール")

with col2:
    st.markdown("### 🛠️ 2026年第2四半期")
    st.caption("発達")
    st.info("📱 ベータ版アプリのリリース")
    st.write("創設者のみを対象にプロトタイプアプリをリリース")

with col3:
    st.markdown("### 🌑 2026年第3四半期")
    st.caption("トークン")
    st.info("💰 VRB エアドロップ")
    st.write("早期支援者に 10,000 VRB トークンを配布")

with col4:
    st.markdown("### 🚀 2026年第4四半期")
    st.caption("グローバル")
    st.warning("🌏 公式リリース")
    st.write("DEX（分散型取引所）に公開・上場。")

st.divider()

# ファウンダーズパック (CTA)
st.header("⚡ 今すぐ参加：ファウンダーズパック")
st.warning("⚠️ このオファーは先着100名様限定です。上場時に価値が3倍以上になる可能性があります。")

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
    
    st.write("Special Price")
    st.markdown("## $30.00 USD <span style='color:green; font-size:0.6em; background-color:#e6ffe6; padding:2px 5px; border-radius:5px;'>↑ Limited Time Offer</span>", unsafe_allow_html=True)
    
    # PayPal Link: Inferred from image "@akis3956" -> https://paypal.me/akis3956/30USD
    paypal_url = "https://paypal.me/akis3956/30USD" 
    
    # Custom PayPal Button (Yellow)
    st.markdown(f"""
    <a href="{paypal_url}" target="_blank" style="text-decoration: none;">
        <div style="
            background-color: #FFC439;
            color: #000000;
            padding: 15px 20px;
            border-radius: 50px;
            text-align: center;
            font-weight: bold;
            font-size: 18px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.2s;
            margin-top: 10px;
            margin-bottom: 5px;
        ">
            👉 Get Founder's Pack ($30)
        </div>
    </a>
    """, unsafe_allow_html=True)
    st.caption("※PayPalによる安全な支払い")
    st.caption("※支払先: Akis Create (@akis3956)")

st.divider()

# FAQ
st.subheader("❓ よくある質問")
with st.expander("Q: 本当に稼げるのですか？"):
    st.write("A: はい。学びながらトークンを獲得できます。獲得したトークンは将来的に取引所で売買可能になる予定です。")

with st.expander("Q: 日本語教師アキとは誰ですか？"):
    st.write("A: 私はプロの日本語教師です。多くの学生が金銭的な理由で学習を諦めるのを見て、このプロジェクトを立ち上げました。")

