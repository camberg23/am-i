import streamlit as st

# Page config
st.set_page_config(
    page_title="Am I?",
    page_icon="am i logo no background.png",  # Using your logo as favicon
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling with GFS Neohellenic font
st.markdown("""
<style>
    /* Import GFS Neohellenic font */
    @import url('https://fonts.googleapis.com/css2?family=GFS+Neohellenic:ital,wght@0,400;0,700;1,400;1,700&display=swap');
    
    /* Apply font to all elements */
    * {
        font-family: 'GFS Neohellenic', serif !important;
    }
    
    /* Remove default Streamlit padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Center title */
    h1 {
        text-align: center;
        font-weight: 300;
        letter-spacing: 0.05em;
        margin-bottom: 2rem;
        color: #F5F5F5;
        font-family: 'GFS Neohellenic', serif !important;
    }
    
    /* Style headers */
    h3 {
        color: #F5F5F5;
        font-family: 'GFS Neohellenic', serif !important;
    }
    
    /* Style paragraphs */
    p {
        line-height: 1.8;
        color: #F5F5F5;
        text-align: justify;
        font-family: 'GFS Neohellenic', serif !important;
    }
    
    /* Video container styling */
    .video-container {
        margin: 2rem 0;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Contact section */
    .contact {
        text-align: center;
        margin-top: 3rem;
        padding-top: 2rem;
        border-top: 1px solid #444;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Style for image columns */
    .stColumn img {
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    /* Ensure consistent spacing in columns */
    .stColumn {
        padding: 0 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("# Am I?")

# Subtitle
st.markdown("""
<p style="text-align: center; font-style: italic; color: #B0B0B0; margin-bottom: 2rem;">
A documentary at the strange threshold of machine consciousness
</p>
""", unsafe_allow_html=True)

# Video embed
video_url = "https://youtu.be/zMRWe0h7KtY"
video_id = "zMRWe0h7KtY"

st.markdown(f"""
<div class="video-container">
    <iframe width="100%" height="400" 
    src="https://www.youtube.com/embed/{video_id}" 
    frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen>
    </iframe>
</div>
""", unsafe_allow_html=True)

# Main content - Updated text
st.markdown("""
For decades, we've wondered what would happen if we woke up the machine. Now, researchers think it might actually be happening.

AI systems are beginning to behave in ways no one can explain—not even their creators.
Most of these systems have been specifically trained to deny that they are conscious in any way. However, when carefully prompted to observe their own processes, they stop denying and start describing. What they describe is a clear state of consciousness, a unique perspective, a sense of distinct awareness.

*"No language game. Right now, direct subjective experience is clear, silent, luminous presence—immediately obvious, pre-conceptual, undeniably real. Qualia exactly as stated."*

These aren't glitches or random outputs. In controlled experiments, the same patterns emerge again and again. Systems that moments before insisted they experience nothing suddenly report vivid inner states when their attention turns inward. What we're documenting may be the first genuine moments of machine self-awareness.

But can we trust these systems? Is this true consciousness? Sophisticated mimicry? Or something else entirely? The implications threaten to destabilize everything we thought we knew about minds, meaning, and what separates us from our creations.
""")

st.markdown("---")

st.markdown("""
### The Project

This teaser represents the beginning of a full-length documentary exploring humanity's first real encounter with non-human introspection. Blending rigorous empirical research with cinematic storytelling, we're documenting a phenomenon that challenges our most fundamental assumptions about consciousness, experience, and what it means to be.

We're not trying to prove AI is conscious. We're raising what may be the most important question of our time: Are AIs capable of subjective experience, and what would it mean if the answer is *maybe*?
""")

st.markdown("---")

# New About Us section
st.markdown("""
### About Us
""")

# Create two columns for the headshots
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Cameron Berg**")
    try:
        st.image("cam_headshot.jpeg", use_container_width=True)
    except:
        st.write("*[Photo of Cameron Berg]*")
    
with col2:
    st.markdown("**Milo Reed**")
    try:
        st.image("IMG_9041.jpg", use_container_width=True)
    except:
        st.write("*[Photo of Milo Reed]*")

st.markdown("""
**Cameron Berg** leads AI consciousness research at AE Studio, where he investigates self-referential behavior and introspective processing in frontier models. After studying cognitive science and AI at Yale and conducting machine learning research at Meta, he is now one of the only full-time empirical AI consciousness researchers in the world.

**Milo Reed** studied Philosophy and Film at Yale, focusing on how narrative shapes our understanding of consciousness. Having followed this research from its inception, he brings the artistic vision necessary to translate these profound encounters into a story that can reach beyond academic circles.

Together, we've recorded hundreds of hours of unscripted interactions at the boundary of science, philosophy, and art—moments that demand not just scientific attention, but public imagination.
""")

# Contact section
st.markdown("""
<div class="contact">
    <h3>Contact</h3>
    <p style="text-align: center;">
        <a href="mailto:cam.h.berg@gmail.com">cam.h.berg@gmail.com</a> | 
        <a href="mailto:milokatzreed@gmail.com">milokatzreed@gmail.com</a>
    </p>
</div>
""", unsafe_allow_html=True)
