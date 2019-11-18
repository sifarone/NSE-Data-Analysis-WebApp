This is a Full Stack Web Application for analyzing End-of-day NSE Data.
The whole application is Docker container based and Deployed on Google cloud's Kubernetes Engine.
The system is highly scalable wrt to incoming user requests and is loosely based on microservices architecture.

Backend:
- Python (3.7)
- aiohttp webserver (asynchronous RESTdul API server)
- MongoDB with Motor APIs (for asynchronous DB access)
- Redis Server (For server side caching)

Frontend:
- ReactJS
- Redux
- ChartJS
- Metallic UI

Folder Structure:
- /K8s      : Kubernetes config files
- /reader   : Read Server (Python)
- /writer   : Write Server (Python)
- /ui_app   : Frontend (ReactJs + Redux)



