import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Career Validator",
    page_icon="🎓",
    layout="wide"
)

# =========================================================
# LOAD SURVEY DATA
# =========================================================

try:
    df = pd.read_csv("survey_responses.csv")
    survey_loaded = True
    total_responses = len(df)
except FileNotFoundError:
    survey_loaded = False
    df = pd.DataFrame()
    total_responses = 0

# =========================================================
# CUSTOMER DEMAND SCORE
# =========================================================

customer_score = 65.0

if survey_loaded:

    q_ai = (
        "Would you use an AI platform that recommends "
        "career paths based on your profile?"
    )

    if q_ai in df.columns and total_responses > 0:

        positive_responses = df[q_ai].isin(
            ["Definitely", "Probably"]
        ).sum()

        customer_score = (
            positive_responses / total_responses
        ) * 100

# =========================================================
# VALIDATION SCORES
# =========================================================

market_score = 85
competition_score = 60
financial_score = 75

# =========================================================
# OVERALL VALIDATION SCORE
# =========================================================

final_score = (
    market_score * 0.25
    + customer_score * 0.30
    + competition_score * 0.20
    + financial_score * 0.25
)

# =========================================================
# TAM / SAM / SOM
# =========================================================

tam_students = 4.46 * 10**7
sam_students = 89.2 * 10**5
som_students = 89200

monthly_price = 99

tam_revenue = tam_students * monthly_price
sam_revenue = sam_students * monthly_price
som_revenue = som_students * monthly_price

# =========================================================
# FINANCIAL FEASIBILITY
# PROJECT ASSUMPTIONS
# =========================================================

premium_price = 99
paid_users = 100
monthly_operating_cost = 5000

monthly_revenue = premium_price * paid_users
monthly_profit = monthly_revenue - monthly_operating_cost

if monthly_revenue > 0:
    profit_margin = (
        monthly_profit / monthly_revenue
    ) * 100
else:
    profit_margin = 0

annual_revenue = monthly_revenue * 12
annual_profit = monthly_profit * 12

# =========================================================
# GOOGLE TRENDS RESEARCH DATA
# =========================================================

trends_data = pd.DataFrame({
    "Search Term": [
        "Career Guidance",
        "Skill Development",
        "Career Assessment",
        "AI Career",
        "Career Counselling"
    ],
    "Current Interest": [
        39,
        65,
        100,
        93,
        0
    ],
    "Growth / Change": [
        "+20%",
        "+6%",
        "+90%",
        "+1350%",
        "+30%"
    ]
})

# =========================================================
# COMPETITOR DATA
# =========================================================

competitors = pd.DataFrame({
    "Company": [
        "CareerGuide",
        "Edumilestones",
        "Mindler",
        "Our Platform"
    ],
    "Career Assessment": [
        "Yes",
        "Yes",
        "Yes",
        "Yes"
    ],
    "Career Guidance": [
        "Yes",
        "Yes",
        "Yes",
        "Yes"
    ],
    "AI Features": [
        "AI-based tools",
        "AI insights",
        "AI-enabled tools",
        "AI recommendations"
    ],
    "Target Users": [
        "Students",
        "Graduates & Professionals",
        "Students & Graduates",
        "College Students"
    ],
    "Pricing": [
        "From ₹1,000",
        "₹5,999",
        "From ₹2,399",
        "₹0 / ₹99 per month"
    ]
})

# =========================================================
# TITLE
# =========================================================

st.title("🎓 AI Career & Skill Recommendation Platform")

st.subheader(
    "AI-Powered Career Guidance for College Students"
)

st.write(
    "A research-based startup validation platform that "
    "analyzes market demand, customer demand, competition "
    "and financial feasibility."
)

st.divider()

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("📌 Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "🏠 Home",
        "📋 Research Data",
        "📊 Market Size",
        "🏢 Competitor Analysis",
        "💰 Financial Feasibility",
        "📈 Google Trends",
        "🤖 AI Recommendation",
        "🚀 Validate Idea"
    ]
)

