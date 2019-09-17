docker build -t sifarone/k8s_read_server:latest -t sifarone/k8s_read_server:$GIT_SHA -f ./reader/Dockerfile ./reader
docker build -t sifarone/k8s_write_server:latest -t sifarone/k8s_write_server:$GIT_SHA -f ./writer/Dockerfile ./writer
docker build -t sifarone/k8s_ui_app:latest -t sifarone/k8s_ui_app:$GIT_SHA -f ./ui_app/Dockerfile ./ui_app

docker push sifarone/k8s_read_server:latest
docker push sifarone/k8s_write_server:latest
docker push sifarone/k8s_ui_app:latest

docker push sifarone/k8s_read_server:$GIT_SHA
docker push sifarone/k8s_write_server:$GIT_SHA
docker push sifarone/k8s_ui_app:$GIT_SHA

kubectl apply -f k8s

kubectl set image deployments/read-server-deployment read-server=sifarone/k8s_read_server:$GIT_SHA
kubectl set image deployments/write-server-deployment write-server=sifarone/k8s_write_server:$GIT_SHA
kubectl set image deployments/ui-app-deployment client=sifarone/k8s_ui_app:$GIT_SHA