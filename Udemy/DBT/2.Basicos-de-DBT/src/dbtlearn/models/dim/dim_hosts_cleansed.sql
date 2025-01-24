{{
  config(
    materialized = 'view',
    )
}}
WITH SRC_HOSTS AS (
    SELECT * FROM {{ref("src_hosts")}}
)
SELECT HOST_ID, NVL(HOST_NAME, 'Anonymous') as HOST_NAME, IS_SUPERHOST, 
CREATED_AT, UPDATED_AT FROM SRC_HOSTS