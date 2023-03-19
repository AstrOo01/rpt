import re,requests
import time
from os import system
import re
import time
from libs .user_agents import get_user_agent 
import time
Z = '\033[1;31m' #ر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m'
rrep='"status_code":0,"status_msg":"Thanks for your feedback"'
print(X+'''
  ____                       _    
 |  _ \ ___ _ __   ___  _ __| |_  
 | |_) / _ \ '_ \ / _ \| '__| __| 
 |  _ <  __/ |_) | (_) | |  | |_  
 |_| \_\___| .__/ \___/|_|   \__| 
           |_|         Tiktok
- By ASTRO / DARK
- instagram : @ab_dou01
- My Tiktok : t.me/ab.dou_48
1-[report content]
2-[spam and fake engagement]
3-[user could be under 13 years old]
4-[Fake Information]
5-[hateful behavior]
6-[adult nudity and sexual activies]
7-[Terrorist, criminal, and hateful organizations]
8-[Suicide and self-harm]
9-[Bullying and harassment]
10-[Violent and graphic content]
------------------------------------------	''')
astro =int(input(B+"chose report:"))
if astro >=11:
	print(Z+f'number not found {astro}')
	exit('instagram : @ab_dou01')
session = input(B+'? set your session id : \n')
user=input(B+'? set target user :\n')
sleep = int(input(B+'? set delay [5/10] : \n'))
url = 'https://api16-normal-c-alisg.tiktokv.com/passport/account/info/v2/?scene=normal&multi_login=1&account_sdk_soupp&passport-sdk-version=19&os_api=25&device_type=A5010&ssmix=a&manifest_version_code=2018093009&dpi=191&carrier_region=JO&uoo=1&region=US&app_name=musical_ly&version_name=7.1.2&timezone_offset=28800&ts=1628767214&ab_version=7.1.2&residence=SA&cpu_support64=false&current_region=JO&ac2=wifi&ac=wifi&app_type=normal&host_abi=armeabi-v7a&channel=googleplay&update_version_code=2018093009&_rticket=1628767221573&device_platform=android&iid=7396386396296286392&build_number=7.1.2&locale=en&op_region=SA&version_code=200705&timezone_name=Asia%2FShanghai&cdid=f61ca549-c9ee-450b-90da-8854423b74e7&openudid=3e5afbd3f6dde322&sys_region=US&device_id=7296396296396396393&app_language=en&resolution=576*1024&device_brand=OnePlus&language=en&os_version=7.1.2&aid=1233&mcc_mnc=2947'

headers={'Host': 'api16-normal-c-alisg.tiktokv.com', 'Cookie': 'sessionid='+session,'Accept-Encoding': 'gzip, deflate',
'User-Agent': get_user_agent()}
re = requests.get(url,headers=headers)
if '"session expired, please sign in again"' in re.text:
	print(Z+'session id errour [!]')
	exit(0)
elif 'user_id' in re.text:
	useo = str(re.json()['data']['user_id']) 
#i
#==========lol=============9
head={
'Host': 'www.tiktok.com',
'User-Agent': get_user_agent(),
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
'Accept-Encoding': 'gzip, deflate',
'Upgrade-Insecure-Requests': '1',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'Te': 'trailers',
'Connection': 'close',
}

user = 'exampleuser'
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
# Get user ID
req = requests.get(f'https://www.tiktok.com/@{user}?lang=ar', headers=head)
try:
    user_id = re.findall('''"user":{"id":"(.*?)"''', req.text)[0]
    print(user_id)
except:
    print('user not found / banned')

