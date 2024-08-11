# 3. Despliegue a AWS

## **¿Terraform puede desplegar recursos en paralelo o lo hace secuencial?**

**La respuesta es que por defecto, crea 10 recursos en paralelo aunque esta cantidad es personalizable.**

## Guardar un plan

Cuando se visualiza un plan, se puede guardar este plan con el comando `terraform plan --out bucket.plan` y si se quiere ejecutar ese mismo plan, se debe de ejecuta `terraform apply "bucket.plan"`. La finalidad de esta función es para evitar desplegar cosas indeseadas, porque por ejemplo, se puede guardar el plan y así alguien haya modificado el código terraform, solo se desplegará lo que quedó en el plan. Cuando se aplica un plan en terraform, esta vez directamente terraform no mostrará el plan ni preguntará si quiere realmente desplegar eso.
