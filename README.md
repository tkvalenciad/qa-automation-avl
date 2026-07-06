# PRUEBA TÉCNICA: INGENIERO DE AUTOMATIZACIÓN QA - AVL Mobility Solutions

![CI](https://github.com/tkvalenciad/qa-automation-avl/actions/workflows/ci.yml/badge.svg)

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



# Estrategia de priorización por riesgo

En AVL se gestionan miles de eventos telemáticos en tiempo real, por lo que la automatización se priorizó según el **riesgo de negocio** y el **impacto al usuario**: primero los flujos cuya falla detiene la operación o genera pérdida de datos/ingresos, y después los de menor severidad.

| Prioridad | Riesgo de negocio | Caso automatizado | Capa | Por qué se priorizó |
| --------- | ----------------- | ----------------- | ---- | ------------------- |
| **P0 (crítico)** | Un usuario no puede acceder → bloquea toda la operación | Login válido / inválido | Mobile | Es la puerta de entrada; si falla, ningún otro flujo es alcanzable. Además valida manejo de credenciales incorrectas (seguridad). |
| **P0 (crítico)** | Pérdida de eventos de telemetría → datos de flota incompletos | Integridad Produce → Consume + contrato JSON | Eventos | El core del negocio es ingerir telemetría sin pérdida ni corrupción; se valida que lo publicado se recibe íntegro y con la estructura esperada. |
| **P1 (alto)** | El usuario no completa una compra → pérdida de ingreso | Agregar al carrito + Checkout hasta pago | Mobile | Flujo transaccional que cambia estado; se asegura la confirmación lógica del cambio (item agregado, avance a pago). |
| **P1 (alto)** | Datos mal escritos/validados en backend | POST / PUT + validación de estado y JSON Schema | API | Las peticiones mutables con contrato garantizan que la ingesta de datos respete tipos y estructura. |
| **P2 (medio)** | Degradación de experiencia / SLA | SLA API (<1.5s) + latencia de eventos | API / Eventos | En tiempo real la latencia importa; se valida rendimiento como parte del contrato, no solo la funcionalidad. |
| **P2 (medio)** | Rupturas de navegación tras cambios de UI | Navegación entre pantallas + detalle de producto | Mobile | Verifica transiciones y estados intermedios usando selectores estables para mitigar flakiness. |

**Decisiones clave de priorización:**

- **Foco en Mobile (35% del peso):** mayor inversión en robustez (esperas dinámicas, POM, selectores estables) por ser la capa de mayor peso y mayor fragilidad.
- **Contrato + integridad antes que volumen:** se prefirió validar profundamente los flujos críticos (contrato, integridad, SLA) en lugar de multiplicar casos superficiales.
- **Reproducibilidad en CI:** las capas API y Eventos corren en CI (deterministas); Mobile se ejecuta localmente por requerir hardware físico, evitando falsos negativos.

---



# Integración Continua (CI)

El proyecto incluye un pipeline de **GitHub Actions** (`.github/workflows/ci.yml`) que se ejecuta automáticamente en cada `push` y `pull request` sobre la rama `main`.

En cada ejecución el pipeline:

- Instala las dependencias en un entorno limpio (Python 3.12).
- Ejecuta la **suite de API** contra los servicios públicos.
- Levanta un broker **Kafka (Redpanda)** con `docker compose` y ejecuta la **suite de eventos** (produce → consume de telemetría).
- Publica los reportes (`reports/`, `allure-results/`) como *artifacts* descargables.

La **capa Mobile no se ejecuta en CI** de forma intencional, ya que requiere un dispositivo Android físico y Appium Server, por lo que se ejecuta localmente. De esta manera el pipeline valida de forma continua las capas reproducibles en la nube (API y eventos) sin introducir falsos negativos por falta de hardware.

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

```
qa-automation-avl/
├── .github/
│   └── workflows/
│       └── ci.yml                  # Pipeline CI (API + eventos Kafka)
├── app/
│   └── Android-MyDemoApp.apk       # APK de la app bajo prueba
├── config/
│   ├── reporting.py                # Rutas de reportes y evidencias
│   └── settings.py                 # Configuracion global (Appium, device)
├── mobile/                         # Capa Movil (Appium + POM)
│   ├── locators/                   # Selectores estables (accessibilityId/UiAutomator)
│   ├── pages/                      # Page Objects (base, login, home, cart, checkout...)
│   ├── payloads/                   # Datos de prueba (checkout)
│   ├── tests/                      # Tests: login, navegacion, carrito, checkout, producto
│   ├── utils/                      # Driver factory, helpers y evidencias
│   └── conftest.py                 # Fixtures del driver + evidencias mobile
├── api_tests/                      # Capa API (requests + jsonschema)
│   ├── client/                     # Cliente HTTP reutilizable
│   ├── config/                     # URLs, endpoints y SLA
│   ├── helpers/                    # Aserciones, schema, SLA y evidencias
│   ├── payloads/                   # Datos de prueba (auth, posts)
│   ├── schemas/                    # JSON Schemas por dominio
│   ├── tests/                      # Tests: auth, posts (POST/PUT/GET/SLA)
│   └── conftest.py                 # Fixtures por servicio + evidencias API
├── event_tests/                    # Capa Eventos/Telemetria (Kafka - bonus)
│   ├── client/                     # Productor + consumidor Kafka (kafka-python)
│   ├── config/                     # Broker, topic gps-raw-events, SLA
│   ├── helpers/                    # Aserciones de contrato/integridad y evidencias
│   ├── payloads/                   # Constructor del evento de telemetria GPS
│   ├── schemas/                    # JSON Schema del evento
│   ├── tests/                      # Tests: produce->consume, contrato, SLA, integridad
│   ├── conftest.py                 # Fixtures producer/consumer + evidencias
│   └── requirements-events.txt     # Dependencia del cliente Kafka
├── conftest.py                     # Hooks globales de pytest
├── docker-compose.yml              # Kafka local ligero (Redpanda)
├── pytest.ini                      # Configuracion de pytest (testpaths, markers, reportes)
├── requirements.txt                # Dependencias del proyecto
├── README.md
└── AI_USAGE.md
```

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

