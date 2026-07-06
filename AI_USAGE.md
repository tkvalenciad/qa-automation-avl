# AI Usage Report

Este documento describe de forma transparente cómo utilicé asistentes de Inteligencia Artificial durante el desarrollo de la prueba técnica. La IA fue utilizada como una herramienta para acelerar tareas repetitivas, generar ideas y revisar código, mientras que todas las decisiones de diseño, validaciones y pruebas fueron realizadas y verificadas manualmente.

---

# 1. Herramientas utilizadas


| Herramienta                   | ¿Cómo la utilicé?                                                                                                                                                                         |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ChatGPT**                   | Me ayudó para discutir decisiones de arquitectura, resolver dudas, revisar código, proponer mejoras y acompañarme paso a paso durante la implementación.                                  |
| **Cursor (Claude)**           | Lo utilicé como copiloto de programación para generar código repetitivo, realizar refactors, crear Page Objects, organizar la estructura del proyecto y acelerar la escritura de pruebas. |
| **Appium Inspector**          | Se utilizó manualmente para inspeccionar la aplicación Android e identificar selectores estables antes de incorporarlos a la automatización.                                              |
| **Docker Desktop + Redpanda** | Se utilizaron para levantar un broker Kafka local y validar la capa de mensajería solicitada en el reto.                                                                                  |


---

# 2. Casos de uso específicos

Durante el desarrollo utilicé la IA principalmente como apoyo para tareas repetitivas o de análisis, entre ellas:

- Analizar el documento de la prueba técnica para identificar los requisitos y verificar el avance del proyecto.
- Generar la estructura inicial de la automatización para API, Mobile y Eventos siguiendo buenas prácticas como Page Object Model y reutilización de componentes.
- Crear boilerplate para Page Objects, locators, clientes HTTP, fixtures y pruebas en pytest.
- Diseñar los contratos JSON Schema utilizados para validar respuestas de API y eventos Kafka.
- Revisar y mejorar la estrategia de localizadores en Appium, reemplazando selectores frágiles por alternativas más estables como `accessibilityId` y `UiAutomator`.
- Diseñar la capa de mensajería utilizando `kafka-python`, incluyendo productor, consumidor, helpers y validaciones sobre un broker Kafka real.
- Ayudar en el diagnóstico y solución de problemas del entorno, especialmente durante la configuración de Docker, WSL2 y Kafka.
- Refactorizar código duplicado y proponer una estructura más limpia y mantenible.
- Apoyar la redacción de la documentación del proyecto.

En todos los casos, el código generado fue revisado, adaptado y validado manualmente antes de incorporarlo al proyecto.

---

# 3. Ejemplos de prompts utilizados

## Prompt 1 – Diseñar la capa de eventos

**Contexto**

Estoy desarrollando una prueba técnica para una posición de QA Automation utilizando Python y pytest.

**Objetivo**

Necesito implementar la capa de mensajería solicitada en el reto utilizando Kafka.

**Prompt**

> Actúa como un QA Automation Senior especializado en sistemas orientados a eventos.
>
> Ayúdame a implementar paso a paso una capa de mensajería utilizando kafka-python siguiendo buenas prácticas de automatización.
>
> La solución debe incluir productor, consumidor, payloads reutilizables, validación mediante JSON Schema, helpers para assertions y pruebas organizadas con pytest.
>
> Evita sobreingeniería y explica cada decisión técnica antes de escribir el código.

**Valor aportado**

Este prompt permitió construir la estructura inicial de la capa de eventos y comprender el propósito de cada componente antes de implementarlo.

---

## Prompt 2 – Validar el cumplimiento del reto

**Contexto**

Ya tenía implementada una primera versión del bonus, pero quería asegurarme de que realmente cumpliera con el enunciado de la prueba.

**Prompt**

> Revisa nuevamente el PDF de la prueba técnica y verifica si la implementación cumple exactamente con lo solicitado.
>
> Si encuentras diferencias entre el código y el documento, indícalas antes de proponer cualquier cambio.
>
> No hagas suposiciones; utiliza únicamente la información del PDF como fuente de verdad.

**Valor aportado**

Gracias a este prompt detecté que la primera propuesta modelaba un escenario de e-commerce, mientras que el reto solicitaba eventos de telemetría GPS publicados y consumidos desde un broker Kafka real. Esto permitió corregir el enfoque antes de finalizar la implementación.

---

# 4. Reflexión técnica

El uso de IA tuvo un impacto importante en la velocidad de desarrollo, especialmente en tareas repetitivas como la generación de boilerplate, la organización inicial del proyecto, la creación de esquemas JSON y la documentación.

Sin embargo, todas las decisiones de arquitectura y las validaciones finales fueron tomadas de forma manual. Cada sugerencia fue revisada, adaptada y comprobada ejecutando las pruebas antes de integrarla al proyecto.

Uno de los aprendizajes más importantes fue que la IA no reemplaza el criterio de ingeniería. Por ejm, fue necesario corregir sugerencias relacionadas con selectores móviles, descartando varios XPath propuestos inicialmente en favor de `accessibilityId` y `UiAutomator`, que resultaron mucho más estables al ejecutar las pruebas sobre un dispositivo físico.

En resumen, la IA me permitió acelerar el desarrollo y reducir el tiempo dedicado a tareas repetitivas, pero el resultado final dependió del análisis crítico, las validaciones manuales y la ejecución continua de las pruebas para asegurar que la solución cumpliera realmente con los requisitos planteados.

