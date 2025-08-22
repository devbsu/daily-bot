# daily-bot
[개발자를 위한 DISCORD](https://discord.com/developers)

* [New Application] 생성

* [Bot] TOKEN 발급: 저장
<img width="1902" height="205" alt="image" src="https://github.com/user-attachments/assets/d27d98c4-b721-458e-af5d-e4862d999275" />

* [Bot] 접근 권한 체크
<img width="1909" height="358" alt="image" src="https://github.com/user-attachments/assets/5ae491b1-536a-4583-b8da-7340e0234bc8" />

* OAuth2 설정

**SCOPES**   
✔ bot
<img width="1920" height="357" alt="image" src="https://github.com/user-attachments/assets/81928399-43a6-4420-934b-4fa479d11be6" />

**TEXT PERMISSIONS**   
✔ Send Messages ✔ Create Public Threads ✔ Create Private Threads ✔ Send Messages in Threads
<img width="1910" height="784" alt="image" src="https://github.com/user-attachments/assets/9fd3f3db-c53d-4009-8254-fbe8ce76acb8" />

* GENERATED URL [Copy]
<img width="1370" height="197" alt="image" src="https://github.com/user-attachments/assets/2f126faf-5177-4fba-b71a-d2dd5c874017" />

* Copy한 URL 붙여넣어 서버에 봇 추가
<img width="1916" height="908" alt="image" src="https://github.com/user-attachments/assets/834d452b-f9c4-4055-8e52-1670c61371a9" />


* bot.py에서 channel_id 변경

```python
token = os.getenv("DISCORD_TOKEN") # Github Actions에 등록된 토큰
channel_id = 12345  # 메시지 보낼 디스코드 채널 ID로 변경
```

* Github Actions 설정
Settings > secrets and variables > Actions에 [DISCORD_TOKEN] 발급받은 토큰 등록
<img width="1130" height="306" alt="image" src="https://github.com/user-attachments/assets/0beec602-96ac-4b8f-a755-28a05ea0f864" />
