import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import datetime
from requests import get 
from PIL import Image
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.support.ui import WebDriverWait, Select  
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

image = Image.open('Data/logo.jpg')

col1, col2 = st.columns([0.5,0.9])
with col1:
   st.image(image,width=100)
col3, col4, col5 =st.columns([0.5,0.1,0.1])
with col3:
    box_date = str(datetime.datetime.now().strftime("%d %B %Y"))
st.write(f"Dernier mis à jour: \n {box_date}")

st.markdown("""
    <style>
    .stApp {
        background-color: #e0f7fa;  /* Arrière-plan en bleu clair */
    }
    .stButton>button {
        background-color: #0078ff;  /* Bouton en bleu */
        color: white;
    }
    </style>""",
    unsafe_allow_html=True
)

st.title("Application de scrapping de données sur Expat Dakar")
st.subheader("Auteur : Hamady Ngansou SABALY")
st.write(
    ("Cette application permet de collecter des données de voitures, de motos-scooters et d'équipements-pièces sur Expat Dakar par la méthode de Sélénium ou par l'outil web scrapper.")
)
st.markdown("""
***Data source:*** [Expat-Dakar](https://www.expat-dakar.com/).
""")
st.title("Scraping des Données avec la méthode Sélénium")
url = st.text_input("Entrez l'URL à scrapper")
url1 = 'https://www.expat-dakar.com/voitures'
url2 = 'https://www.expat-dakar.com/mostos-scooters'
url3 = 'https://www.expat-dakar.com/equipements-pieces'

