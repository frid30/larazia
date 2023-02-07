from capmonster_python import RecaptchaV2Task,RecaptchaV3Task

url = "https://login.yahoo.com/account/challenge/recaptcha/redirect?.intl=uk&intl=uk&.lang=en-GB&src=homepage&specId=yidregsimplified&activity=ybar-signin&pspid=2023392312&done=https%3A%2F%2Fuk.yahoo.com%2F%3Fp%3Dus%26guccounter%3D1&context=reg&authMechanism=reg&authCredentialsType=WyJjb29raWVzIl0%3D&sessionIndex=Qg--&acrumb=DpNTndDC&lang=en-GB&siteKey=6Ldbp6saAAAAAAwuhsFeAysZKjR319pRcKUitPUO&recaptchaLang=en-GB&recaptchaDomain=www.google.com"
capmonster = RecaptchaV2Task("5d4fc8d721ca7365258b20e9de8c06fc")
task_id = capmonster.create_task(
    url,    "6Ldbp6saAAAAAAwuhsFeAysZKjR319pRcKUitPUO")
result = capmonster.join_task_result(task_id)
a = result.get("gRecaptchaResponse")
print(a)
