import streamlit as st
import pandas as pd
import plotly.express as px

# ✅ STEP 1: 10 ENTERPRISE PERSONALITIES
personalities = {
    "Friendly Neighbor": "OMG thank you SO much! 😍 We're blushing over here! DM us for 10% off! ✨",
    "Corporate Professional": "Thank you for your feedback. We appreciate your business and value your opinion.",
    "Gen Z Casual": "Yo thanks for the review! 🙌 Hit us up for a discount code next time! 🔥",
    "Luxury Boutique": "Thank you for sharing your experience. We're honored to serve you.",
    "Tech Startup": "Love the feedback! 🚀 Let's chat about making your next experience even better.",
    "TikTok Viral": "CLOCK IT! 👀 This review SLAPS harder than a 6-7! Puuuuurrrrr 😻💯 DM for discount code! #SmallBiz 🔥",
    "Country Western": "YEEHAW partner! 🤠 This review's got us two-steppin'! Saddle up for 20% off! 💃🕺",
    "90s R&B": "Ooooh chile! 😩 You just made my heart sing like Mary J! Slide in DMs for BOGO! 🎤✨",
    "Grandma Wisdom": "Bless your heart darlin'! 🥰 Come back soon - fresh cookies + 15% off! 🍪💕",
    "Custom Brand": "Custom voice loading..."
}

# ✅ STEP 2: LUXURY CSS + GOLD FONTS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Inter:wght@300;400;500&display=swap');
html, body, [class*="css"]  {
    font-family: 'Inter', sans-serif;
}
.main {
    background: linear-gradient(135deg, #0a0a0e 0%, #1a0d24 50%, #000000 100%);
    color: #f5e8c7;
    padding: 2rem;
}
.stApp {background: transparent !important;}
/* Gold selectors */
.stSelectbox > div > div > div { 
    background: linear-gradient(145deg, #1a1a1a, #2d2d2d) !important;
    border: 2px solid #b89778 !important; 
    border-radius: 12px !important;
    box-shadow: 0 8px 32px rgba(184,151,120,0.3) !important;
}
.stSelectbox [data-baseweb="select"] {color: #f5e8c7 !important}
/* Velvet preview */
.luxury-preview {
    background: linear-gradient(90deg, #1a1a1a, #2d1b14);
    border-left: 6px solid #b89778; 
    padding: 1.5rem; 
    border-radius: 16px;
    color: #f5e8c7;
    font-size: 1.1rem;
    font-weight: 500;
    box-shadow: 0 12px 40px rgba(184,151,120,0.2);
    backdrop-filter: blur(10px);
    margin: 1rem 0;
}
/* Diamond buttons */
.stButton > button {
    background: linear-gradient(45deg, #b89778, #d4af37) !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    font-family: 'Inter', sans-serif !important;
    box-shadow: 0 8px 25px rgba(184,151,120,0.4) !important;
    border: none !important;
}
/* Metric cards */
.metric-card {
    background: linear-gradient(145deg, #1a1a1a, #2d2d2d);
    border: 1px solid #b89778;
    border-radius: 12px;
    padding: 1.5rem;
    margin: 0.5rem 0;
    box-shadow: 0 8px 32px rgba(184,151,120,0.2);
}
/* Gold graph */
.css-1gyo7hw {border: 1px solid #b89778 !important}
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Enterprise Review AI", page_icon="💎", layout="wide")

# ✅ STEP 4: EXECUTIVE HEADER
st.markdown("""
<div style='text-align: center; margin-bottom: 3rem;'>
    <h1 style='font-family: Playfair Display, serif; font-size: 3rem; 
                background: linear-gradient(45deg, #b89778, #d4af37); 
                -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
                font-weight: 700; margin: 0;'>Enterprise Review AI</h1>
    <p style='color: #b89778; font-size: 1.2rem; font-weight: 500;'>Intelligent Brand Voice Personalization</p>
</div>
""", unsafe_allow_html=True)

# ✅ STEP 5: MAIN LAYOUT
col1, col2, col3 = st.columns([3, 2, 2])

with col3:
    st.markdown("### 🔄 **SerpAPI Intelligence**")
    st.markdown("""
    <div class="metric-card">
    <h3 style='color: #b89778; margin: 0;'>Queries / Limit</h3>
    <h2 style='font-family: Playfair Display, serif; color: #f5e8c7; margin: 0.5rem 0;'>123/500</h2>
    </div>
    """, unsafe_allow_html=True)
    st.progress(0.25)

with col1:
    # Reviews data
    reviews_df = pd.DataFrame({
        'reviewer': ['John D.', 'Sarah K.', 'Mike L.'],
        'rating': [5, 1, 4],
        'text': ['Great service!', 'Too slow, disappointed.', 'Good but pricey.'],
        'date': pd.to_datetime(['2026-02-10', '2026-02-12', '2026-02-13'])
    })
    
    st.markdown("### 🆕 **New Reviews**")
    st.dataframe(reviews_df, use_container_width=True)

with col2:
    st.markdown("### 🎩 **Enterprise Brand Voice**")
    
    # 10 Personality selector
    personality = st.selectbox("🎭 **Select Voice**", list(personalities.keys()))
    
    # LIVE PREVIEW
    preview_text = personalities[personality] if personality != "Custom Brand" else "Hi from Your Brand! Thanks for the love! 💯"
    st.markdown(f"""
    <div class="luxury-preview">
    ✦ **Executive Preview:** {preview_text}
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("✨ Generate Enterprise Reply", help="AI-powered response"):
        st.success("✅ Enterprise reply generated!")

# Review expanders
for idx, row in reviews_df.iterrows():
    with st.expander(f"{'⭐' * int(row['rating'])} {row['reviewer']}: {row['text'][:50]}..."):
        st.markdown(f"**🤖 AI Reply ({personality}):** {preview_text}")
        if st.button("✅ Post Reply", key=f"post_{idx}"):
            st.success("Posted successfully! 🎉")

# GOLD GRAPH
fig = px.bar(reviews_df, x='rating', title="Sentiment Distribution", 
             color='rating', color_continuous_scale=['#b89778', '#d4af37'])
fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font_color='#f5e8c7',
    title_font_family='Playfair Display'
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.markdown("### ⚡ **Enterprise Ready**")
st.info("💎 10+ brand voices | Live SerpAPI dashboard | Millionaire aesthetic")