if astro==1:
	while True:
		time.sleep(sleep)
		url = f'https://www.tiktok.com/aweme/v2/aweme/feedback/?aid=1988&app_language=en&app_name=tiktok_web&battery_info=1&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36&channel=tiktok_web&cookie_enabled=true&current_region=MA&device_id=7208628865014138374&device_platform=web_pc&focus_state=true&from_page=user&history_len=11&is_fullscreen=false&is_page_visible=true&lang=en&nickname=🖤Malak🐍&object_id=7153975578554991621&os=windows&owner_id=7153975578554991621&priority_region=MA&reason=9002&referer=&region=MA&report_type=user&reporter_id=7208629228966757382&screen_height=900&screen_width=1600&secUid=MS4wLjABAAAADipJjxMSLAh-97MYlht4ufYnJkSii95cacALzv4Li1gZlE_kgzL4RHaRcX0WPD2S&target=7153975578554991621&tz_name=America/Los_Angeles&verifyFp=verify_lf219hyq_a3xmlT0o_VNt6_457w_9pjO_6zaRoLOafKnM&webcast_language=en'
		hea_rep = {
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
			'Accept-Encoding':'gzip, deflate, br',
			'Accept-Language':'en-US,en;q=0.5',
			'Connection':'keep-alive',
			'Cookie':'sessionid='+session,
			'Host':'www.tiktok.com',
			'Sec-Fetch-Dest':'document',
			'Sec-Fetch-Mode': 'navigate',
			'Sec-Fetch-Site':'none',
			'Sec-Fetch-User':'?1',
			'Upgrade-Insecure-Requests':'1',
			'User-Agent' : get_user_agent()}
		data={
			"object_id":id,
			"owner_id":id,
			"report_type":"user",
			"target":id}
		rept = requests.post(url,headers=hea_rep,data=data)
		if rrep in rept.text:
			print(Z+"[!] An error has occurred..")
		else:
			print(F+"[+] repport succecs ")	
elif astro ==2:
	while True:
		time.sleep(sleep)
		url2=f'https://www.tiktok.com/aweme/v2/aweme/feedback/?aid=1988&app_language=en&app_name=tiktok_web&battery_info=1&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36&channel=tiktok_web&cookie_enabled=true&current_region=MA&device_id=7208628865014138374&device_platform=web_pc&focus_state=true&from_page=user&history_len=11&is_fullscreen=false&is_page_visible=true&lang=en&nickname=🖤Malak🐍&object_id=7153975578554991621&os=windows&owner_id=7153975578554991621&priority_region=MA&reason=90081&referer=&region=MA&report_type=user&reporter_id=7208629228966757382&screen_height=900&screen_width=1600&secUid=MS4wLjABAAAADipJjxMSLAh-97MYlht4ufYnJkSii95cacALzv4Li1gZlE_kgzL4RHaRcX0WPD2S&target=7153975578554991621&tz_name=America/Los_Angeles&verifyFp=verify_lf219hyq_a3xmlT0o_VNt6_457w_9pjO_6zaRoLOafKnM&webcast_language=en'
		hea_rep2 = {
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
			'Accept-Encoding':'gzip, deflate, br',
			'Accept-Language':'en-US,en;q=0.5',
			'Connection':'keep-alive',
			'Cookie':'sessionid='+session,
			'Host':'www.tiktok.com',
			'Sec-Fetch-Dest':'document',
			'Sec-Fetch-Mode': 'navigate',
			'Sec-Fetch-Site':'none',
			'Sec-Fetch-User':'?1',
			'Upgrade-Insecure-Requests':'1',
			'User-Agent' : get_user_agent()}
		data2={
			"object_id":id,
			"owner_id":id,
			"report_type":"user",
			"target":id}
		rept2 = requests.post(url2,headers=hea_rep2,data=data2)
		if rrep in rept2.text:
			print(Z+"[!] An error has occurred..")
		else:
			print(F+"[+] Repport succecs ")	
