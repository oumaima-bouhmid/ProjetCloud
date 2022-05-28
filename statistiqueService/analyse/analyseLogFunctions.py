import pandas as pd


# prend en argument un fichier log et retourne un dataframe qui contient les données du log
def logToDf(fichierOrigine):
    df=pd.read_csv(fichierOrigine, sep=" ", encoding="utf-8")
    df.columns =['IP', 'Client Identity', 'ID', 'Time','GMT', 'HTTP request', 'Status Code','Data(Bytes)', 'From Url','SE']
    df.head(5)
    return df

#convertir to dict
def convertToDict(association):
  dictAssociation = dict()
  liste = []
  j = 0
  for i in association:
    for key in i:
      liste.append(i[key])
  while j != len(liste):
    dictAssociation[liste[j]] = liste[j+1]
    j = j+2
  return dictAssociation
  
# Prend en arg un dataframe et retourne Nombre de fois consulter par une ip (pour cibler une zone par exemple)
def nb_consultation_ip(df):
    SearchIp = []
    for ip in df.loc[:, "IP"]:
        if ip not in SearchIp:
            SearchIp.append(ip)

    NumberPerIp = dict()
    for ip in df.loc[:, "IP"]:
        if(ip not in NumberPerIp):
            NumberPerIp[ip] = 1
        else:
            NumberPerIp[ip] = NumberPerIp[ip] + 1
    return NumberPerIp

def reduction_ip(NumberPerIp):
    NumberPerIp_reduit = dict()
    for ip in NumberPerIp.keys():
        if(NumberPerIp[ip] > 20):
            NumberPerIp_reduit[ip] = NumberPerIp[ip]
    return NumberPerIp_reduit
           
def sort_reduction_ip(NumberPerIp_reduit):
    sorted_NumberPerPage = {k: v for k, v in sorted(NumberPerIp_reduit.items(), key=lambda item: item[1])}
    res = dict(reversed(list(sorted_NumberPerPage.items())))
    return res

#nombre total ip
def nbTotalIp(df):
    nbTotalIp = nb_consultation_ip(df)
    return len(nbTotalIp)



# Prend en arg un dataframe et retourne Nombre d'apparence des pages dans le fichier log
def nb_apparence_pages(df):
    SearchPage = []
    for page in df.loc[:, "HTTP request"]:
        if page not in SearchPage:
            SearchPage.append(page)

    NumberPerPage = dict()
    for page in df.loc[:, "HTTP request"]:
        if(page not in NumberPerPage):
            NumberPerPage[page] = 1
        else:
            NumberPerPage[page] = NumberPerPage[page] + 1
    return NumberPerPage


def sort_nb_apparence_pages(NumberPerPage):
    sorted_NumberPerPage = {k: v for k, v in sorted(NumberPerPage.items(), key=lambda item: item[1])}
    return sorted_NumberPerPage


def top5_pages(sorted_NumberPerPage):
    l = len(sorted_NumberPerPage)-5
    top5_page = {page: sorted_NumberPerPage[page] for page in list(sorted_NumberPerPage)[l:]}
    return top5_page


# Top 5 search engines
def all_search_engines(df):
    SearchSE = []
    for se in df.loc[:, "SE"]:
        if se not in SearchSE:
            SearchSE.append(se)

    NumberPerSE = dict()
    for se in df.loc[:, "SE"]:
        if(se not in NumberPerSE):
            NumberPerSE[se] = 1
        else:
            NumberPerSE[se] = NumberPerSE[se] + 1
    return NumberPerSE
        

def sort_all_search_engines(NumberPerSE):
    sorted_NumberPerSE = {k: v for k, v in sorted(NumberPerSE.items(), key=lambda item: item[1])}
    return sorted_NumberPerSE


def top5_se(sorted_NumberPerSE):
    l = len(sorted_NumberPerSE)-5
    top5_SE = {page: sorted_NumberPerSE[page] for page in list(sorted_NumberPerSE)[l:]}
    return top5_SE


# Codes status
def all_code_status(df):
    SearchSC = []
    for sc in df.loc[:, "Status Code"]:
        if sc not in SearchSC:
            SearchSC.append(sc)

    NumberPerSC = dict()
    for sc in df.loc[:, "Status Code"]:
        if(sc not in NumberPerSC):
            NumberPerSC[sc] = 1
        else:
            NumberPerSC[sc] = NumberPerSC[sc] + 1
    return NumberPerSC


def sort_all_code_status(NumberPerSC):
    sorted_NumberPerSC = {k: v for k, v in sorted(NumberPerSC.items(), key=lambda item: item[1])}
    return sorted_NumberPerSC


def top5_codestatus(sorted_NumberPerSC):
    l = len(sorted_NumberPerSC)-5
    top5_SC = {page: sorted_NumberPerSC[page] for page in list(sorted_NumberPerSC)[l:]}
    return top5_SC


# Canaux de distributions les plus frequentés, il faut aussi ajouté TO a l'equations
def all_canaux(df):
    SearchFU = []
    for fu in df.loc[:, "From Url"]:
        if fu not in SearchFU:
            SearchFU.append(fu)

    NumberPerFU = dict()
    for fu in df.loc[:, "From Url"]:
        if(fu not in NumberPerFU):
            NumberPerFU[fu] = 1
        else:
            NumberPerFU[fu] = NumberPerFU[fu] + 1
    return NumberPerFU


def sort_all_canaux(NumberPerFU):
    sorted_NumberPerFU = {k: v for k, v in sorted(NumberPerFU.items(), key=lambda item: item[1])}
    return sorted_NumberPerFU


def top10_canaux(sorted_NumberPerFU):
    l = len(sorted_NumberPerFU)-10
    top5_FU = {fu: sorted_NumberPerFU[fu] for fu in list(sorted_NumberPerFU)[l:]}
    return top5_FU