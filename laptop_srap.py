from bs4 import BeautifulSoup
import requests,json

url = "https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=2bdd30fa-a88c-4b18-abae-4accdf5df6b6&as-searchtext=lap"
page = requests.get(url)

soup = BeautifulSoup(page.text,'html.parser')
# print(soup.getText())

def lap():
    print("LOading...............\nwait...............")
    d = {}
    l = []
    main_d = soup.find('div',class_='_1YokD2 _3Mn1Gg')
    # print(main_d.getText())
    sec_d=main_d.find_all('div',class_="_2kHMtA")
    c =0 
    for i in sec_d:
        c+=1
        #scrap laptop name 
        find_name_d = i.find('div',class_='col col-7-12')
        name1= find_name_d.find('div',class_='_4rR01T').getText()
        name =""
        for lett in name1:
            if lett == '-':
                break
            else:
                name+=lett
        d['name'] = name 
        
        #scrap rating 
        rat_d = i.find('div',class_='gUuXy-')
        rating = rat_d.find('div',class_='_3LWZlK').getText()
        d['rating'] = rating

        #scrap laptop price 
        find_d_P = i.find('div',class_='col col-5-12 nlI3QM')
        price = find_d_P.find('div',class_='_30jeq3 _1_WHN1').getText()
        d['price'] = price

        #scrap details 
        de_d = find_name_d.find('div',class_='fMghEO')
        det = de_d.find_all('ul',class_='_1xgFaf')
        for dett in det:
            de_list = []
            full_d = dett.find_all('li',class_='rgWa7D')
            for detail in full_d:
                de_list.append(detail.text)
            d['details'] = de_list
        l.append(d.copy())
        if c == 20 :
            break
    return l
done = lap()
with open('laptop.json','w') as obj:
    json.dump(done,obj,indent=4)
print("done......")