elif astro==3:
	while True:
		time.sleep(sleep)
		url3=f'https://www.tiktok.com/aweme/v1/aweme/feedback/?aid=1233&app_name=tiktok_web&device_platform=web_mobile&device_id=7008218736944907778&region=SA&priority_region=SA&os=ios&referer=https:%2F%2Fwww.tiktok.com%2Fsetting&root_referer=https:%2F%2Fwww.tiktok.com%2F&cookie_enabled=true&screen_width=375&screen_height=667&browser_language=en-US&browser_platform=iPhone&browser_name=Mozilla&browser_version=5.0+(iPhone%3B+CPU+iPhone+OS+15_0_1+like+Mac+OS+X)+AppleWebKit%2F605.1.15+(KHTML,+like+Gecko)+InspectBrowser&browser_online=true&verifyFp=verify_kvxyp4rs_dANMHnrG_lvVu_4qPI_97cp_HhJjttqMJhNK&app_language=en&timezone_name=Asia%2FRiyadh&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=10&reason=317&report_type=user&object_id={id}&owner_id={id}&target={id}&reporter_id=27568146&current_region=SA'
		hea_rep3 = {
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
			'Accept-Encoding':'gzip, deflate, br',
			'Accept-Language':'en-US,en;q=0.5',
			'Connection':'keep-alive',
			'Cookie':'sessionid='+session,
			'Host':'www.tiktok.com',
			'Sec-Fetch-Dest':'document',
			'Sec-Fetch-Mode': 'navigate',
			'Sec-Fetch-Site':'none',
			'Sec-Fetch-User':'?1',
			'Upgrade-Insecure-Requests':'1',
			'User-Agent':  get_user_agent()}
		data3={
			"object_id":id,
			"owner_id":id,
			"report_type":"user",
			"target":id}
		rept3 = requests.post(url3,headers=hea_rep3,data=data3)
		if rrep in rept3.text:
			print(Z+"[!] An error has occurred..")
		else:
			print(F+"[+] Repport succecs ")
elif astro==4:
	while True:
		time.sleep(sleep)
		url4=f'https://www.tiktok.com/aweme/v2/aweme/feedback/?aid=1988&app_language=en&app_name=tiktok_web&battery_info=1&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20(Windows%20NT%2010.0;%20Win64;%20x64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/109.0.0.0%20Safari/537.36&channel=tiktok_web&cookie_enabled=true&current_region=MA&device_id=7208628865014138374&device_platform=web_pc&focus_state=true&from_page=user&history_len=11&is_fullscreen=false&is_page_visible=true&lang=en&nickname=%F0%9F%96%A4Malak%F0%9F%90%8D&object_id=7153975578554991621&os=windows&owner_id=7153975578554991621&priority_region=MA&reason=1001&referer=&region=MA&report_type=user&reporter_id=7208629228966757382&screen_height=900&screen_width=1600&secUid=MS4wLjABAAAADipJjxMSLAh-97MYlht4ufYnJkSii95cacALzv4Li1gZlE_kgzL4RHaRcX0WPD2S&target=7153975578554991621&tz_name=America/Los_Angeles&verifyFp=verify_lf219hyq_a3xmlT0o_VNt6_457w_9pjO_6zaRoLOafKnM&webcast_language=en'
		hea_rep4 = {
				'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
				'Accept-Encoding':'gzip, deflate, br',
				'Accept-Language':'en-US,en;q=0.5',
				'Connection':'keep-alive',
				'Cookie':'sessionid='+session,
				'Host':'www.tiktok.com',
				'Sec-Fetch-Dest':'document',
				'Sec-Fetch-Mode': 'navigate',
				'Sec-Fetch-Site':'none',
				'Sec-Fetch-User':'?1',
				'Upgrade-Insecure-Requests':'1',
				'User-Agent' : get_user_agent()}
		data4={
			"object_id":id,
			"owner_id":id,
			"report_type":"user",
			"target":id}
		rept4 = requests.post(url4,headers=hea_rep4,data=data4)
		if rrep in rept4.text:
			print(Z+"[!] An error has occurred..")
		else:
			print(F+"[+] Repport succecs ")	
