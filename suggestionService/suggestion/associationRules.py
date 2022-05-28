import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import association_rules, apriori

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
      liste.append(str(i[key]))
  while j != len(liste):
    dictAssociation[liste[j]] = liste[j+1]
    j = j+2
  return dictAssociation


def dfToDataset(df):
    SearchIp = []
    for ip in df.loc[:, "IP"]:
        if ip not in SearchIp:
            SearchIp.append(ip)

    dataset = [0] * len(SearchIp)
    NumberPerIp = dict()
    i = -1
    for ip in df.loc[:, "IP"]:
        i = i + 1
        if(ip not in NumberPerIp):
            NumberPerIp[ip] = 1
            dataset[SearchIp.index(ip)] = []
            dataset[SearchIp.index(ip)].append(df.at[i,"HTTP request"])
        else:
            NumberPerIp[ip] = NumberPerIp[ip] + 1
            dataset[SearchIp.index(ip)].append(df.at[i,"HTTP request"])
    return dataset


def transform_datasetTodf(dataset):
    te = TransactionEncoder()
    te_ary = te.fit(dataset).transform(dataset)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    return df


def frequent_itemsets(df):
    frequent_itemsets = apriori(df, min_support=0.1, use_colnames = True)
    fg = frequent_itemsets.sort_values(by = 'support')
    return fg


def association_rules_log(frequent_itemsets):
    res = association_rules(frequent_itemsets, metric = "confidence", min_threshold = 0.97)
    res = res.sort_values(by = 'lift')
    res = res[len(res)-10:]
    return res


#resulat final
def filtering_associations(res):
    res1 = res[['antecedents', 'consequents']]
    res1 = res1.iloc[::-1]
    association = res1.to_dict(orient ='records')

    return association
