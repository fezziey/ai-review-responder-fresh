import streamlit as st
import pandas as pd
import plotly.express as px

col1, col2, col3 = st.columns([3, 1, 2])
with col3:
    st.markdown("### 🔄 SerpAPI") 
    st.metric("123/500", "25%")
    st.progress(0.25)
    st.markdown("### 🎙️ Tone")
    tone = st.selectbox("Reply Style", ["Friendly", "Professional", "Casual"])

st.title("🚀 AI Review Responder – Auto-Reply & Boost Ratings")

reviews_df = pd.DataFrame({
    'reviewer': ['John D.', 'Sarah K.', 'Mike L.'],
    'rating': [5, 1, 4],
    'text': ['Great service!', 'Too slow, disappointed.', 'Good but pricey.'],
    'date': pd.to_datetime(['2026-02-10', '2026-02-12', '2026-02-13'])
})

st.subheader("🆕 New Reviews")
st.dataframe(reviews_df)

for idx, row in reviews_df.iterrows():
    with st.expander(f"{row['rating']}⭐ {row['reviewer']}: {row['text'][:50]}..."):
        st.write(f"**🤖 AI Reply ({tone}):** Thanks for your feedback!")
        if st.button("✅ Post Reply", key=f"post_{idx}"):
            st.success("Posted! 🎉")

fig = px.bar(reviews_df, x='rating', title="Sentiment Trends")
st.plotly_chart(fig)

st.subheader("⚡ Get Started")
st.info("👆 Try tone toggle + Post Reply. **Upgrade** for live Google/Yelp.")
