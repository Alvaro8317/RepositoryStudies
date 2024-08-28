# Bloques dinamicos, modulos y terraform cloud

## Bloques

Los bloques dinámicos en Terraform te permiten generar bloques de configuración repetitivos de manera programática, usando un enfoque más flexible y eficiente que simplemente copiar y pegar bloques similares. Esto es útil cuando necesitas crear múltiples recursos o subbloques dentro de un recurso de manera dinámica, basándote en una lista o un mapa.

## Sintaxis y Uso de Bloques Dinámicos

Un bloque dinámico se define usando la palabra clave dynamic, seguida del tipo de bloque que se desea generar. Dentro de este, se usa for_each para iterar sobre una lista o mapa, y content para definir el contenido de cada bloque generado.

## Modulos

Usar modulos ayuda a que el código sea más simple de mantener y más fácil de reutilizar, con modulos se puede simplificar la Iac

## Terraform cloud

El tfstate se puede guardar en terraform cloud pero también, cuenta con muchas funcionalidades más. Terraform cloud es SaaS, permite almacenar el state, permite realizar todas las operaciones, crear equipos, proyectos y mucho más desde una misma plataforma. Se puede integrar con github con un CI/CD y cuenta con capa gratuita.

### Ventajas

- Terraform state compartido
- Entorno consistente y confiable
- UI de usuario
- Gestión de equipos y permisos
- Control de políticas
- Registro privado para guardar modulos
