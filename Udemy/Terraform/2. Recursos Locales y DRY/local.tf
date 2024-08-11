resource "local_file" "product_file" {
  count    = 5
  content  = "Producto,Precio,Cantidades\nMortadela,5000,10"
  filename = "productos-${random_string.sufix[count.index].id}.csv"
}
