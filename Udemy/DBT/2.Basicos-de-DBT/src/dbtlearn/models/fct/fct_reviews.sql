{{
      config(
        materialized = 'incremental',
        on_schema_change = 'fail'
        )
}}
WITH src_reviews AS (
 SELECT * FROM {{ ref('src_reviews') }}
)
SELECT * FROM src_reviews
WHERE review_text is not null
{% if is_incremental() %}
  and REVIEW_DATE > (SELECT MAX(REVIEW_DATE) FROM {{this}})
{% else %}
{% endif %}