# =========================================================
# HOME PAGE
# =========================================================

if page == "🏠 Home":

    st.header("🔍 Startup Validation Dashboard")

    st.write(
        "The platform evaluates the proposed startup idea "
        "using four major validation dimensions."
    )

    # SCORE CARDS

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📈 Market Demand",
            f"{market_score}/100"
        )

    with col2:
        st.metric(
            "👥 Customer Demand",
            f"{customer_score:.0f}/100"
        )

    with col3:
        st.metric(
            "🏢 Competition",
            f"{competition_score}/100"
        )

    with col4:
        st.metric(
            "💰 Financial Feasibility",
            f"{financial_score}/100"
        )

    st.divider()

    # OVERALL SCORE

    st.header("🎯 Overall Validation Score")

    st.metric(
        "Startup Validation Score",
        f"{final_score:.1f}/100"
    )

    st.progress(
        min(final_score / 100, 1.0)
    )

    st.info(
        "The score is a project-based analytical indicator "
        "using research findings and stated assumptions."
    )

    st.divider()

    # PROJECT FEATURES

    st.header("🚀 Platform Features")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.subheader("📊 Market Research")

        st.write(
            "Google Trends and TAM/SAM/SOM market analysis."
        )

    with col2:

        st.subheader("👥 Customer Research")

        st.write(
            "Analysis of responses collected from college students."
        )

    with col3:

        st.subheader("🏢 Competition")

        st.write(
            "Comparison with existing career guidance platforms."
        )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.subheader("💰 Financial Analysis")

        st.write(
            "Revenue, cost, profit and margin estimation."
        )

    with col2:

        st.subheader("🤖 AI Recommendations")

        st.write(
            "Personalized career and skill recommendations."
        )

    with col3:

        st.subheader("🚀 Startup Validation")

        st.write(
            "Combined validation score based on four factors."
        )

    st.divider()

    st.header("📚 Research Sources")

    st.markdown("""
### Primary Research
- Google Forms questionnaire
- 20 student responses

### Secondary Research
- Google Trends
- Competitor research
- Market research

### Technology
- Python
- Pandas
- Plotly
- Streamlit
    """)

# =========================================================
# RESEARCH DATA PAGE
# =========================================================

