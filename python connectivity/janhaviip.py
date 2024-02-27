import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random


print("  ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print("  ..                                                                                                                                                  ..")
print("  ..                                                        TOPIC  : CROP PRODUCTION IN INDIA                                                         ..")
print("  ..                                                                                                                                                  ..")
print("  :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print(" ")
print("")
print("  SCHOOL : ALPINE ACADEMY")
print("  Name : Janhavi Ambad")
print("  Class : XII 'PCM'      ")
print("  Roll no. :           ")
print("  Subject code : 065")
print("        ")
print( " Aim : Aim of the project is to take data stored in  csv or database file  and analyze using python libraries and generate appropriate charts to visualize .")
print("")
print("")
print("")
df=pd.read_csv("cropp.csv")

df4= pd.DataFrame(df)
df7=df4['Area']
df8=df7.values.tolist()
df5=df4['State_Name']
df6=df5.values.tolist()
lenght=len(df6)
uni=[]
dup=[]
count=i=0
while i<lenght:
    element=df6[i]
    count=1
    if element not in uni and element not in dup:
        i+=1
        for j in range(i,lenght):
            if element==df6[j]:
                count+=1
        else:
            if count==1:
                uni.append(element)
            else:
                dup.append(element)
    else:
        i+=1
list1=dup
lenght1=len(list1)




df10=df4['Crop_Year']
df16=df10.values.tolist()
lenght3=len(df16)
uniq=[]
dupl=[]
countt=p=0
while p<lenght3:
    elementt=df16[p]
    countt=1
    if elementt not in uniq and elementt not in dupl:
        p+=1
        for q in range(p,lenght3):
            if elementt==df16[q]:
                countt+=1
        else:
            if countt==1:
                uniq.append(elementt)
            else:
                dupl.append(elementt)
    else:
        p+=1
list3=dupl
lenght4=len(list3)



df11=df4['Crop']
df17=df11.values.tolist()
lenght5=len(df17)
uniqu=[]
dupli=[]
counttt=c=0
while c<lenght4:
    elementtt=df17[c]
    countt=1
    if elementtt not in uniqu and elementtt not in dupli:
        c+=1
        for b in range(c,lenght4):
            if elementtt==df17[b]:
                counttt+=1
        else:
            if counttt==1:
                uniqu.append(elementtt)
            else:
                dupli.append(elementtt)
    else:
        c+=1
list4=dupli
list99=uniqu
lenght6=len(list4)



df112=df4['Season']
df116=df112.values.tolist()
lenght7=len(df116)
unique=[]
duplicate=[]
countt=g=0
while g<lenght7:
    elemenntt=df116[g]
    counntt=1
    if elemenntt not in unique and elemenntt not in duplicate:
        g+=1
        for h in range(g,lenght7):
            if elemenntt==df116[h]:
                counntt+=1
        else:
            if counntt==1:
                unique.append(elemenntt)
            else:
                duplicate.append(elemenntt)
    else:
        g+=1
list7=duplicate
lenght8=len(list7)



def bar_plot():
    print(list1)
    el=input('enter the state name:')
    el2=input('enter the 2nd state name:')
    af=pd.DataFrame(df[df.State_Name==el])
    r=af.groupby('Crop_Year')['Area'].sum()
    s=pd.DataFrame(r)
    ar=s['Area']
    cy=s.index.tolist()
    ag=pd.DataFrame(df[df.State_Name==el2])
    rr=ag.groupby('Crop_Year')['Area'].sum()
    ss=pd.DataFrame(rr)
    arar=ss['Area']
    cky=ss.index.tolist()
    ckyy=np.array(cky)
    plt.bar(cy,ar,color='violet',label=el,width=0.25 )
    plt.bar(ckyy+0.25,arar,color='purple',label=el2,width=0.25 )
    plt.legend()
    plt.xlabel('Year')
    plt.ylabel('Area')
    plt.title('comparison of area between {} and {}'.format(el,el2))
    plt.xticks(list3,rotation='vertical',fontsize=8)
    
    for a in range(len(list1)):
        if el in list1 and el2 in list1:
            plt.show()
    else:
        print("")
        print(" The state name is/are wrong. please check the state name from above list.")
    


   

def pie_plot():
    print(list1)
    ell=input('enter the state name:')
    ab=pd.DataFrame(df[df.State_Name==ell])
    kl=ab.groupby('Season')['Production'].sum()
    kk=pd.DataFrame(kl)
    print(kk)
    arr=kk['Production']
    cyy=kk.index.tolist()
    colarr =random.sample(list(mcolors.CSS4_COLORS.values()),6)
    colr=['violet','lightblue','orange','gold','grey','green']
    plt.pie(arr,labels=cyy,colors=colr, shadow = True ,autopct="%3.2f%%",radius=1.16,textprops={'fontsize':8})
    plt.title('Total production of all seasons took place in {}'.format(ell),fontsize=10)
    plt.legend()
    for a in range(len(list1)):
        if ell in list1:
            plt.show()
    else:
        print("")
        print(" The entered state name is wrong. please check the state name from above list.")
    

    
           

def line_plot():
    print(list1)
    abc,kkl,kkk,rar,ycy=0,0,0,0,0
    count=0
    ans='yes'
    while ans=='yes':
        naaa=input('ener the state name:')
        abc=pd.DataFrame(df[df.State_Name==naaa])
        kkl=abc.groupby('Crop_Year')['Production'].sum()
        kkk=pd.DataFrame(kkl)
        rar=kkk['Production']
        ycy=kkk.index.tolist()
        plt.plot(ycy,rar,linestyle='solid',label=naaa,marker='d',markersize=3)
        plt.xlabel('year')
        plt.ylabel('production')
        plt.xticks(list3,rotation='vertical')
        plt.title('comparison of production in every year between  states of your choice')
        plt.legend()
        count=count+1
        ans=input(' want to compare other states ?:( yes or no)    ')
    if naaa in list1 :
        plt.show()
    else:
        print("")
        print(" The entered state name is wrong. please check the state name from above list.")
    
   


    



def scatter_plot():
    
    print(list3)
    namee1=int(input('enter the year'))
    dm=pd.DataFrame(df[df.Crop!='Sugarcane'])
    dm1=pd.DataFrame(dm[dm.Crop!='Wheat'])
    dm2=pd.DataFrame(dm1[dm1.Crop!='Maize'])
    dm3=pd.DataFrame(dm2[dm2.Crop!='Rice'])
    dm4=pd.DataFrame(dm3[dm3.Crop!='Jute'])
    dg=dm4.groupby("Crop_Year")
    dg.groups
    aaa=dg.get_group(namee1)
    aacc=pd.DataFrame(aaa)
    gdg=aacc['State_Name']
    gddg=gdg.values.tolist()
    lenght10=len(gddg)
    uniquee=[]
    duplicatee=[]
    countttt=r=0
    while r<lenght10:
        elementttt=gddg[r]
        countttt=1
        if elementttt not in uniquee and elementttt not in duplicatee:
            r+=1
            for w in range(r,lenght10):
                if elementttt==gddg[w]:
                    countttt+=1
            else:
                if countttt==1:
                    uniquee.append(elementttt)
                else:
                    duplicatee.append(elementttt)
        else:
            r+=1
    list9=duplicatee
    print(list9)
    nammee=input("enter state name")
    xyxy=aacc.groupby('State_Name')
    xyxy.groups
    xxyyy=xyxy.get_group(nammee)
    xxxyyy=pd.DataFrame(xxyyy)
    print(xxxyyy)
    xxxxyy=xxxyyy.groupby('Crop')['Production'].sum()
    xxxxyyy=pd.DataFrame(xxxxyy)
    print(xxxxyyy)
    accaa=xxxxyyy.index.tolist()
    aaacf=len(accaa)
    cacaacc=xxxxyyy['Production']
    cacacc=np.array(cacaacc)
    colarr =random.sample(list(mcolors.CSS4_COLORS.values()),aaacf)
    plt.scatter(accaa,cacacc,c=colarr,s=20)
    plt.xticks(rotation='vertical',fontsize=7)
    plt.xlabel('crops')
    plt.ylabel('production')
    plt.title('Production of every crop except(Sugarcane,Rice,maize,jute,wheat) in {} in {}'.format(nammee,namee1))
    for a in range(len(list1)):
        if namee1 in list3 and nammee in list1:
                plt.show()
        else:
            print("")
            print(" The entered State name or year is/are invalid.please check tha state name and year from above list.")



def pie1_plot():
    print(list3)
    namee3=int(input('enter the year'))
    dn1=df.groupby('Crop')
    dn1.groups
    dn2=dn1.get_group('Sugarcane')
    dnn2=pd.DataFrame(dn2)
    dn3=dn1.get_group('Wheat')
    dnn3=pd.DataFrame(dn3)
    dn4=dn1.get_group('Maize')
    dnn4=pd.DataFrame(dn4)
    dn5=dn1.get_group('Rice')
    dnn5=pd.DataFrame(dn5)
    dn6=dn1.get_group('Jute')
    dnn6=pd.DataFrame(dn6)
    dnnn1=dnn2._append(dnn3,ignore_index=True)
    dnnn2=dnnn1._append(dnn4,ignore_index=True)
    dnnn3=dnnn2._append(dnn5,ignore_index=True)
    dn=dnnn3._append(dnn6,ignore_index=True)
    dk=dn.groupby("Crop_Year")
    dk.groups
    aak=dk.get_group(namee3)
    aack=pd.DataFrame(aak)
    gdg=aack['State_Name']
    gddg=gdg.values.tolist()
    lenght10=len(gddg)
    uniquee=[]
    duplicatee=[]
    countttt=r=0
    while r<lenght10:
        elementttt=gddg[r]
        countttt=1
        if elementttt not in uniquee and elementttt not in duplicatee:
            r+=1
            for w in range(r,lenght10):
                if elementttt==gddg[w]:
                    countttt+=1
            else:
                if countttt==1:
                    uniquee.append(elementttt)
                else:
                    duplicatee.append(elementttt)
        else:
            r+=1
    list9=duplicatee
    print(list9)
    nammee4=input("enter state name")
    xyxk=aack.groupby('State_Name')
    xyxk.groups
    xxyyk=xyxk.get_group(nammee4)
    xxxyyk=pd.DataFrame(xxyyk)
    xxxxyk=xxxyyk.groupby('Crop')['Production'].sum()
    xxxxyyk=pd.DataFrame(xxxxyk)
    print(xxxxyyk)
    accak=xxxxyyk.index.tolist()
    aaack=len(accak)
    cacaack=xxxxyyk['Production']
    cacack=np.array(cacaack)
    f=['Sugarcane','Wheat','Maize','Rice','Jute']
    crr=['lightgreen','violet','yellow','magenta','lightblue']
    plt.pie(cacaack,labels=accak,colors=crr,autopct='%1.1f%%',shadow= True)
    plt.title('Production of every crop(Sugarcane,Rice,maize,jute,wheat) in {} in {}'.format(nammee4,namee3))
    if nammee4 in list1 and namee3 in list3:
        plt.show()
    else:
        print('')
        print(" The entered State name or year is/are invalid.please check tha state name and year from above list.")

     
    

    




def scatter1_plot():
    print(list7)
    crop_name=input("enter the season")
    dgg=df4.groupby("Season")
    dgg.groups
    dgg1=dgg.get_group(crop_name)
    dgg2=pd.DataFrame(dgg1)
    gdg=dgg2['State_Name']
    gddg=gdg.values.tolist()
    lenght10=len(gddg)
    uniquee=[]
    duplicatee=[]
    countttt=r=0
    while r<lenght10:
        elementttt=gddg[r]
        countttt=1
        if elementttt not in uniquee and elementttt not in duplicatee:
            r+=1
            for w in range(r,lenght10):
                if elementttt==gddg[w]:
                    countttt+=1
            else:
                if countttt==1:
                    uniquee.append(elementttt)
                else:
                    duplicatee.append(elementttt)
        else:
            r+=1
    list222=duplicatee
    print(list222)
    state_name=input("enter the state name")
    state_name1=input("enter the state name")
    print(dgg2)
    dgg3=dgg2.groupby('State_Name')
    dgg3.groups
    dgg4=dgg3.get_group(state_name)
    dgg5=pd.DataFrame(dgg4)
    dgg6=dgg5.groupby('Crop_Year')['Production'].sum()
    dgg7=pd.DataFrame(dgg6)
    print(dgg7)
    gg1=dgg7.index.tolist()
    gg=dgg7['Production']
    gg2=np.array(gg)
    dgg8=dgg3.get_group(state_name1)
    dgg9=pd.DataFrame(dgg8)
    dgg10=dgg9.groupby('Crop_Year')['Production'].sum()
    dgg11=pd.DataFrame(dgg10)
    print(dgg11)
    gg3=dgg11.index.tolist()
    ggg=dgg11['Production']
    gg4=np.array(ggg)
    plt.scatter(gg1,gg2,color='b',s=10,marker='D',label=state_name)
    plt.scatter(gg3,gg4,color='r',s=20,marker='>',label=state_name1)
    plt.legend()
    plt.xticks(list3)
    plt.xlabel("Year")
    plt.ylabel("Production")
    plt.title('production in {} ,{} of {} season in every year '.format(state_name,state_name1,crop_name))
    for f in range(len(list222)):
        if state_name in list222 and state_name1 in list222:
            plt.show()
    else:
        print(" The entered State name/s or season is/are invalid.Please check state name and season from above list")




def line1_plot():
    print(list1)
    print(list7)
    df25=pd.DataFrame(df4[df4.Season!='Whole Year'])
    df24=pd.DataFrame(df25[df25.Season!='Kharif'])
    print(df24)
    print(df)
    sc1=df24.groupby(['Season','Crop_Year'])['Production'].sum()
    sc2=pd.DataFrame(sc1)
    print(sc2)
    sc2.unstack(level=0).plot(kind='line',figsize=(10,10),fontsize='xx-small',marker='o',markersize='3')
    plt.title("prouction of crops in (autumn,rabi,winter,summer)seasons by years")
    plt.ylabel("Production")
    plt.show()





def bar2_plot():
    print(list1)
    print(list7)
    df35=pd.DataFrame(df4[df4.Season!='Rabi'])
    df34=pd.DataFrame(df35[df35.Season!='Summer'])
    df33=pd.DataFrame(df34[df34.Season!='Winter'])
    df32=pd.DataFrame(df33[df33.Season!='Autumn'])
    df31=pd.DataFrame(df32[df32.Season!='Kharif'])
    sc1=df31.groupby(['Season','Crop_Year'])['Production'].sum()
    sc2=pd.DataFrame(sc1)
    print(sc2)
    ccs=sc2.values.tolist()
    css=len(ccs)
    sc2.unstack(level=0).plot(kind='bar',subplots=True,figsize=(10,10),fontsize='xx-small',color='lightgreen')
    plt.title("production in whole year in every years")
    plt.show()



def bar3_plot():
    print(list1)
    print(list7)
    df45=pd.DataFrame(df4[df4.Season!='Rabi'])
    df44=pd.DataFrame(df45[df45.Season!='Summer'])
    df43=pd.DataFrame(df44[df44.Season!='Winter'])
    df42=pd.DataFrame(df43[df43.Season!='Autumn'])
    df41=pd.DataFrame(df42[df42.Season!='Whole Year'])
    sc9=df41.groupby(['Season','Crop_Year'])['Production'].sum()
    sc10=pd.DataFrame(sc9)
    print(sc10)
    ccbs=sc10.values.tolist()
    csbs=len(ccbs)
    sc10.unstack(level=0).plot(kind='bar',subplots=True,figsize=(10,10),fontsize='xx-small',color='violet')
    plt.title("production in kharif season in every season")
    plt.show()






def bar1_plot():
    print(list1)
    pi=input("enter the state name : ")
    pq=pd.DataFrame(df4[df4.State_Name==pi])
    pf=pq.groupby('District_Name')['Production'].sum()
    pj=pd.DataFrame(pf)
    pjjj=pj['Production']
    pjj=pj.index.tolist()
    colarr =random.sample(list(mcolors.CSS4_COLORS.values()),len(pjj))
    plt.bar(pjj,pjjj,color=colarr)
    plt.title(' Production in {}'.format(pi))
    plt.xticks(pjj,rotation='vertical',fontsize=7)
    plt.ylabel('Production')
    plt.xlabel('District Name')
    if pi in list1:
        plt.show()
    else:
        print("")
        print("The entered State name is wrong.Please check it from above list.")






def histogram_plot():
    dw=df4.groupby('Crop_Year')['Area'].sum()
    dww=pd.DataFrame(dw)
    dwww=dww.values.tolist()
    flatt_list=[]
    for sub in dwww:
        for ittem in sub:
            flatt_list.append(ittem)
    print(flatt_list)
    plt.hist(flatt_list,bins=100,histtype='barstacked',color='purple')
    plt.title(' histogram showing total production by year ')
    plt.ylabel('production')
    plt.show()





def histogram1_plot():
   ll1=['Rabi','Summer','Winter','Autumn','Whole Year']
   print(ll1)
   yy=input('enter the 1st season')
   zz=input('enter the 2nd season')
   uy=pd.DataFrame(df4[df4.Season==yy])
   uy1=uy[['State_Name','Season','Production']]
   uy2=uy1.groupby('State_Name')['Production'].sum()
   uy3=uy2.values.tolist()
   print(uy3)
   ut=pd.DataFrame(df4[df4.Season==zz])
   ut1=ut[['State_Name','Season','Production']]
   ut2=ut1.groupby('State_Name')['Production'].sum()
   ut3=ut2.values.tolist()
   print(ut3)
   coolr=['magenta','blue']
   plt.hist([uy3,ut3],bins=100,histtype='step',color=coolr,linewidth=1.5,label=[yy,zz])
   plt.title('histogram comparing {} production and {} production'.format(yy,zz))
   plt.ylabel('Production')
   plt.legend()
   if yy in ll1 and zz in ll1:
       plt.show()
   else:
       print("")
       print("The entered Season/s name is/are wrong.Please check it from above list.")




def line2_plot():
    print(list1)
    name=input("Enter the state name : ")
    a=pd.DataFrame(df4[df4.State_Name==name])
    b=a.groupby('District_Name')['Area'].sum()
    c=pd.DataFrame(b)
    print(c)
    d=c['Area']
    print(d)
    e=c.index.tolist()
    plt.plot(e,d,'green',linestyle='-.',marker='X',markeredgecolor='green',markerfacecolor='lightgreen')
    plt.xticks(e,rotation='vertical',fontsize=7)
    plt.xlabel('District name')
    plt.ylabel('Area of Production')
    plt.title("Total area of production in every district of {} ".format(name))
    if name in list1:
        plt.show()
    else:
        print("")
        print("The entered State name is wrong.Please check it from above list.")



def pie2_plot():
    print(list99)
    print(list4)
    name=input(" Enter the crop name : ")
    a=pd.DataFrame(df4[df4.Crop==name])
    b=a.groupby('Crop_Year')['Production'].sum()
    c=pd.DataFrame(b)
    print(c)
    d=c.index.tolist()
    e=c['Production']
    colarr =random.sample(list(mcolors.CSS4_COLORS.values()),len(e))
    plt.pie(e,labels=d,colors=colarr,autopct='%3.2f%%',textprops={'fontsize':7},radius=1.1)
    plt.title("Production of {} in India".format(name))
    if name in list4:
        plt.show()
    else:
        print("")
        print("The entered State name is wrong.Please check it from above list.")




def scatter2_plot():
    print(list99)
    print(list4)
    name=input(" Enter the crop name : ")
    a=pd.DataFrame(df4[df4.Crop==name])
    b=a.groupby('Crop_Year')['Area'].sum()
    c=pd.DataFrame(b)
    print(c)
    d=c.index.tolist()
    e=c['Area']
    colarr =random.sample(list(mcolors.CSS4_COLORS.values()),len(e))
    plt.scatter(d,e,c=colarr)
    plt.title(" Area of production of {} in India".format(name))
    plt.xticks(d,rotation='vertical')
    plt.xlabel(' Year')
    plt.ylabel('Area of production')
    if name in list4:
        plt.show()
    else:
        print("")
        print("The entered State name is wrong.Please check it from above list.")


def bar4_plot():
    pr=['Rabi','Summer','Winter','Autumn','Whole Year','Kharif']
    print(pr)
    name=input("Enter the season : ")
    a=pd.DataFrame(df4[df4.Season==name])
    b=a['State_Name']
    gddg=b.values.tolist()
    lenght10=len(gddg)
    uniquee=[]
    duplicatee=[]
    countttt=r=0
    while r<lenght10:
        elementttt=gddg[r]
        countttt=1
        if elementttt not in uniquee and elementttt not in duplicatee:
            r+=1
            for w in range(r,lenght10):
                if elementttt==gddg[w]:
                    countttt+=1
            else:
                if countttt==1:
                    uniquee.append(elementttt)
                else:
                    duplicatee.append(elementttt)
        else:
            r+=1
    list9=duplicatee
    print(list9)
    name1=input("Enter the state name :")
    g=pd.DataFrame(a[a.State_Name==name1])
    h=g.groupby('District_Name')['Production'].sum()
    i=pd.DataFrame(h)
    print(i)
    ii=i.index.tolist()
    i3=i['Production']
    colarr =random.sample(list(mcolors.CSS4_COLORS.values()),len(i3))
    plt.bar(ii,i3,color=colarr)
    plt.xticks(ii,rotation='vertical', fontsize=7)
    plt.xlabel('District name')
    plt.ylabel('Prouction of {} crop'.format(name))
    plt.title(" Total production of {} crop in {}".format(name,name1))
    for a in range(len(list1)):
        if name1 in list1 and name in pr:
            plt.show()
    else:
        print("")
        print("The entered State name or season is/are wrong.")




def line3_plot():
    pr=['Rabi','Summer','Winter','Autumn','Whole Year','Kharif']
    print(pr)
    name=input("Enter the season : ")
    a=pd.DataFrame(df4[df4.Season==name])
    b=a['State_Name']
    gddg=b.values.tolist()
    lenght10=len(gddg)
    uniquee=[]
    duplicatee=[]
    countttt=r=0
    while r<lenght10:
        elementttt=gddg[r]
        countttt=1
        if elementttt not in uniquee and elementttt not in duplicatee:
            r+=1
            for w in range(r,lenght10):
                if elementttt==gddg[w]:
                    countttt+=1
            else:
                if countttt==1:
                    uniquee.append(elementttt)
                else:
                    duplicatee.append(elementttt)
        else:
            r+=1
    list9=duplicatee
    print(list9)
    name1=input("Enter the state name :")
    g=pd.DataFrame(a[a.State_Name==name1])
    h=g.groupby('District_Name')['Area'].sum()
    i=pd.DataFrame(h)
    print(i)
    ii=i.index.tolist()
    i2=i['Area']
    i3=i2.values.tolist()
    plt.plot(ii,i3,'purple',linestyle='--',marker='o',markerfacecolor='magenta',markeredgecolor='blue')
    plt.xticks(ii,rotation='vertical', fontsize=7)
    plt.xlabel('District name')
    plt.ylabel(' Area of prouction of {} crop'.format(name))
    plt.title(" Total area of  production of {} crop in {}".format(name,name1))
    for a in range(len(list1)):
        if name1 in list1:
            plt.show()
    else:
        print("")
        print("The entered State name or season is/are wrong.")

         
    
    
    

    
    
    


def info():
    print("")
    print("")
    print("....................................................... INFORMATION.........................................................................................")
    print("")
    print("")
    print(df4.info())
    print("")
    print("")
    print("............................................................................................................................................................")
    print("")
    print("")



def describe():
    print("")
    print("")
    print(".........................................................DESCRIPTION OF DATA.................................................................................")
    print("")
    print("")
    print("     (Maximum value ,count ,mean  , stanard deviation  and 25% , 50%, 75% percentile of values in column)") 
    print("")
    print("")
    print(df4.describe())
    print("")
    print("")
    print("....................................................................................................................................................................")
    print("")
    print("")



def total_production_season_wise():
    r=df4[['Season','Production']]
    rr=r.groupby('Season')['Production'].sum()
    print("")
    print("")
    print("..................................................TOTAL PRODUCTION SEASON WISE.......................................................................... ")
    print("")
    print("")
    print(rr)
    print("")
    print("")
    print(".............................................................................................................................................................")
    print("")
    print("")


def max_and_min_production():
    j=df4.groupby('State_Name')['Production'].sum()
    jj=pd.DataFrame(j)
    s=jj.sort_values(by=['Production'],ascending=False)
    print("")
    print("")
    print("................................................... STATE HAVING MAXIMUM PRODUCTION....................................................................... ")
    print("")
    print("")
    print(s.head(1))
    print("")
    print("")
    print("................................................... STATE HAVING MINIMUM PRODUCTION....................................................................... ")
    print("")
    print("")
    print(s.tail(1))
    print("")
    print("")
    print("....................................................................................................................................................................")
    print("")
    print("")


def district_and_production():
    print(list1)
    name=input("Enter the state name")
    p=pd.DataFrame(df4[df4.State_Name==name])
    s=p.groupby('District_Name')['Production'].sum()
    sa=pd.DataFrame(s)
    print(s)
    ss=sa.sort_values(by=['Production'],ascending=False)
    print("")
    print("")
    print("......................................................... DISTRICT HAVING MAXIMUM PRODUCTION................................................................... ")
    print("")
    print("")
    if name in list1:
        print(ss.head(1))
    else:
        print("")
        print("The entered State name is invalid.Please check it from above list.")
    print("")
    print("")
    print("......................................................... DISTRICT HAVING MINIMUM PRODUCTION.................................................................... ")
    print("")
    print("")
    if name in list1:
        print(ss.tail(1))
    else:
        print("")
        print("The entered State name is invalid.Please check it from above list.")
    print("")
    print("")
    print(".......................................................................................................................................................")
    print("")
    print("")

def crop_and_production():
    l=df4.groupby('Crop')['Production'].sum()
    ll=pd.DataFrame(l)
    print(l)
    jj=ll.sort_values(by=['Production'],ascending=False)
    print("")
    print("")
    print("........................................................ CROP HAVING MAXIMUM PRODUCTION...............................................................")
    print("")
    print("")
    print(jj.head(1))
    print("")
    print("")
    print(".........................................................CROP HAVING MINIMUM PRODUCTION ................................................................ ")
    print("")
    print("")
    print(jj.tail(1))
    print("")
    print("")
    print(".............................................................................................................................................................")
    print("")
    print("")


def crop_statewise():
    print(list1)
    name=input("Enter the state name  : ")
    p=pd.DataFrame(df4[df4.State_Name==name])
    s=p.groupby('Crop')['Production'].sum()
    sa=pd.DataFrame(s)
    print(s)
    ss=sa.sort_values(by=['Production'],ascending=False)
    print("")
    print("")
    print(".....................................................CROP HAVING MAXIMUM PRODUCTION...................................................................... ")
    print("")
    print("")
    print(ss.head(1))
    print("")
    print("")
    print(".................................................... CROP HAVING MINIMUM PRODUCTION...................................................................... ")
    print("")
    print("")
    print(ss.tail(1))
    print("")
    print("")
    print("..........................................................................................................................................................")
    print("")
    print("")




def state_max_min_area():
    d=df4.groupby('State_Name')['Area'].sum()
    dd=pd.DataFrame(d)
    print(d)
    ddd=dd.sort_values(by=['Area'],ascending=False)
    print("")
    print("")
    print("..........................................................STATE HAVING MAXIMUM AREA FOR PRODUCTION........................................................")
    print("")
    print("")
    print(ddd.head(1))
    print("")
    print("")
    print("...........................................................STATE HAVING MINIMUM AREA FOR PRODUCTION...................................................... ")
    print("")
    print("")
    print(ddd.tail(1))
    print("")
    print("")
    print("...........................................................................................................................................................")
    print("")
    print("")

def state_district_production():
    print(list1)
    name=input("Enter the state name")
    p=pd.DataFrame(df4[df4.State_Name==name])
    t=p[['District_Name']]
    gddg=t.values.tolist()
    lenght10=len(gddg)
    uniquee=[]
    duplicatee=[]
    
    countttt=r=0
    while r<lenght10:
        elementttt=gddg[r]
        countttt=1
        if elementttt not in uniquee and elementttt not in duplicatee:
            r+=1
            for w in range(r,lenght10):
                if elementttt==gddg[w]:
                    countttt+=1
            else:
                if countttt==1:
                    uniquee.append(elementttt)
                else:
                    duplicatee.append(elementttt)
        else:
            r+=1
    list9=duplicatee
    print(list9)
    nammee4=input("enter district  name : ")
    tt=pd.DataFrame(p[p.District_Name==nammee4])
    t4=tt.groupby('District_Name')['Production'].sum()
    t1=pd.DataFrame(t4)
    print("")
    print("")
    print(".........................................................Production in {}................................................................................".format(nammee4))
    print("")
    print("")
    if name in list1 and nammee4 in list9:
        print(t1)
    else:
        print("")
        print("The entered State name or district name is invalid.Please check it from above list.")
    print("")
    print("")
    print("........................................................................................................................................................")
    print("")
    print("")
 
def data_visualization():
    print("                                                                               ")
    print("#####################################################################################################################################################")
    print("                                                                        ")
    print("                                      DATA VISUALIZATION ON CROPS PRODUCTION AND  AREA OF PROUCTION  IN INDIA      ")
    print("                                                                        ")
    print("######################################################################################################################################################")
    print("                                                                               ")
    print("  01.)  press 1 :  bar plot showing of increase/decrease in area in every year(2001-2015) of two states (of your choice)")
    print("                                         ")
    print("  02.)  press 2 :  pie  plot showing total production took place in state (of your choice)")
    print("                                         ")
    print("  03.)  press 3 :  line plot comparing production in every year(2001-2015) between any states( as many of your choice)")
    print("                                         ")
    print("  04.)  press 4 :  scatter plot showing production of every crop except(Sugarcane,Rice,maize,jute,wheat) in particular state and year (of your choice) ")
    print("                                         ")
    print("  05.)  press 5 :  scatter plot showing production of every crop(Sugarcane,Rice,maize,jute,wheat) in particular state and year( of your choice) ")
    print("                                         ")
    print("  06.)  press 6 :  scatter plot comparing production in two states of particular season in every year (of your choice)")
    print("                                         ")
    print("  07.)  press 7 :  line plot showing prouction in (autumn,rabi,winter,summer)seasons by years")
    print("                                         ")
    print("  08.)  press 8 :  bar plot showing production in whole year in every year")
    print("                                         ")
    print("  09.)  press 9 :  bar plot showing prouction in kharif season in every year")
    print("                                         ")
    print("  10.)  press 10 : bar plot showing production of crop district wise of any state (of your choice)")
    print("                                         ")
    print("  11.)  press 11 :  histogram showing total production by year")
    print("                                         ")
    print("  12.)  press 12 :  histogram comparing production of two season(of your choice) ")
    print("                                         ")
    print("  13.)  press 13 :  line plot showing area of production in every district of a particular state(of your choice)")
    print("                                         ")
    print("  14.)  press 14 :  pie plot showing production of crops(Arecanut,Other Kharif pulses, Rice, Banana, Cashewnut, Coconut , Dry ginger, Sugarcane, Sweet potato, Tapioca)")
    print("                                         ")
    print("  15.)  press 15 :  scatter plot showing area of production of crops(Arecanut,Kharif pulses, Rice,Banana,Cashewnut,Coconut ,Dry ginger,Sugarcane,Sweet potato,Tapioca)")
    print("                                         ")
    print("  16.)  press 16 :  bar plot showing total production of a season(of your choice) in a particular state(of your choice)")
    print("                                         ")
    print("  17.)  press 17 :  line plot showing total area of production of a season(of your choice) in a particular state(of your choice)")
    print("                                         ")
    print("-------...----------...----------...----------...-------...------...----------...----------...----------...----------...-------...------...----------...--")
    print("-------...----------...----------...----------...-------...------...----------...----------...----------...----------...-------...------...----------...--")
    print("                                         ")
    option=""
    while(1):
        option=int(input("Enter your choice : "))
        if option==1:
            bar_plot()
        elif option==2:
            pie_plot()
        elif option==3:
            line_plot()
        elif option==4:
            scatter_plot()
        elif option==5:
            pie1_plot()
        elif option==6:
            scatter1_plot()
        elif option==7:
            line1_plot()
        elif option==8:
            bar2_plot()
        elif option==9:
            bar3_plot()
        elif option==10:
            bar1_plot()
        elif option==11:
            histogram_plot()
        elif option==12:
            histogram1_plot()
        elif option==13:
            line2_plot()
        elif option==14:
            pie2_plot()
        elif option==15:
            scatter2_plot()
        elif option==16:
            bar4_plot()
        elif option==17:
            line3_plot()
        else:
            print("invalid input")
            print("\a")
        print("")
        print("")
        i=input("Do you wish to continue yes or no:-")
        if i=='yes' or i=='YES':
            continue
        else:
            break




def data_analysis():
    print("                                        ")
    print("#########################################################################################################################################################")
    print("                                                                        ")
    print("                                               DATA ANALYSIS ON CROPS PRODUCTION AND  AREA OF PROUCTION  IN INDIA")
    print("                                                                        ")
    print("#########################################################################################################################################################")
    print("                                         ")
    print("  01.) Press 01 to view information about data.")
    print("                                  ")
    print("  02.) Press 02 to view the description (mean , count,standard deviation,percentile ,maximum value )of data")
    print("                                  ")
    print("  03.) Press 03 to view total production of every season .")
    print("                                  ")
    print("  04.) Press 04 to view  (a) State having maximum production.")
    print("                  (b) State having minimum production.")
    print("                                  ")
    print("  05.) Press 05 to view  (a) Total production of any state(of you choice) in every district")                 
    print("                  (b)District having maximum production.")
    print("                  (c)District having minimum production.")
    print("                                  ")
    print("  06.) Press 06 to view  (a)Total production of all crops.")
    print("                  (b)Crop having maximum production.")
    print("                  (c)Crop having minimum production.")
    print("                                  ")
    print("  07.) Press 07 to view  (a) Total production of any state(of you choice) of every crop")                 
    print("                  (b)Crop having maximum production in that particular state .")
    print("                  (c)Crop having minimum production in that particular state .")
    print("                                  ")
    print("  08.) Press 08 to view  (a)Total area of production of all state")                 
    print("                  (b)State having maximum area of production.")
    print("                  (c)State having minimum area of production.")
    print("                                  ")
    print("  09.) Press 09 to view total production in any district in india (of your coice)")
    print("                                  ")
    print("-------...----------...----------...----------...-------...------...----------...----------...----------...----------...-------...------...----------...--")
    print("-------...----------...----------...----------...-------...------...----------...----------...----------...----------...-------...------...----------...--")
    option=""
    while(1):
        print("")
        print("")
        option=int(input("Enter your choice  : "))
        if option==1:
            info()
        elif option==2:
            describe()
        elif option==3:
            total_production_season_wise()
        elif option==4:
            max_and_min_production()
        elif option==5:
            district_and_production()
        elif option==6:
            crop_and_production()
        elif option==7:
            crop_statewise()
        elif option==8:
            state_max_min_area()
        elif option==9:
            state_district_production()
            
            
        else:
            print("invalid input")
            print("\a")
        print("")
        print("")
        i=input("Do you wish to continue yes or no:-")
        if i=='yes' or i=='YES':
            continue
        else:
            break
        


        

def heading():
    choice=0
    while choice!=4:
        print("        *************************************************************************************************************************************************")
        print("        *                                                       MAIN MENU(CROP PRODUCTION IN INDIA)                                                     *")
        print("        *************************************************************************************************************************************************")
        print("        *                                                                                                                                               *")
        print("        *                                                         press 1 : DISPLAY DATA.                                                               *")
        print("        *                                                         press 2 : DATA ANALYSIS.                                                              *")
        print("        *                                                         press 3 : DATA VISUALIZATION.                                                         *")
        print("        *                                                                                                                                               *")
        print("        *                                                                                                                                               *")
        print("        *************************************************************************************************************************************************")
        print("")
        print("")
        choice=int(input("Choose an option from main menu :  "))
        if choice==1:
            df=pd.read_csv("C:\janvi\python connectivity\cropp.csv")
            print("")
            print("")
            print(".............................................................. DISPLAY DATA ........................................................................")
            print("....................................................................................................................................................")
            print(" ")
            print("")
            print(df)
            print(df.columns)
            print("")
            print("")
            print(".....................................................................................................................................................")
            print(".....................................................................................................................................................")
        elif choice==2:
            data_analysis()
        elif choice==3:
            data_visualization()
        else:
            print("invalid input")
            print("\a")
        print("")
        print("")
        i=input("Do you want to go to main menu yes or no:-")
        if i=='yes' or i=='YES':
            continue
        else:
            break
heading()
            





   
    
    

    


    


        


        
