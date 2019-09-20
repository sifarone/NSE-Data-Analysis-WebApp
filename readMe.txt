mongodb version     : 4.0.10
mongoengine version : 0.18.0
Python version      : 3.7.1
Flask Version       : 1.0.2
flask-wtf           :
motor               : 2.0.0 (asyncio based mongodb driver)
aiohttp             : 3.5.4 (http server based on asyncio)
redis-Server        : 3.0.6
python 3.7 redis    : 3.3.4
pyjwt               :

Python3.7 pip Install commands ---------------------------------------------
python3 -m pip install pymongo
sudo python3.7 -m pip install mongoengine
sudo python3.7 -m pip install flask

GIT: ---------------------------------------------
git rm -r --cached ./k8s/issuer.yaml 

robomongo gui: -------------------------------------------
/usr/local/bin/robo3t/bin$ ./robo3t

Mongo db backup: --------------------------------------------------------------
 - use <database-name>
 - db.stats().dataSize
exit out of mongo shell
 $ mongodump -d <database-name> -o <path where the backup needs to be created>

 $ mongodump --out ./     < --- this works

Restoring from mongodb backup:
 $ mongorestore <backed up file path>

 $ mongorestore -d MasterStockData_DB MasterStockData_DB    <--- this works

MongoDB Indexes: --------------------------------------------------------------

STKOPT INDEXES:
 db.StockOptionsData_C.ensureIndex({symbol:1, expiryDate:1, strikePrice:1})
 db.StockOptionsData_C.ensureIndex({symbol:1, expiryDate:1})
 db.StockOptionsData_C.ensureIndex({symbol:1})

 db.IndexOptionsData_C.ensureIndex({symbol:1, expiryDate:1, strikePrice:1})
 db.IndexOptionsData_C.ensureIndex({symbol:1, expiryDate:1})
 db.IndexOptionsData_C.ensureIndex({symbol:1})

 db.StockFuturesData_C.ensureIndex({symbol:1, expiryDate:1})
 db.StockFuturesData_C.ensureIndex({symbol:1})

 db.IndexFuturesData_C.ensureIndex({symbol:1, expiryDate:1})
 db.IndexFuturesData_C.ensureIndex({symbol:1})

 db.StockBhavData_C.ensureIndex({symbol:1})

 db.StockOptionsData_C.ensureIndex({symbol:1, expiryDate:1, strikePrice:1})


Docker Hub: ---------------------------------------------------------------

docker build -t sifarone/eod_analysis:read-server-1.0 .
docker push sifarone/eod_analysis:read-server-1.0

Kubectl -------------------------------------------------------------------

kubectl create secret docker-registry regcred --docker-server=https://cloud.docker.com/repository/docker/sifarone/eod_analysis --docker-username=sifarone --docker-password=<gl@123> --docker-email=just.naushad@gmail.com

kubectl apply -f write-server-deployment.yaml
kubectl delete -f write-server-deployment.yaml

kubectl describe pod write-server-deployment-55cf74cc6-8hkwz
kubectl logs write-server-deployment-55cf74cc6-8hkwz

kubectl cp ./31Aug2019 mongodb-deploymnet-7f4c659f94-xlk8h:/

Minikube ---------------------------------------------------------------

eval $(minikube docker-env)


ERRORs -----------------------------------------------------------------
{"LOAD_DATA": {"Error": {"ERROR": "No columns to parse from file"}}}

<html>
<head><title>504 Gateway Time-out</title></head>
<body>
<center><h1>504 Gateway Time-out</h1></center>
<hr><center>openresty/1.15.8.1</center>
</body>
</html>
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
