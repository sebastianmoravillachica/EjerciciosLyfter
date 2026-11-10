## 1. Del Cliente al Servidor

El cliente (navegador):
El cliente envía una solicitud cuando el usuario escribe una dirección, por ejemplo, www.youtube.com, en el navegador.

El DNS:
El DNS traduce el nombre de dominio www.youtube.com a una dirección IP para que el navegador pueda localizar el servidor correcto.

La dirección IP y el servidor.

Una vez que el navegador obtiene la dirección IP, puede establecer una conexión con el servidor correspondiente. El servidor procesa la solicitud y envía los recursos necesarios para mostrar la página web y reproducir el video.

HTTP/HTTPS:

HTTP y HTTPS son los protocolos que permiten la comunicación entre el cliente y el servidor. El navegador envía una solicitud (request) y el servidor devuelve una respuesta (response). HTTPS protege la comunicación mediante cifrado.

## 2. Frontend y Backend en acción

1. Frontend y backend

El frontend sería la parte visual de la aplicación, por ejemplo, el formulario de inicio de sesión, la información de la clínica y el calendario para agendar citas.

El backend se encargaría de la lógica de negocio, como validar las credenciales del usuario, comprobar la disponibilidad de los horarios y guardar las citas en la base de datos.

2. Tecnologías

Para el frontend utilizaría HTML, CSS y React.

Para el backend utilizaría Python, Flask y PostgreSQL.

3. Comunicación entre frontend y backend

El frontend se comunicaría con el backend mediante una API utilizando el protocolo HTTP o HTTPS.

Por ejemplo, cuando un usuario agenda una cita, el frontend envía un request mediante el método POST con la información de la cita. El backend recibe la solicitud, valida los datos y guarda la cita en la base de datos si todo es correcto. Finalmente, devuelve un response indicando si la cita se registró correctamente o si ocurrió algún error.


## 3. REST vs SOAP vs GraphQL

| Tipo de API  | Formato de datos usado |  Nivel de flexibilidad  |  Dificultad de implementación  |  Uso actual (Alta / Media / Baja) |
|--------------|------------------------| ------------------------|--------------------------------|-----------------------------------|
| REST         |||||JSON,XML            |Son muy flexibles. No hay| Baja-Media                     | Alta                              |
|-------------------------------------- |tantas reglas definidas. |                                |                                   |
|                                       |-------------------------|--------------------------------|-----------------------------------|
| SOAP         |||||XML                 |Son muy complejos de     | Alta                           | Baja                              |     
|                                       | crear e implementar.    |                                |                                   |
|---------------------------------------|-------------------------|--------------------------------|-----------------------------------|
| GraphQL      |||||JSON(respuestas),   |El cliente especifica los| Media-Alta                     | Alta                              |
|                lenguaje de consultas  | datos que necesita.     |                                |                                   |
|                GraphQL.               |                         |                                |                                   |
----------------------------------------------------------------------------------------------------------------------------------------


¿Cuál considera más apropiada para una startup moderna que desarrolla un sistema de reservas en línea? ¿Por qué?

Considero que REST sería la opción más apropiada para una startup moderna que desarrolla un sistema de reservas en línea, porque es fácil de implementar, utiliza normalmente JSON y tiene una amplia variedad de herramientas y documentación.

Además, permite realizar operaciones como consultar horarios disponibles mediante GET y registrar una reserva mediante POST.

GraphQL también sería una buena opción si la aplicación necesita consultas más flexibles y complejas. SOAP sería más apropiado en sistemas empresariales que requieren contratos estrictos y estándares específicos de seguridad o transacciones.

## 4. Explorando APIs con Postman
### 4.1

- **Nombre de la API:** restful-api.dev
- **Descripcion:** restful-api.dev es una API REST diseñada para practicar operaciones CRUD (Create, Read, Update y Delete) mediante solicitudes HTTP. Permite crear, consultar, actualizar y eliminar objetos utilizando datos en formato JSON. Es útil para aprender a trabajar con los métodos HTTP GET, POST, PUT, PATCH y DELETE desde Postman..

### 4.2 Configuración en Postman

Se creó una colección llamada restful-api.dev en Postman. Dentro de esta colección se configuraron cinco solicitudes HTTP para practicar las operaciones de consulta (Get_item_by_ID), creación (Add_PlayStation), actualización (PUT=updating_model_and_storage y PATCH=updating_storage) y eliminación (delete_item_by_id) de objetos.

## 4.3 Ejecución y análisis

1. GET - Get_item_by_ID

Método HTTP: GET

Objetivo: Obtener información de objetos almacenados en la API.

Endpoint: https://api.restful-api.dev/objects?id=ff808181a09d98f701a13d5b701b6312&id=1

Parámetros: Se enviaron dos parámetros llamados id, con los valores ff808181a09d98f701a13d5b701b6312 y 1.

Código de estado: 200 OK.

Respuesta: El servidor devolvió una lista de objetos en formato JSON, incluyendo información sobre una PlayStation 5 y un Google Pixel 6 Pro.

Header relevante: Content-Type: application/json;charset=UTF-8.

Ejemplo de respuesta JSON:

[
    {
        "id": "ff808181a09d98f701a13d5b701b6312",
        "name": "PlayStation5",
        "data": {
            "realase_year": 2020,
            "storage": "1 TB"
        }
    },
    {
        "id": "1",
        "name": "Google Pixel 6 Pro",
        "data": {
            "color": "Cloudy White",
            "capacity": "128 GB"
        }
    }
]

