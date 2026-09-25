# Domain 8: Tools and MCPs

> Curso: Claude Certified Developer Foundations (CCDV-F)

Resumen del PDF oficial de **Domain 8: Tools and MCPs**. Cubre tres lecciones: cómo
funciona el `tool use` por dentro, `Model Context Protocol (MCP)` como estándar para
conectar todo, y cómo construir y usar `MCP servers` en la práctica.

## 1. How Tool Use Works

### ¿Qué es un tool?

Claude, por sí solo, **solo produce texto**. Un `tool` es lo que le permite pasar de
"decir cosas" a "hacer cosas": buscar un pedido, consultar el clima, hacer una query a
una base de datos.

> 📌 Un tool deja que Claude *pida* una acción. Esto ya se vio en Domain 1 (el
> request-execute gap) y en Domain 2 (la mecánica de la API) — aquí se formaliza.

### La definición del tool

Toda `tool definition` tiene **tres partes**:

```text
name:         get_weather
description:  when to use it
input_schema: { city: string }
```

| Parte | Qué responde |
| --- | --- |
| `name` | Cómo se llama |
| `description` | CUÁNDO usarlo |
| `input_schema` | QUÉ parámetros necesita (JSON Schema, ver Domain 2) |

> 💡 Claude lee la `description` para decidir si usar el tool — o para decidir **no**
> usarlo, si la pregunta no lo necesita.

> 🎯 Las descripciones buenas importan: son la forma en que Claude elige el tool
> correcto en el momento correcto.

### El tool-use loop

```text
1. Claude requests   → call get_weather("Pune")
2. Your code runs    → ejecuta el tool real
3. Result returns    → "32°C, sunny"
4. Claude answers    → usa el resultado para responder
```

> ⚠️ Claude **nunca** ejecuta el tool él mismo — lo ejecuta tu código. Este es el
> request-execute gap, formalizado.

> 📌 Después el loop puede repetirse: Claude puede llamar a otro tool antes de terminar.

### Parallel tool use

Varios tools a la vez, cuando **no dependen entre sí** (ej. Claude pide weather,
calendar y stock price al mismo tiempo — todos se disparan juntos y los resultados
vuelven juntos).

> 🎯 Funciona cuando las llamadas son independientes — ninguna necesita el resultado de
> otra. Es más rápido que una a la vez. Si el tool B necesita el resultado del tool A,
> corren en secuencia en su lugar.

### Built-in vs Custom tools

| | Built-in | Custom |
| --- | --- | --- |
| Quién lo provee | Anthropic, listo para activar | Tú lo defines y lo corres |
| Ejemplos | `web search`, `code exec` | tu base de datos, tu API |

> 🎯 Es el mismo loop para ambos. Elige built-in cuando ya existe; construye custom para
> lo específico de tu app.

## 2. MCP — One Way to Connect Everything

### El problema: demasiadas integraciones custom

Cada app × cada tool = un lío que mantener. Antes de MCP, cada app necesitaba código
custom para cada tool, y cada integración inventaba su propia forma de manejar auth y
datos — inconsistente y propenso a errores.

> ⚠️ M apps × N tools = M×N integraciones separadas que construir y mantener (ej. 3 apps
> × 3 tools = 9 integraciones custom). Tenía que haber una mejor forma.

### ¿Qué es MCP?

> 📌 **MCP = Model Context Protocol** — un estándar abierto de Anthropic (finales de
> 2024). Piénsalo como el USB-C de los tools de IA.

Con MCP, cada app y cada tool se conectan a **un protocolo compartido** en el medio, en
vez de conectarse entre sí directamente.

> 💡 Construyes un conector una vez; cualquier app compatible con MCP puede usarlo.
> Convierte M×N en M+N.

### Los tres roles: Host, Client, Server

| Rol | Qué es | Ejemplos |
| --- | --- | --- |
| **Host** | La app de IA con la que interactúa el usuario | Claude Desktop, Claude Code, Cursor |
| **Client** | Vive **dentro** del host; un client por server | (parte del host) |
| **Server** | Programa independiente que expone tools y datos al host | (proveedor de la capacidad) |

> 📌 El host maneja la función; el client es el cable; el server provee la capacidad. Un
> host puede tener muchos clients — uno por cada server al que se conecta.

### Cómo funciona una conexión

