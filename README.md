# Thundermeet
Thundermeet 是針對有相約時間需求的用戶，我們提供 Google 行事曆和內部活動間的匯入匯出、參與時間優先度區分、簡便篩選特定參與者或時間優先度、個人頁面活動整合等功能，透過 Thundermeet 的平台，我們希望能有效解決使用者在相約時間時會遇到的困擾，給用戶在過程中更好的使用者體驗。

## notification
因為像是註冊、填寫event、修改event等行為是不能被重複的，所以我們有些selenium code 是不能被重複的執行的，例如註冊流程如果被執行第二遍就會報錯，該使用者已存在，所以如果有執行多次的需要的話可能需要在有"send_keys"的地方將傳入的資料修改一下再執行。

## Getting Started
1.clone this repository<br>
git clone https://github.com/viola50420/thunderMeet_pytest<br>
2.Open your terminal and run `pip instsall selenium`<br>
3.`cd` to this repository<br>
4.if selenium is successfully installed, than run `python -i 'testcase'.py`<br>

## tested Features
### signup
在首頁註冊一個使用者的流程
### forgetPassword
在首頁中reset 使用者密碼的流程
### editprofile&groups
在個人頁面中編輯個人信息和活動分組
### addevent
登入後創建一個活動的流程
### editevent
編輯一個曾經創建的活動
### fillin&addTogroup
填寫一個欲參加的活動並從過去參加過的活動import 可參與的時間，並將它加入一個活動分組的流程
