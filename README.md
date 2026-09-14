[![My Annict watched animes](https://annict.penguincabinet.com/?user_id=PenguinCabinet&type=watched_count)](https://annict.com/@PenguinCabinet) [![My Annict create at](https://annict.penguincabinet.com/?user_id=PenguinCabinet&type=created_at)](https://annict.com/@PenguinCabinet) [![My Annict followers](https://annict.penguincabinet.com/?user_id=PenguinCabinet&type=followers_count)](https://annict.com/@PenguinCabinet)



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