elif page == "📋 Research Data":

    st.header("📋 Primary Research Analysis")

    if survey_loaded:

        st.success(
            f"✅ Survey data loaded successfully — "
            f"{total_responses} responses"
        )

        q_ai = (
            "Would you use an AI platform that recommends "
            "career paths based on your profile?"
        )

        q_personalized = (
            "Would you provide your skills and interests to "
            "get personalized recommendations?"
        )

        q_importance = (
            "How important is personalized career guidance to you?"
        )

        # -------------------------------------------------
        # PERSONALIZATION
        # -------------------------------------------------

        if q_personalized in df.columns:

            skill_yes = (
                df[q_personalized] == "Yes"
            ).sum()

            skill_percentage = (
                skill_yes / total_responses
            ) * 100

        else:

            skill_percentage = 0

        # -------------------------------------------------
        # IMPORTANCE
        # -------------------------------------------------

        if q_importance in df.columns:

            important_count = df[q_importance].isin(
                ["Very important", "Important"]
            ).sum()

            importance_percentage = (
                important_count / total_responses
            ) * 100

        else:

            importance_percentage = 0

        # -------------------------------------------------
        # KPI CARDS
        # -------------------------------------------------

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "🤖 AI Platform Interest",
                f"{customer_score:.0f}%"
            )

        with col2:

            st.metric(
                "🔐 Willing to Share Skills",
                f"{skill_percentage:.0f}%"
            )

        with col3:

            st.metric(
                "🎯 Guidance Importance",
                f"{importance_percentage:.0f}%"
            )

        st.divider()

        # -------------------------------------------------
        # AI INTEREST CHART
        # -------------------------------------------------

        st.subheader(
            "🤖 Interest in AI Career Recommendation Platform"
        )

        if q_ai in df.columns:

            ai_counts = df[q_ai].value_counts()

            fig1 = go.Figure(
                data=[
                    go.Bar(
                        x=ai_counts.index,
                        y=ai_counts.values,
                        text=ai_counts.values,
                        textposition="auto"
                    )
                ]
            )

            fig1.update_layout(
                xaxis_title="Response",
                yaxis_title="Students",
                height=400
            )

            st.plotly_chart(
                fig1,
                use_container_width=True
            )

        st.divider()

        # -------------------------------------------------
        # CAREER CHALLENGE
        # -------------------------------------------------

        st.subheader(
            "🎯 Major Career Challenges"
        )

        challenge_column = (
            "What is your biggest career-related challenge?"
        )

        if challenge_column in df.columns:

            challenge_counts = (
                df[challenge_column].value_counts()
            )

            fig2 = go.Figure(
                data=[
                    go.Bar(
                        x=challenge_counts.index,
                        y=challenge_counts.values,
                        text=challenge_counts.values,
                        textposition="auto"
                    )
                ]
            )

            fig2.update_layout(
                xaxis_title="Career Challenge",
                yaxis_title="Students",
                height=450
            )

            st.plotly_chart(
                fig2,
                use_container_width=True
            )

        st.divider()

        # -------------------------------------------------
        # RAW DATA
        # -------------------------------------------------

        with st.expander("📄 View All Survey Responses"):

            st.dataframe(
                df,
                use_container_width=True
            )

    else:

        st.error(
            "❌ survey_responses.csv was not found. "
            "Place it in the same folder as app.py."
        )

# =========================================================
# MARKET SIZE PAGE
# =========================================================

elif page == "📊 Market Size":

    st.header("📊 Market Size Analysis")

    st.write(
        "Estimated market opportunity for the proposed "
        "AI-powered career platform."
    )

    st.info(
        "⚠️ TAM, SAM and SOM are project assumptions "
        "used for market-sizing analysis."
    )

    st.divider()

    # -------------------------------------------------
    # MARKET CARDS
    # -------------------------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "🌍 TAM",
            "4.46 Crore"
        )

        st.caption(
            "Total Addressable Market"
        )

    with col2:

        st.metric(
            "🎯 SAM",
            "89.2 Lakh"
        )

        st.caption(
            "Serviceable Available Market"
        )

    with col3:

        st.metric(
            "🚀 SOM",
            "89,200"
        )

        st.caption(
            "Serviceable Obtainable Market"
        )

    st.divider()

    # -------------------------------------------------
    # DEFINITIONS
    # -------------------------------------------------

    st.subheader("🔎 Market Definition")

    st.markdown("""
**TAM – Total Addressable Market**

Total potential higher-education student population
considered for the platform.

**SAM – Serviceable Available Market**

20% of TAM representing the serviceable segment.

**SOM – Serviceable Obtainable Market**

1% of SAM representing the initial obtainable segment.
    """)

    st.divider()

    # -------------------------------------------------
    # CHART
    # -------------------------------------------------

    st.subheader("📈 TAM vs SAM vs SOM")

    fig_market = go.Figure(
        data=[
            go.Bar(
                x=["TAM", "SAM", "SOM"],
                y=[
                    tam_students,
                    sam_students,
                    som_students
                ],
                text=[
                    "4.46 Cr",
                    "89.2 Lakh",
                    "89,200"
                ],
                textposition="auto"
            )
        ]
    )

    fig_market.update_layout(
        title="Estimated Student Market Size",
        yaxis_title="Students",
        height=450
    )

    st.plotly_chart(
        fig_market,
        use_container_width=True
    )

    st.divider()

    # -------------------------------------------------
    # REVENUE OPPORTUNITY
    # -------------------------------------------------

    st.subheader("💰 Illustrative Revenue Opportunity")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "TAM Monthly Revenue",
            f"₹{tam_revenue / 1e7:.2f} Cr"
        )

    with col2:

        st.metric(
            "SAM Monthly Revenue",
            f"₹{sam_revenue / 1e7:.2f} Cr"
        )

    with col3:

        st.metric(
            "SOM Monthly Revenue",
            f"₹{som_revenue / 1e5:.2f} Lakh"
        )

    st.divider()

    st.subheader("📌 Market Assumptions")

    st.markdown("""
| Metric | Assumption |
|---|---:|
| TAM | 4.46 Crore students |
| SAM | 20% of TAM |
| SOM | 1% of SAM |
| Premium Price | ₹99/month |
    """)

