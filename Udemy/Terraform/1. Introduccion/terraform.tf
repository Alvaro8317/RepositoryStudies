resource "local_file" "product_file" {
  content  = "Producto,Precio,Cantidades\nMortadela,5000,10"
  filename = "productos.csv"
}
