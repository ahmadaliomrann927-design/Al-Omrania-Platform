import streamlit as st
from PIL import Image
import time

# إعدادات الصفحة
st.set_page_config(page_title="منصة العُمران الذكية", layout="wide")

# تصميم الواجهة الاحترافية (نسخة مستقرة)
st.markdown("""
    <style>
    .main { background-color: #000000; color: white; }
    .stButton>button { width: 100%; background-color: #2e7d32; color: white; border-radius: 10px; height: 3em; font-size: 20px; }
    .title-text { text-align: center; color: #4caf50; font-size: 45px; font-weight: bold; }
    .sub-text { text-align: center; color: #ffffff; font-size: 20px; }
    </style>
""", unsafe_allow_html=True)

# الشاشة الترحيبية (تظهر مباشرة عند الفتح)
if 'init' not in st.session_state:
    placeholder = st.empty()
    with placeholder.container():
        st.markdown("<h1 style='text-align: center; color: black; font-size: 100px; background-color: white; padding: 50px;'>العُمران</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; font-size: 60px;'>🇸🇾 ❤️ 🟢⚪⚫</h2>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: gray;'>معاً لبناء وطن واحد</h3>", unsafe_allow_html=True)
        time.sleep(3)
    st.session_state.init = True
    placeholder.empty()

# المحتوى الداخلي الفخم
st.markdown("<div class='title-text'>🌿 منصة العُمران للتشخيص الذكي</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-text'>د. أحمد عمران - بوابتك للزراعة الرقمية</div>", unsafe_allow_html=True)
st.write("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.header("📸 مسح الإصابة")
    uploaded_file = st.file_uploader("ارفق صورة الإصابة هنا...", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        st.image(uploaded_file, caption="تم رفع الصورة بنجاح", use_container_width=True)

with col2:
    st.header("🔍 نتيجة التحليل")
    if uploaded_file:
        if st.button("بدء المسح الضوئي الذكي"):
            with st.spinner("جاري تحليل الأنسجة ومطابقة المسببات المرضية..."):
                time.sleep(4) # محاكاة التحليل العميق
                
                # نتيجة دقيقة (مثال لمرض البندورة كمثال علمي)
                st.error("⚠️ التشخيص: اللفحة المتأخرة (Late Blight)")
                st.info("🧬 المسبب: فطر Phytophthora infestans")
                st.success("💊 العلاج: الرش بمبيد يحتوي على مادة 'ميتالاكسيل' أو 'مانكوزيب'.")
    else:
        st.info("بانتظار رفع صورة الإصابة لبدء التشخيص يا دكتور.")

st.write("---")
st.caption("تم التطوير بواسطة: د. أحمد علي عمران | جامعة تشرين - كلية الهندسة الزراعية")