if st.button("Télécharger"):
    if url == url1:
        from requests import get 
        from selenium import webdriver 
        from selenium.webdriver.chrome.service import Service 
        from selenium.webdriver.support.ui import WebDriverWait, Select  
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By 
        import pandas as pd
        
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        
        driver.get('https://www.expat-dakar.com/voitures')
        containers = driver.find_elements(By.CSS_SELECTOR, "[class= 'listing-card__content 1']")
        
        container = containers[0]
        gen_info = container.find_element(By.CSS_SELECTOR, 'div.listing-card__header__tags')
        etat = gen_info.find_element(By.CSS_SELECTOR, 'span').text
        marque = container.find_element(By.CSS_SELECTOR, "span.listing-card__header__tags__item--make").text
        annee = container.find_element(By.CSS_SELECTOR, "span.listing-card__header__tags__item--buildyear").text
        boite_vitesse = container.find_element(By.CSS_SELECTOR, "span.listing-card__header__tags__item--transmission").text
        adresse = container .find_element(By.CSS_SELECTOR, "div.listing-card__header__location").text
        prix_F_Cfa = container.find_element(By.CSS_SELECTOR, "div.listing-card__info-bar__price").text.replace("\u202f","").replace("F Cfa","").strip()
        image_element = driver.find_element(By.CLASS_NAME, 'listing-card__image__inner-container')
        image_lien = image_element.find_element(By.TAG_NAME, "img").get_attribute("src")

        data = []
        for container in containers : 
            try:
                container = containers[0]
                gen_info = container.find_element(By.CSS_SELECTOR, 'div.listing-card__header__tags')
                etat = gen_info.find_element(By.CSS_SELECTOR, 'span').text
                marque = container.find_element(By.CSS_SELECTOR, "span.listing-card__header__tags__item--make").text
                annee = container.find_element(By.CSS_SELECTOR, "span.listing-card__header__tags__item--buildyear").text
                boite_vitesse = container.find_element(By.CSS_SELECTOR, "span.listing-card__header__tags__item--transmission").text
                adresse = container .find_element(By.CSS_SELECTOR, "div.listing-card__header__location").text
                prix_F_Cfa = container.find_element(By.CSS_SELECTOR, "div.listing-card__info-bar__price").text.replace("\u202f","").replace("F Cfa","").strip()
                image_element = driver.find_element(By.CLASS_NAME, 'listing-card__image__inner-container')
                image_lien = image_element.find_element(By.TAG_NAME, "img").get_attribute("src")

                dic = {'etat': etat,
                        'marque': marque,
                        'annee': annee,
                        'boite_vitesse': boite_vitesse,
                        'adresse': adresse,
                        'prix_F_Cfa': prix_F_Cfa,
                        'image_url': image_lien}
                data.append(dic)
            except:
                pass

        df = pd.DataFrame(data)
        for p in range(1,2): 
            driver.get(f'https://www.expat-dakar.com/voitures?page=1&page={p}')
            containers = driver.find_elements(By.CSS_SELECTOR, "[class= 'listing-card__content 1']")
            data = []
            for container in containers : 
                try:
                    container = containers[0]
                    gen_info = container.find_element(By.CSS_SELECTOR, 'div.listing-card__header__tags')
                    etat = gen_info.find_element(By.CSS_SELECTOR, 'span').text
                    marque = container.find_element(By.CSS_SELECTOR, "span.listing-card__header__tags__item--make").text
                    annee = container.find_element(By.CSS_SELECTOR, "span.listing-card__header__tags__item--buildyear").text
                    boite_vitesse = container.find_element(By.CSS_SELECTOR, "span.listing-card__header__tags__item--transmission").text
                    adresse = container .find_element(By.CSS_SELECTOR, "div.listing-card__header__location").text
                    prix_F_Cfa = container.find_element(By.CSS_SELECTOR, "div.listing-card__info-bar__price").text.replace("\u202f","").replace("F Cfa","").strip()
                    image_element = driver.find_element(By.CLASS_NAME, 'listing-card__image__inner-container')
                    image_lien = image_element.find_element(By.TAG_NAME, "img").get_attribute("src")

                    dic = {'etat': etat,
                        'marque': marque,
                        'annee': annee,
                        'boite_vitesse': boite_vitesse,
                        'adresse': adresse,
                        'prix_F_Cfa': prix_F_Cfa,
                        'image_url': image_lien}
                    data.append(dic)
                except:
                 pass

            DF = pd.DataFrame(data)
            df = pd.concat([df, DF], axis = 0).reset_index(drop=True)
            df.to_csv('Data/voitures.csv', index=False)
            
    elif url == url2:
        
        from requests import get 
        from selenium import webdriver 
        from selenium.webdriver.chrome.service import Service 
        from selenium.webdriver.support.ui import WebDriverWait, Select  
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By 
        import pandas as pd
        
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        
        driver.get('https://www.expat-dakar.com/motos-scooters')
        containers = driver.find_elements(By.CSS_SELECTOR, "[class= 'listing-card__content 1']")
        
        container = containers[0]
        gen_info =container.find_element(By.CSS_SELECTOR, 'div.listing-card__header__tags')
        etat = gen_info.find_element(By.CSS_SELECTOR, 'span').text
        marque = container.find_element(By.CSS_SELECTOR, "span.listing-card__header__tags__item--make").text
        annee = container.find_element(By.CSS_SELECTOR, "span.listing-card__header__tags__item--buildyear").text
        adresse = container .find_element(By.CSS_SELECTOR, "div.listing-card__header__location").text
        prix_F_Cfa = container.find_element(By.CSS_SELECTOR, "div.listing-card__info-bar__price").text.replace("\u202f","").replace("F Cfa","").strip()
        image_element = driver.find_element(By.CLASS_NAME, 'listing-card__image__inner-container')
        image_lien = image_element.find_element(By.TAG_NAME, "img").get_attribute("src")

        data = []
        for container in containers : 
            try:
                gen_info =container.find_element(By.CSS_SELECTOR, 'div.listing-card__header__tags')
                etat = gen_info.find_element(By.CSS_SELECTOR, 'span').text
                marque = container.find_element(By.CSS_SELECTOR, "span.listing-card__header__tags__item--make").text
                annee = container.find_element(By.CSS_SELECTOR, "span.listing-card__header__tags__item--buildyear").text
                adresse = container .find_element(By.CSS_SELECTOR, "div.listing-card__header__location").text
                prix_F_Cfa = container.find_element(By.CSS_SELECTOR, "div.listing-card__info-bar__price").text.replace("\u202f","").replace("F Cfa","").strip()
                image_element = driver.find_element(By.CLASS_NAME, 'listing-card__image__inner-container')
                image_lien = image_element.find_element(By.TAG_NAME, "img").get_attribute("src")

                dic = {'etat': etat,
                    'marque': marque,
                    'annee': annee,
                    'adresse': adresse,
                    'prix_F_Cfa': prix_F_Cfa,
                    'image_url': image_lien}
                data.append(dic)
            except:
                pass
        DF = pd.DataFrame(data)
        df = pd.DataFrame(data)
        for p in range(1,2): 
            driver.get(f'https://www.expat-dakar.com/motos-scooters?page=1&page={p}')
            containers = driver.find_elements(By.CSS_SELECTOR, "[class= 'listing-card__content 1']")
            data = []
            for container in containers : 
                try:
                    gen_info =container.find_element(By.CSS_SELECTOR, 'div.listing-card__header__tags')
                    etat = gen_info.find_element(By.CSS_SELECTOR, 'span').text
                    marque = container.find_element(By.CSS_SELECTOR, "span.listing-card__header__tags__item--make").text
                    annee = container.find_element(By.CSS_SELECTOR, "span.listing-card__header__tags__item--buildyear").text
                    adresse = container .find_element(By.CSS_SELECTOR, "div.listing-card__header__location").text
                    prix_F_Cfa = container.find_element(By.CSS_SELECTOR, "div.listing-card__info-bar__price").text.replace("\u202f","").replace("F Cfa","").strip()
                    image_element = driver.find_element(By.CLASS_NAME, 'listing-card__image__inner-container')
                    image_lien = image_element.find_element(By.TAG_NAME, "img").get_attribute("src")

                    dic = {'etat': etat,
                        'marque': marque,
                        'annee': annee,
                        'adresse': adresse,
                        'prix_F_Cfa': prix_F_Cfa,
                        'image_url': image_lien}
                    data.append(dic)
                except:
                    pass

            DF = pd.DataFrame(data)
            df = pd.concat([df, DF], axis = 0).reset_index(drop=True)
            df.to_csv('Data/motos_scooters.csv', index=False)
    
    elif url == url3:
        
        from requests import get 
        from selenium import webdriver 
        from selenium.webdriver.chrome.service import Service 
        from selenium.webdriver.support.ui import WebDriverWait, Select  
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By 
        
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        
        driver.get('https://www.expat-dakar.com/equipements-pieces')
        containers = driver.find_elements(By.CSS_SELECTOR, "[class= 'listing-card__content 1']")
        
        container = containers[0]
        details = container.find_element(By.CSS_SELECTOR, 'div.listing-card__header__title').text
        gen_info =container.find_element(By.CSS_SELECTOR, 'div.listing-card__header__tags')
        etat = gen_info.find_element(By.CSS_SELECTOR, 'span').text
        adresse = container .find_element(By.CSS_SELECTOR, "div.listing-card__header__location").text
        prix_F_Cfa = container.find_element(By.CSS_SELECTOR, "div.listing-card__info-bar__price").text.replace("\u202f","").replace("F Cfa","").strip()
        image_element = driver.find_element(By.CLASS_NAME, 'listing-card__image__inner-container')
        image_lien = image_element.find_element(By.TAG_NAME, "img").get_attribute("src")
        
        data = []
        for container in containers : 
            try:
                container = containers[0]
                details = container.find_element(By.CSS_SELECTOR, 'div.listing-card__header__title').text
                gen_info =container.find_element(By.CSS_SELECTOR, 'div.listing-card__header__tags')
                etat = gen_info.find_element(By.CSS_SELECTOR, 'span').text
                adresse = container .find_element(By.CSS_SELECTOR, "div.listing-card__header__location").text
                prix_F_Cfa = container.find_element(By.CSS_SELECTOR, "div.listing-card__info-bar__price").text.replace("\u202f","").replace("F Cfa","").strip()
                image_element = driver.find_element(By.CLASS_NAME, 'listing-card__image__inner-container')
                image_lien = image_element.find_element(By.TAG_NAME, "img").get_attribute("src")

                dic = {'details': details,
                    'etat': etat,
                    'adresse': adresse,
                    'prix_F_Cfa': prix_F_Cfa,
                    'image_url': image_lien}
                data.append(dic)
            except:
                pass
        
        DF = pd.DataFrame(data)
        df = pd.DataFrame(data)
        
        for p in range(1,2): 
            driver.get(f'https://www.expat-dakar.com/equipements-pieces?page=1&page={p}')
            containers = driver.find_elements(By.CSS_SELECTOR, "[class= 'listing-card__content 1']")
            data = []
            for container in containers : 
                try:
                    container = containers[0]
                    details = container.find_element(By.CSS_SELECTOR, 'div.listing-card__header__title').text
                    gen_info =container.find_element(By.CSS_SELECTOR, 'div.listing-card__header__tags')
                    etat = gen_info.find_element(By.CSS_SELECTOR, 'span').text
                    adresse = container .find_element(By.CSS_SELECTOR, "div.listing-card__header__location").text
                    prix_F_Cfa = container.find_element(By.CSS_SELECTOR, "div.listing-card__info-bar__price").text.replace("\u202f","").replace("F Cfa","").strip()
                    image_element = driver.find_element(By.CLASS_NAME, 'listing-card__image__inner-container')
                    image_lien = image_element.find_element(By.TAG_NAME, "img").get_attribute("src")

                    dic = {'details': details,
                        'etat': etat,
                        'adresse': adresse,
                        'prix_F_Cfa': prix_F_Cfa,
                        'image_url': image_lien}
                    data.append(dic)
                except:
                    pass

            DF = pd.DataFrame(data)
            df = pd.concat([df, DF], axis = 0).reset_index(drop=True)
            df.to_csv('Data/equipements_pieces.csv', index=False)
    st.write("Données scrapées avec succès!")