2. POST - Add_PlayStation

Método HTTP: POST

Objetivo: Crear un nuevo objeto que represente una consola PlayStation 5.

Endpoint: https://api.restful-api.dev/objects

Cuerpo de la solicitud: Se enviaron el nombre de la consola, el año de lanzamiento y su capacidad de almacenamiento en formato JSON.

Código de estado: 200 OK.

Header relevante: Content-Type: application/json;charset=UTF-8.

Respuesta: El servidor devolvió el objeto creado, incluyendo un identificador único generado por la API y los datos enviados.

Cuerpo enviado:

{
  "name": "PlayStation5",
  "data": {
    "realase_year": 2020,
    "storage": "1 TB"
  }
}

Ejemplo de respuesta JSON:

{
  "id": "ff808181a09d98f701a13d5b701b6312",
  "name": "PlayStation5",
  "createdAt": 1792030765084,
  "data": {
    "realase_year": 2020,
    "storage": "1 TB"
  }
}

3. PUT - Updating_model_and_storage

Método HTTP: PUT

Objetivo: Actualizar la información de un objeto existente en la API.

Endpoint: https://api.restful-api.dev/objects/ff808181a09d98f701a13d5b701b6312

Cuerpo de la solicitud: Se envió un objeto JSON con el nombre PlayStation4 y una capacidad de almacenamiento de 500 GB.

Código de estado exitoso: 200 OK.

Header relevante: Content-Type: application/json;charset=UTF-8.

Respuesta: El servidor devolvió el objeto actualizado, incluyendo su identificador, nombre, fecha de actualización y datos de almacenamiento.

Cuerpo enviado:

{
  "name": "PlayStation4",
  "data": {
    "storage": "500 GB"
  }
}

Ejemplo de respuesta exitosa:

{
  "id": "ff808181a09d98f701a13d5b701b6312",
  "name": "PlayStation4",
  "updatedAt": 1792031096402,
  "data": {
    "storage": "500 GB"
  }
}

Prueba adicional: manejo de errores

Durante una prueba inicial, se obtuvo el código de estado 404 Not Found porque la URL contenía un identificador incompleto. Faltaba el número 2 al final del ID del objeto.

El error se identificó al revisar la URL de la solicitud. Esta prueba permitió comprender que el endpoint debe contener un identificador válido para localizar el recurso que se desea actualizar.

4. PATCH - updating_storage

Método HTTP: PATCH

Objetivo: Actualizar parcialmente los atributos de un objeto existente sin necesidad de enviar toda su información.

Endpoint: https://api.restful-api.dev/objects/ff808181a09d98f701a13d5b701b6312

Cuerpo de la solicitud: Se envió un objeto JSON con el nuevo valor de almacenamiento.

Código de estado: 200 OK.

Header relevante: Content-Type: application/json;charset=UTF-8.

Respuesta: El servidor devolvió el objeto actualizado con su identificador, nombre, fecha de actualización y capacidad de almacenamiento de 1 TB.

Cuerpo enviado:

{
  "data": {
    "storage": "1 TB"
  }
}

Ejemplo de respuesta JSON:

{
  "id": "ff808181a09d98f701a13d5b701b6312",
  "name": "PlayStation4",
  "updatedAt": 1792031325948,
  "data": {
    "storage": "1 TB"
  }
}

5. DELETE - delete_item_by_id

Método HTTP: DELETE

Objetivo: Solicitar la eliminación de un objeto mediante su identificador.

Endpoint: https://api.restful-api.dev/objects/ff808181a09d98f701a13d6efd646340

Cuerpo de la solicitud: No requiere cuerpo.

Código de estado: 200 OK.

Header relevante: Content-Type: application/json;charset=UTF-8.

Respuesta obtenida:

{
  "message": "Object with id = ff808181a09d98f701a13d6efd646340 has been deleted."
}

## 4.4 Explicación técnica

Descripcion general:restful-api.dev es una API REST gratuita que permite crear, consultar, actualizar y eliminar objetos mediante solicitudes HTTP. Utiliza datos en formato JSON y permite practicar los métodos GET, POST, PUT, PATCH y DELETE utilizando Postman.

Durante las pruebas se observaron los siguientes códigos de estado:

Código

Significado

Resultado observado

200 OK

La solicitud se procesó correctamente.

GET, POST, PUT, PATCH y DELETE.

404 Not Found

No se encontró el recurso solicitado mediante la URL o el identificador proporcionado.

Prueba inicial de PUT con un ID incompleto.

También se revisaron los encabezados HTTP de las respuestas.

Content-Type: application/json;charset=UTF-8. Indica que el cuerpo de la respuesta contiene JSON codificado en UTF-8.

Content-Encoding: br. Indica que la respuesta se envió comprimida mediante Brotli.

Server: cloudflare. Identifica a Cloudflare como el servidor o intermediario que atendió la solicitud.

Cf-Cache-Status: DYNAMIC. Indica que Cloudflare clasificó la respuesta como contenido dinámico.

## 5.Reflexión final

1. Aprendí que las APIs permiten que diferentes aplicaciones se comuniquen mediante solicitudes HTTP. También comprendí la función de los métodos GET, POST, PUT, PATCH y DELETE para consultar, crear, actualizar y eliminar información.

2. Postman me ayudó a probar estas solicitudes sin necesidad de programar una aplicación, permitiéndome observar las respuestas JSON, los códigos de estado y los encabezados HTTP. Así pude comprender mejor cómo el cliente envía solicitudes y cómo el servidor procesa y devuelve la información.
