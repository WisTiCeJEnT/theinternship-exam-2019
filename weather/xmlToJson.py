import json

RAW_XML = ([i.strip() for i in open("weather.xml").read().split('\n')[1:]])
def toDict(rtext):
    if(rtext[0]!=''):
        ans = {}
        print("rtext",rtext[0])
        if('=' in rtext[0][:rtext[0].index('>')]):#have inner
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
            while(rtext[i]!=f"</{ckey}>"):
                #print(ans,rtext[i],f"</{ckey}>")
                #print(json.dumps(ans,indent=4, separators=(',', ': ')), rtext[i],f"</{ckey}>")
                #input()
                subans = toDict(rtext[i:])
                if(subans!=None):
                    ans[subans[0]] = subans[1]
                i+=1
        #print(ckey)
        #print(rtext[:rtext.index(f'</{ckey}>')])
        #print(rtext[:rtext.index(f'>')])
        return[ckey,ans]
print()
print(json.dumps(toDict(RAW_XML)[1],indent=4, separators=(',', ': ')))