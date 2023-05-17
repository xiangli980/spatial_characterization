python run_infer.py \
--gpu='0' \
--nr_types=3 \
--type_info_path=type_info.json \
--model_mode=original \
--model_path=./logs/net_epoch=50.tar \
--nr_inference_workers=8 \
--nr_post_proc_workers=8 \
wsi \
--chunk_shape=5000 \
--tile_shape=1024 \
--input_dir=./data_MCD/ \
--output_dir=./output_MCD/ \
--save_thumb \
--save_mask \
#--input_mask_dir=./output_MCD/mask/ \

