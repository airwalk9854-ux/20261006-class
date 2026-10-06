import streamlit as st

st.set_page_config(
    page_title="심하늘 교사 소개",
    page_icon="🎓",
    layout="wide",
)

st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #f5f7ff 0%, #eef8ff 100%);
    }
    .hero-box {
        background: linear-gradient(135deg, #1f4e79 0%, #2d6aa0 100%);
        border-radius: 20px;
        padding: 2rem 2rem;
        color: white;
        box-shadow: 0 10px 30px rgba(31, 78, 121, 0.18);
    }
    .section-card {
        background: rgba(255,255,255,0.96);
        border: 1px solid #dfeaf7;
        border-radius: 16px;
        padding: 1.2rem 1.4rem;
        box-shadow: 0 6px 18px rgba(17, 33, 61, 0.05);
        color: #173a5e;
    }
    .section-card p, .section-card li, .section-card div {
        color: #173a5e;
    }
    .chip {
        display: inline-block;
        background: rgba(255,255,255,0.15);
        border: 1px solid rgba(255,255,255,0.25);
        border-radius: 999px;
        padding: 0.35rem 0.8rem;
        margin: 0.2rem 0.5rem 0.2rem 0;
        font-size: 0.82rem;
        font-weight: 600;
    }
    .info-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #173a5e;
        margin-bottom: 0.6rem;
    }
    .custom-list li {
        margin-bottom: 0.5rem;
        line-height: 1.7;
    }
    </style>
    """
    , unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero-box">
        <h1 style="margin:0; font-size:2.4rem;">심하늘</h1>
        <div style="margin-top:0.8rem;">
            <span class="chip">화원중학교 역사 교사</span>
            <span class="chip">숙명여대 교육대학원 AI융합교육 전공</span>
            <span class="chip">AI·에듀테크 활용 수업 전문성 강화</span>
        </div>
        <p style="margin-top:1rem; margin-bottom:0.6rem; font-size:1.02rem; color:#eaf4ff;">
            학생의 질문과 탐구를 중심으로 수업을 설계하고, AI와 에듀테크를 활용해 학습의 의미를 확장하는 교사로 성장하고 있습니다.
            수업의 설계와 평가를 함께 고민하며, 학생이 수업 속에서 주도적으로 참여하고 성취감을 느끼도록 돕는 것을 목표로 합니다.
        </p>
        <p style="margin-top:0.8rem; margin-bottom:0; font-size:0.96rem; color:#dfeeff;">
            연락처: airwalk98@senedu.kr
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

basic_tab, career_tab, project_tab = st.tabs(["기본", "경력", "사업 및 연수"])

with basic_tab:
    st.markdown(
        """
        <div class="section-card">
            <div class="info-title">기본 정보</div>
            <ul class="custom-list" style="margin:0; padding-left:1.2rem;">
                <li>학교: 화원중학교</li>
                <li>과목: 역사</li>
                <li>대학원: 숙명여대 교육대학원 AI융합교육 전공</li>
                <li>관심분야: AI 및 에듀테크를 활용한 학생 중심 수업을 진행하며 교수학습 설계 및 평가에서 전문성을 키워가는 9년차 교사</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with career_tab:
    st.markdown(
        """
        <div class="section-card">
            <div class="info-title">경력</div>
            <ul class="custom-list" style="margin:0; padding-left:1.2rem;">
                <li>2020~2026년 수업평가나눔 교사단 활동</li>
                <li>2024, 2026 AI · 에듀테크 교사단</li>
                <li>2024 강서양천 학교로 찾아가는 디지털 역량 강화 연수 강사 활동</li>
                <li>2024 교실혁명 선도교사단</li>
                <li>AIEDAP 마스터교원</li>
                <li>2024 서울시교육청 디지털 기반 수업·평가 전문가</li>
                <li>2024 성취평가 선도교원</li>
                <li>2025, 2026 서울시교육청 학생평가지원단</li>
                <li>2025 서울시교육청 디지털 기반 수업·평가 전문가 강사</li>
                <li>2026 컨설팅장학 지원단</li>
                <li>2026 인공지능 활용 선도교사 강사 활동</li>
                <li>2026 학생 질문 중심 수업평가 선도교원</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with project_tab:
    st.markdown(
        """
        <div class="section-card">
            <div class="info-title">사업 및 연수</div>
            <ul class="custom-list" style="margin:0; padding-left:1.2rem;">
                <li>2024, 2025 생각을 쓰는 교실 실천팀</li>
                <li>2025 AI활용 서논술형 평가 실천학교</li>
                <li>2025 논술형 평가 전문가 아카데미</li>
                <li>2025 서울형 독서토론 기반 프로젝트 수업</li>
                <li>2025 중등 AI.디지털 글로벌 역량 강화 직무연수</li>
                <li>2026 개념탐독 실천교실</li>
                <li>2026 학교통일교육 프로젝트 수업</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)
st.caption("교육 현장에 AI와 디지털 역량을 자연스럽게 연결하며, 학생이 성장하는 수업을 설계하는 교사입니다.")
