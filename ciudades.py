Bogota,Bucaramanga,Medellin,separaciones,separador='19,19,17,18,20','27,26,26,26,27','27,26,26,27,29',1,(',')
bogota,bucaramanga,medellin=(Bogota.split(sep=',')),(Bucaramanga.split(sep=',')),(Medellin.split(sep=','))
bogota1,bucaramanga1,medellin1=[round(float(x)) for x in bogota],[round(float(x)) for x in bucaramanga],[round(float(x)) for x in medellin]
import statistics

print(f'El promedio de la temperatura en los proximos 5 dias de Bogota es de: {statistics.mean(bogota1)}\nEl maximo de la temperatura va a ser de: {max(bogota1)}\nEl minimo de la temperatura va a ser de: {min(bogota1)}')
print(f'El promedio de la temperatura en los proximos 5 dias de Bucaramanga es de: {statistics.mean(bucaramanga1)}\nEl maximo de la temperatura es: {max(bucaramanga1)}\nEl minimo de la temperatura va a ser de: {min(bucaramanga1)}')
print(f'El promedio de la temperatura en los proximos 5 dias de Medellin es de: {statistics.mean(medellin1)}\nEl maximo de la temperatura es: {max(medellin1)}\nEl minimo de la temperatura va a ser de: {min(medellin1)}')
