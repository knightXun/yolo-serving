## 构建docker镜像

docker build -t . knightxun/yolo .

## 运行

docker run -d -p 8888:8888 knightxun/yolo 

## 测试
```
curl -F "file=@/mnt/e/download/yolo3-keras/image/smoke_10.jpg" http://172.20.167.207:8888/predict
```
结果
```
"{\"objects\": [{\"xmin\": \"170\", \"xmax\": \"0\", \"ymin\": \"207\", \"ymax\": \"83\", \"name\": \"smoke\"}]}"
```