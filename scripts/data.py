import pdal
import json

PUBLIC_DATA_PATH="https://s3-us-west-2.amazonaws.com/usgs-lidar-public/"
REGION='IA_FullState/'
BOUNDS="([-10425171.940, -10423171.940], [5164494.710, 5166494.710])"
PUBLIC_ACCESS_PATH=PUBLIC_DATA_PATH + REGION + "ept.json"
OUTPUT_FILENAME_LAZ="laz/lowa_farm.laz"
OUTPUT_FILENAME_TIF="tif/lowa_farm.tif"
PIPELINE_PATH='get_data.json'

def get_raster_terrain(bounds:str,region:str, PUBLIC_ACCESS_PATH:str=PUBLIC_ACCESS_PATH,OUTPUT_FILENAME_LAZ:str=OUTPUT_FILENAME_LAZ, OUTPUT_FILENAME_TIF:str=OUTPUT_FILENAME_TIF,PIPELINE_PATH:str=PIPELINE_PATH)->None:


    with open(PIPELINE_PATH) as json_file:
        the_json= json.load(json_file)
    
    the_json['pipeline'][0]['bounds']=bounds
    the_json['pipeline'][0]['filename']=PUBLIC_ACCESS_PATH
    the_json['pipeline'][3]['filename']=OUTPUT_FILENAME_LAZ
    the_json['pipeline'][4]['filename']=OUTPUT_FILENAME_TIF
   
    pipeline=pdal.Pipeline(json.dumps(the_json))
    
    try:
        pipe_exec=pipeline.execute()
        metadata=pipeline.metadata
        print('meta data: ',metadata)
    except RuntimeError as er:
        print(er)
        print('Runtime error, writing 0s and moving to next bounds')
        pass
if __name__=="__main__":
    get_raster_terrain(bounds=BOUNDS,region=REGION)




