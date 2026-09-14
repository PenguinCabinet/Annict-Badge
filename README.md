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
