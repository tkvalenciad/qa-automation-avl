# PRUEBA TÉCNICA: INGENIERO DE AUTOMATIZACIÓN QA - AVL Mobility Solutions

## Descripción

Este proyecto corresponde a la prueba técnica para **AVL Mobility Solutions**.

La solución implementa una estrategia de automatización para un ecosistema de movilidad compuesto por tres capas:

- Mobile Testing (Android)
- API Testing
- Event-Driven Testing (Kafka)

El objetivo fue construir una solución reutilizable, escalable y fácil de mantener siguiendo buenas prácticas como:

- Page Object Model
- Fixtures reutilizables
- JSON Schema Validation
- Evidencias automáticas
- Configuración mediante variables de entorno
- Separación por capas

Actualmente la suite cuenta con **17 pruebas automatizadas**:

```
6 Mobile
7 API
4 Eventos Kafka

17 passed
```

---

# Tecnologías utilizadas


| Tecnología        | Uso                          |
| ----------------- | ---------------------------- |
| Python 3.12       | Lenguaje principal           |
| Pytest            | Framework de pruebas         |
| Appium            | Automatización móvil         |
| Requests          | Cliente HTTP                 |
| JsonSchema        | Validación de contratos      |
| Kafka Python      | Productor y consumidor Kafka |
| Docker + Redpanda | Broker Kafka local           |
| Allure            | Reportes                     |
| Pytest HTML       | Reporte HTML                 |
| Appium Inspector  | Obtención de selectores      |


---

# Prerrequisitos

El proyecto fue desarrollado y validado utilizando estas versiones:


| Herramienta                      | Versión usada                   |
| -------------------------------- | ------------------------------- |
| Python                           | 3.12.10                         |
| Java JDK                         | 21.0.2 LTS                      |
| Node.js                          | 20.11.0 (npm 10.2.4)            |
| Appium Server                    | 2.19.0                          |
| Appium driver UiAutomator2       | 3.9.7                           |
| Android SDK platform-tools (adb) | 37.0.0 (adb 1.0.41)             |
| Appium-Python-Client             | 5.3.1                           |
| Dispositivo                      | Samsung Galaxy S25 (Android 16) |


---

# Variables de entorno

Configurar las siguientes variables:

```
$env:ANDROID_HOME="C:\Users\<usuario>\AppData\Local\Android\Sdk"

$env:ANDROID_UDID="RFCY510RLSL"

$env:APPIUM_SERVER="http://127.0.0.1:4723"

$env:JSONPLACEHOLDER_URL="https://jsonplaceholder.typicode.com"

$env:DUMMYJSON_URL="https://dummyjson.com"
```

Para la suite de eventos también pueden configurarse:

```
$env:KAFKA_BOOTSTRAP_SERVERS="localhost:9092"

$env:GPS_RAW_EVENTS_TOPIC="gps-raw-events"
```

---

# Instalación paso a paso

## 1. Clonar el repositorio

```
git clone <url>

cd qa-automation-avl
```

---

## 2. Crear el entorno virtual

```
python -m venv .venv
```

---

## 3. Activarlo

Windows

```
.venv\Scripts\activate
```

Linux / Mac

```
source .venv/bin/activate
```

---

## 4. Instalar dependencias

```
pip install -r requirements.txt
```

---

## 5. Instalar Appium

```
npm install -g appium

appium driver install uiautomator2
```

---

## 6. Verificar el dispositivo Android

```
adb devices
```

Debe aparecer algo similar a:

```
List of devices attached

RFCY510RLSL device
```

---

## 7. Levantar Appium

```
appium
```

---

## 8. Instalar la aplicación (si es necesario)

```
adb install Android-MyDemoApp.apk
```

---

## 9. Levantar Kafka (solo suite de eventos)

```
docker compose up -d
```

---

# Estructura del proyecto

(Dejar exactamente el árbol que tienes actualmente)

---

# Ejecución de pruebas

## Ejecutar toda la suite

```
pytest -v
```

---

## Ejecutar únicamente Mobile

```
pytest mobile/tests -v
```

---

## Ejecutar únicamente API

```
pytest api_tests/tests -v
```

---

## Ejecutar únicamente Eventos

```
pytest event_tests/tests -v
```

---

# Reportes

Después de cada ejecución se generan automáticamente:


| Reporte            | Ubicación              |
| ------------------ | ---------------------- |
| HTML               | reports/report.html    |
| Allure             | allure-results         |
| Screenshots Mobile | screenshots/mobile     |
| Evidencia API      | reports/api-evidence   |
| Evidencia Kafka    | reports/event-evidence |


---

## Abrir reporte Allure

```
allure serve allure-results
```

---

# Cobertura implementada

### Mobile

✔ Login válido

✔ Login inválido

✔ Navegación entre pantallas

✔ Detalle de producto

✔ Agregar producto al carrito

✔ Checkout hasta pantalla de pago

---

### API

✔ POST

✔ PUT

✔ Login

✔ Validación JSON Schema

✔ SLA

---

### Eventos

✔ Publicación Kafka

✔ Consumo Kafka

✔ Validación JSON Schema

✔ Integridad Produce → Consume

✔ SLA

✔ Evento inválido

---

# Credenciales de prueba


| Campo    | Valor                                     |
| -------- | ----------------------------------------- |
| Usuario  | [bob@example.com](mailto:bob@example.com) |
| Password | 10203040                                  |


---

# Consideraciones

- La suite Mobile requiere un dispositivo Android conectado y Appium Server en ejecución. 
- La suite de Eventos requiere un broker Kafka disponible. Si el broker no está accesible, las pruebas se omiten automáticamente (`pytest.skip`) sin afectar el resto de la ejecución. 
- Todas las evidencias se generan automáticamente para facilitar el análisis de resultados.

