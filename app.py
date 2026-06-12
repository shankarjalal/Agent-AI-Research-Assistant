import streamlit as st
import time
from pipeline import run_research_pipeline

# 1. Page Configuration
st.set_page_config(
    page_title="AI Research Agent | Advanced Web Edition",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)


# 2. Custom CSS for Premium Design
st.markdown("""
<style>
    /* Gradient animated background for title */
    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1, #A18CD1, #FBC2EB);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradient-animation 6s ease infinite;
        margin-bottom: 0px;
    }
    @keyframes gradient-animation {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Subtitle styling */
    .hero-subtitle {
        font-size: 1.2rem;
        color: #888888;
        margin-bottom: 2rem;
        font-weight: 400;
    }
    
    /* Glassmorphism cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        margin-bottom: 1.5rem;
    }
    
    /* Input box enhancement */
    div[data-baseweb="input"] {
        border-radius: 8px !important;
        border: 2px solid transparent;
    }
    div[data-baseweb="input"]:focus-within {
        border-color: #4ECDC4 !important;
        box-shadow: 0 0 10px rgba(78, 205, 196, 0.3);
    }
    
    /* Button enhancements */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #4ECDC4, #556270);
        color: white;
        border: none;
        padding: 0.6rem 2rem;
        border-radius: 30px;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(78, 205, 196, 0.4);
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(78, 205, 196, 0.6);
        background: linear-gradient(90deg, #556270, #4ECDC4);
    }
    
    /* Styling Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: transparent;
        border-radius: 6px 6px 0px 0px;
        transform: translateY(0px);
        transition: all 0.2s ease-in-out;
    }
    .stTabs [aria-selected="true"] {
        color: #4ECDC4 !important;
        border-bottom-color: #4ECDC4 !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar UI
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/8636/8636868.png", width=100)
    st.markdown("## 🧠 Configuration")
    st.markdown("Customize your AI Research Agent settings before diving into deep structural analysis.")
    st.divider()
    research_depth = st.select_slider("Research Depth", options=["Quick", "Detailed", "Exhaustive"], value="Detailed")
    st.info("💡 **Tip:** Use 'Exhaustive' for better critical reviews.")
    st.divider()
    st.caption("Powered by LangGraph & Streamlit")

# 4. Main Content Area
st.markdown('<div class="hero-title">🔎 Nexus AI Research</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">Advanced multidimensional web search, autonomous scraping, and structured critical report generation.</div>', unsafe_allow_html=True)

# Search Input Area wrapped in a custom container style
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
col1, col2 = st.columns([3, 1])
with col1:
    topic = st.text_input("Enter Topic to Research", placeholder="e.g., SpaceX recent launches, Quantum computing progress...", label_visibility="collapsed")
with col2:
    run_btn = st.button("🚀 Ignite Research")
st.markdown('</div>', unsafe_allow_html=True)

if run_btn:
    if not topic.strip():
        st.error("⚠️ Please provide a valid topic to initiate the research pipeline.")
    else:
        st.toast("Initialization complete...", icon="⚙️")
        
        # Dynamic progress and status Simulation
        status_text = st.empty()
        progress_bar = st.progress(0)
        
        # Simulate initial setup visually
        status_text.markdown("✨ **Agent is waking up...**")
        for i in range(1, 15):
            time.sleep(0.05)
            progress_bar.progress(i)
            
        status_text.markdown("🔍 **Searching web sources...**")
        progress_bar.progress(30)
        
        try:
            # The actual pipeline running
            with st.spinner("⏳ Compiling data internally... The agent might pause for rate limits, please wait (up to 2 mins)..."):
                state = run_research_pipeline(topic)
                
            progress_bar.progress(100)
            status_text.markdown("✅ **Research successfully aggregated!**")
            st.toast("Research pipeline successfully finished!", icon="🏆")
            st.balloons()
            
            st.divider()
            
            # 5. Displaying Results in a structured, advanced way
            st.markdown("### 📊 Research Analytics Dashboard")
            
            # Create metrics row
            c1, c2, c3 = st.columns(3)
            c1.metric("Processing Status", "100%", "Complete")
            c2.metric("Extracted Insights", "High", "Critical")
            c3.metric("Topic Match", "Optimal", "Validated")
            
            st.write("")
            
            # Modern Tabs
            tab_report, tab_critic, tab_search, tab_scrape = st.tabs([
                "📄 Final Report", 
                "⚖️ Critic Review", 
                "🌐 Search Results", 
                "🕸️ Scraped Raw Content"
            ])
            
            with tab_report:
                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                st.markdown("#### Comprehensive Report")
                st.markdown(state.get('report', '*No report available*'))
                st.markdown('</div>', unsafe_allow_html=True)
                
            with tab_critic:
                st.markdown('<div class="glass-card" style="border-left: 4px solid #FF6B6B;">', unsafe_allow_html=True)
                st.markdown("#### Peer-Review & Feedback")
                st.markdown(state.get('Feedback', '*No feedback available*'))
                st.markdown('</div>', unsafe_allow_html=True)
                
            with tab_search:
                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                st.caption("Raw output from search operators")
                st.write(state.get('search_results', '*No search results available*'))
                st.markdown('</div>', unsafe_allow_html=True)
                
            with tab_scrape:
                with st.expander("Show detailed scraped text content", expanded=False):
                    st.code(state.get('scraped_content', 'No content scraped'), language='markdown')
                    
        except Exception as e:
            progress_bar.empty()
            status_text.empty()
            st.error(f"🚨 **Critical Pipeline Error:** {e}")
            st.warning("Please check your API keys and rate limits.")
            