elif url not in [url1, url2, url3]:
    st.write("URL non reconnue. Veuillez entrer une URL valide.")              


# Section pour télécharger des données déjà scrapées
st.header("Télécharger des données non nétoyées Scrapées par web scraper")

def load_(dataframe, title, key) :
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    </style>""", unsafe_allow_html=True)

    if st.button(title,key):
      
        st.subheader('Display data dimension')
        st.write('Data dimension: ' + str(dataframe.shape[0]) + ' rows and ' + str(dataframe.shape[1]) + ' columns.')
        st.dataframe(dataframe)

# définir quelques styles liés aux box
st.markdown('''<style> .stButton>button {
    font-size: 12px;
    height: 3em;
    width: 25em;
}</style>''', unsafe_allow_html=True)

          
# Charger les données 
load_(pd.read_csv('Data/Scrapping_voitures_with_WS.csv'), 'Données Voitures', '1')
load_(pd.read_csv('Data/scrapping_motos_with_WS.csv'), 'Données Motos-Scooters', '2')
load_(pd.read_csv('Data/scrapping_pieces_with_WS.csv'), 'Données Equipements-pièces', '3')



# Section pour visualiser un dashboard
st.header("Dashboard d'analyse des véhicules")
data = pd.read_csv("Data/voitures_net.csv")
data = data[data["Prix"] > 1000]  # Filtrer les prix aberrants
#st.set_page_config(page_title="Analyse de voitures", layout="wide")
# Filtres
st.sidebar.header("Filtres")
selected_brands = st.sidebar.multiselect("Marques", options=data["Marque"].unique())
min_year, max_year = st.sidebar.slider("Année", 
                                      int(data["Annee"].min()), 
                                      int(data["Annee"].max()), 
                                      (2015, 2020))

# Application des filtres
filtered_data = data[
    (data["Marque"].isin(selected_brands) if selected_brands else True) &
    (data["Annee"] >= min_year) &
    (data["Annee"] <= max_year)
]

# Métriques clés
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Nombre total", filtered_data.shape[0])
with col2:
    st.metric("Prix moyen", f"{filtered_data['Prix'].mean():,.0f}Cfa")
with col3:
    st.metric("Année moyenne", int(filtered_data['Annee'].mean()))

# Visualisations
tab1, tab2, tab3 = st.tabs(["Distribution", "Comparaisons", "Données brutes"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        fig = px.histogram(filtered_data, x="Prix", title="Distribution des prix")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.pie(filtered_data, names="Boite_Vitesse", title="Répartition des boîtes de vitesse")
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(filtered_data.groupby("Marque")["Prix"].mean().reset_index(), 
                    x="Marque", y="Prix", title="Prix moyen par marque")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.scatter(filtered_data, x="Annee", y="Prix", color="Etat", 
                        title="Relation Année/Prix")
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.dataframe(filtered_data.sort_values("Prix", ascending=False), 
                height=400, 
                column_config={
                    "Prix": st.column_config.NumberColumn(format="%d F Cfa")
                })

# Analyse supplémentaire
st.subheader("Top 10 des véhicules les plus chers")
st.table(filtered_data.nlargest(10, "Prix")[["Marque", "Annee", "Prix", "Etat"]]
        .style.format({"Prix": "{:,.0f} F Cfa"}))
    
# Section pour remplir un formulaire d'évaluation
st.header("Évaluation de l'Application")
# st.subheader("https://ee.kobotoolbox.org/i/htBTb6Dx")
st.markdown("""
***Lien:*** [Evaluation](https://ee.kobotoolbox.org/i/htBTb6Dx)
""")
# with st.form("evaluation_form"):
#     st.write("Veuillez remplir ce formulaire pour évaluer l'application.")
#     nom = st.text_input("Nom")
#     email = st.text_input("Email")
#     evaluation = st.slider("Évaluation", 1, 5)
#     commentaire = st.text_area("Commentaire")
#     soumis = st.form_submit_button("Soumettre")
#     if soumis:
#         st.write("Merci pour votre évaluation!")
