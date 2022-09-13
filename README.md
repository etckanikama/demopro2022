# 環境
- python3.8.10

自分の場合は、demopro2022/yolov5内で以下を実行して環境を作成している
```
pyenv activate 3.7.2
```
(python3.6.2より前のバージョンはtorchが入らないので注意, pyenvとかvirtualenvの環境を作ってください)
- ubuntu20.04
- yolov5

# インストール手順

```
git clone https://github.com/ultralytics/yolov5
```


```
cd yolov5/
pip install -r requirements.txt
```

#### webカメラ（内部カメラ）で学習済みモデルで検証する方法</br>
```
cd yolov5
python detect.py --source 0 --conf 0.5 --weights yolov5s.pt
```

#### 自前の画像や動画を検証する方法<br>
yolov5/data/imagesの中にpng,jpg,mp4のいずれかを追加して,
以下のコマンドで実行(person_screem.mp4は自分の画像名に適宜変更)
```
cd yolov5
python detect.py --source data/images/person_screem.mp4 --conf 0.5 --weights yolov5s.pt
```
実行結果<br>
yolov5/runs/detectの中にexp(数字があるどれか)に実行結果が入ってる


# labelの対応付
yolov5/data/coco.yamlの中

0番ならperson


# 参考資料
https://qiita.com/suginaga/items/468ea7d232b8a24501bf

https://human-blog.com/%E3%83%AA%E3%82%A2%E3%83%AB%E3%82%BF%E3%82%A4%E3%83%A0%E7%89%A9%E4%BD%93%E6%A4%9C%E5%87%BA%EF%BC%86%E3%83%8F%E3%83%95%E5%A4%89%E6%8F%9B/


https://note.com/npaka/n/n371912b48ee2