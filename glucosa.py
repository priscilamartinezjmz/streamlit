import streamlit as st

st.title("Checador de glucosa")
st.write("Hola, parece que fuiste a revisar tus niveles de glucosa...")

glucosa=st.number_input("Cual fue el valor de tu glucosa en mg/dL?", min_value=0, step=1)

if(glucosa<70):
    prediagnostico="Hipoglucemia"
    nivel="Tu valor parece estar un poco mas bajo de lo normal"
    recomendacion="Intenta consumir mas carbohidratos para evitar desmayos!"

elif(70<= glucosa <=100):
    prediagnostico="Normal/saludable"
    nivel="Tu valor parece estar dentro del rango normal"
    recomendacion="Mantente asi de saludable, felicidades!"

elif(101<= glucosa <=125):
    prediagnostico="Prediabetes"
    nivel="Tu valor esta un poco mas elevado de lo normal"
    recomendacion="Intenta modificar tu estilo de vida para mantenerte sano" 

else:
    prediagnostico="Diabetes"
    nivel="Tu valor esta muy elevado"
    recomendacion="Corre al hospital por atencion medica"

st.subheader("Resultados listos:")

st.write("Pre-diagnostico:", prediagnostico)
st.write(nivel)
st.warning(recomendacion)

st.info("Espero haber sido de ayuda, no olvides acudir con tu medico para un diagnostico mas preciso!")
