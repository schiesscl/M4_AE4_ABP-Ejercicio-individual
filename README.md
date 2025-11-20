# M4_AE4_ABP-Ejercicio individual

## Hans Schiess

### Descripción General, Archivos de código fuente relevantes

* [`main.py`](main.py)
* [`persona.py`](persona.py)
* [`tamagotchi.py`](tamagotchi.py)

### Propósito y Alcance

Este documento proporciona una introducción de alto nivel al sistema de simulación de mascota virtual Tamagotchi. Describe el propósito del sistema, sus componentes principales, características clave y patrones de arquitectura. Esta descripción general está destinada a dar a los desarrolladores y lectores técnicos una comprensión rápida de lo que hace el sistema y cómo está organizado.

### Resumen del Sistema

El sistema de simulación Tamagotchi es una aplicación de interfaz de línea de comandos (CLI) que permite a los usuarios interactuar con una mascota virtual. El sistema implementa un bucle de juego clásico al estilo Tamagotchi donde el usuario puede realizar acciones que afectan el estado interno de la mascota (salud, felicidad y energía). La aplicación está escrita en Python y sigue un diseño orientado a objetos con una clara separación de responsabilidades a través de tres módulos principales.

**Características Clave:**

* **Plataforma**: Aplicación de consola en Python 3.
* **Modelo de Interacción**: CLI controlada por menú con opciones numeradas.
* **Arquitectura**: Diseño de tres capas (Presentación, Controlador, Dominio).
* **Extensibilidad**: Sistema de tipos de mascotas basado en herencia.

### Mapa de Componentes del Sistema

El sistema consta de tres módulos principales de Python, cada uno con clases y funciones específicas.

**Descripciones de los Módulos:**

| Módulo | Clase Principal | Responsabilidad |
| :--- | :--- | :--- |
| `main.py` | N/A (punto de entrada) | Orquestación de la aplicación, bucle interactivo, visualización del menú, manejo de entrada del usuario. |
| `persona.py` | `Persona` | Proxy del usuario que añade registros antes de delegar acciones al `Tamagotchi`. |
| `tamagotchi.py` | `Tamagotchi` (clase base) | Gestión del estado de la mascota virtual, manejo de acciones, validación de estado. |
| `tamagotchi.py` | `Gozarutchi` (subclase) | Tipo de mascota especializada con diferentes tasas de modificación de atributos. |

### Estructura de Objetos en Tiempo de Ejecución

En tiempo de ejecución, el sistema crea un conjunto fijo de objetos que interactúan según un patrón específico.

**Secuencia de Inicialización de Objetos:**

1. En [`main.py`](main.py), se crea una instancia de `Gozarutchi` que representa la mascota virtual.
2. A continuación, se crea una instancia de `Persona`, que recibe la mascota creada anteriormente.
3. Un bucle infinito en `main()` maneja la interacción del usuario hasta que se elige salir.

La instancia de `Persona` mantiene una referencia a la instancia de `Tamagotchi` ([`persona.py`](persona.py)) y actúa como intermediario para la mayoría de las acciones. Sin embargo, la acción "mostrar estado" ([`main.py`](main.py)) omite a `Persona` y consulta directamente al `Tamagotchi`.

### Acciones de Usuario Disponibles

El sistema proporciona cinco acciones distintas accesibles a través de un menú numerado:

| Opción del Menú | Método Invocado | Efecto en el Estado de la Mascota (`Gozarutchi`) |
| :--- | :--- | :--- |
| 1 - Jugar | `persona3.jugar_con_tamagotchi() -> gozarutchi.jugar()` | Felicidad +15, Salud -3 |
| 2 - Alimentar | `persona3.darle_comida() -> gozarutchi.comer()` | Felicidad +10, Salud +5 |
| 3 - Curar | `persona3.curarlo() -> gozarutchi.curar()` | Felicidad -2, Salud +15 |
| 4 - Mostrar estado | `gozarutchi.mostrar_estado()` | Sin cambio de estado, muestra los atributos actuales. |
| 5 - Salir | Sale del bucle | La aplicación termina. |

