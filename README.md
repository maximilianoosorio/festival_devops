Festival DevOps Music Fest
Este proyecto consiste en el despliegue de una plataforma web para la gestión de un festival de música, estructurado bajo una arquitectura de microservicios contenerizados utilizando Docker y Docker Compose.

El enfoque principal de esta entrega radica en la correcta implementación de una estrategia de control de versiones profesional utilizando Git Flow básico y GitHub como repositorio remoto, garantizando el aislamiento de funciones y la trazabilidad en el ciclo de vida del software.

Tecnologías Utilizadas
Frontend: HTML5, CSS3 y JavaScript.

Backend: Python con el microframework Flask.

DevOps & Contenedores: Docker (Dockerfiles independientes para servicios) y Docker Compose.

Control de Versiones: Git y GitHub utilizando la metodología Git Flow básico.

Implementación del Flujo de Trabajo (Git Flow)
La estrategia de desarrollo se dividió en ramas dedicadas a características específicas (Feature Branches) que posteriormente se integraron a la rama principal mediante fusiones explícitas:

main: Contiene el código fuente completamente estable y validado en su versión de producción.

feature-landing: Desarrollo y maquetación de la interfaz de usuario de la landing page.

feature-backend: Implementación técnica del servidor Flask y su configuración Docker.

feature-artistas: (Reto Avanzado) Estructuración modular para el catálogo y el Line-Up oficial de bandas.

feature-tickets: (Reto Avanzado) Implementación del flujo de simulación para la adquisición de boletas.

feature-contacto: (Reto Avanzado) Diseño del formulario de contacto para atención al usuario.

Arquitectura y Despliegue con Docker
El sistema se compone de dos servicios principales que se comunican de forma aislada dentro de una red nativa de Docker:

Frontend: Servidor web que expone la interfaz de usuario de la landing page.

Backend: API en Flask que gestiona los servicios internos de la aplicación.

Estructura del Directorio
festival-devops/

├── backend/

│   ├── app.py

│   ├── Dockerfile

│   └── requirements.txt

├── frontend/

│   ├── artistas.html

│   ├── contacto.html

│   ├── Dockerfile

│   ├── index.html

│   ├── style.css

│   └── tickets.html

├── docker-compose.yml

└── README.md

Instrucciones para ejecutar el entorno local
Para construir las imágenes personalizadas y levantar los servicios (junto con sus redes y volúmenes correspondientes), ejecuta el siguiente comando en la raíz del proyecto:

docker-compose up --build
