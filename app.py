import streamlit as st
import pandas as pd
import plotly.express as px

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

# YOTPO-INSPIRED CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
html, body, [class*="css"] {font-family: 'Poppins', sans-serif;}
.main {
    background: linear-gradient(135deg, #ffffff 0%, #f8fafc 50%, #f1f5f9 100%);
    color: #1e293b;
    padding: 2rem;
}
.stApp {background: transparent !important;}

/* Yotpo Blue-Gold Cards */
.yotpo-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 2rem;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08), 0 1px 3px rgba(0,0,0,0.1);
    margin-bottom: 1.5rem;
}
.stSelectbox > div > div > div { 
    background: white !important;
    border: 2px solid #3b82f6 !important; 
    border-radius: 12px !important;
    box-shadow: 0 4px 12px rgba(59,130,246,0.15) !important;
}
.stSelectbox [data-baseweb="select"] {color: #1e293b !important}

/* Live preview - Yotpo style */
.yotpo-preview {
    background: linear-gradient(90deg, #eff6ff, #dbeafe);
    border-left: 5px solid #3b82f6; 
    padding: 1.5rem; 
    border-radius: 12px;
    color: #1e293b;
    font-weight: 500;
    box-shadow: 0 4px 12px rgba(59,130,246,0.1);
}

/* Yotpo Blue buttons */
.stButton > button {
    background: linear-gradient(135deg, #3b82f6, #1d4ed8) !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    box-shadow: 0 4px 12px rgba(59,130,246,0.3) !important;
}

/* SerpAPI metric */
.metric-modern {
    background: linear-gradient(135deg, #eff6ff, #dbeafe);
    border: 1px solid #93c5fd;
    border-radius: 12px;
    padding: 1.5rem;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Review AI", page_icon="⭐", layout="wide")

# YOTPO HEADER
st.markdown("""
<div style='text-align: center; margin-bottom: 3rem;'>
    <h1 style='font-family: Poppins, sans-serif; font-size: 3rem; font-weight: 700; 
                background: linear-gradient(135deg, #3b82f6, #1d4ed8); 
                -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
                margin: 0;'>Review AI Pro</h1>
    <p style='color: #64748b; font-size: 1.2rem; font-weight: 500;'>10x Faster Review Responses | Enterprise Ready</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([3, 2, 1.5])

with col3:
    st.markdown('<div class="yotpo-card">', unsafe_allow_html=True)
    st.markdown("### 🔄 SerpAPI Dashboard")
    st.markdown("""
    <div class="metric-modern">
    <h3 style='color: #1e293b; margin: 0;'>Queries Used</h3>
    <h2 style='font-size: 2rem; color: #3b82f6; margin: 0.5rem 0;'>123/500</h2>
    </div>
    """, unsafe_allow_html=True)
    st.progress(0.25)
    st.markdown('</div>', unsafe_allow_html=True)

with col1:
    st.markdown('<div class="yotpo-card">', unsafe_allow_html=True)
    reviews_df = pd.DataFrame({
        'reviewer': ['John D.', 'Sarah K.', 'Mike L.'],
        'rating': [5, 1, 4],
        'text': ['Great service!', 'Too slow, disappointed.', 'Good but pricey.'],
        'date': pd.to_datetime(['2026-02-10', '2026-02-12', '2026-02-13'])
    })
    
    st.markdown("### 🆕 Recent Reviews")
    st.dataframe(reviews_df, use_container_width=True, hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="yotpo-card">', unsafe_allow_html=True)
    st.markdown("### 🎙️ Brand Voice")
    
    personality = st.selectbox("Select Voice", list(personalities.keys()))
    preview_text = personalities[personality] if personality != "Custom Brand" else "Hi from Your Brand! Thanks for the love! 💯"
    
    st.markdown(f"""
    <div class="yotpo-preview">
    <strong>→ Live Preview:</strong> {preview_text}
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("✨ Generate Reply", help="AI-powered brand response"):
        st.success("✅ Reply generated!")
    st.markdown('</div>', unsafe_allow_html=True)

# Smart review expanders
st.markdown('<div class="yotpo-card">', unsafe_allow_html=True)
st.markdown("### 📝 Review Responses")
for idx, row in reviews_df.iterrows():
    with st.expander(f"{'⭐' * int(row['rating'])} {row['reviewer']}: {row['text'][:50]}..."):
        if row['rating'] >= 4:
            reply = f"{personalities[personality]} We love making {row['reviewer']} smile! ✨"
        elif row['rating'] == 3:
            reply = f"{personalities[personality]} Thanks for the honest feedback, {row['reviewer']} - let's make it 5⭐ next time!"
        else:
            reply = f"{personalities[personality]} We're so sorry {row['reviewer']} - DM us to make this right immediately! 🙏"
        
        st.markdown(f"**🤖 AI Reply:** {reply}")
        if st.button("✅ Post Reply", key=f"post_{idx}"):
            st.success(f"Posted to {row['reviewer']}! 🎉")
st.markdown('</div>', unsafe_allow_html=True)

# Yotpo-style graph
fig = px.bar(reviews_df, x='rating', title="📊 Sentiment Trends", 
             color='rating', color_continuous_scale=['#93c5fd', '#3b82f6', '#1d4ed8'])
fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='white',
    font_color='#1e293b',
    font_family='Poppins',
    title_font_size=18,
    bargap=0.3
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.markdown("*Powered by SerpAPI | 10 Brand Voices | Enterprise Scale*")
