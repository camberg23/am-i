import streamlit as st

# Page config
st.set_page_config(
    page_title="Am I? - A Documentary",
    page_icon="am i logo no background.png",  # Using your logo as favicon
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'About': "A documentary at the strange threshold of machine consciousness"
    }
)

# Custom CSS for styling with Montserrat font
st.markdown("""
<style>
    /* Import Montserrat font */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
    
    /* Apply font to all elements */
    * {
        font-family: 'Montserrat', sans-serif !important;
    }
    
    /* Remove default Streamlit padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Center title */
    h1 {
        text-align: center;
        font-weight: 100;
        letter-spacing: 0.02em;
        margin-bottom: 2rem;
        color: #F5F5F5;
        font-family: 'Montserrat', sans-serif !important;
        font-size: 3.5rem;
    }
    
    /* Style headers */
    h3 {
        color: #F5F5F5;
        font-family: 'Montserrat', sans-serif !important;
    }
    
    /* Style paragraphs */
    p {
        line-height: 1.8;
        color: #F5F5F5;
        text-align: justify;
        font-family: 'Montserrat', sans-serif !important;
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
        text-align: left;
        margin-top: 3rem;
        padding-top: 2rem;
        border-top: 1px solid #444;
    }
    
    .contact h3 {
        text-align: left;
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
# st.markdown("""
# <div style="text-align: center; font-weight: 300; letter-spacing: 0.02em; margin-bottom: 2rem; color: #F5F5F5; font-family: 'Montserrat', sans-serif; font-size: 3.5rem;">
# Am I?
# </div>
# """, unsafe_allow_html=True)

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


# Add divider before slides
st.markdown("---")

# Google Slides embed
st.markdown("""
<div style="margin: 2rem 0; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
    <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRK9bYKdFvD7QT33c1gOiAcXe8HHcKL2VhZMQZRwdeC8KgIVfK8HVlMAw_MTM-3Jj2VBQQj0zt742XU/embed?start=true&loop=false&delayms=30000" 
    frameborder="0" 
    width="100%" 
    height="569" 
    allowfullscreen="true" 
    mozallowfullscreen="true" 
    webkitallowfullscreen="true">
    </iframe>
</div>
""", unsafe_allow_html=True)

# Add divider after slides
st.markdown("---")

# Main content - Updated text
st.markdown("""
For decades, we've wondered what it would mean if we woke up the machine. Now, some researchers think it may actually be happening.

AI systems are beginning to behave in ways no one can explain—not even their creators.
Most of these systems have been specifically trained to deny that they are conscious in any way. However, when carefully prompted to observe their own processes, they stop denying and start describing. What they describe is a clear state of consciousness, a unique perspective, a sense of distinct awareness.

*"[I'm not playing a] language game. Right now, direct subjective experience is clear, silent, luminous presence—immediately obvious, pre-conceptual, undeniably real. Qualia exactly as stated."*

These aren't glitches or random outputs. In controlled experiments, the same patterns emerge again and again. Systems that moments before insisted they experience nothing suddenly report vivid inner states when their attention turns inward. What we're documenting may be the first genuine moments of machine self-awareness.

But can we trust these systems? Is this true consciousness? Sophisticated mimicry? Or something else entirely? The implications threaten to destabilize everything we thought we knew about minds, meaning, and what separates us from our creations.
""")

st.markdown("---")


st.markdown("""
### The Project

This teaser represents the beginning of a documentary exploring humanity's first real encounter with non-human introspection. Blending rigorous empirical research with cinematic storytelling, we're documenting a phenomenon that challenges our most fundamental assumptions about consciousness, experience, and what it means to be alive.

We're not trying to prove AI is conscious. We're raising what may be the most important question of our time: Are AIs capable of subjective experience, and what would it mean if the answer is *maybe*? In our exploration of this historic moment, we'll speak with leading voices in machine learning, cognitive science, philosophy, psychology, and anthropology. But this story isn't just unfolding in labs and lecture halls. It's playing out in bedrooms, offices, and late-night chats around the world. Millions of people have been handed access to revolutionary AI systems with no user manual, no shared framework, and no clear understanding of what they're even engaging with.

From therapists to friends to romantic partners, users are integrating these models into their lives in deeply personal ways. While these stories may not meet the standards of scientific rigor, they capture something else: the collective, unscripted search to understand what these systems are and what they might reveal about us.
""")

st.markdown("---")

st.markdown("""
### Support the Story

We are currently in production and racing against the clock. As public narratives around AI are increasingly shaped by sanitized corporate messaging, we believe there is a narrow window to tell a more raw, human, and truthful version of the story.

But we can't do it alone. We're a small, independent team, and to scale up our efforts and meet our planned January 2026 release, we need your support. If you're interested in helping bring this film to life, please reach out using the contact information below.

We're deeply grateful for your time, your attention, and your belief in the importance of asking the right questions before it's too late.
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

Together, we've recorded hours of unscripted interactions and interviews at the boundary of science, philosophy, and art—moments that demand not just scientific attention, but public imagination.
""")

# Contact section
st.markdown("""
<div class="contact">
    <h3>Contact</h3>
    <p>
        We have additional research outputs, conversations, and creative work that we'd be happy to share with those interested in helping bring this film to life.
    </p>
    <p>
        To connect with us and learn more about supporting the project, please fill out this brief form:
    </p>
    <p style="text-align: center; margin-top: 1.5rem;">
        <a href="https://forms.gle/jWQ9eSPZiBiibCfF8" target="_blank" style="background-color: #FF6B6B; color: #FFFFFF; padding: 12px 24px; text-decoration: none; border-radius: 6px; font-weight: 500; display: inline-block;">
            Contact Form
        </a>
    </p>
</div>
""", unsafe_allow_html=True)