elif astro==5:
	while True:
		time.sleep(sleep)
		url5=f'https://www.tiktok.com/aweme/v1/aweme/feedback/?aid=1233&app_name=tiktok_web&device_platform=web_mobile&device_id=7034110346035136001&region=SA&priority_region=SA&os=ios&referer=https:%2F%2Fwww.tiktok.com%2Fsetting&root_referer=https:%2F%2Fwww.tiktok.com%2Fsetting&cookie_enabled=true&screen_width=375&screen_height=667&browser_language=en-US&browser_platform=iPhone&browser_name=Mozilla&browser_version=5.0+(iPhone%3B+CPU+iPhone+OS+15_1+like+Mac+OS+X)+AppleWebKit%2F605.1.15+(KHTML,+like+Gecko)+InspectBrowser&browser_online=true&verifyFp=verify_kx800pjx_bJTxKplQ_YGw2_4nQz_9ti1_lo63INRiR3i0&app_language=ar&timezone_name=Asia%2FRiyadh&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=7&reason=306&report_type=user&object_id={id}&owner_id={id}&target={id}&reporter_id=6955107540677968897&current_region=SA'
		hea_rep5 = {
				'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
				'Accept-Encoding':'gzip, deflate, br',
				'Accept-Language':'en-US,en;q=0.5',
				'Connection':'keep-alive',
				'Cookie':'sessionid='+session,
				'Host':'www.tiktok.com',
				'Sec-Fetch-Dest':'document',
				'Sec-Fetch-Mode': 'navigate',
				'Sec-Fetch-Site':'none',
				'Sec-Fetch-User':'?1',
				'Upgrade-Insecure-Requests':'1',
				'User-Agent' : get_user_agent()}
		data5={
			"object_id":id,
			"owner_id":id,
			"report_type":"user",
			"target":id}
		rept5 = requests.post(url5,headers=hea_rep5,data=data5)
		if rrep in rept5.text:
			print(Z+"[!] An error has occurred..")
		else:
			print(F+"[+] Repport succecs ")
elif astro==6:
	while True:
		time.sleep(sleep)
		url6=f'https://www.tiktok.com/aweme/v1/aweme/feedback/?aid=1233&app_name=tiktok_web&device_platform=web_mobile&device_id=7034110346035136001&region=SA&priority_region=SA&os=ios&referer=https:%2F%2Fwww.tiktok.com%2Flogin%2Fphone-or-email%3Fenter_method%3Denter_personal_homepage%26lang%3Den%26launch_type%3D0%26redirect_url%3Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fprofile%25253Flang%25253Den%26enter_from%3Dpersonal_homepage&root_referer=https:%2F%2Fwww.tiktok.com%2Fsetting&cookie_enabled=true&screen_width=375&screen_height=667&browser_language=en-US&browser_platform=iPhone&browser_name=Mozilla&browser_version=5.0+(iPhone%3B+CPU+iPhone+OS+15_1+like+Mac+OS+X)+AppleWebKit%2F605.1.15+(KHTML,+like+Gecko)+InspectBrowser&browser_online=true&verifyFp=verify_kx800pjx_bJTxKplQ_YGw2_4nQz_9ti1_lo63INRiR3i0&app_language=ar&timezone_name=Asia%2FRiyadh&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=14&reason=308&report_type=user&object_id={id}&owner_id={id}&target={id}&reporter_id=310430566162530304&current_region=SA'
		hea_rep6 = {
				'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
				'Accept-Encoding':'gzip, deflate, br',
				'Accept-Language':'en-US,en;q=0.5',
				'Connection':'keep-alive',
				'Cookie':'sessionid='+session,
				'Host':'www.tiktok.com',
				'Sec-Fetch-Dest':'document',
				'Sec-Fetch-Mode': 'navigate',
				'Sec-Fetch-Site':'none',
				'Sec-Fetch-User':'?1',
				'Upgrade-Insecure-Requests':'1',
				'User-Agent' : get_user_agent()}
		data6={
			"object_id":id,
			"owner_id":id,
			"report_type":"user",
			"target":id}
		rept6 = requests.post(url6,headers=hea_rep6,data=data6)
		if rrep in rept6.text:
			print(Z+"[!] An error has occurred..")
		else:
			print(F+"[+] Repport succecs ")