*Nota: Los valores mostrados son específicos para `Gozarutchi`. La clase base `Tamagotchi` tiene diferentes tasas de modificación ([`tamagotchi.py`](tamagotchi.py)).*

### Patrón de Arquitectura Principal

El sistema implementa una arquitectura de tres capas con dependencias unidireccionales.

**Responsabilidades de las Capas:**

* **Capa de Presentación (`main.py`)**: Maneja todas las preocupaciones de la interfaz de usuario, incluyendo la visualización del menú, la captura de entradas y el bucle de eventos principal. Esta capa no tiene lógica de negocio, solo coordina entre el usuario y las capas de controlador/dominio.
* **Capa de Controlador (`persona.py`)**: Actúa como mediador entre la UI y el modelo de dominio. La clase `Persona` añade registros amigables para el usuario antes de delegar a los métodos de `Tamagotchi`. Esto proporciona una abstracción de nivel superior sobre las operaciones crudas de la mascota.
* **Capa de Dominio (`tamagotchi.py`)**: Contiene toda la lógica de negocio para la simulación de la mascota virtual. Gestiona el estado de la mascota, impone invariantes a través de la validación y es completamente independiente de cómo se utiliza. Esta capa podría ser reutilizada en una aplicación diferente (por ejemplo, una versión con GUI) sin modificaciones.

### Sistema de Gestión de Estado

Todos los atributos de la mascota se gestionan a través de un sistema de estado validado.

**Atributos de Estado:**

| Atributo | Valor Inicial | Rango Válido | Descripción |
| :--- | :--- | :--- | :--- |
| `nombre` | "Gozarutchi" | String | Nombre de la mascota, establecido en la creación. |
| `color` | "Azul" | String | Color de la mascota, establecido en la creación. |
| `salud` | 100 | [0, 100] | Nivel de salud, afectado por todas las acciones. |
| `felicidad` | 50 | [0, 100] | Nivel de felicidad, afectado por todas las acciones. |
| `energia` | 80 | [0, 100] | Nivel de energía, actualmente no modificado por las acciones. |

**Mecanismo de Validación:**

El método `_validar_estado()` en [`tamagotchi.py`](tamagotchi.py) se llama después de cada modificación de estado para asegurar que los atributos permanezcan dentro de los rangos válidos [0, 100]. Este enfoque de programación defensiva asegura que los atributos nunca excedan los límites, manteniendo la consistencia del estado.

### Herencia y Especialización

El sistema admite múltiples tipos de mascotas a través de la herencia. La clase `Gozarutchi` hereda de `Tamagotchi`.

**Diferencias de Comportamiento:**

La subclase `Gozarutchi` ([`tamagotchi.py`](tamagotchi.py)) sobrescribe los tres métodos de interacción (`jugar`, `comer`, `curar`) para proporcionar características de juego diferentes.

| Acción | `Tamagotchi` Base | Especialización de `Gozarutchi` |
| :--- | :--- | :--- |
| `jugar()` | Felicidad +10, Salud -5 | Felicidad +15, Salud -3 |
| `comer()` | Felicidad +5, Salud +10 | Felicidad +10, Salud +5 |
| `curar()` | Felicidad -5, Salud +20 | Felicidad -2, Salud +15 |

Esto demuestra el Principio Abierto/Cerrado: el sistema está abierto a la extensión (se pueden añadir nuevos tipos de mascotas mediante subclases) pero cerrado a la modificación (la clase base `Tamagotchi` no necesita cambios).

### Patrón de Delegación

El sistema utiliza la delegación de métodos para separar las responsabilidades entre la interacción del usuario y la lógica de la mascota.

**Cadena de Delegación para Acciones:**

1. El usuario selecciona una acción del menú en [`main.py`](main.py).
2. `main()` llama al método apropiado de `Persona`.
3. El método de `Persona` registra la acción y delega la llamada al método correspondiente de `Tamagotchi`.
4. `Tamagotchi` modifica su estado y muestra los resultados.
