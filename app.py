import streamlit as st
from supabase import create_client, Client

# 1. Connect to Supabase
url: str = "https://ivcwoqyyzekeewabavds.supabase.co"
key: str = "sb_publishable_KZua9F4-DPPFDAc-p89S-Q_qSePGzHb"
supabase: Client = create_client(url, key)

# Configure elegant UI layout canvas
st.set_page_config(page_title="Career Compass Pro", page_icon="🧭", layout="centered")

# Inject Custom CSS overrides to mimic a sleek, premium SaaS application framework
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    html, body, [data-testid="stAppViewContainer"] { font-family: 'Inter', sans-serif; background-color: #fafafa; }
    .stRadio > div { background-color: #ffffff; padding: 24px; border-radius: 14px; border: 1px solid #e5e7eb; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
    .stButton>button { width: 100%; border-radius: 10px; background-color: #4f46e5; color: white; font-weight: 500; padding: 12px; border: none; transition: all 0.2s; }
    .stButton>button:hover { background-color: #4338ca; box-shadow: 0 4px 12px rgba(79, 70, 229, 0.2); }
    h1, h2, h3 { color: #1f2937; font-weight: 700; }
    .css-10trblm { color: #4b5563; }
    </style>
""", unsafe_allow_html=True)

# Application Header Framework
st.markdown("<h1 style='text-align: center; margin-bottom: 0;'>🧭 Career Compass Pro</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6b7280; font-size: 1.1em;'>Adaptive Predictive Behavioral & Role Alignment Assessment</p>", unsafe_allow_html=True)
st.write("---")

# Initialize Session State Variables for Enterprise Orchestration
if "user_email" not in st.session_state: st.session_state.user_email = None
if "current_step" not in st.session_state: st.session_state.current_step = "auth"
if "answers" not in st.session_state: st.session_state.answers = {}
if "scores" not in st.session_state: st.session_state.scores = {
    "Data Analyst": 0, "Software Engineer": 0, "UX/UI Designer": 0, 
    "Product Manager": 0, "Marketing Specialist": 0, "Project Manager": 0
}

def allocate_weights(weight_dictionary):
    for role, points in weight_dictionary.items():
        st.session_state.scores[role] += points

# ----------------- MODULE 1: AUTHENTICATION INTERFACE -----------------
if st.session_state.current_step == "auth":
    st.markdown("### 🔐 Evaluator Identity Access")
    st.caption("Please authenticate or declare an evaluation session identity below.")
    
    email = st.text_input("Corporate / Candidate Email Address", placeholder="name@company.com")
    password = st.text_input("Secure Session Token / Password", type="password", placeholder="••••••••")
    
    if st.button("Access Application Matrix ➔"):
        if email and password:
            try:
                res = supabase.auth.sign_in_with_password(credentials={"email": email, "password": password})
                st.session_state.user_email = email
                st.session_state.user_id = res.user.id
            except Exception:
                try:
                    res = supabase.auth.sign_up(credentials={"email": email, "password": password})
                    st.session_state.user_email = email
                    st.session_state.user_id = res.user.id
                except Exception as e:
                    st.error(f"Authentication Node Exception: {str(e)}")
            
            if st.session_state.user_email:
                try:
                    data = supabase.table("assessment_results").select("*").eq("user_id", st.session_state.user_id).order("created_at", desc=True).limit(1).execute()
                    if data.data:
                        st.session_state.past_result = data.data[0]
                        st.session_state.current_step = "dashboard"
                    else:
                        st.session_state.current_step = "q1"
                except Exception:
                    st.session_state.current_step = "q1"
                st.rerun()

# ----------------- MODULE 2: RETURNING EVALUATOR STATE -----------------
elif st.session_state.current_step == "dashboard":
    past = st.session_state.past_result
    st.markdown(f"### 👋 Welcome Back, `{st.session_state.user_email}`")
    st.write("The platform has matched your historic credentials to an established diagnostic deployment profile.")
    
    st.markdown(f"""
    <div style="background-color:#ffffff; padding:24px; border-radius:12px; border: 1px solid #e5e7eb; border-left: 6px solid #4f46e5; margin: 20px 0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
        <span style="color:#4f46e5; font-weight:600; font-size:0.85em; text-transform:uppercase; tracking-wider:0.1em;">Retrieved Assessment Profile</span>
        <h3 style="margin-top:4px; margin-bottom:8px; color:#111827;">{past['top_match']}</h3>
        <p style="color:#4b5563; font-size:0.95em; line-height:1.5;">{past['explanation']}</p>
        <span style="color:#9ca3af; font-size:0.8em;">Logged Run Date: {past['created_at'][:10]}</span>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Initialize Fresh Diagnostic Run"):
        st.session_state.answers = {}
        st.session_state.scores = {c: 0 for c in st.session_state.scores}
        st.session_state.current_step = "q1"
        st.rerun()

# ----------------- MODULE 3: 10-QUESTION DEEPLY ADAPTIVE ENGINE -----------------
elif st.session_state.current_step == "q1":
    st.progress(0.1, text="Progress: 10%")
    st.markdown("### **Question 1:** When you open a product or app, what component catches your eye first?")
    choice = st.radio("Select an option:", [
        "A) The raw business logic, database responsiveness, and architectural flow.",
        "B) The layout structure, visual rhythm, micro-animations, and visual balance.",
        "C) The target market alignment, core feature roadmap, and operational utility."
    ])
    if st.button("Process Step ➔"):
        st.session_state.answers["Q1"] = choice
        if "A)" in choice: st.session_state.current_step = "q2_tech"
        elif "B)" in choice: st.session_state.current_step = "q2_creative"
        else: st.session_state.current_step = "q2_biz"
        st.rerun()

# --- TRACK A: TECH & DATA (QUESTIONS 2, 3, 4) ---
elif st.session_state.current_step == "q2_tech":
    st.progress(0.2, text="Progress: 20%")
    st.markdown("### **Question 2:** Faced with massive structured arrays, your primary instinct is to:")
    choice = st.radio("Select an option:", [
        "A) Build statistical tracking layers, extract underlying correlations, and render insights.",
        "B) Optimize the ingestion pipeline speed, normalize database structures, and structure reusable code blocks."
    ])
    if st.button("Process Step ➔"):
        st.session_state.answers["Q2"] = choice
        if "A)" in choice:
            allocate_weights({"Data Analyst": 3, "Product Manager": 1})
            st.session_state.current_step = "q3_data"
        else:
            allocate_weights({"Software Engineer": 3, "Project Manager": 1})
            st.session_state.current_step = "q3_eng"
        st.rerun()

elif st.session_state.current_step == "q3_data":
    st.progress(0.3, text="Progress: 30%")
    st.markdown("### **Question 3:** How do you view business reports and KPI metrics?")
    choice = st.radio("Select an option:", [
        "A) As a canvas to build elegant, interactive BI data stories and performance visualization dashboards.",
        "B) As raw feature variables to feed into machine learning models or statistical prediction engines."
    ])
    if st.button("Process Step ➔"):
        st.session_state.answers["Q3"] = choice
        allocate_weights({"Data Analyst": 3} if "A)" in choice else {"Data Analyst": 2, "Software Engineer": 1})
        st.session_state.current_step = "q4_tech_shared"
        st.rerun()

elif st.session_state.current_step == "q3_eng":
    st.progress(0.3, text="Progress: 30%")
    st.markdown("### **Question 3:** Which codebase system scaling vector sounds most rewarding?")
    choice = st.radio("Select an option:", [
        "A) Writing multi-threaded web API architectures and robust backend logic models.",
        "B) Engineering interactive browser-side interface frameworks and components."
    ])
    if st.button("Process Step ➔"):
        st.session_state.answers["Q3"] = choice
        allocate_weights({"Software Engineer": 3} if "A)" in choice else {"Software Engineer": 2, "UX/UI Designer": 1})
        st.session_state.current_step = "q4_tech_shared"
        st.rerun()

elif st.session_state.current_step == "q4_tech_shared":
    st.progress(0.4, text="Progress: 40%")
    st.markdown("### **Question 4:** When an unexpected server or validation bug compromises production, you:")
    choice = st.radio("Select an option:", [
        "A) Dive directly into logging records and execution scripts to find the logic breakdown.",
        "B) Re-evaluate user journey reports to assess behavioral dropoffs and immediate systemic impacts."
    ])
    if st.button("Process Step ➔"):
        st.session_state.answers["Q4"] = choice
        allocate_weights({"Software Engineer": 2, "Data Analyst": 2} if "A)" in choice else {"Product Manager": 2, "Project Manager": 1})
        st.session_state.current_step = "q5_cross_all"
        st.rerun()

# --- TRACK B: CREATIVE (QUESTIONS 2, 3, 4) ---
elif st.session_state.current_step == "q2_creative":
    st.progress(0.2, text="Progress: 20%")
    st.markdown("### **Question 2:** When evaluating human-computer interfaces, your design priority focuses on:")
    choice = st.radio("Select an option:", [
        "A) Crafting effortless user flow hierarchies, cognitive empathy maps, and seamless interactions.",
        "B) Designing compelling visual assets, conversion copywriting, and targeted audience brand hooks."
    ])
    if st.button("Process Step ➔"):
        st.session_state.answers["Q2"] = choice
        if "A)" in choice:
            allocate_weights({"UX/UI Designer": 3, "Product Manager": 1})
            st.session_state.current_step = "q3_design"
        else:
            allocate_weights({"Marketing Specialist": 3, "Product Manager": 1})
            st.session_state.current_step = "q3_marketing"
        st.rerun()

elif st.session_state.current_step == "q3_design":
    st.progress(0.3, text="Progress: 30%")
    st.markdown("### **Question 3:** What phase of the design evolution process satisfies you most?")
    choice = st.radio("Select an option:", [
        "A) Translating chaotic user feedback interviews into wireframes and dynamic UI design systems.",
        "B) Polishing brand palettes, structural layouts, and asset graphics for advertising campaigns."
    ])
    if st.button("Process Step ➔"):
        st.session_state.answers["Q3"] = choice
        allocate_weights({"UX/UI Designer": 3} if "A)" in choice else {"UX/UI Designer": 1, "Marketing Specialist": 2})
        st.session_state.current_step = "q5_cross_all"
        st.rerun()

elif st.session_state.current_step == "q3_marketing":
    st.progress(0.3, text="Progress: 30%")
    st.markdown("### **Question 3:** In optimizing client conversion channels, which strategy takes priority?")
    choice = st.radio("Select an option:", [
        "A) Launching multivariate growth loops, audience segment models, and advertising frameworks.",
        "B) Designing immersive brand interactive pages to maximize organic consumer retention."
    ])
    if st.button("Process Step ➔"):
        st.session_state.answers["Q3"] = choice
        allocate_weights({"Marketing Specialist": 3} if "A)" in choice else {"Marketing Specialist": 1, "UX/UI Designer": 2})
        st.session_state.current_step = "q5_cross_all"
        st.rerun()

# --- TRACK C: BUSINESS & OPERATION (QUESTIONS 2, 3, 4) ---
elif st.session_state.current_step == "q2_biz":
    st.progress(0.2, text="Progress: 20%")
    st.markdown("### **Question 2:** Where do you position your primary operational impact?")
    choice = st.radio("Select an option:", [
        "A) Owning structural roadmaps, discovering product market fits, and defining features.",
        "B) Unblocking complex cross-team schedules, allocating project budgets, and hitting execution sprints."
    ])
    if st.button("Process Step ➔"):
        st.session_state.answers["Q2"] = choice
        if "A)" in choice:
            allocate_weights({"Product Manager": 3, "Marketing Specialist": 1})
            st.session_state.current_step = "q3_pm"
        else:
            allocate_weights({"Project Manager": 3, "Software Engineer": 1})
            st.session_state.current_step = "q3_pjm"
        st.rerun()

elif st.session_state.current_step == "q3_pm":
    st.progress(0.3, text="Progress: 30%")
    st.markdown("### **Question 3:** What asset represents the foundation of a successful deployment cycle?")
    choice = st.radio("Select an option:", [
        "A) A meticulously backed business thesis founded on verified market telemetry.",
        "B) A beautifully clean, multi-department Gantt chart and milestone tracking sheet."
    ])
    if st.button("Process Step ➔"):
        st.session_state.answers["Q3"] = choice
        allocate_weights({"Product Manager": 3} if "A)" in choice else {"Product Manager": 1, "Project Manager": 2})
        st.session_state.current_step = "q5_cross_all"
        st.rerun()

elif st.session_state.current_step == "q3_pjm":
    st.progress(0.3, text="Progress: 30%")
    st.markdown("### **Question 3:** When resource shortages or scheduling changes threaten delivery, your immediate strategy is to:")
    choice = st.radio("Select an option:", [
        "A) Rescope sprints, balance operational capacity, and negotiate timeline trade-offs.",
        "B) Dive into technical tasks directly to support engineering velocity."
    ])
    if st.button("Process Step ➔"):
        st.session_state.answers["Q3"] = choice
        allocate_weights({"Project Manager": 3} if "A)" in choice else {"Project Manager": 1, "Software Engineer": 2})
        st.session_state.current_step = "q5_cross_all"
        st.rerun()

# --- MODULE 4: UNIVERSAL CORE SCALING VECTORS (QUESTIONS 5 TO 10) ---
elif st.session_state.current_step == "q5_cross_all":
    st.progress(0.5, text="Progress: 50%")
    st.markdown("### **Question 5:** Which operational workflow pace matches your peak cognitive output?")
    choice = st.radio("Select an option:", [
        "A) Highly dynamic, rapid experimental cycles deploying updates daily based on user metrics.",
        "B) Rigorous, stable, deeply architectural planning phases that guarantee predictable system deployment."
    ])
    if st.button("Process Step ➔"):
        st.session_state.answers["Q5"] = choice
        allocate_weights({"Marketing Specialist": 2, "Product Manager": 2} if "A)" in choice else {"Project Manager": 2, "Software Engineer": 2, "Data Analyst": 1})
        st.session_state.current_step = "q6"
        st.rerun()

elif st.session_state.current_step == "q6":
    st.progress(0.6, text="Progress: 60%")
    st.markdown("### **Question 6:** When collaborating within multi-disciplinary groups, you naturally become:")
    choice = st.radio("Select an option:", [
        "A) The Execution Catalyst: Resolving operational blockers and managing timelines.",
        "B) The Analytical Filter: Evaluating technical feasibility constraints and empirical data trends."
    ])
    if st.button("Process Step ➔"):
        st.session_state.answers["Q6"] = choice
        allocate_weights({"Project Manager": 2, "Product Manager": 1} if "A)" in choice else {"Data Analyst": 2, "Software Engineer": 1, "UX/UI Designer": 1})
        st.session_state.current_step = "q7"
        st.rerun()

elif st.session_state.current_step == "q7":
    st.progress(0.7, text="Progress: 70%")
    st.markdown("### **Question 7:** What metric matters most when defining project success?")
    choice = st.radio("Select an option:", [
        "A) Quantifiable conversions, revenue optimization metrics, and user growth data numbers.",
        "B) Platform processing stability, visual design integrity, and absolute bug elimination."
    ])
    if st.button("Process Step ➔"):
        st.session_state.answers["Q7"] = choice
        allocate_weights({"Marketing Specialist": 2, "Product Manager": 2, "Data Analyst": 1} if "A)" in choice else {"Software Engineer": 2, "UX/UI Designer": 2, "Project Manager": 1})
        st.session_state.current_step = "q8"
        st.rerun()

elif st.session_state.current_step == "q8":
    st.progress(0.8, text="Progress: 80%")
    st.markdown("### **Question 8:** Faced with an ambiguous problem statement with no historical data, your next move is to:")
    choice = st.radio("Select an option:", [
        "A) Build structured user journey models, wireframe variations, or structural proof-of-concepts.",
        "B) Aggregate secondary data fields, survey populations, or deploy tracking telemetry frameworks."
    ])
    if st.button("Process Step ➔"):
        st.session_state.answers["Q8"] = choice
        allocate_weights({"UX/UI Designer": 2, "Software Engineer": 1, "Product Manager": 1} if "A)" in choice else {"Data Analyst": 3, "Marketing Specialist": 1})
        st.session_state.current_step = "q9"
        st.rerun()

elif st.session_state.current_step == "q9":
    st.progress(0.9, text="Progress: 90%")
    st.markdown("### **Question 9:** Which communication archetype aligns closest with your professional style?")
    choice = st.radio("Select an option:", [
        "A) Presenting high-impact strategic business updates to leadership teams and managing alignment.",
        "B) Authoring clear technical logs, mapping precise variable structures, or documenting workflows."
    ])
    if st.button("Process Step ➔"):
        st.session_state.answers["Q9"] = choice
        allocate_weights({"Product Manager": 2, "Project Manager": 2, "Marketing Specialist": 1} if "A)" in choice else {"Software Engineer": 2, "Data Analyst": 2, "UX/UI Designer": 1})
        st.session_state.current_step = "q10"
        st.rerun()

elif st.session_state.current_step == "q10":
    st.progress(1.0, text="Progress: 100%")
    st.markdown("### **Question 10:** If you had a dedicated day for career development, you would focus on:")
    choice = st.radio("Select an option:", [
        "A) Perfecting systemic logic models, scripting data flows, or building interactive tools.",
        "B) Studying user behavioral patterns, strategic target variables, or product metrics frameworks."
    ])
    if st.button("Finalize Predictive Analysis ➔"):
        st.session_state.answers["Q10"] = choice
        allocate_weights({"Software Engineer": 2, "Data Analyst": 2, "UX/UI Designer": 1} if "A)" in choice else {"Product Manager": 2, "Marketing Specialist": 2, "Project Manager": 1})
        
        # Calculate maximum value alignment
        top_match = max(st.session_state.scores, key=st.session_state.scores.get)
        st.session_state.match = top_match
        st.session_state.current_step = "results"
        st.rerun()

# ----------------- MODULE 5: ANALYTICAL RESULTS & REPORT EXPORT -----------------
elif st.session_state.current_step == "results":
    match = st.session_state.match
    
    explanations = {
        "Data Analyst": "Your profile demonstrates strong alignment with empirical data translation, mathematical logic modeling, and business intelligence reporting. You focus on tracking key metrics and turning database arrays into clear insights.",
        "Software Engineer": "Your profile shows a natural tendency toward structural algorithms, reusable backend systems engineering, and automated programmatic code execution.",
        "UX/UI Designer": "Your answers indicate deep alignment with human-centric interfaces, interface visual balance heuristics, and structured interaction layout maps.",
        "Product Manager": "Your focus maps closely to macro strategic lifecycle control, value metric trade-offs, and discovering product-market fit parameters.",
        "Marketing Specialist": "Your skills align with strategic growth frameworks, consumer data attribution metrics, and targeted messaging strategies.",
        "Project Manager": "Your profile excels at resource allocation modeling, cross-functional timeline controls, and running organized agile project methodologies."
    }
    
    st.balloons()
    st.markdown(f"""
    <div style="background-color:#f0fdf4; padding:24px; border-radius:12px; border-left: 6px solid #16a34a; margin-bottom:24px;">
        <h2 style="color:#16a34a; margin:0;">🎉 Predictive Target Met!</h2>
        <p style="font-size:1.3em; margin-top:8px; margin-bottom:4px; color:#14532d;">Top Alignment Vector: <b>{match}</b></p>
        <p style="color:#14532d; font-size:0.95em; line-height:1.6;">{explanations[match]}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Render interactive evaluation visualizers for the review panel
    st.markdown("#### 📊 Accumulation Factor Matrix")
    st.bar_chart(st.session_state.scores)
    
    # Database Payload Synchronization
    payload = {
        "user_id": st.session_state.user_id,
        "answers": st.session_state.answers,
        "top_match": match,
        "explanation": explanations[match],
        "scores": st.session_state.scores
    }
    
    try:
        supabase.table("assessment_results").insert(payload).execute()
        st.success("✅ Run state successfully recorded in database registry.")
    except Exception as e:
        st.error(f"Database sync exception: {e}")
        
    if st.button("Reset Matrix Sandbox"):
        st.session_state.current_step = "auth"
        st.session_state.answers = {}
        st.session_state.scores = {c: 0 for c in st.session_state.scores}
        st.rerun()