elif astro==7:
	while True:
		time.sleep(sleep)
		url7=f'https://www.tiktok.com/aweme/v1/aweme/feedback/?aid=1233&app_name=tiktok_web&device_platform=web_mobile&device_id=7034110346035136001&region=SA&priority_region=SA&os=ios&referer=https:%2F%2Fwww.tiktok.com%2Flogin%2Fphone-or-email%3Fenter_method%3Denter_personal_homepage%26lang%3Den%26launch_type%3D0%26redirect_url%3Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fprofile%25253Flang%25253Den%26enter_from%3Dpersonal_homepage&root_referer=https:%2F%2Fwww.tiktok.com%2Fsetting&cookie_enabled=true&screen_width=375&screen_height=667&browser_language=en-US&browser_platform=iPhone&browser_name=Mozilla&browser_version=5.0+(iPhone%3B+CPU+iPhone+OS+15_1+like+Mac+OS+X)+AppleWebKit%2F605.1.15+(KHTML,+like+Gecko)+InspectBrowser&browser_online=true&verifyFp=verify_kx800pjx_bJTxKplQ_YGw2_4nQz_9ti1_lo63INRiR3i0&app_language=ar&timezone_name=Asia%2FRiyadh&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=14&reason=3011&report_type=user&object_id={id}&owner_id={id}&target={id}&reporter_id=310430566162530304&current_region=SA'
		hea_rep7 = {
				'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
				'Accept-Encoding':'gzip, deflate, br',
				'Accept-Language':'en-US,en;q=0.5',
				'Connection':'keep-alive',
				'Cookie':'sessionid='+session,
				'Host':'www.tiktok.com',
				'Sec-Fetch-Dest':'document',
				'Sec-Fetch-Mode': 'navigate',
				'Sec-Fetch-Site':'none',
				'Sec-Fetch-User':'?1',
				'Upgrade-Insecure-Requests':'1',
				'User-Agent' : get_user_agent()}
		data7={
			"object_id":id,
			"owner_id":id,
			"report_type":"user",
			"target":id}
		rept7 = requests.post(url7,headers=hea_rep7,data=data7)
		if rrep in rept7.text:
			print(Z+"[!] An error has occurred..")
		else:
			print(F+"[+] Repport succecs ")
elif astro==8:
	while True:
		time.sleep(sleep)
		url8=f'https://www.tiktok.com/aweme/v1/aweme/feedback/?aid=1233&app_name=tiktok_web&device_platform=web_mobile&device_id=7034110346035136001&region=SA&priority_region=SA&os=ios&referer=https:%2F%2Fwww.tiktok.com%2Flogin%2Fphone-or-email%3Fenter_method%3Denter_personal_homepage%26lang%3Den%26launch_type%3D0%26redirect_url%3Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fprofile%25253Flang%25253Den%26enter_from%3Dpersonal_homepage&root_referer=https:%2F%2Fwww.tiktok.com%2Fsetting&cookie_enabled=true&screen_width=375&screen_height=667&browser_language=en-US&browser_platform=iPhone&browser_name=Mozilla&browser_version=5.0+(iPhone%3B+CPU+iPhone+OS+15_1+like+Mac+OS+X)+AppleWebKit%2F605.1.15+(KHTML,+like+Gecko)+InspectBrowser&browser_online=true&verifyFp=verify_kx800pjx_bJTxKplQ_YGw2_4nQz_9ti1_lo63INRiR3i0&app_language=ar&timezone_name=Asia%2FRiyadh&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=14&reason=3052&report_type=user&object_id={id}&owner_id={id}&target={id}&reporter_id=310430566162530304&current_region=SA'
		hea_rep8 = {
				'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
				'Accept-Encoding':'gzip, deflate, br',
				'Accept-Language':'en-US,en;q=0.5',
				'Connection':'keep-alive',
				'Cookie':'sessionid='+session,
				'Host':'www.tiktok.com',
				'Sec-Fetch-Dest':'document',
				'Sec-Fetch-Mode': 'navigate',
				'Sec-Fetch-Site':'none',
				'Sec-Fetch-User':'?1',
				'Upgrade-Insecure-Requests':'1',
				'User-Agent' : get_user_agent()}
		data8={
			"object_id":id,
			"owner_id":id,
			"report_type":"user",
			"target":id}
		rept8 = requests.post(url8,headers=hea_rep8,data=data8)
		if rrep in rept8.text:
			print(Z+"[!] An error has occurred..")
		else:
			print(F+"[+] Repport succecs ")
