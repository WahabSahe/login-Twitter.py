from requests import post
# By Sahe-Wahab (Uhoe)
headers = {
	"Content-Type":"application/x-www-form-urlencoded",
	"User-Agent": "TwitterAndroid/8.95.0-release.00 (28950000-r-0) A5010/7.1.2 (OnePlus;A5010;OnePlus;A5010;0;;1;2013)",
	"Timezone": "Asia/Shanghai",
	"Accept": "application/json",
	"Authorization": "Basic M25WdVNvQlpueDZVNHZ6VXhmNXc6QmNzNTlFRmJic2RGNlNsOU5nNzFzbWdTdFdFR3dYWEtTall2UFZ0N3F5cw==" 
}
Token = post("https://api.twitter.com/oauth2/token", data={"grant_type":"client_credentials"}, headers=headers).json()["access_token"]
headers = {
	"Content-Type":"text/plain",
	"User-Agent": "TwitterAndroid/8.95.0-release.00 (28950000-r-0) A5010/7.1.2 (OnePlus;A5010;OnePlus;A5010;0;;1;2013)",
	"Timezone": "Asia/Shanghai",
	"Accept": "application/json",
	"Authorization": f"Bearer {Token}"
}
Guest = post("https://api.twitter.com/1.1/guest/activate.json", headers=headers).json()["guest_token"]
headers = {
	"Content-Type":"application/x-www-form-urlencoded",
	"User-Agent": "TwitterAndroid/8.95.0-release.00 (28950000-r-0) A5010/7.1.2 (OnePlus;A5010;OnePlus;A5010;0;;1;2013)",
	"Timezone": "Asia/Shanghai",
	"Accept": "application/json",
	"X-Guest-Token":Guest,
	"Authorization": f"Bearer {Token}"
}
User = input(" User Or Email : ")
Pass = input(" Password : ")
Login = post("https://api.twitter.com/auth/1/xauth_password.json", headers=headers, data=f"x_auth_identifier={User}&x_auth_password={Pass}&send_error_codes=true&x_auth_login_challenge=1&x_auth_login_verification=1&ui_metrics=").text
if "oauth_token" in Login:
	print(" Success Login")
elif "parameter is missing" in Login or "Could not authenticate you" in Login:
	print(" Failure Login")
elif "login_verification_request_id" in Login:
	print(" Custom Login")
