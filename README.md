<img width="553" height="45" alt="https___qiita-image-store s3 ap-northeast-1 amazonaws com_0_206651_e4307854-d0b8-3dcf-4870-09e91a810168" src="https://github.com/user-attachments/assets/acfff94a-de11-41af-8899-480a555159a6" />

# 👏Annict-Badge
[Annict](https://annict.com/)のユーザーデータをShields Badgeにして表示します。   

## 🔨使い方
[詳しくはこちらの記事をご覧ください](https://qiita.com/PenguinCabinet/items/6cdb6db6a5f8083295e5)。
```
https://annict.penguincabinet.com/?user_id=<user_id>&type=<type>&style=<style>
```

## セルフホスト
```
echo -n "<annict-api-key>" | gcloud secrets create annict-badge-key --data-file=-
make deploy
```
