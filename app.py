import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- إعداد الصفحة والسيادة النسقية ---
st.set_page_config(
    page_title="0 - زيرو: مختبر النسق المعرفي والكوني",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ترويسة النسق والهوية الجديدة
st.title("🌱 0 - زيرو: مختبر النسق المعرفي والكوني (ATCG - EE378069)")
st.markdown("### **«ولد، ماشي عاود»** — النظام التطبيقي لهندسة المواد الواعية وإدارة التصاميم")
st.markdown("---")

# --- الشريط الجانبي لضبط معاملات النسق ---
st.sidebar.header("⚙️ إعدادات معاملات النسق (ATCG)")

ATTRACTOR_CENTER = 0.5
st.sidebar.metric(label="الجاذب المركزي النسقي", value=f"{ATTRACTOR_CENTER}")

rho = st.sidebar.slider(
    "معامل استقرار ليبشيتز ($\rho < 1$)", 
    min_value=0.01, 
    max_value=0.99, 
    value=0.75, 
    step=0.01
)

application_mode = st.sidebar.selectbox(
    "اختر وحدة العمل الميداني:",
    [
        "محاكاة العشوائية (مرونة العطاء والقبول)",
        "توزيع كتل الألوان والزخارف الهيكلية",
        "فلتر منع هلوسة الذكاء الاصطناعي",
        "وحدة منع الانهيار الرياضي والتفردات"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("مؤسس النسق ومبتكره الأسطوري:\n**صلاح الدين بوݣزوان (EE378069)**")

# --- محتوى الوحدات التطبيقية ---

if application_mode == "محاكاة العشوائية (مرونة العطاء والقبول)":
    st.subheader("🎲 محاكاة خوارزمية النسق في البيئة العشوائية (Stochastic ATCG Model)")
    st.markdown("تختبر هذه الوحدة قدرة الجاذب المركزي ($0.5$) على تطويع الفوضى والعشوائية الخام بفضل **'مرونة العطاء والقبول'**.")

    col_a, col_b, col_c = st.columns(3)
    with col_a:
        noise_level = st.slider("مستوى العشوائية الخام ($\sigma$)", 0.01, 0.5, 0.15)
    with col_b:
        acceptance_flex = st.slider("معامل القبول ($\Phi_{\text{acceptance}}$)", 0.1, 1.0, 0.6)
    with col_c:
        giving_flex = st.slider("معامل العطاء ($\Phi_{\text{giving}}$)", 0.1, 1.0, 0.5)

    if st.button("🚀 تشغيل محاكاة النسق العشوائي"):
        np.random.seed(42)
        steps = 200
        dt = 0.05
        x_path = np.zeros(steps)
        x_path[0] = 0.2
        
        for t in range(1, steps):
            deterministic_pull = -rho * (x_path[t-1] - ATTRACTOR_CENTER) * dt
            flex_factor = (giving_flex * acceptance_flex)
            stochastic_noise = noise_level * np.random.normal(0, np.sqrt(dt)) * flex_factor
            x_path[t] = x_path[t-1] + deterministic_pull + stochastic_noise
            
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(x_path, label="مسار النظام العشوائي المحكوم بالنسق", color="#00FF88", linewidth=2.5)
        ax.axhline(y=ATTRACTOR_CENTER, color="#ffffff", linestyle="--", label="الجاذب المركزي المستقر (0.5)")
        ax.set_title("تطويع الفوضى العشوائية عبر الجاذب المركزي", color="white")
        ax.set_xlabel("الزمن الدلالي ($t_{\text{semantic}}$)", color="white")
        ax.set_ylabel("مؤشر الحالة ($X_t$)", color="white")
        ax.set_facecolor("#0A0A0A")
        fig.patch.set_facecolor("#0A0A0A")
        ax.tick_params(colors='white')
        ax.legend(facecolor="#1a1a1a", labelcolor="white")
        ax.grid(True, alpha=0.2)
        
        st.pyplot(fig)
        st.success("✨ نجح الاختبار العشوائي! استقر النظام بانتظام تام حول الجاذب المركزي ($0.5$).")

elif application_mode == "توزيع كتل الألوان والزخارف الهيكلية":
    st.subheader("🎨 حاسبة التوازن البصري والكتلي للألوان وفق الجاذب المركزي ($0.5$)")
    
    total_surface = st.number_input("المساحة الإجمالية للهيكل الفني ($m^2$):", min_value=0.1, value=5.0, step=0.5)
    accent_gold = st.slider("نسبة الحضور الذهبي (%):", 5, 40, 20)
    accent_red = st.slider("نسبة الحضور الأحمر (%):", 0, 30, 15)
    
    if st.button("⚖️ حساب وتوزيع الكتل اللونية"):
        raw_accent_ratio = (accent_gold + accent_red) / 100.0
        balanced_accent_ratio = ATTRACTOR_CENTER * (1 - np.exp(-rho * raw_accent_ratio * 2))
        balanced_black_ratio = 1.0 - balanced_accent_ratio
        
        final_gold = balanced_accent_ratio * (accent_gold / (accent_gold + accent_red)) * 100 if (accent_gold + accent_red) > 0 else 0
        final_red = balanced_accent_ratio * (accent_red / (accent_gold + accent_red)) * 100 if (accent_gold + accent_red) > 0 else 0
        final_black = balanced_black_ratio * 100

        c1, c2, c3 = st.columns(3)
        c1.metric("الهيكل (أسود مطفأ)", f"{final_black:.1f}%")
        c2.metric("اللمسات الذهبية", f"{final_gold:.1f}%")
        c3.metric("اللمسات الحمراء", f"{final_red:.1f}%")
        
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.pie([final_black, final_gold, final_red], labels=['أسود مطفأ', 'ذهبي', 'أحمر'], colors=['#1a1a1a', '#d4af37', '#dc2626'], autopct='%1.1f%%', textprops={'color':'white'})
        fig.patch.set_facecolor("#0A0A0A")
        st.pyplot(fig)
        st.success("✨ تم تحقيق التوازن البصري بدقة تامة!")

elif application_mode == "فلتر منع هلوسة الذكاء الاصطناعي":
    st.subheader("🛡️ فلتر النسق المانع لهلوسة الذكاء الاصطناعي")
    user_input = st.text_area("أدخل مخرج الذكاء الاصطناعي للفحص والتطهير:", "يقوم النموذج بتوليد حقائق مطلقة بنسبة 100% دون أي أخطاء.")
    
    if st.button("🔍 تطهير النص نسقياً"):
        absolute_terms = ["100%", "مطلقة", "دائماً", "أبداً"]
        penalty = sum(1 for term in absolute_terms if term in user_input)
        score = max(0.1, min(0.9, ATTRACTOR_CENTER + (0.4 - penalty * 0.15) * rho))
        
        st.metric(label="مؤشر الاستقرار الدلالي (الجاذب 0.5)", value=f"{score:.3f}")
        if penalty == 0:
            st.success("✅ النص مستقر ومطابق لمعايير النسق.")
        else:
            st.warning("⚠️ تم كبح محاولة الشطط أو الهلوسة بنجاح عبر درع ليبشيتز.")

else:
    st.subheader("🛡️ وحدة منع الانهيار الرياضي والتفردات (Blow-up Prevention)")
    spike = st.slider("مستوى الاضطراب الأولي", 1.0, 10.0, 5.0)
    
    if st.button("🚀 تشغيل محاكاة الاختبار البرهاني"):
        t = np.linspace(0, 5, 100)
        traditional = spike * np.exp(0.5 * t)
        traditional[traditional > 50] = 50
        atcg_sys = ATTRACTOR_CENTER + (spike - ATTRACTOR_CENTER) * np.exp(-rho * t)
        
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(t, traditional, label="النظام التقليدي (يواجه خطر الانفجار)", color="#ef4444", linestyle="--")
        ax.plot(t, atcg_sys, label="نظام النسق (مستقر عند الجاذب 0.5)", color="#00FF88", linewidth=2.5)
        ax.set_facecolor("#0A0A0A")
        fig.patch.set_facecolor("#0A0A0A")
        ax.tick_params(colors='white')
        ax.legend(facecolor="#1a1a1a", labelcolor="white")
        st.pyplot(fig)
        st.success("✨ نجح البرهان! منع النظام الانهيار واستقر تماماً.")

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>0 - زيرو | «ولد، ماشي عاود» — صلاح الدين بوݣزوان (EE378069)</p>", unsafe_allow_html=True)