elif astro==9:
	while True:
		time.sleep(sleep)
		url9=f'https://www.tiktok.com/aweme/v1/aweme/feedback/?aid=1233&app_name=tiktok_web&device_platform=web_mobile&device_id=7034110346035136001&region=SA&priority_region=SA&os=ios&referer=https:%2F%2Fwww.tiktok.com%2Flogin%2Fphone-or-email%3Fenter_method%3Denter_personal_homepage%26lang%3Den%26launch_type%3D0%26redirect_url%3Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fprofile%25253Flang%25253Den%26enter_from%3Dpersonal_homepage&root_referer=https:%2F%2Fwww.tiktok.com%2Fsetting&cookie_enabled=true&screen_width=375&screen_height=667&browser_language=en-US&browser_platform=iPhone&browser_name=Mozilla&browser_version=5.0+(iPhone%3B+CPU+iPhone+OS+15_1+like+Mac+OS+X)+AppleWebKit%2F605.1.15+(KHTML,+like+Gecko)+InspectBrowser&browser_online=true&verifyFp=verify_kx800pjx_bJTxKplQ_YGw2_4nQz_9ti1_lo63INRiR3i0&app_language=ar&timezone_name=Asia%2FRiyadh&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=14&reason=3072&report_type=user&object_id={id}&owner_id={id}&target={id}&reporter_id=310430566162530304&current_region=SA'
		hea_rep9 = {
				'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
				'Accept-Encoding':'gzip, deflate, br',
				'Accept-Language':'en-US,en;q=0.5',
				'Connection':'keep-alive',
				'Cookie':'sessionid='+session,
				'Host':'www.tiktok.com',
				'Sec-Fetch-Dest':'document',
				'Sec-Fetch-Mode': 'navigate',
				'Sec-Fetch-Site':'none',
				'Sec-Fetch-User':'?1',
				'Upgrade-Insecure-Requests':'1',
				'User-Agent' : get_user_agent()}
		data9={
			"object_id":id,
			"owner_id":id,
			"report_type":"user",
			"target":id}
		rept9 = requests.post(url9,headers=hea_rep9,data=data9)
		if rrep in rept9.text:
			print(Z+"[!] An error has occurred..")
		else:
			print(F+"[+] Repport succecs ")
elif astro==10:
	while True:
		time.sleep(sleep)
		url10=f'https://www.tiktok.com/aweme/v1/aweme/feedback/?aid=1233&app_name=tiktok_web&device_platform=web_mobile&device_id=7034110346035136001&region=SA&priority_region=SA&os=ios&referer=https:%2F%2Fwww.tiktok.com%2Flogin%2Fphone-or-email%3Fenter_method%3Denter_personal_homepage%26lang%3Den%26launch_type%3D0%26redirect_url%3Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fprofile%25253Flang%25253Den%26enter_from%3Dpersonal_homepage&root_referer=https:%2F%2Fwww.tiktok.com%2Fsetting&cookie_enabled=true&screen_width=375&screen_height=667&browser_language=en-US&browser_platform=iPhone&browser_name=Mozilla&browser_version=5.0+(iPhone%3B+CPU+iPhone+OS+15_1+like+Mac+OS+X)+AppleWebKit%2F605.1.15+(KHTML,+like+Gecko)+InspectBrowser&browser_online=true&verifyFp=verify_kx800pjx_bJTxKplQ_YGw2_4nQz_9ti1_lo63INRiR3i0&app_language=ar&timezone_name=Asia%2FRiyadh&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=14&reason=303&report_type=user&object_id={id}&owner_id={id}&target={id}&reporter_id=310430566162530304&current_region=SA'
	hea_rep10 = {
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
			'Accept-Encoding':'gzip, deflate, br',
			'Accept-Language':'en-US,en;q=0.5',
			'Connection':'keep-alive',
			'Cookie':'sessionid='+session,
			'Host':'www.tiktok.com',
			'Sec-Fetch-Dest':'document',
			'Sec-Fetch-Mode': 'navigate',
			'Sec-Fetch-Site':'none',
			'Sec-Fetch-User':'?1',
			'Upgrade-Insecure-Requests':'1',
			'User-Agent' : get_user_agent()}
	data10={
		"object_id":id,
		"owner_id":id,
		"report_type":"user",
		"target":id}
	rept10 = requests.post(url10,headers=hea_rep10,data=data10)
	if rrep in rept10.text:
		print(Z+"[!] An error has occurred..")
	else:
		print(F+"[+] Repport succecs " )
