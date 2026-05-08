import streamlit as st
import base64
from PIL import Image
import requests
import json
import time

# إعدادات الصفحة الفخمة
st.set_page_config(page_title="منصة العُمران للذكاء الاصطناعي", layout="wide", initial_sidebar_state="collapsed")

# حيلة لإظهار النص الأسود على خلفية سوداء (سنستخدم CSS لجعل النص الأسود يظهر بظل خفيف)
def load_css():
    st.markdown("""
        <style>
        /* إخفاء القوائم الافتراضية */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* تصميم الشاشة السوداء الأولى */
        .black-intro-screen {
            background-color: black;
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 9999;
            animation: fadeOut 3s forwards 2s; /* يختفي بعد 2 ثوانٍ */
        }
        
        @keyframes fadeOut {
            to { opacity: 0; visibility: hidden; }
        }
        
        .intro-content {
            text-align: center;
        }
        
        /* اسم العمران أسود بظل أبيض ليظهر */
        .intro-text {
            color: black;
            font-size: 80px;
            font-weight: bold;
            font-family: 'Arial Black', sans-serif;
            text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.5); /* ظل خفيف ليظهر */
            margin-bottom: -10px;
        }
        
        /* تنسيق العلم السوري */
        .intro-flag {
            font-size: 50px;
            margin: 20px 0;
        }
        
        .intro-slogan {
            color: white;
            font-size: 24px;
            font-weight: light;
            margin-top: 10px;
        }

        /* تنسيق المحتوى الفخم الداخلي */
        .main-container {
            margin-top: -100px; /* للتعويض عن الهيدر المخفي */
        }
        
        .fakhma-card {
            background-color: #f0f2f6;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }
        
        .title-container {
            text-align: center;
            margin-bottom: 40px;
        }
        
        .main-title {
            color: #15462c; /* أخضر عمراني فخم */
            font-size: 42px;
            font-weight: bold;
        }
        
        .analysis-result {
            background-color: #e8f5e9;
            border-left: 10px solid #2e7d32;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
        }
        
        .diagnosis-disease {
            color: #d32f2f;
            font-size: 28px;
            font-weight: bold;
        }
        
        </style>
    """, unsafe_check_html=True)

load_css()

# --- الشاشة السوداء الأولى ---
# نستخدم حيلة لإظهارها مرة واحدة عند التحميل
if 'intro_shown' not in st.session_state:
    st.session_state.intro_shown = False

if not st.session_state.intro_shown:
    st.markdown("""
        <div class="black-intro-screen">
            <div class="intro-content">
                <div class="intro-text">العُمران</div>
                <div class="intro-flag">🟢⚪⚫ ❤️ 🇸🇾</div> /* العلم ذو الثلاث نجوم والقلب */
                <div class="intro-slogan">معاً لبناء وطن واحد</div>
            </div>
        </div>
    """, unsafe_check_html=True)
    st.session_state.intro_shown = True
    # نستخدم تايمر لجعل الشاشة تظهر قليلاً قبل الاختفاء
    time.sleep(2.5) 
    st.rerun() # إعادة تحميل الصفحة لإظهار المحتوى الداخلي

# --- المحتوى الداخلي الفخم ---
st.markdown('<div class="main-container">', unsafe_check_html=True)

# الهيدر الفخم
st.markdown("""
    <div class="title-container">
        <h1 class="main-title">🌿 منصة العُمران للذكاء الاصطناعي الزراعي</h1>
        <p style="font-size: 18px; color: #555;">دكتور أحمد عمران، رؤيتك العلمية أصبحت حقيقة</p>
    </div>
""", unsafe_check_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('<div class="fakhma-card">', unsafe_check_html=True)
    st.subheader("🛠️ التشخيص بالذكاء الاصطناعي")
    st.write("ارفق صورة الورقة المصابة ليقوم المحرك الذكي بتحليلها بدقة:")
    
    # خانة رفع الصورة الأنيقة
    uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])
    
    st.write("---")
    analyser_button = st.button("بدء تحليل الصورة بدقة", use_container_width=True)
    st.markdown('</div>', unsafe_check_html=True)

# محاكاة لربط حقيقي (سنضع هذا في `with col2`)
with col2:
    if uploaded_file is not None and analyser_button:
        # عرض الصورة
        image = Image.open(uploaded_file)
        st.image(image, caption='الصورة التي يراها الذكاء الاصطناعي', use_column_width=True)
        
        with st.spinner("جاري المسح الضوئي وتحليل الصورة (دقيق)..."):
            # --- هذا هو كود الربط الفعلي بمحرك الذكاء الاصطناعي (API) ---
            # في الحقيقة، سنرسل الصورة إلى سيرفر مثل Gemini API أو TensorFlow Serving
            # حالياً، سنحاكي الرد لإظهار الفخامة والدقة
            time.sleep(3) # محاكاة للوقت الذي يستغرقه التحليل
            
            # محاكاة لبيانات حقيقية (دقيقة)
            result_disease = "بياض دقيقي (Powdery Mildew)"
            result_cause = "فطر Podosphaera xanthii"
            result_treatment = "الرش بالكبريت الميكروني (Sulfur) أو مبيد فطري تخصصي مثل توباس (Topas 100 EC)."

            st.markdown("""
                <div class="analysis-result">
                    <p style="font-size: 18px; color: #555; margin-bottom: 5px;">التحليل دقيق ✅</p>
                    <p class="diagnosis-disease">المرض المكتشف: {result_disease}</p>
                    <hr>
                    <p><b>العامل المسبب:</b> {result_cause}</p>
                    <p><b>الأدوية المقترحة للعلاج:</b> {result_treatment}</p>
                </div>
            """.format(result_disease=result_disease, result_cause=result_cause, result_treatment=result_treatment), unsafe_check_html=True)
            
            st.success("تم تحليل الصورة بدقة يا دكتور!")
            
    elif uploaded_file is not None and not analyser_button:
        st.warning("اضغط على زر 'بدء تحليل الصورة' لنتحقق من الإصابة.")

# الفوتر
st.write("---")
st.caption("تم التطوير بواسطة: د. أحمد علي عمران | معاً لبناء وطن واحد")
st.markdown('</div>', unsafe_check_html=True)
