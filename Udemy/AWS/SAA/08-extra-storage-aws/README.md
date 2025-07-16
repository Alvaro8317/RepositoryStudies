# Extras de almacenamiento de AWS

## 📊 Comparativa de AWS Snow Family

| Característica                 | **Snowcone**                              | **Snowball Edge**                                                                     | **Snowmobile**                                            |
| ------------------------------ | ----------------------------------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| 📦 Tamaño y portabilidad       | Muy portátil (2.1 kg)                     | Medio (como una maleta grande)                                                        | Enorme (tráiler de 45 pies)                               |
| 💾 Capacidad de almacenamiento | Hasta 8 TB (SSD)                          | - 80 TB (modo solo transferencia) - 42 TB HDD / 28 TB NVMe (modo computación)         | Hasta 100 PB por Snowmobile (exabytes al combinar varios) |
| ⚙️ Capacidades de cómputo      | Limitado (uso básico de Edge Computing)   | Alta (Soporta EC2, Lambda, S3 local)                                                  | No tiene cómputo integrado                                |
| 🌍 Edge computing              | ✅ Sí, uso en terreno remoto              | ✅ Sí, con soporte de contenedores y EC2                                              | ❌ No                                                     |
| 🔌 Energía y conectividad      | Requiere batería/cables externos          | Energía y red cableada estándar                                                       | En sitio con infraestructura propia                       |
| ☁️ Integración con servicios   | Compatible con **AWS DataSync**           | AWS OpsHub, EC2, S3 compatible, Lambda                                                | Directo a S3 una vez que se conecta en AWS                |
| 🚚 Modo de transferencia       | - Online con DataSync - Offline con envío | - Offline - Con AWS DataSync online                                                   | Sólo offline (entrega física)                             |
| 🔒 Seguridad                   | Cifrado automático con AWS KMS            | Cifrado con AWS KMS, carcasa resistente                                               | Nivel militar, monitoreo GPS, acceso biométrico           |
| 🛠️ Casos de uso típicos        | Sitios remotos, IoT, drones, sensores     | Migración de datos, aplicaciones en terreno, grabación médica, procesamiento en sitio | Migraciones masivas (data centers)                        |
| 🌐 Reutilizable                | Sí                                        | Sí                                                                                    | No (AWS lo instala y retira una vez)                      |

---

### 🧠 ¿Qué es **Edge Computing**?

Edge computing se refiere a **procesar datos cerca de donde se generan**, en lugar de enviarlos directamente a la nube. Es útil en entornos con poca o intermitente conectividad (campos petroleros, barcos, zonas militares, etc.).

---

### ✅ ¿Cuándo usar cada uno?

- **Snowcone**: Ideal si necesitas algo **ligero y portátil** para sitios remotos, con poco volumen de datos (hasta 8 TB).
- **Snowball Edge**: Para **migraciones medianas**, entornos industriales, y computación en terreno (puede ejecutar EC2 y Lambda local).
- **Snowmobile**: Cuando necesitas **migrar grandes centros de datos** (10 PB en adelante), de forma física y ultra segura.

Perfecto, aquí tienes un apunte claro sobre la **restricción de mover objetos desde Snowball a Glacier** y cómo manejarlo correctamente en AWS:

---

## 🧊 ❌ ¿Por qué **no se puede mover directamente a Glacier** desde Snowball?

Cuando se usan dispositivos **AWS Snowball** para **importar datos a AWS**, hay una **restricción importante**:

### 🚫 No es posible mover datos **directamente** desde Snowball a S3 Glacier o Glacier Deep Archive

---

## ✅ ¿Cómo se hace entonces?

Para almacenar datos en Glacier, **debes seguir este flujo**:

1. **Importar datos con Snowball** → Se almacenan en **Amazon S3 estándar**.
2. Una vez en S3, configuras una **regla del ciclo de vida** en el bucket.
3. La regla moverá automáticamente los objetos a:

   - ❄️ S3 Glacier
   - 📦 Glacier Deep Archive

---

### 📘 Ejemplo práctico:

Supón que importaste 50 TB con un **Snowball Edge** a un bucket S3 llamado `imported-data`.

Puedes definir una **regla de ciclo de vida** como esta:

```json
{
  "Rules": [
    {
      "ID": "MoveToGlacier",
      "Filter": {
        "Prefix": ""
      },
      "Status": "Enabled",
      "Transitions": [
        {
          "Days": 0,
          "StorageClass": "GLACIER"
        }
      ]
    }
  ]
}
```

🔁 Esta política transicionará todos los objetos del bucket a Glacier **inmediatamente después** de su carga.

---

## 🎯 ¿Por qué existe esta restricción?

- ❗ **Snowball solo soporta mover objetos al almacenamiento S3 estándar.**
- Glacier es una **clase de almacenamiento fría y de archivo**, que **no está disponible como destino directo** en operaciones de importación.
- AWS requiere que los objetos existan primero como objetos S3 válidos y luego apliques la transición.

---

## 🧠 Notas adicionales

| Tema                             | Detalle                                                                                                      |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| ❄️ ¿Y si quieres solo Glacier?   | Se recomienda moverlo a S3 estándar **y luego** aplicar la política.                                         |
| ⏳ ¿Cuánto tarda la transición?  | Depende de la regla (`Days` en 0 es inmediato), pero la transición puede tardar algunas horas en ejecutarse. |
| 🔐 ¿Puedo cifrar el bucket?      | Sí, puedes importar los datos cifrados y mantener el cifrado durante la transición.                          |
| 📦 ¿Puedo usar versiones o tags? | Sí, las reglas del ciclo de vida pueden aplicarse por **etiquetas**, **versiones**, o **prefijos**.          |
