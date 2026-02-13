import streamlit as st
from utils import analyze_resume

st.set_page_config(page_title="Resume Keyword Analyzer", layout="centered")

st.title("📄 Resume Keyword Analyzer")
st.write("Compare your resume with a job description and see your match score.")

resume_text = st.text_area("Paste your Resume here", height=200)
jd_text = st.text_area("Paste Job Description here", height=200)

if "results" not in st.session_state:
    st.session_state.results = None

if st.button("Analyze"):
    if resume_text.strip() and jd_text.strip():
        st.session_state.results = analyze_resume(resume_text, jd_text)
    else:
        st.warning("Please fill both fields.")

if st.session_state.results:
    results = st.session_state.results

    st.subheader("Match Score")
    score = results["match_score"]
    st.progress(int(score))

    if score > 75:
        st.success(f"{score}% Match — Strong Fit ✅")
    elif score > 50:
        st.warning(f"{score}% Match — Moderate Fit ⚠️")
    else:
        st.error(f"{score}% Match — Needs Improvement ❌")

    st.subheader("Top Matching Keywords")
    for word in results["common_keywords"]:
        st.markdown(f"- 🔹 {word}")

    st.subheader("Missing Keywords")

    if results["missing_keywords"]:
        for word in results["missing_keywords"]:
            st.markdown(f"- ❌ {word}")
    else:
        st.success("None! Your resume covers all the keywords in the job description.")