# =========================================================
# COMPETITOR ANALYSIS PAGE
# =========================================================

elif page == "🏢 Competitor Analysis":

    st.header("🏢 Competitor Analysis")

    st.write(
        "Comparison of existing career guidance platforms "
        "with the proposed platform."
    )

    st.info(
        "Competitor information is used as research input "
        "for the academic project."
    )

    st.divider()

    # -------------------------------------------------
    # COMPETITOR TABLE
    # -------------------------------------------------

    st.subheader("📊 Competitor Comparison")

    st.dataframe(
        competitors,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # -------------------------------------------------
    # PRICING CHART
    # -------------------------------------------------

    st.subheader("💰 Indicative Pricing Comparison")

    pricing_values = [
        1000,
        5999,
        2399,
        99
    ]

    pricing_names = [
        "CareerGuide",
        "Edumilestones",
        "Mindler",
        "Our Platform"
    ]

    fig_price = go.Figure(
        data=[
            go.Bar(
                x=pricing_names,
                y=pricing_values,
                text=[
                    "₹1,000+",
                    "₹5,999",
                    "₹2,399+",
                    "₹99/month"
                ],
                textposition="auto"
            )
        ]
    )

    fig_price.update_layout(
        title="Indicative Pricing",
        xaxis_title="Platform",
        yaxis_title="Price (₹)",
        height=450
    )

    st.plotly_chart(
        fig_price,
        use_container_width=True
    )

    st.divider()

    # -------------------------------------------------
    # MARKET GAP
    # -------------------------------------------------

    st.subheader("🔍 Proposed Market Position")

    st.markdown("""
### Proposed Platform Focus

- College students
- Personalized career recommendations
- AI-based skill recommendations
- Course recommendations
- Certification recommendations
- Internship and job recommendations
- Affordable premium subscription
    """)

    st.divider()

    # -------------------------------------------------
    # DIFFERENTIATION
    # -------------------------------------------------

    st.subheader("🚀 Platform Differentiation")

    differentiation = pd.DataFrame({
        "Feature": [
            "College Student Focus",
            "AI Career Recommendation",
            "Skill Recommendation",
            "Course Recommendation",
            "Certification Recommendation",
            "Internship / Job Recommendation",
            "Affordable Premium Plan"
        ],
        "Proposed Platform": [
            "✓",
            "✓",
            "✓",
            "✓",
            "✓",
            "✓",
            "✓"
        ]
    })

    st.table(
        differentiation
    )

    st.divider()

    st.subheader("📌 Competition Assessment")

    st.metric(
        "Competition Score",
        f"{competition_score}/100"
    )

    st.progress(
        competition_score / 100
    )

# =========================================================
# FINANCIAL FEASIBILITY PAGE
# =========================================================

elif page == "💰 Financial Feasibility":

    st.header("💰 Financial Feasibility")

    st.write(
        "Illustrative financial model for the proposed "
        "AI career recommendation platform."
    )

    st.info(
        "⚠️ All financial figures below are project assumptions."
    )

    st.divider()

    # -------------------------------------------------
    # FINANCIAL INPUTS
    # -------------------------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "💳 Premium Price",
            "₹99/month"
        )

    with col2:

        st.metric(
            "👥 Paid Users",
            "100/month"
        )

    with col3:

        st.metric(
            "💻 Operating Cost",
            "₹5,000/month"
        )

    st.divider()

    # -------------------------------------------------
    # FINANCIAL OUTPUTS
    # -------------------------------------------------

    st.subheader("📊 Monthly Financial Estimate")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Revenue",
            f"₹{monthly_revenue:,.0f}"
        )

    with col2:

        st.metric(
            "Operating Cost",
            f"₹{monthly_operating_cost:,.0f}"
        )

    with col3:

        st.metric(
            "Estimated Profit",
            f"₹{monthly_profit:,.0f}"
        )

    st.divider()

    # -------------------------------------------------
    # PROFIT MARGIN
    # -------------------------------------------------

    st.subheader("📈 Profit Margin")

    st.metric(
        "Estimated Profit Margin",
        f"{profit_margin:.1f}%"
    )

    st.progress(
        min(profit_margin / 100, 1.0)
    )

    st.divider()

    # -------------------------------------------------
    # ANNUAL ESTIMATE
    # -------------------------------------------------

    st.subheader("📅 Annual Estimate")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Annual Revenue",
            f"₹{annual_revenue:,.0f}"
        )

    with col2:

        st.metric(
            "Annual Profit",
            f"₹{annual_profit:,.0f}"
        )

    st.divider()

    # -------------------------------------------------
    # FINANCIAL CHART
    # -------------------------------------------------

    st.subheader("💹 Revenue vs Cost vs Profit")

    fig_finance = go.Figure(
        data=[
            go.Bar(
                x=[
                    "Revenue",
                    "Operating Cost",
                    "Profit"
                ],
                y=[
                    monthly_revenue,
                    monthly_operating_cost,
                    monthly_profit
                ],
                text=[
                    f"₹{monthly_revenue}",
                    f"₹{monthly_operating_cost}",
                    f"₹{monthly_profit}"
                ],
                textposition="auto"
            )
        ]
    )

    fig_finance.update_layout(
        title="Monthly Financial Model",
        yaxis_title="Amount (₹)",
        height=450
    )

    st.plotly_chart(
        fig_finance,
        use_container_width=True
    )

    st.divider()

    st.subheader("📌 Financial Assumptions")

    st.markdown("""
| Item | Assumption |
|---|---:|
| Free Plan | ₹0 |
| Premium Plan | ₹99/month |
| Paid Users | 100/month |
| Monthly Revenue | ₹9,900 |
| Monthly Operating Cost | ₹5,000 |
| Monthly Profit | ₹4,900 |
| Profit Margin | 49.5% |
    """)

    st.divider()

    st.subheader("💰 Financial Feasibility Score")

    st.metric(
        "Financial Feasibility",
        f"{financial_score}/100"
    )

