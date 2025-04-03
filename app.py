import streamlit as st
import numpy as np
from joblib import load
import pandas as pd
df = pd.read_excel(r"C:\Users\acer\Downloads\real\dataset.xlsx")
# Carica il modello
model = load('model.joblib')

st.set_page_config(page_title="Stima Prezzo Casa")

st.title("Stima il Prezzo della Casa a Taipei")
st.markdown("Inserisci latitudine e longitudine per stimare il prezzo dell'abitazione al metro^2 in TWD.")

# Input utente
lat = st.number_input("Latitudine", format="%.6f")
lon = st.number_input("Longitudine", format="%.6f")

lat_min, lat_max = df["X5 latitude"].min(), df["X5 latitude"].max()
lon_min, lon_max = df["X6 longitude"].min(), df["X6 longitude"].max()
if st.button("Stima Prezzo"):
    if lat < lat_min or lat > lat_max:
        st.error(f"Latitudine fuori range! ({lat_min:.2f} - {lat_max:.2f})")

    elif lon < lon_min or lon > lon_max:
        st.error(f"Longitudine fuori range! ({lon_min:.2f} - {lon_max:.2f})")

    else:
        try:
            X = np.array([[lat, lon]])
            prediction = model.predict(X)[0]

            if prediction < 0:
                st.warning("⚠️ Il modello ha restituito un valore negativo. Verifica i dati.")
            else:
                st.success(f"Prezzo stimato: **{round(prediction, 2)} TWD**")
        except Exception as e:
            st.error(f"Errore durante la previsione: {e}")
