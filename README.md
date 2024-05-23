# ChatULL Backend

Este repositorio contiene el backend de la plataforma **ChatULL**, desarrollada para mi Trabajo de Fin de Grado (TFG). ChatULL es un chatbot que responde preguntas relacionadas con documentos universitarios utilizando técnicas de **prompt engineering** para proporcionar respuestas precisas después de un tratamiento minucioso de la información.

## Índice

1. [Introducción](#introducción)
2. [Instalación](#instalación)
3. [Uso](#uso)
4. [API Endpoints](#api-endpoints)
5. [Contacto](#contacto)

## Introducción

ChatULL es una plataforma diseñada para ayudar a los estudiantes y personal universitario a obtener respuestas rápidas y precisas sobre diversos documentos universitarios. Utiliza procesamiento de lenguaje natural y técnicas de prompt engineering para interpretar las preguntas y proporcionar respuestas basadas en la información contenida en los documentos.

## Instalación

Para comenzar, siga estos pasos:

1. Clone este repositorio:
    ```bash
    git clone https://github.com/ULL-prompt-engineering/chatull-backend.git
    cd chatull-backend
    ```

2. Cree un entorno virtual:
    ```bash
    python -m venv env
    source env/bin/activate  # En Windows use `env\Scripts\activate`
    ```

3. Instale las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

Para iniciar el servidor, ejecute el siguiente comando:
```bash
flask run
```
El servidor se iniciará en http://127.0.0.1:5000.

## API Endpoints

### `POST /set_api_key`

Este endpoint se utiliza para configurar la API key y obtener un token JWT.

#### Request

```json
{
    "api_key": "tu_api_key"
}
```
#### Response

```json
{
    "message": "API key guardada exitosamente",
    "jwt": "tu_token_jwt"
}
```

### `GET /get_answer`

Este endpoint se utiliza para obtener una respuesta a una pregunta sobre una materia específica. Requiere un token JWT válido.

#### Request

```json
- Headers:
  - `Authorization`: `Bearer tu_token_jwt`
- Query Parameters:
  - `question`: La pregunta que se desea hacer.
  - `subject`: La materia sobre la cual se hace la pregunta.
  
  Ejemplo:
  http://servidor/get_answer?question=pregunta&subject=materia

```
#### Response

```json
{
    "answer": "respuesta_formateada"
}
```

### `GET /get_regulation_answer`

Este endpoint se utiliza para obtener una respuesta a una pregunta sobre una regulación. Requiere un token JWT válido.


#### Request

```json
- Headers:
  - `Authorization`: `Bearer tu_token_jwt`
- Query Parameters:
  - `question`: La pregunta que se desea hacer.
  
  Ejemplo:
  http://servidor/get_regulation_answer?question=pregunta

```
#### Response

```json
{
    "answer": "respuesta_formateada"
}
```

### `GET /documents`

Este endpoint devuelve una lista de todos los documentos disponibles, incluyendo materias y regulaciones.

#### Request

No requiere de parametros adicionales

#### Response


```json
[
    {
        "name": "nombre_de_la_materia"
    },
    {
        "name": "nombre_de_la_regulación"
    },
    ...
]

```

### `GET /logs`

Este endpoint devuelve los registros de tiempo guardados en el archivo times.csv para cada una de las preguntas realizadas.


#### Request

No requiere de parametros adicionales

#### Response


```json
    [
        "question1, answer1, duration1",
        "question2, answer2, duration2",
        ...
    ]
```

### Contacto
Para cualquier duda o consulta, por favor contacta con jonayve.dev@gmail.com

¡Gracias por utilizar ChatULL!
