# Autenticación y autorización

Autenticación consiste en demostrar quien soy.

Autorización es conceder a una parte autenticada, significa a donde puedo ir y qué puedo hacer.

## Microsoft Entra ID (Antes azure Active directory)

Es un servicio de gestión de identidades en la nube ofrecido por microsoft, está construido para trabajar en la nube y ofrece una serie de funcionalidades y características dirigidas a aplicaciones web y móviles. NO SE DEBE DE CONFUNDIR con el Active Directory tradicional.

Este servicio permite

- Gestión de identidades y acceso - Admite SSO y MFA
- Integración de aplicaciones
- Desarrollo de aplicaciones - Los desarrolladores pueden utilizar Entra ID como plataforma de identidad para sus aplicaciones
- Seguridad e inteligencia - Ofrece capacidades avanzadas con Entra ID Protection
- Es B2B y B2C, acceso condicionado, gestión de privilegios, etc.

### Inquilino (Tenant)

Un inquilino representa una organización, se trata de una instancia dedicada de Microsoft Entra ID que una organización o un desarrollador de aplicaciones recibe al principio de su relación con Microsoft. Cada tenant de Microsoft Entra es distinto e independiente de otros Tenants.

Se puede tener una arquitectura híbrida con Microsoft Entra ID, porque las aplicaciones que están a nivel local se pueden conectar a Entra ID para manejar la autenticación y autorización.

### Recomendaciones

- No se debe de confundir con Active Directory
- Cada cuenta de azure viene con una instancia de Microsoft Entra ID
- Un tenant es una instancia dedicada de Microsoft Entra ID y simboliza a la organización dentro de Azure
- Un usuario generalmente pertenece a un único tenant pero puede ser invitado a otros tenants

