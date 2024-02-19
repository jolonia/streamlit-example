import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
#SAMPLE APP DASHBOARD SCRUMBUMS
"""


st.set_page_config(layout="wide")

st.title("VS Santa Monica and totals")

col1, col2, col3 = st.columns([0.3, 0.3, 0.4])

custom_css = """
<style>
div[data-baseweb="input"] input[type="number"] {
    width: 70px;  /* minimize icons*/
}
</style>
"""

# CSS apply z style
st.markdown(custom_css, unsafe_allow_html=True)

with col1:
    gal, tr = st.columns([0.5, 0.5])
    gal_value = gal.number_input("BELMONT", min_value=0, max_value=10, step=1)
    tr_value = tr.number_input("ST. MONICA", min_value=0, max_value=10, step=1)
    text = ''' --- '''
    st.markdown(text)
    hs5, as5 = st.columns([0.5, 0.5])
    hir_value = hs5.number_input("Aztecs", min_value=0, max_value=10, step=1)
    erm_value = as5.number_input("ST. MONICA", min_value=0, max_value=10, step=1)
    st.markdown(text)
    hs8, as8 = st.columns([0.5, 0.5])
    rom_value = hs8.number_input("EAGLE ROCK", min_value=0, max_value=10, step=1)
    swi_value = as8.number_input("ST. MONICA", min_value=0, max_value=10, step=1)
    st.markdown(text)
    hs9, as9 = st.columns([0.5, 0.5])
    ceb_value = hs9.number_input("LIFE", min_value=0, max_value=10, step=1)
    hol_value = as9.number_input("🇳🇱 Hollanda", min_value=0, max_value=10, step=1)

with col2:
    data = {
        'Rnk': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
        'Grp': ['J', 'B', 'A', 'F', 'C', 'G', 'D', 'H', 'E', 'I',
                'F', 'A', 'J', 'B', 'G', 'D', 'C', 'H', 'E', 'I', 'D'],
        'Team': ['Portekiz', 'Fransa', 'İspanya', 'Belçika', 'İngiltere',
                 'Macaristan', 'Türkiye', 'Danimarka', 'Arnavutluk', 'Romanya',
                 'Avusturya', 'İskoçya', 'Slovenya', 'Slovakya', 'Çekya',
                 'Hollanda', 'İtalya', 'Sırbistan', 'Hırvatistan', 'İsviçre',
                 'Galler', ],
        'P': [24, 21, 21, 20, 20, 18, 16, 16, 15, 13,
              19, 17, 16, 16, 15, 15, 14, 14, 13, 11, 11],
        'Av.': [28, 26, 20, 18, 18, 9, 7, 4, 8, 4,
                10, 9, 5, 5, 6, 4, 7, 6, 8, 8, 0],
        'Siralama': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
    }

    ct = pd.DataFrame(data)
    # Yeni "Grp_Rnk" sütunu ekleyerek istenilen değerleri atayalım
    # ct['Siralama'] = pd.cut(ct['Rnk'], bins=[0, 10, 20, float('inf')], labels=[1, 2, 3], right=False).astype(int)

    # Türkiye
    if tr_value > gal_value:
        ct.loc[ct['Team'] == 'Türkiye', 'P'] += 3
    elif tr_value == gal_value:
        ct.loc[ct['Team'] == 'Türkiye', 'P'] += 1
    elif (tr_value < gal_value) & (erm_value < hir_value):
        ct.loc[ct['Team'] == 'Türkiye', 'Siralama'] = 2
        ct.loc[ct['Team'] == 'Hırvatistan', 'Siralama'] = 1
    else:
        ct.loc[ct['Team'] == 'Türkiye', 'P'] += 0
df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))
