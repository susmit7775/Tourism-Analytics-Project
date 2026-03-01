import streamlit as st
import pandas as pd
import joblib
import os

# --- PAGE SETUP ---
st.set_page_config(page_title="Travel AI", page_icon="✈️", layout="centered")

# --- LOAD BRAINS ---
@st.cache_resource
def load_models():
    path = 'models'
    if not os.path.exists(path): return None
    try:
        return (
            joblib.load(f'{path}/rating_model.pkl'),
            joblib.load(f'{path}/mode_classifier.pkl'),
            joblib.load(f'{path}/rec_matrix.pkl'),
            joblib.load(f'{path}/le_continent.pkl'),
            joblib.load(f'{path}/le_category.pkl'),
            joblib.load(f'{path}/le_mode.pkl')
        )
    except: return None

models = load_models()
if not models:
    st.error("⚠️ Models missing. Please run the training notebook first.")
    st.stop()

reg, clf, rec, le_cont, le_cat, le_mode = models

# --- HEADER ---
st.image("https://cdn-icons-png.flaticon.com/512/826/826070.png", width=80)
st.title("Smart Travel Assistant")
st.write("I use AI to help you plan the perfect trip.")
st.divider()

# --- SIDEBAR: WHO ARE YOU? ---
st.sidebar.header("👤 Traveler Profile")
user_from = st.sidebar.selectbox("I am from:", le_cont.classes_)
avg_rating = st.sidebar.slider("I usually rate places:", 1, 5, 4)

# --- THE 3 FEATURES ---
t1, t2, t3 = st.tabs(["🔮 Will I like it?", "💼 Trip Type?", "📍 Where to go?"])

# 1. RATING PREDICTION
with t1:
    st.subheader("Check a place before you go")
    c1, c2 = st.columns(2)
    place_type = c1.selectbox("Place Category", le_cat.classes_)
    visit_type = c2.selectbox("How are you visiting?", le_mode.classes_)
    
    if st.button("Analyze Match"):
        # Encode
        x = [[
            le_cont.transform([user_from])[0],
            le_cat.transform([place_type])[0],
            le_mode.transform([visit_type])[0]
        ]]
        score = reg.predict(x)[0]
        
        st.write("---")
        if score >= 4.0:
            st.success(f"✅ Great Match! Predicted Rating: {score:.1f}/5")
        elif score >= 3.0:
            st.info(f"⚖️ It's Okay. Predicted Rating: {score:.1f}/5")
        else:
            st.error(f"❌ Skip it. Predicted Rating: {score:.1f}/5")

# 2. CLASSIFICATION
with t2:
    st.subheader("What kind of trip is this?")
    st.write("AI detects if this is Business, Family, or Solo.")
    
    if st.button("Detect Trip Type"):
        x = [[
            le_cont.transform([user_from])[0],
            le_cat.transform([place_type])[0], # Taken from Tab 1
            avg_rating
        ]]
        result = clf.predict(x)[0]
        st.success(f"This looks like a **{result}** trip.")

# 3. RECOMMENDATION
with t3:
    st.subheader("Discover New Places")
    uid = st.number_input("Enter your User ID", value=14)
    
    if st.button("Show Recommendations"):
        if uid in rec.index:
            user_likes = rec.loc[uid]
            similar = rec.corrwith(user_likes).sort_values(ascending=False).head(4)
            
            st.write("People like you also loved:")
            for place in similar.index[1:]:
                st.info(f"📍 {place}")
        else:
            st.warning("New user? Try visiting the Eiffel Tower first!")