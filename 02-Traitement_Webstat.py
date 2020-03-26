import pandas as pd

df = pd.read_csv("Webstat_Export_20190823_delais_de_paiement.csv",sep=";").rename(columns={"Unnamed: 0": "dates"})
df_title = pd.read_csv("Webstat_Export_20190823_delais_de_paiement_titre.csv",sep=";", encoding="cp1252")

final = pd.DataFrame(columns=['elements','dates','value'])
for i in list(df):
    if i =='dates':
        pass
    else:
        temp = df[['dates',i]].rename(columns={i: "value"})
        temp['elements'] = i
        final = final.append(temp)
        
final['elem_split']=final.elements.str.split('.')

final['jeu_de_donnees'] = final.elem_split.map(lambda x: x[0])
final['Periodicite'] = final.elem_split.map(lambda x: x[1])
final['Zone_geographique'] = final.elem_split.map(lambda x: x[2])
final['Theme_economique'] = final.elem_split.map(lambda x: x[3])
final['Nature_entreprise'] = final.elem_split.map(lambda x: x[4])
final['Objet'] = final.elem_split.map(lambda x: x[5])
final['Mesure'] = final.elem_split.map(lambda x: x[6])
final['Coreection_Statistique'] = final.elem_split.map(lambda x: x[7])
final['Secteur_activite'] = final.elem_split.map(lambda x: x[8])
final['Taile_des_entreprises'] = final.elem_split.map(lambda x: x[9])

final = pd.merge(final,df_title,how='left',on='elements')

final.to_csv('Data_Frame_delais_de_paiement.csv', sep=';', encoding='utf-8', index=False)


df = pd.read_csv("Data_Frame_delais_de_paiement.csv",sep=";")



