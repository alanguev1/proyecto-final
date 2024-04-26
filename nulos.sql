-- Validación de valores nulos en toda la tabla
SELECT *
FROM taxis_amarillos.`2021 - 1`
WHERE VendorID IS NULL 
   OR tpep_pickup_datetime IS NULL 
   OR tpep_dropoff_datetime IS NULL 
   OR passenger_count IS NULL 
   OR trip_distance IS NULL 
   OR RatecodeID IS NULL 
   OR store_and_fwd_flag IS NULL 
   OR PULocationID IS NULL 
   OR DOLocationID IS NULL 
   OR payment_type IS NULL 
   OR fare_amount IS NULL 
   OR extra IS NULL 
   OR mta_tax IS NULL 
   OR tip_amount IS NULL 
   OR tolls_amount IS NULL 
   OR improvement_surcharge IS NULL 
   OR total_amount IS NULL 
   OR congestion_surcharge IS NULL 
   OR airport_fee IS NULL;