```text
1. Client se conecta al server
2. Server declara qué ofrece
3. Host ya puede usar esas capacidades
```

> 💡 Al conectarse, el server declara qué puede hacer — **capability discovery**. El
> host aprende automáticamente qué tools existen, sin cableado manual de prompts.

> 💡 El discovery estandarizado es la magia: cualquier host entiende cualquier server.

### MCP se construye sobre tool use

MCP no reemplaza a los tools — **estandariza cómo se conectan**. Por debajo sigue
corriendo el mismo tool-use loop de la Lección 1 (Claude requests → your code runs →
result returns); MCP le agrega **tres capas** alrededor:

| Capa | Qué hace |
| --- | --- |
| **Discovery** | Los servers anuncian sus capacidades |
| **Transport** | Un canal estándar |
| **Session** | Una conexión administrada |

> 🎯 MCP no compite con el tool use — es la plomería que hace que los tools sean
> reutilizables. Primero se aprenden los tools (ya está); MCP es la capa de arriba.

## 3. Building and Using MCP Servers

### Qué expone un server: tres primitivas

Un `MCP server` puede ofrecer cualquier combinación de:

| Primitiva | Qué es |
| --- | --- |
| **Tools** | Acciones ejecutables |
| **Resources** | Datos de solo lectura |
| **Prompts** | Plantillas reutilizables |

> 📌 En la Lección 2 el server DECLARABA sus capacidades al conectarse — esto es lo que
> esas capacidades son en realidad.

### Tools vs Resources vs Prompts

| Necesitas... | Usa un... | Ejemplo |
| --- | --- | --- |
| Leer datos | **Resource** | leer un archivo, obtener un registro |
| Hacer algo | **Tool** | correr una query, enviar un email |
| Reutilizar un flujo | **Prompt** | una plantilla de tarea pre-armada |

> 💡 Regla práctica: **resources consultan, tools actúan, prompts estandarizan**.

> 📌 Esta separación entre leer y actuar es lo que hace que MCP sea más que un simple
> retrieval.

### Local vs Remote: los dos transportes

| | `stdio` | `Streamable HTTP` |
| --- | --- | --- |
| Alcance | LOCAL — misma máquina | REMOTE — sobre HTTPS |
| Qué es | El server corre en tu propia computadora | Un servicio hosteado al que se llega por internet |
| Uso típico | El default de Claude Desktop y Claude Code | Para conectores compartidos y hosteados |

> 📌 El mismo formato de mensajes por debajo — así que los tools de un server funcionan
> de cualquiera de las dos formas.

### El ecosistema: construir una vez, reusar en todas partes

Ejemplos de servers ya existentes que cualquier host MCP puede conectar: `GitHub`,
`Google Drive`, `Slack`, bases de datos.

> 📌 Como MCP es un estándar compartido, los servers son reutilizables entre apps —
> conecta uno que ya exista o construye el tuyo.

> 📌 Construir el propio sigue la misma forma: declarar tus tools, resources y prompts.

> ⚠️ Una precaución importante: la descripción de un tool es texto que Claude lee — solo
> conecta servers en los que confíes (ver Domain 7, Security and Safety).

## Puntos clave del dominio

- Un tool le permite a Claude **actuar**, no solo producir texto; una `tool definition`
  = `name` + `description` + `input_schema`, y Claude lee la `description` para decidir
  si usarlo.
- El tool-use loop es siempre: Claude pide → tu código ejecuta → el resultado vuelve →
  Claude responde. Claude nunca ejecuta el tool él mismo.
- El `parallel tool use` acelera llamadas independientes; si una depende del resultado
  de otra, corren en secuencia.
- MCP resuelve el problema M×N de integraciones custom: construyes un conector una vez
  y cualquier app compatible con MCP lo usa (M×N se vuelve M+N).
- Los tres roles de MCP: **host** (la app), **client** (el cable, uno por server) y
  **server** (quien provee la capacidad) — conectar, descubrir capacidades y luego usar.
- MCP no reemplaza el tool use: le agrega discovery, transport y session por encima del
  mismo loop.
- Un `MCP server` expone tools (actuar), resources (leer) y prompts (plantillas
  reutilizables), y puede correr local (`stdio`) o remoto (`Streamable HTTP`).
- Conectar un `MCP server` de terceros implica confiar en su texto (las descripciones de
  sus tools) — solo se deben conectar servers de confianza.
