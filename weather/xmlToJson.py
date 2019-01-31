import json

RAW_XML = ([i.strip() for i in open("weather.xml").read().split('\n')[1:]])
def lastCheck(jsn):
    if(type(jsn)==type({})):
        for i in jsn.keys():
            if(len(jsn[i])==1 and type(jsn[i])==type({})):
                if(i in jsn[i].keys()):
                    jsn[i] = jsn[i][i][jsn[i][i].index('>')+1:jsn[i][i].index('<',2)]
            lastCheck(jsn[i])
        return jsn

def toDict(rtext):
    if(rtext[0]!=''):
        ans = {}
        #print("rtext",rtext[0])
        if('=' in rtext[0][:rtext[0].index('>')]):#have inner
            #print("Have inner")
            inner = str(rtext[0][rtext[0].index(' ')+1:rtext[0].index(f'>')])
            if(inner[-1]=='/'):
                inner = inner[:-2]
            while(inner!=''):
                #print(inner)
                cname = inner[:inner.index('=')]
                if(inner[inner.index('=')+1] == '"'):
                    cvalue = inner[inner.index('=')+2:inner.index('"',inner.index('=')+2)]
                else:
                    cvalue = ''
                ans[cname] = cvalue
                inner = inner[inner.index('"',inner.index('=')+2)+2:]
                #print(ans)
            ckey = rtext[0][1:rtext[0].index(' ')]
        else:
            ckey = rtext[0][1:rtext[0].index('>')]

        if("/" not in rtext[0]):
            i = 1
            tmp = {}
            while(rtext[i]!=f"</{ckey}>"):
                #print(rtext[i],f"</{ckey}>")
                #print(json.dumps(ans,indent=4, separators=(',', ': ')), rtext[i],f"</{ckey}>")
                #input()
                subans = toDict(rtext[i:])
                if(subans!=None and subans[0] not in tmp.keys() and subans[0][1:] not in ans.keys()):
                    ans[subans[0]] = subans[1]
                    tmp = subans[1]
                    #print(len(subans[1]))
                i+=1
        #print(ckey)
        #print(rtext[:rtext.index(f'</{ckey}>')])
        #print(rtext[:rtext.index(f'>')])
        if(ans == {}):
            ans = {ckey:rtext[0]}
        return[ckey,ans]
#print(toDict(RAW_XML)[1])
print(json.dumps(lastCheck(toDict(RAW_XML)[1]),indent=4, separators=(',', ': ')))