with 
source as ( 
    select * from {{ source ('nasa', 'visualization') }}
),

renamed as (
    select 
        id, 
        code as model_code, 
        title, 
        description,
        category,
        license, 
        field7 as cat_license, 
        field8 as link, 
        center 
        
    from source
)

select * from renamed 
