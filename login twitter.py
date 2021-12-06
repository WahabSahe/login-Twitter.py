from requests import post
headers = {
	"Host": "mobile.twitter.com",
	"x-guest-token": "1467951281234972683",
	"Accept": "*/*",
	"Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
	"x-twitter-client-language": "ar",
	"Accept-Language": "ar",
	"Content-Type": "application/json",
	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15",
	"x-csrf-token": "bf9f68ca28f922b50579116d896114d7",
	"x-twitter-active-user": "yes"
}
data = {"input_flow_data":{"flow_context":{"debug_overrides":{},"start_location":{"location":"unknown"}}},"subtask_versions":{"contacts_live_sync_permission_prompt":0,"email_verification":1,"topics_selector":1,"wait_spinner":1,"cta":4}}
Token = post("https://mobile.twitter.com/i/api/1.1/onboarding/task.json?flow_name=login", json=data, headers=headers).json()["flow_token"]
data = {"flow_token":Token,"subtask_inputs":[{"subtask_id":"LoginJsInstrumentationSubtask","js_instrumentation":{"response":"{\"rf\":{\"a31814228ea2f06a413eb10801ff48af2c29a3a35e0bcf8ca74a0025f69d90ba\":0,\"a08325feec32d07c1b443763792ee9652cca9d199b3d9543f070907ea55a66b2\":5,\"ea2a2efd3cb3f8b07b19e8283844caf6468dc4227e748f935a956719142f8980\":-1,\"ac8805f3750785f428a10891f367886cd6a4ba69a4d6c43ad6a529800f61e78a\":38},\"s\":\"1BO5FgIWGNCobmMOlOdEPKntp_KfHChMif5Is6s2FnMjOeU--QNcuXyYvDdLbCS3bk2jcchgr0RckdkI-7n5t6ebg299mUVLi4d2YAm1va_VD4tfTdPIA4tkrk7LUklskXR8r0zKN2wmzYEw7b2QwWFlPoV1cEshR6Ch_E1nVVKRnDmdSW6KL0DkVY5XQhjW8C2fwdTE-ewMXJ6y8upqmaoS4uE7BoRqE9kdWCivCePLXOtoftrv9eFDIGYkBZEtpsfUTTUVR5eOTEEteBrzJp72jnhBC08KMf9CizszYRCEZWIwocmSM2kOy4Pz1fNfZc4jJsFwmYsNRBh_qQtcWQAAAX2RbAbk\"}","link":"next_link"}}]}
Token = post("https://mobile.twitter.com/i/api/1.1/onboarding/task.json", json=data, headers=headers).json()["flow_token"]
data = {"flow_token":Token,"subtask_inputs":[{"subtask_id":"LoginEnterUserIdentifierSSOSubtask","settings_list":{"setting_responses":[{"key":"user_identifier","response_data":{"text_data":{"result":input("Username : ")}}}],"link":"next_link"}}]}
Token = post("https://mobile.twitter.com/i/api/1.1/onboarding/task.json", json=data, headers=headers).json()["flow_token"]
data = {"flow_token":Token,"subtask_inputs":[{"subtask_id":"AccountDuplicationCheck","check_logged_in_account":{"link":"AccountDuplicationCheck_false"}}]}
Token = post("https://mobile.twitter.com/i/api/1.1/onboarding/task.json", json=data, headers=headers).json()["flow_token"]
data = {"flow_token":Token,"subtask_inputs":[{"subtask_id":"LoginEnterPassword","enter_password":{"password":input("Password : "),"link":"next_link"}}]}
print(post("https://mobile.twitter.com/i/api/1.1/onboarding/task.json", json=data, headers=headers).json())
