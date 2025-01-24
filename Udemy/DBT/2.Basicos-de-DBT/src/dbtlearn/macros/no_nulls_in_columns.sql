{% macro no_nulls_in_columns(model) %}
 SELECT * FROM {{ model }} WHERE
 {% for col in adapter.get_columns_in_relation(model) -%} {# El menos al final es para eliminar los espacios de la línea #}
 {{ col.column }} IS NULL OR
 {% endfor %}
 FALSE
{% endmacro %}
