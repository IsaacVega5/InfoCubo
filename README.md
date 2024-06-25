# InfoCubo
InfoCubo es una aplicación simple que permite calcular indices de imágenes hiperespectrales.

## Instalación
Basta con descargar el archivo .zip de https://github.com/IsaacVega5/InfoCubo/releases, descomprimirlo y ejecutar el archivo `InfoCubo.exe`.

## Uso
De forma simplificada esta es la forma de utilizar esta aplicación:
  1. Seleccionar la carpeta donde se encuentran la imagen.
  2. Seleccionar los índices que se calcularán.
  3. Seleccionar el método de procesamiento.
  4. Hacer click en `Calcular índices` y seleccionar el destino de las imágenes con los indices calculados.

Las imágenes se guardaran en la carpeta `c:/destino/result_nombre_imagen/`

### Métodos de procesamiento
Actualmente hay dos métodos de procesamiento:
  1. **RAM**: Es el método más rápido, este método guarda la imagen en memoria RAM, por lo que consume más recursos, pero es más veloz.
  2. **Directo**: Es el método más lento, este método no guarda la imagen en memoria RAM, es más lento, pero consume menos recursos.
  
Recomiendo utilizar el método en base a la memoria RAM disponible y al peso de la imagen. Hay que considerar que si la imagen pesa 4gb el programa necesitará al rededor de 4.5gb de RAM para funcionar con el primer método.  

## Indices 
Los valores que se obtendrán son los siguientes:
* NDVI
* PRI
* SAVI
* MCARI
* WBI
* RDVI
* EVI
* ARI2
* CRI2
  
## Autor

- [Isaac Vega Salgado - IsaacVega5](https://github.com/IsaacVega5)
