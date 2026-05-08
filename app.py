import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="المنصة الزراعية - الساحل السوري", layout="centered")

# الواجهة الرئيسية
st.markdown("<h1 style='text-align: center; color: #2E7D32;'>منصة العُمرانية للخدمات الزراعية</h1>", unsafe_check_html=True)
st.markdown("<p style='text-align: center; font-weight: bold;'>بوابة الخدمات المتكاملة لمزارعي الساحل السوري</p>", unsafe_check_html=True)
st.write("---")

# نظام التشخيص
st.subheader("🛠️ نظام التشخيص السريع")
col1, col2 = st.columns(2)

with col1:
    crop_type = st.selectbox("نوع المحصول المحمي أو المكشوف:", ["بندورة", "باذنجان", "فليفلة", "حمضيات", "تبغ"])
with col2:
    observation = st.selectbox("العرض الملاحظ:", ["اصفرار أوراق", "ذبول مفاجئ", "بقع دقيقية", "تعفن جذور", "أعراض حشرية"])

if st.button("تحليل البيانات الزراعية"):
    st.write("---")
    if crop_type == "بندورة" and observation == "بقع دقيقية":
        st.success("التحليل التقني: الإصابة (بياض دقيقي).")
        st.info("الإجراء المقترح: الرش بالكبريت الميكروني أو مبيد فطري تخصصي.")
    else:
        st.warning("يرجى مراجعة قاعدة البيانات المركزية للمزيد من التفاصيل.")

st.write("---")
st.markdown("<p style='text-align: center; font-size: 0.8em;'>تم التطوير بواسطة: د. أحمد علي عمران</p>", unsafe_check_html=True)