Entra ID cuenta con una GUI personalizada para administrar los usuarios que es el centro de administración de Microsoft Entra, se puede acceder [aquí](https://entra.microsoft.com/#home)

## Microsoft Entra Connect (Antes AD Connect)

Es una aplicación de local de microsoft diseñada para cumplir y lograr los obbjetivos de identidad híbrida, es decir, se sincroniza el active directory local con Entra ID. Se puede tener un SSO unificado con modos flexibles y brinda seguridad avanzada como MFA y políticas condicionales.

### Entra Connect Health

Es una ayuda a supervisar y conocer la infraestructura de identidad local, lo que garantiza la confiablidad del entorno. Es tan sencillo como instalar un agente en cada uno de los servidores de identidad locales.

## Confianza cero

No es un producto, es un enfoque o estrategia de seguridad para diseñar e implementar el siguiente conjunto de principios de seguridad compuesto por:

1. Comprobación explícita - Valida siempre las operaciones de autorización y autenticación
2. Acceso con privilegios mínimos - Limita el acceso de los usuarios
3. Asunción de que hay brechas - Minimiza el radio de explosión y el acceso a los segmentos

Este modelo presupone que hay brechas y siempre comprueba todas las solicitudes como si provinieran de una red no controlada, con este enfoque nunca se confia, siempre se realizan las comprobaciones pertinentes. Está diseñado para adaptarse a las complejidades del entorno moderno que abarca la fuerza de trabajo móvil, protege a las personas, los dispositivos y no se basa en la ubicación del usuario, sino en su identidad y credenciales validadas.

## MFA

MFA es un procedimiento que se solicita a los usuarios durante el login una forma adicional de identificación. Este se basa en exigir uno de los siguientes métodos de autenticación:

- Algo que conozco
- Algo que tengo
- Algo que soy

## Acceso condicional

Este concepto reúne las señales para tomar decisiones y aplicar las directivas de la organización. Es decir, es el motor de directivas de confianza cero de Microsoft que tiene en cuenta señales de varios orígenes al aplicar decisiones de directivas.

### Señales comunes

El acceso condicional tiene en cuenta señales de varios orígenes al tomar decisiones de acceso, ejemplo:

- Pertenece a un usuario o grupo
- Información de la IP
- Dispositivo
- Aplicación
- Detección de riesgo calculado y en tiempo real
- Microsoft Defender para aplicaciones en la nube

#### Decisiones comunes

Ante alguna señal se puede tomar estas decisiones:

- Bloquear acceso
- Conceder acceso
  - Requiere MFA
  - Requiere intensidad de autenticación
  - Requiere que el dispositivo sea compatible
  - Requiere un dispositivo unido a Microsoft Entra
  - Requiere una aplicación cliente aprobada
  - Condiciones de uso
  - Cambio de contraseña
  - Etc

## Opciones de autenticación

### Sin contraseña

En lugar de usar una contraseña, se puede utilizar algo en conjunto conmigo, ejemplo, como un telefono, la cara, un PIN, etc.

Eliminando la contraseña se aumenta la comodidad y seguridad, porque con la contraseña se elimina el sistema de login reemplazandolo con algo que tengo o algo que soy.

Azure global y Azure government ofrecen las sigtuientes 3 opciones de autenticación integrables con Entra ID:

- Windows hello
- Microsoft Authenticator
- Claves de seguridad FIDO2

## Acceso de usuarios externos

Si se requiere dar una cuenta de organización separada, se puede:

1. Crear una cuenta de organización separada para el usuario externo (implicaría al ususario gestionar dos cuentas)
2. Invitar al usuario al tenant de azure (colaboración B2B donde el usuario utiliza su cuenta existente como colaborador externo)

Si se va a hacer uso de esta funcionalidad se debe de:

1. Configurar proveedores de identidad
2. Asignar permisos para la cuenta de invitado - Minimi privilegio

Los pasos son:

1. Configurar el proveedor de identidad si no es microsoft
2. Invitar al externo
3. Después de que acepte el externo, dar permisos
4. Opcional, asignar aplicaciones y política de acceso condicional

## Azure Active Directory Domain Services (Azure AD DS)

Es como un llavero mágico, es un servicio gestionado que facilita la implementación de servicios de dominio en Azure, esencial para las organizaciones que quieren migrar aplicaciones al cloud sin perder el Active Directory. Permite unificar el manejo de las identidades corporativas en entornos híbridos.

- Es un servicio gestionado
- Crea un nombre de dominio / espacios de nombres únicos con un dominio independiente
- Sincronización unidireccional de Entra ID a Azure AD DS

Este servicio al tener integración con Entra ID, permite conectar Entra ID a AD DS y brinda acceso a los usuarios de la corporación con Active Directory

Casos de uso:

- Migración de aplicaciones
- Desarrollo y pruebas

## SSO

Es un método de autenticación que permite a los usuarios iniciar sesión con un conjunto de credenciales en varios sistemas independientes.

Habilitar el SSO facilita el acceso a múltiples aplicaciones con:

- Una sola credencial
- Acceso sin interrupciones
- Mayor seguridad
- Gestión centralizada

## Resumen

Entra ID - Servicio de identidad y acceso en la nube que conecta múltiples aplicaciones y usuarios
Confianza cero - Enfoque de seguridad que no confía en ningún ususario o sistema por defecto
MFA - Técnica de seguridad
Acceso condicional - Política que permite o niega el acceso a recursos basándose en condiciones específicas como ubicación del usuario
Sin contraseña - Estrategia de autenticación
Acceso de usuarios externos - Gestión y control de acceso de usuarios que no pertenecen directamente a la organización
Azure Active Directory Domain Services (AD DS) - Permite a las organizaciones usar servicios de dominio en la nube
SSO - Permite a los usuarios acceder a múltiples aplicaciones y servicios con una sola autenticación o conjunto de credenciales

La autenticación es el proceso de confirmar que alguien es quien dice ser

Microsoft Entra ID solía llamarse Azure Active Directory (Azure AD)

La confianza cero se basa en el principio de no confiar en nada dentro o fuera de las redes corporativas

MFA implica el uso de dos o más métodos de verificación para asegurarse de que un usuario es legítimo

El acceso condicional permite o niega el acceso basándose en ciertas condiciones

Sin contraseña" se refiere a métodos de autenticación que no dependen de contraseñas tradicionales"

El acceso de usuarios externos se refiere a permitir a personas fuera de la organización acceder a ciertos recursos

Azure AD DS es una extensión de Microsoft Entra ID que ofrece capacidades de directorio tradicionales pero administradas en la nube

SSO permite a los usuarios acceder a múltiples aplicaciones o servicios con una única autenticación

La autenticación se refiere a la verificación de la identidad de un usuario, mientras que la autorización se refiere a otorgar o negar permisos basándose en esa identidad verificada

El Inicio de sesión único (SSO) permite a los usuarios acceder a múltiples servicios con una única autenticación