# =========================================================
# GOOGLE TRENDS PAGE
# =========================================================

elif page == "📈 Google Trends":

    st.header("📈 Google Trends Market Research")

    st.write(
        "Selected Google Trends observations used as "
        "secondary research for the project."
    )

    st.info(
        "The values below are research inputs collected "
        "during the project and are not live data."
    )

    st.divider()

    # -------------------------------------------------
    # TRENDS TABLE
    # -------------------------------------------------

    st.subheader("🔎 Search Interest")

    display_trends = trends_data.copy()

    display_trends["Current Interest"] = (
        display_trends["Current Interest"].replace(
            0,
            "Not recorded"
        )
    )

    st.dataframe(
        display_trends,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # -------------------------------------------------
    # TRENDS CHART
    # -------------------------------------------------

    st.subheader("📊 Google Trends Interest")

    chart_data = trends_data[
        trends_data["Current Interest"] > 0
    ]

    fig_trends = go.Figure(
        data=[
            go.Bar(
                x=chart_data["Search Term"],
                y=chart_data["Current Interest"],
                text=chart_data["Current Interest"],
                textposition="auto"
            )
        ]
    )

    fig_trends.update_layout(
        title="Current Google Trends Interest",
        xaxis_title="Search Term",
        yaxis_title="Interest",
        height=450
    )

    st.plotly_chart(
        fig_trends,
        use_container_width=True
    )

    st.divider()

    # -------------------------------------------------
    # KEY OBSERVATIONS
    # -------------------------------------------------

    st.subheader("🔍 Key Research Observations")

    st.markdown("""
- Career guidance showed positive growth.
- Skill development showed continued search interest.
- Career assessment showed strong interest.
- AI career showed significant growth during the research period.
- Career counselling also showed positive growth.
    """)

    st.divider()

    st.subheader("📈 Market Demand Score")

    st.metric(
        "Market Demand",
        f"{market_score}/100"
    )

# =========================================================
# AI RECOMMENDATION PAGE
# =========================================================

elif page == "🤖 AI Recommendation":

    st.header("🤖 AI Career & Skill Recommendation Engine")

    st.write(
        "Enter a student's profile to generate a "
        "rule-based career and skill recommendation."
    )

    st.divider()

    # -------------------------------------------------
    # STUDENT INPUT
    # -------------------------------------------------

    degree = st.selectbox(
        "🎓 Degree / Education",
        [
            "B.Com",
            "BBA",
            "B.Sc",
            "BCA",
            "B.Tech",
            "MBA",
            "Other"
        ]
    )

    interests = st.multiselect(
        "❤️ Areas of Interest",
        [
            "Finance",
            "Marketing",
            "Human Resources",
            "Data Analytics",
            "Technology",
            "Business",
            "Design",
            "Entrepreneurship"
        ]
    )

    skills = st.multiselect(
        "🛠️ Current Skills",
        [
            "Excel",
            "Power BI",
            "SQL",
            "Python",
            "Communication",
            "Marketing",
            "Accounting",
            "Leadership",
            "Problem Solving"
        ]
    )

    career_goal = st.selectbox(
        "🎯 Career Goal",
        [
            "Get a Job",
            "Get an Internship",
            "Higher Studies",
            "Start a Business",
            "Explore Career Options"
        ]
    )

    st.divider()

    if st.button(
        "🤖 Generate Recommendation",
        use_container_width=True
    ):

        st.success(
            "✅ Personalized recommendation generated!"
        )

        # -------------------------------------------------
        # CAREER RECOMMENDATION LOGIC
        # -------------------------------------------------

        recommended_careers = []
        recommended_skills = []

        if (
            "Data Analytics" in interests
            or "Power BI" in skills
            or "SQL" in skills
            or "Python" in skills
        ):

            recommended_careers.extend([
                "Data Analyst",
                "Business Analyst",
                "BI Analyst"
            ])

            recommended_skills.extend([
                "Advanced Excel",
                "SQL",
                "Power BI",
                "Python",
                "Statistics"
            ])

        if (
            "Finance" in interests
            or "Accounting" in skills
        ):

            recommended_careers.extend([
                "Financial Analyst",
                "Accounts Analyst",
                "Investment Analyst"
            ])

            recommended_skills.extend([
                "Financial Modelling",
                "Advanced Excel",
                "Financial Analysis",
                "SQL"
            ])

        if (
            "Marketing" in interests
            or "Marketing" in skills
        ):

            recommended_careers.extend([
                "Digital Marketing Analyst",
                "Marketing Analyst",
                "Brand Executive"
            ])

            recommended_skills.extend([
                "Digital Marketing",
                "SEO",
                "Google Analytics",
                "Content Marketing"
            ])

        if (
            "Human Resources" in interests
            or "Leadership" in skills
        ):

            recommended_careers.extend([
                "HR Analyst",
                "HR Executive",
                "Talent Acquisition Specialist"
            ])

            recommended_skills.extend([
                "HR Analytics",
                "Excel",
                "Communication",
                "Recruitment"
            ])

        if (
            "Technology" in interests
            or "BCA" == degree
            or "B.Tech" == degree
        ):

            recommended_careers.extend([
                "Software Developer",
                "Technology Analyst",
                "Product Analyst"
            ])

            recommended_skills.extend([
                "Python",
                "SQL",
                "Git",
                "Problem Solving"
            ])

        if "Business" in interests:

            recommended_careers.extend([
                "Business Analyst",
                "Management Consultant"
            ])

            recommended_skills.extend([
                "Business Analysis",
                "Excel",
                "Power BI",
                "Communication"
            ])

        if "Entrepreneurship" in interests:

            recommended_careers.extend([
                "Entrepreneur",
                "Startup Founder",
                "Business Development Executive"
            ])

            recommended_skills.extend([
                "Business Planning",
                "Financial Management",
                "Marketing",
                "Leadership"
            ])

        # -------------------------------------------------
        # DEFAULT RECOMMENDATIONS
        # -------------------------------------------------

        if not recommended_careers:

            recommended_careers = [
                "Business Analyst",
                "Data Analyst",
                "Management Trainee"
            ]

        if not recommended_skills:

            recommended_skills = [
                "Excel",
                "Communication",
                "SQL",
                "Power BI",
                "Problem Solving"
            ]

        # -------------------------------------------------
        # REMOVE DUPLICATES
        # -------------------------------------------------

        recommended_careers = list(
            dict.fromkeys(recommended_careers)
        )

        recommended_skills = list(
            dict.fromkeys(recommended_skills)
        )

        # -------------------------------------------------
        # DISPLAY PROFILE
        # -------------------------------------------------

        st.divider()

        st.subheader("👤 Student Profile")

        st.write(
            f"**Education:** {degree}"
        )

        st.write(
            f"**Career Goal:** {career_goal}"
        )

        st.write(
            f"**Interests:** "
            f"{', '.join(interests) if interests else 'Not specified'}"
        )

        st.write(
            f"**Current Skills:** "
            f"{', '.join(skills) if skills else 'Not specified'}"
        )

        st.divider()

        # -------------------------------------------------
        # CAREER RECOMMENDATIONS
        # -------------------------------------------------

        st.subheader("🎯 Recommended Career Paths")

        for career in recommended_careers[:5]:

            st.success(
                f"💼 {career}"
            )

        st.divider()

        # -------------------------------------------------
        # SKILL RECOMMENDATIONS
        # -------------------------------------------------

        st.subheader("🛠️ Recommended Skills")

        skill_columns = st.columns(3)

        for index, skill in enumerate(
            recommended_skills[:9]
        ):

            with skill_columns[index % 3]:

                st.info(
                    f"📚 {skill}"
                )

        st.divider()

        # -------------------------------------------------
        # COURSE / CERTIFICATION
        # -------------------------------------------------

        st.subheader(
            "🎓 Suggested Learning Areas"
        )

        st.markdown("""
- Advanced Excel
- SQL
- Power BI
- Python
- Communication & Presentation
- Industry-specific certifications
- Internship / project experience
        """)

        st.warning(
            "⚠️ These recommendations are generated by "
            "the project's rule-based recommendation engine "
            "and should be treated as guidance."
        )

# =========================================================
# VALIDATE IDEA PAGE
# =========================================================

elif page == "🚀 Validate Idea":

    st.header("💡 Validate Your Startup Idea")

    idea = st.text_input(
        "Enter your startup idea",
        placeholder=(
            "AI-powered career and skill recommendation platform"
        )
    )

    target = st.text_input(
        "Who is your target customer?",
        placeholder="College students"
    )

    st.divider()

    if st.button(
        "🚀 Validate Idea",
        use_container_width=True
    ):

        if idea and target:

            st.success(
                "✅ Startup idea analyzed successfully!"
            )

            st.header("📊 Validation Results")

            st.write(
                f"**Startup Idea:** {idea}"
            )

            st.write(
                f"**Target Customer:** {target}"
            )

            st.divider()

            # -------------------------------------------------
            # SCORE CARDS
            # -------------------------------------------------

            col1, col2, col3, col4 = st.columns(4)

            with col1:

                st.metric(
                    "📈 Market Demand",
                    f"{market_score}/100"
                )

            with col2:

                st.metric(
                    "👥 Customer Demand",
                    f"{customer_score:.0f}/100"
                )

            with col3:

                st.metric(
                    "🏢 Competition",
                    f"{competition_score}/100"
                )

            with col4:

                st.metric(
                    "💰 Financial Feasibility",
                    f"{financial_score}/100"
                )

            st.divider()

            # -------------------------------------------------
            # VALIDATION CHART
            # -------------------------------------------------

            st.subheader(
                "📊 Validation Score Analysis"
            )

            scores = {
                "Market Demand": market_score,
                "Customer Demand": customer_score,
                "Competition": competition_score,
                "Financial Feasibility": financial_score
            }

            fig_validation = go.Figure(
                data=[
                    go.Bar(
                        x=list(scores.keys()),
                        y=list(scores.values()),
                        text=[
                            f"{value:.0f}"
                            for value in scores.values()
                        ],
                        textposition="auto"
                    )
                ]
            )

            fig_validation.update_layout(
                title="Startup Validation Factors",
                yaxis=dict(
                    range=[0, 100],
                    title="Score"
                ),
                xaxis_title="Validation Factor",
                height=450
            )

            st.plotly_chart(
                fig_validation,
                use_container_width=True
            )

            st.divider()

            # -------------------------------------------------
            # OVERALL SCORE
            # -------------------------------------------------

            st.subheader(
                "🎯 Overall Validation Score"
            )

            st.metric(
                "Validation Score",
                f"{final_score:.1f}/100"
            )

            st.progress(
                min(final_score / 100, 1.0)
            )

            if final_score >= 75:

                st.success(
                    "🟢 Promising Potential"
                )

            elif final_score >= 50:

                st.warning(
                    "🟡 Moderate Potential"
                )

            else:

                st.error(
                    "🔴 Low Potential"
                )

            st.divider()

            # -------------------------------------------------
            # STRENGTHS
            # -------------------------------------------------

            st.header(
                "💪 Key Strengths"
            )

            st.markdown("""
- Student interest in AI-based career guidance
- Personalized career recommendations
- Skill development recommendations
- Large potential student market
- Affordable premium pricing model
            """)

            st.divider()

            # -------------------------------------------------
            # RISKS
            # -------------------------------------------------

            st.header(
                "⚠️ Potential Risks"
            )

            st.markdown("""
- Existing career guidance platforms
- AI recommendations require reliable data
- Students may have concerns about AI accuracy
- Job-market information needs regular updating
- Customer acquisition may require strong marketing
            """)

            st.divider()

            # -------------------------------------------------
            # IMPROVEMENTS
            # -------------------------------------------------

            st.header(
                "💡 Suggested Improvements"
            )

            st.markdown("""
1. Add expert and mentor validation.
2. Add course and certification recommendations.
3. Add internship and job recommendations.
4. Integrate updated job-market data.
5. Improve AI personalization.
6. Add student progress tracking.
7. Develop a chatbot-based career assistant.
            """)

            st.divider()

            # -------------------------------------------------
            # RESEARCH BASIS
            # -------------------------------------------------

            st.header(
                "📚 Research Basis"
            )

            st.write("""
The validation framework combines:

1. Google Trends market research
2. Primary research from 20 students
3. Competitor analysis
4. Financial feasibility assumptions
5. TAM / SAM / SOM market sizing
6. AI-based career recommendation concept
            """)

            st.info(
                "⚠️ The validation score is a project-based "
                "analytical indicator and does not guarantee "
                "startup success."
            )

        else:

            st.warning(
                "⚠️ Please enter both the startup idea "
                "and target customer."
            )

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "AI Career & Skill Recommendation Platform | "
    "Entrepreneurship Project"
)