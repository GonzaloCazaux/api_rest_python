from django.shortcuts import render
from django.http import JsonResponse
from .models import Clases
from django.db import connection

def obtener_clases_con_asignaturas(request):
   # Ejecutar una consulta SELECT
    sql='SELECT * FROM  miapp_asignaturas'
    with connection.cursor() as cursor:
        cursor.execute(sql)
        resultados = cursor.fetchall()
        
    # Procesar los resultados y devolver una respuesta JSON
    data = [{'asignaturaid': fila[0], 'nombreasignatura': fila[1], 'des': fila[2]} for fila in resultados]
    data2 = {'asignaturaid': '1', 'nombreasignatura': 'mate', 'des': 'estadisticas'}
    print(resultados)
    print(data)
    return JsonResponse(data2, safe=False)
